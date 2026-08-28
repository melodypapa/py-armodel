import os
import tempfile

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventSwcInternalBehavior import (
    TDEventSwcInternalBehavior,
    TDEventSwcInternalBehaviorReference,
    TDEventSwcInternalBehaviorTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import ComponentInCompositionInstanceRef
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def make_ref(value: str, dest: str = None) -> RefType:
    ref = RefType()
    ref.setValue(value)
    if dest is not None:
        ref.setDest(dest)
    return ref


def make_enum(enum_cls, value: str):
    enum = enum_cls()
    enum.value = value
    return enum


def make_component_iref() -> ComponentInCompositionInstanceRef:
    iref = ComponentInCompositionInstanceRef()
    iref.setTargetComponentRef(make_ref("/Root/Comp", "SW-COMPONENT-PROTOTYPE"))
    return iref


class TestTDEventSwcFamilyRoundTrip:
    def test_round_trip_all_swc_events(self):
        """Parse (build) -> write -> re-parse -> compare for the SW-C event family."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("TimingPkg")
        swc_timing = pkg.createSwcTiming("SwcTiming1")
        component_iref = make_component_iref()

        ib = TDEventSwcInternalBehavior(swc_timing, "Ib1")
        ib.setComponentIRef(component_iref)
        ib.setRunnableRef(make_ref("/Root/Runnable", "RUNNABLE-ENTITY"))
        ib.setTdEventSwcInternalBehaviorType(make_enum(TDEventSwcInternalBehaviorTypeEnum, "runnableEntityStarted"))
        ib.setVariableAccessRef(make_ref("/Root/VarAccess", "VARIABLE-ACCESS"))
        swc_timing.addTimingDescription(ib)

        ib_ref = TDEventSwcInternalBehaviorReference(swc_timing, "IbRef1")
        ib_ref.setComponentIRef(component_iref)
        ib_ref.setReferencedTDEventSwcRef(make_ref("/Root/OtherEvent", "TD-EVENT-SWC-INTERNAL-BEHAVIOR"))
        swc_timing.addTimingDescription(ib_ref)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            swc_timing_2 = document_2.getARPackages()[0].getSwcTimings()[0]
            descriptions = {d.getShortName(): d for d in swc_timing_2.getTimingDescriptions()}
            assert set(descriptions.keys()) == {"Ib1", "IbRef1"}

            ib_2 = descriptions["Ib1"]
            assert isinstance(ib_2, TDEventSwcInternalBehavior)
            assert ib_2.getComponentIRef() is not None
            assert ib_2.getComponentIRef().getTargetComponentRef().getValue() == "/Root/Comp"
            assert ib_2.getRunnableRef().getValue() == "/Root/Runnable"
            assert ib_2.getRunnableRef().getDest() == "RUNNABLE-ENTITY"
            assert ib_2.getTdEventSwcInternalBehaviorType().value == "runnableEntityStarted"
            assert ib_2.getVariableAccessRef().getValue() == "/Root/VarAccess"

            ib_ref_2 = descriptions["IbRef1"]
            assert isinstance(ib_ref_2, TDEventSwcInternalBehaviorReference)
            assert ib_ref_2.getComponentIRef() is not None
            assert ib_ref_2.getReferencedTDEventSwcRef().getValue() == "/Root/OtherEvent"
            assert ib_ref_2.getReferencedTDEventSwcRef().getDest() == "TD-EVENT-SWC-INTERNAL-BEHAVIOR"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_unset_omits_optional_elements(self):
        """Unset optional attributes must not emit XML elements and round-trip to None."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("TimingPkg")
        swc_timing = pkg.createSwcTiming("SwcTiming1")

        ib = TDEventSwcInternalBehavior(swc_timing, "IbMin")
        swc_timing.addTimingDescription(ib)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            with open(file_path, "r", encoding="utf-8") as handle:
                content = handle.read()
            assert "COMPONENT-IREF" not in content
            assert "RUNNABLE-REF" not in content
            assert "TD-EVENT-SWC-INTERNAL-BEHAVIOR-TYPE" not in content
            assert "VARIABLE-ACCESS-REF" not in content

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            swc_timing_2 = document_2.getARPackages()[0].getSwcTimings()[0]
            ib_2 = swc_timing_2.getTimingDescriptions()[0]
            assert ib_2.getComponentIRef() is None
            assert ib_2.getRunnableRef() is None
            assert ib_2.getTdEventSwcInternalBehaviorType() is None
            assert ib_2.getVariableAccessRef() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
