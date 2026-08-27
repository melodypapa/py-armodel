import os
import tempfile

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventVfb import (
    TDEventModeDeclaration,
    TDEventModeDeclarationTypeEnum,
    TDEventOperation,
    TDEventOperationTypeEnum,
    TDEventTrigger,
    TDEventTriggerTypeEnum,
    TDEventVariableDataPrototype,
    TDEventVariableDataPrototypeTypeEnum,
    TDEventVfbReference,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, RefType
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


class TestTDEventVfbFamilyRoundTrip:
    def test_round_trip_all_vfb_events(self):
        """Parse (build) -> write -> re-parse -> compare for the full VFB event family."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("TimingPkg")
        swc_timing = pkg.createSwcTiming("SwcTiming1")
        component_iref = make_component_iref()

        ref_event = TDEventVfbReference(swc_timing, "VfbRef1")
        ref_event.setComponentIRef(component_iref)
        ref_event.setReferencedTDEventVfbRef(make_ref("/Root/OtherEvent", "TD-EVENT-VFB"))
        swc_timing.addTimingDescription(ref_event)

        vdp = TDEventVariableDataPrototype(swc_timing, "Vdp1")
        vdp.setComponentIRef(component_iref)
        vdp.setIsExternal(Boolean().setValue(True))
        vdp.setPortRef(make_ref("/Root/Port", "PORT-PROTOTYPE"))
        vdp.setPortPrototypeBlueprintRef(make_ref("/Root/Bp", "PORT-PROTOTYPE-BLUEPRINT"))
        vdp.setDataElementRef(make_ref("/Root/Data", "VARIABLE-DATA-PROTOTYPE"))
        vdp.setTdEventVariableDataPrototypeType(make_enum(TDEventVariableDataPrototypeTypeEnum, "variableDataPrototypeReceived"))
        swc_timing.addTimingDescription(vdp)

        operation = TDEventOperation(swc_timing, "Op1")
        operation.setComponentIRef(component_iref)
        operation.setPortRef(make_ref("/Root/Port", "PORT-PROTOTYPE"))
        operation.setOperationRef(make_ref("/Root/Op", "CLIENT-SERVER-OPERATION"))
        operation.setTdEventOperationType(make_enum(TDEventOperationTypeEnum, "operationCallReceived"))
        swc_timing.addTimingDescription(operation)

        mode = TDEventModeDeclaration(swc_timing, "Mode1")
        mode.setComponentIRef(component_iref)
        mode.setPortRef(make_ref("/Root/Port", "PORT-PROTOTYPE"))
        mode.setEntryModeDeclarationRef(make_ref("/Root/EntryMode", "MODE-DECLARATION"))
        mode.setExitModeDeclarationRef(make_ref("/Root/ExitMode", "MODE-DECLARATION"))
        mode.setModeDeclarationRef(make_ref("/Root/Mode", "MODE-DECLARATION-GROUP-PROTOTYPE"))
        mode.setTdEventModeDeclarationType(make_enum(TDEventModeDeclarationTypeEnum, "modeDeclarationSwitchInitiated"))
        swc_timing.addTimingDescription(mode)

        trigger = TDEventTrigger(swc_timing, "Trigger1")
        trigger.setComponentIRef(component_iref)
        trigger.setPortRef(make_ref("/Root/Port", "PORT-PROTOTYPE"))
        trigger.setTriggerRef(make_ref("/Root/Trigger", "TRIGGER"))
        trigger.setTdEventTriggerType(make_enum(TDEventTriggerTypeEnum, "triggerReleased"))
        swc_timing.addTimingDescription(trigger)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            swc_timing_2 = document_2.getARPackages()[0].getSwcTimings()[0]
            descriptions = {d.getShortName(): d for d in swc_timing_2.getTimingDescriptions()}
            assert set(descriptions.keys()) == {"VfbRef1", "Vdp1", "Op1", "Mode1", "Trigger1"}

            ref_event_2 = descriptions["VfbRef1"]
            assert isinstance(ref_event_2, TDEventVfbReference)
            assert ref_event_2.getComponentIRef() is not None
            assert ref_event_2.getComponentIRef().getTargetComponentRef().getValue() == "/Root/Comp"
            assert ref_event_2.getReferencedTDEventVfbRef().getValue() == "/Root/OtherEvent"
            assert ref_event_2.getReferencedTDEventVfbRef().getDest() == "TD-EVENT-VFB"

            vdp_2 = descriptions["Vdp1"]
            assert isinstance(vdp_2, TDEventVariableDataPrototype)
            assert vdp_2.getIsExternal().getValue() is True
            assert vdp_2.getPortRef().getValue() == "/Root/Port"
            assert vdp_2.getPortPrototypeBlueprintRef().getValue() == "/Root/Bp"
            assert vdp_2.getDataElementRef().getValue() == "/Root/Data"
            assert vdp_2.getTdEventVariableDataPrototypeType().value == "variableDataPrototypeReceived"

            operation_2 = descriptions["Op1"]
            assert isinstance(operation_2, TDEventOperation)
            assert operation_2.getOperationRef().getValue() == "/Root/Op"
            assert operation_2.getTdEventOperationType().value == "operationCallReceived"

            mode_2 = descriptions["Mode1"]
            assert isinstance(mode_2, TDEventModeDeclaration)
            assert mode_2.getEntryModeDeclarationRef().getValue() == "/Root/EntryMode"
            assert mode_2.getExitModeDeclarationRef().getValue() == "/Root/ExitMode"
            assert mode_2.getModeDeclarationRef().getValue() == "/Root/Mode"
            assert mode_2.getTdEventModeDeclarationType().value == "modeDeclarationSwitchInitiated"

            trigger_2 = descriptions["Trigger1"]
            assert isinstance(trigger_2, TDEventTrigger)
            assert trigger_2.getTriggerRef().getValue() == "/Root/Trigger"
            assert trigger_2.getTdEventTriggerType().value == "triggerReleased"
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

        vdp = TDEventVariableDataPrototype(swc_timing, "VdpMin")
        swc_timing.addTimingDescription(vdp)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            with open(file_path, "r", encoding="utf-8") as handle:
                content = handle.read()
            assert "COMPONENT-IREF" not in content
            assert "IS-EXTERNAL" not in content
            assert "PORT-REF" not in content
            assert "DATA-ELEMENT-REF" not in content
            assert "TD-EVENT-VARIABLE-DATA-PROTOTYPE-TYPE" not in content

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            swc_timing_2 = document_2.getARPackages()[0].getSwcTimings()[0]
            vdp_2 = swc_timing_2.getTimingDescriptions()[0]
            assert vdp_2.getComponentIRef() is None
            assert vdp_2.getIsExternal() is None
            assert vdp_2.getPortRef() is None
            assert vdp_2.getDataElementRef() is None
            assert vdp_2.getTdEventVariableDataPrototypeType() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
