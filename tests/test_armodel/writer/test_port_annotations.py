"""Writer/reader round-trip tests for the PortPrototype port-annotation classes."""

import os
import tempfile

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import (
    DelegatedPortAnnotation,
    ModePortAnnotation,
    NvDataPortAnnotation,
    ParameterPortAnnotation,
    SignalFanEnum,
    TriggerPortAnnotation,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _ref(value, dest):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _round_trip(document):
    file_path = tempfile.mktemp(suffix=".arxml")
    try:
        ARXMLWriter().save(file_path, document)

        document_2 = AUTOSAR.getInstance()
        document_2.clear()
        ARXMLParser().load(file_path, document_2)

        return document_2.getARPackages()[0].getAtomicSwComponentTypes()[0].getPRPortPrototypes()[0]
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


def _new_document_with_port():
    AUTOSAR.getInstance().setARRelease("R23-11")
    document = AUTOSAR.getInstance()
    document.clear()
    pkg = document.createARPackage("AUTOSAR")
    swc = pkg.createApplicationSwComponentType("App")
    return document, swc.createPRPortPrototype("Port")


class TestParameterPortAnnotationRoundTrip:
    def test_round_trip(self):
        _, port = _new_document_with_port()

        param = ParameterPortAnnotation()
        param.setParameterRef(_ref("/Swc/Param", "PARAMETER-DATA-PROTOTYPE"))
        port.addParameterPortAnnotation(param)

        port_2 = _round_trip(AUTOSAR.getInstance())

        param_list = port_2.getParameterPortAnnotations()
        assert len(param_list) == 1
        assert param_list[0].getParameterRef().getValue() == "/Swc/Param"
        assert param_list[0].getParameterRef().getDest() == "PARAMETER-DATA-PROTOTYPE"

    def test_empty_wrapper_list(self):
        _, port = _new_document_with_port()

        port_2 = _round_trip(AUTOSAR.getInstance())

        assert port_2.getParameterPortAnnotations() == []


class TestModePortAnnotationRoundTrip:
    def test_round_trip(self):
        _, port = _new_document_with_port()

        mode = ModePortAnnotation()
        mode.setModeGroupRef(_ref("/Swc/ModeGroup", "MODE-DECLARATION-GROUP-PROTOTYPE"))
        port.addModePortAnnotation(mode)

        port_2 = _round_trip(AUTOSAR.getInstance())

        mode_list = port_2.getModePortAnnotations()
        assert len(mode_list) == 1
        assert mode_list[0].getModeGroupRef().getValue() == "/Swc/ModeGroup"
        assert mode_list[0].getModeGroupRef().getDest() == "MODE-DECLARATION-GROUP-PROTOTYPE"

    def test_empty_wrapper_list(self):
        _, port = _new_document_with_port()

        port_2 = _round_trip(AUTOSAR.getInstance())

        assert port_2.getModePortAnnotations() == []


class TestTriggerPortAnnotationRoundTrip:
    def test_round_trip(self):
        _, port = _new_document_with_port()

        trig = TriggerPortAnnotation()
        trig.setTriggerRef(_ref("/Swc/Trigger", "TRIGGER"))
        port.addTriggerPortAnnotation(trig)

        port_2 = _round_trip(AUTOSAR.getInstance())

        trig_list = port_2.getTriggerPortAnnotations()
        assert len(trig_list) == 1
        assert trig_list[0].getTriggerRef().getValue() == "/Swc/Trigger"
        assert trig_list[0].getTriggerRef().getDest() == "TRIGGER"

    def test_empty_wrapper_list(self):
        _, port = _new_document_with_port()

        port_2 = _round_trip(AUTOSAR.getInstance())

        assert port_2.getTriggerPortAnnotations() == []


class TestNvDataPortAnnotationRoundTrip:
    def test_round_trip(self):
        _, port = _new_document_with_port()

        nv = NvDataPortAnnotation()
        nv.setVariableRef(_ref("/Swc/Nv", "VARIABLE-DATA-PROTOTYPE"))
        port.addNvDataPortAnnotation(nv)

        port_2 = _round_trip(AUTOSAR.getInstance())

        nv_list = port_2.getNvDataPortAnnotations()
        assert len(nv_list) == 1
        assert nv_list[0].getVariableRef().getValue() == "/Swc/Nv"
        assert nv_list[0].getVariableRef().getDest() == "VARIABLE-DATA-PROTOTYPE"

    def test_empty_wrapper_list(self):
        _, port = _new_document_with_port()

        port_2 = _round_trip(AUTOSAR.getInstance())

        assert port_2.getNvDataPortAnnotations() == []


class TestDelegatedPortAnnotationRoundTrip:
    def test_round_trip(self):
        _, port = _new_document_with_port()

        delegated = DelegatedPortAnnotation()
        delegated.setSignalFan(SignalFanEnum().setValue(SignalFanEnum.SINGLE))
        port.setDelegatedPortAnnotation(delegated)

        port_2 = _round_trip(AUTOSAR.getInstance())

        delegated_2 = port_2.getDelegatedPortAnnotation()
        assert delegated_2 is not None
        assert isinstance(delegated_2.getSignalFan(), SignalFanEnum)
        assert delegated_2.getSignalFan().getValue() == SignalFanEnum.SINGLE

    def test_absence(self):
        _, port = _new_document_with_port()

        port_2 = _round_trip(AUTOSAR.getInstance())

        assert port_2.getDelegatedPortAnnotation() is None
