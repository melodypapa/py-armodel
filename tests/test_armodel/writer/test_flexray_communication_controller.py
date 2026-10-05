"""Writer round-trip tests for FlexrayCommunicationController (Table 3.30, p.86).

XML element order per XSD complexType FLEXRAY-COMMUNICATION-CONTROLLER: the outer
element carries SHORT-NAME then FLEXRAY-COMMUNICATION-CONTROLLER-VARIANTS; its
CONDITIONAL carries WAKE-UP-BY-CONTROLLER-SUPPORTED (COMMUNICATION-CONTROLLER-CONTENT)
followed by the FLEXRAY-COMMUNICATION-CONTROLLER-CONTENT leaves in XSD group order.
Coverage runs through the COMM-CONTROLLERS dispatch on writeEcuInstanceCommControllers.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer, PositiveInteger, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import FlexrayFifoConfiguration
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import EcuInstance
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ORDER = [
    "ACCEPTED-STARTUP-RANGE",
    "ALLOW-HALT-DUE-TO-CLOCK",
    "ALLOW-PASSIVE-TO-ACTIVE",
    "CLUSTER-DRIFT-DAMPING",
    "DECODING-CORRECTION",
    "DELAY-COMPENSATION-A",
    "DELAY-COMPENSATION-B",
    "EXTERN-OFFSET-CORRECTION",
    "EXTERN-RATE-CORRECTION",
    "EXTERNAL-SYNC",
    "FALL-BACK-INTERNAL",
    "FLEXRAY-FIFOS",
    "KEY-SLOT-ID",
    "KEY-SLOT-ONLY-ENABLED",
    "KEY-SLOT-USED-FOR-START-UP",
    "KEY-SLOT-USED-FOR-SYNC",
    "LATEST-TX",
    "LISTEN-TIMEOUT",
    "MACRO-INITIAL-OFFSET-A",
    "MACRO-INITIAL-OFFSET-B",
    "MAXIMUM-DYNAMIC-PAYLOAD-LENGTH",
    "MICRO-INITIAL-OFFSET-A",
    "MICRO-INITIAL-OFFSET-B",
    "MICRO-PER-CYCLE",
    "MICROTICK-DURATION",
    "NM-VECTOR-EARLY-UPDATE",
    "OFFSET-CORRECTION-OUT",
    "RATE-CORRECTION-OUT",
    "SAMPLES-PER-MICROTICK",
    "SECOND-KEY-SLOT-ID",
    "TWO-KEY-SLOT-MODE",
    "WAKE-UP-PATTERN",
]

CONDITIONAL_ORDER = ["WAKE-UP-BY-CONTROLLER-SUPPORTED"] + XSD_ORDER


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _integer(text):
    value = Integer()
    value.setValue(text)
    return value


def _positive_integer(text):
    value = PositiveInteger()
    value.setValue(text)
    return value


def _boolean(value):
    value_obj = Boolean()
    value_obj.setValue(value)
    return value_obj


def _time_value(text):
    value = TimeValue()
    value.setValue(text)
    return value


def _new_instance_with_controller():
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    instance = EcuInstance(pkg, "Ecu")
    controller = instance.createFlexrayCommunicationController("ctrl")
    controller.setWakeUpByControllerSupported(_boolean(True))
    controller.setAcceptedStartupRange(_integer("4"))
    controller.setAllowHaltDueToClock(_boolean(True))
    controller.setAllowPassiveToActive(_integer("3"))
    controller.setClusterDriftDamping(_integer("2"))
    controller.setDecodingCorrection(_integer("1"))
    controller.setDelayCompensationA(_integer("6"))
    controller.setDelayCompensationB(_integer("7"))
    controller.setExternOffsetCorrection(_integer("8"))
    controller.setExternRateCorrection(_integer("9"))
    controller.setExternalSync(_boolean(True))
    controller.setFallBackInternal(_boolean(False))
    fifo = FlexrayFifoConfiguration()
    fifo.setBaseCycle(_integer("1"))
    fifo.setFifoDepth(_integer("8"))
    fifo.setMsgIdMask(_integer("16"))
    controller.addFlexrayFifo(fifo)
    controller.setKeySlotID(_positive_integer("2"))
    controller.setKeySlotOnlyEnabled(_boolean(True))
    controller.setKeySlotUsedForStartUp(_boolean(True))
    controller.setKeySlotUsedForSync(_boolean(False))
    controller.setLatestTX(_integer("10"))
    controller.setListenTimeout(_integer("100"))
    controller.setMacroInitialOffsetA(_integer("30"))
    controller.setMacroInitialOffsetB(_integer("31"))
    controller.setMaximumDynamicPayloadLength(_integer("14"))
    controller.setMicroInitialOffsetA(_integer("15"))
    controller.setMicroInitialOffsetB(_integer("16"))
    controller.setMicroPerCycle(_integer("17"))
    controller.setMicrotickDuration(_time_value("0.05"))
    controller.setNmVectorEarlyUpdate(_boolean(True))
    controller.setOffsetCorrectionOut(_integer("18"))
    controller.setRateCorrectionOut(_integer("19"))
    controller.setSamplesPerMicrotick(_integer("20"))
    controller.setSecondKeySlotId(_positive_integer("21"))
    controller.setTwoKeySlotMode(_boolean(False))
    controller.setWakeUpPattern(_integer("22"))
    return instance


def _write_instance(instance):
    parent = ET.Element("ECU-INSTANCE")
    ARXMLWriter().writeEcuInstanceCommControllers(parent, instance)
    return parent


class TestWriteFlexrayCommunicationController:
    def test_write_all_fields_in_xsd_order(self):
        parent = _write_instance(_new_instance_with_controller())
        controller_tag = parent.find("COMM-CONTROLLERS/FLEXRAY-COMMUNICATION-CONTROLLER")
        assert controller_tag is not None
        assert [child.tag for child in controller_tag] == ["SHORT-NAME", "FLEXRAY-COMMUNICATION-CONTROLLER-VARIANTS"]
        conditional_tag = controller_tag.find("FLEXRAY-COMMUNICATION-CONTROLLER-VARIANTS/FLEXRAY-COMMUNICATION-CONTROLLER-CONDITIONAL")
        assert conditional_tag is not None
        assert [child.tag for child in conditional_tag] == CONDITIONAL_ORDER

    def test_write_field_values(self):
        parent = _write_instance(_new_instance_with_controller())
        conditional_tag = parent.find("COMM-CONTROLLERS/FLEXRAY-COMMUNICATION-CONTROLLER/FLEXRAY-COMMUNICATION-CONTROLLER-VARIANTS/FLEXRAY-COMMUNICATION-CONTROLLER-CONDITIONAL")
        assert conditional_tag is not None
        assert conditional_tag.find("ACCEPTED-STARTUP-RANGE").text == "4"
        assert conditional_tag.find("ALLOW-HALT-DUE-TO-CLOCK").text == "true"
        assert conditional_tag.find("KEY-SLOT-ID").text == "2"
        assert conditional_tag.find("SECOND-KEY-SLOT-ID").text == "21"
        assert conditional_tag.find("MICROTICK-DURATION").text == "0.05"
        assert conditional_tag.find("WAKE-UP-PATTERN").text == "22"
        assert conditional_tag.find("WAKE-UP-BY-CONTROLLER-SUPPORTED").text == "true"
        fifo_tag = conditional_tag.find("FLEXRAY-FIFOS/FLEXRAY-FIFO-CONFIGURATION")
        assert fifo_tag is not None
        assert fifo_tag.find("FIFO-DEPTH").text == "8"

    def test_write_controller_without_flexray_fields_omits_elements(self):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        instance = EcuInstance(pkg, "Ecu")
        instance.createFlexrayCommunicationController("ctrl")
        parent = _write_instance(instance)
        conditional_tag = parent.find("COMM-CONTROLLERS/FLEXRAY-COMMUNICATION-CONTROLLER/FLEXRAY-COMMUNICATION-CONTROLLER-VARIANTS/FLEXRAY-COMMUNICATION-CONTROLLER-CONDITIONAL")
        assert conditional_tag is not None
        for xsd_tag in XSD_ORDER:
            assert conditional_tag.find(xsd_tag) is None

    def test_round_trip_preserves_all_values(self):
        instance = _new_instance_with_controller()
        parent = _write_instance(instance)
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner))

        parsed_pkg = AUTOSAR.getInstance().createARPackage("Parsed")
        parsed_instance = EcuInstance(parsed_pkg, "Ecu")
        ARXMLParser().readEcuInstanceCommControllers(root[0], parsed_instance)

        controller = parsed_instance.getCommControllers()[0]
        assert controller.getShortName() == "ctrl"
        assert controller.getWakeUpByControllerSupported().getValue() is True
        assert controller.getAcceptedStartupRange().getValue() == 4
        assert controller.getAllowHaltDueToClock().getValue() is True
        assert controller.getAllowPassiveToActive().getValue() == 3
        assert controller.getClusterDriftDamping().getValue() == 2
        assert controller.getDecodingCorrection().getValue() == 1
        assert controller.getDelayCompensationA().getValue() == 6
        assert controller.getDelayCompensationB().getValue() == 7
        assert controller.getExternOffsetCorrection().getValue() == 8
        assert controller.getExternRateCorrection().getValue() == 9
        assert controller.getExternalSync().getValue() is True
        assert controller.getFallBackInternal().getValue() is False
        fifos = controller.getFlexrayFifos()
        assert len(fifos) == 1
        assert fifos[0].getBaseCycle().getValue() == 1
        assert fifos[0].getFifoDepth().getValue() == 8
        assert fifos[0].getMsgIdMask().getValue() == 16
        assert isinstance(controller.getKeySlotID(), PositiveInteger)
        assert controller.getKeySlotID().getValue() == 2
        assert controller.getKeySlotOnlyEnabled().getValue() is True
        assert controller.getKeySlotUsedForStartUp().getValue() is True
        assert controller.getKeySlotUsedForSync().getValue() is False
        assert controller.getLatestTX().getValue() == 10
        assert controller.getListenTimeout().getValue() == 100
        assert controller.getMacroInitialOffsetA().getValue() == 30
        assert controller.getMacroInitialOffsetB().getValue() == 31
        assert controller.getMaximumDynamicPayloadLength().getValue() == 14
        assert controller.getMicroInitialOffsetA().getValue() == 15
        assert controller.getMicroInitialOffsetB().getValue() == 16
        assert controller.getMicroPerCycle().getValue() == 17
        assert isinstance(controller.getMicrotickDuration(), TimeValue)
        assert controller.getMicrotickDuration().getValue() == 0.05
        assert controller.getNmVectorEarlyUpdate().getValue() is True
        assert controller.getOffsetCorrectionOut().getValue() == 18
        assert controller.getRateCorrectionOut().getValue() == 19
        assert controller.getSamplesPerMicrotick().getValue() == 20
        assert isinstance(controller.getSecondKeySlotId(), PositiveInteger)
        assert controller.getSecondKeySlotId().getValue() == 21
        assert controller.getTwoKeySlotMode().getValue() is False
        assert controller.getWakeUpPattern().getValue() == 22
