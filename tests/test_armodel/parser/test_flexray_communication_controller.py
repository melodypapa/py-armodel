"""Parser tests for FlexrayCommunicationController (Table 3.30, p.86).

XML element order per XSD group FLEXRAY-COMMUNICATION-CONTROLLER-CONTENT; the
WAKE-UP-BY-CONTROLLER-SUPPORTED base element (COMMUNICATION-CONTROLLER group) sits
before the FLEXRAY-COMMUNICATION-CONTROLLER-VARIANTS wrapper. Coverage runs through
the COMM-CONTROLLERS dispatch on readEcuInstanceCommControllers.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer, PositiveInteger, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import FlexrayCommunicationController, FlexrayFifoConfiguration
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import EcuInstance
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

CONDITIONAL_CONTENT = (
    "<ACCEPTED-STARTUP-RANGE>4</ACCEPTED-STARTUP-RANGE>"
    "<ALLOW-HALT-DUE-TO-CLOCK>true</ALLOW-HALT-DUE-TO-CLOCK>"
    "<ALLOW-PASSIVE-TO-ACTIVE>3</ALLOW-PASSIVE-TO-ACTIVE>"
    "<CLUSTER-DRIFT-DAMPING>2</CLUSTER-DRIFT-DAMPING>"
    "<DECODING-CORRECTION>1</DECODING-CORRECTION>"
    "<DELAY-COMPENSATION-A>6</DELAY-COMPENSATION-A>"
    "<DELAY-COMPENSATION-B>7</DELAY-COMPENSATION-B>"
    "<EXTERN-OFFSET-CORRECTION>8</EXTERN-OFFSET-CORRECTION>"
    "<EXTERN-RATE-CORRECTION>9</EXTERN-RATE-CORRECTION>"
    "<EXTERNAL-SYNC>true</EXTERNAL-SYNC>"
    "<FALL-BACK-INTERNAL>false</FALL-BACK-INTERNAL>"
    "<FLEXRAY-FIFOS>"
    "<FLEXRAY-FIFO-CONFIGURATION>"
    "<BASE-CYCLE>1</BASE-CYCLE>"
    "<FIFO-DEPTH>8</FIFO-DEPTH>"
    "<MSG-ID-MASK>16</MSG-ID-MASK>"
    "</FLEXRAY-FIFO-CONFIGURATION>"
    "</FLEXRAY-FIFOS>"
    "<KEY-SLOT-ID>2</KEY-SLOT-ID>"
    "<KEY-SLOT-ONLY-ENABLED>true</KEY-SLOT-ONLY-ENABLED>"
    "<KEY-SLOT-USED-FOR-START-UP>true</KEY-SLOT-USED-FOR-START-UP>"
    "<KEY-SLOT-USED-FOR-SYNC>false</KEY-SLOT-USED-FOR-SYNC>"
    "<LATEST-TX>10</LATEST-TX>"
    "<LISTEN-TIMEOUT>100</LISTEN-TIMEOUT>"
    "<MACRO-INITIAL-OFFSET-A>30</MACRO-INITIAL-OFFSET-A>"
    "<MACRO-INITIAL-OFFSET-B>31</MACRO-INITIAL-OFFSET-B>"
    "<MAXIMUM-DYNAMIC-PAYLOAD-LENGTH>14</MAXIMUM-DYNAMIC-PAYLOAD-LENGTH>"
    "<MICRO-INITIAL-OFFSET-A>15</MICRO-INITIAL-OFFSET-A>"
    "<MICRO-INITIAL-OFFSET-B>16</MICRO-INITIAL-OFFSET-B>"
    "<MICRO-PER-CYCLE>17</MICRO-PER-CYCLE>"
    "<MICROTICK-DURATION>0.05</MICROTICK-DURATION>"
    "<NM-VECTOR-EARLY-UPDATE>true</NM-VECTOR-EARLY-UPDATE>"
    "<OFFSET-CORRECTION-OUT>18</OFFSET-CORRECTION-OUT>"
    "<RATE-CORRECTION-OUT>19</RATE-CORRECTION-OUT>"
    "<SAMPLES-PER-MICROTICK>20</SAMPLES-PER-MICROTICK>"
    "<SECOND-KEY-SLOT-ID>21</SECOND-KEY-SLOT-ID>"
    "<TWO-KEY-SLOT-MODE>false</TWO-KEY-SLOT-MODE>"
    "<WAKE-UP-PATTERN>22</WAKE-UP-PATTERN>"
)

FULL_CONTROLLER = (
    "<COMM-CONTROLLERS>"
    "<FLEXRAY-COMMUNICATION-CONTROLLER>"
    "<SHORT-NAME>ctrl</SHORT-NAME>"
    "<WAKE-UP-BY-CONTROLLER-SUPPORTED>true</WAKE-UP-BY-CONTROLLER-SUPPORTED>"
    "<FLEXRAY-COMMUNICATION-CONTROLLER-VARIANTS>"
    "<FLEXRAY-COMMUNICATION-CONTROLLER-CONDITIONAL>" + CONDITIONAL_CONTENT + "</FLEXRAY-COMMUNICATION-CONTROLLER-CONDITIONAL>"
    "</FLEXRAY-COMMUNICATION-CONTROLLER-VARIANTS>"
    "</FLEXRAY-COMMUNICATION-CONTROLLER>"
    "</COMM-CONTROLLERS>"
)

BARE_CONTROLLER = (
    "<COMM-CONTROLLERS>"
    "<FLEXRAY-COMMUNICATION-CONTROLLER>"
    "<SHORT-NAME>ctrl</SHORT-NAME>"
    "<WAKE-UP-BY-CONTROLLER-SUPPORTED>true</WAKE-UP-BY-CONTROLLER-SUPPORTED>"
    "</FLEXRAY-COMMUNICATION-CONTROLLER>"
    "</COMM-CONTROLLERS>"
)


def _read_into_instance(inner):
    root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner))
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    instance = EcuInstance(pkg, "Ecu")
    ARXMLParser().readEcuInstanceCommControllers(root, instance)
    return instance


class TestReadFlexrayCommunicationController:
    def test_dispatch_creates_flexray_controller_with_short_name(self, parser):
        instance = _read_into_instance(BARE_CONTROLLER)
        controllers = instance.getCommControllers()
        assert len(controllers) == 1
        controller = controllers[0]
        assert isinstance(controller, FlexrayCommunicationController)
        assert controller.getShortName() == "ctrl"

    def test_reads_base_wake_up_by_controller_supported(self, parser):
        instance = _read_into_instance(BARE_CONTROLLER)
        controller = instance.getCommControllers()[0]
        flag = controller.getWakeUpByControllerSupported()
        assert isinstance(flag, Boolean)
        assert flag.getValue() is True

    def test_reads_all_fields_with_values_and_types(self, parser):
        instance = _read_into_instance(FULL_CONTROLLER)
        controller = instance.getCommControllers()[0]

        assert isinstance(controller.getAcceptedStartupRange(), Integer)
        assert controller.getAcceptedStartupRange().getValue() == 4
        assert isinstance(controller.getAllowHaltDueToClock(), Boolean)
        assert controller.getAllowHaltDueToClock().getValue() is True
        assert controller.getAllowPassiveToActive().getValue() == 3
        assert controller.getClusterDriftDamping().getValue() == 2
        assert controller.getDecodingCorrection().getValue() == 1
        assert controller.getDelayCompensationA().getValue() == 6
        assert controller.getDelayCompensationB().getValue() == 7
        assert controller.getExternOffsetCorrection().getValue() == 8
        assert controller.getExternRateCorrection().getValue() == 9
        assert isinstance(controller.getExternalSync(), Boolean)
        assert controller.getExternalSync().getValue() is True
        assert controller.getFallBackInternal().getValue() is False
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
        assert controller.getTwoKeySlotMode().getValue() is False
        assert controller.getWakeUpPattern().getValue() == 22

    def test_reads_positive_integer_leaves_as_positive_integer(self, parser):
        instance = _read_into_instance(FULL_CONTROLLER)
        controller = instance.getCommControllers()[0]
        assert isinstance(controller.getKeySlotID(), PositiveInteger)
        assert controller.getKeySlotID().getValue() == 2
        assert isinstance(controller.getSecondKeySlotId(), PositiveInteger)
        assert controller.getSecondKeySlotId().getValue() == 21

    def test_reads_flexray_fifo_with_field_values(self, parser):
        instance = _read_into_instance(FULL_CONTROLLER)
        controller = instance.getCommControllers()[0]
        fifos = controller.getFlexrayFifos()
        assert len(fifos) == 1
        fifo = fifos[0]
        assert isinstance(fifo, FlexrayFifoConfiguration)
        assert fifo.getBaseCycle().getValue() == 1
        assert fifo.getFifoDepth().getValue() == 8
        assert fifo.getMsgIdMask().getValue() == 16

    def test_reads_controller_without_flexray_elements_to_none_fields(self, parser):
        instance = _read_into_instance(BARE_CONTROLLER)
        controller = instance.getCommControllers()[0]
        assert controller.getAcceptedStartupRange() is None
        assert controller.getFlexrayFifos() == []
        assert controller.getKeySlotID() is None
        assert controller.getWakeUpPattern() is None
