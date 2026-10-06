"""Parser tests for CanControllerXlConfigurationRequirements (Table 3.19, p.72).

The class models the XSD complexType CAN-CONTROLLER-XL-CONFIGURATION-REQUIREMENTS
(AUTOSAR_00052.xsd line 15016) whose element content is the XSD group
CAN-CONTROLLER-XL-CONFIGURATION-REQUIREMENTS (line 14902): ERROR-SIGNALING-ENABLED,
MAX-NUMBER-OF-TIME-QUANTA-PER-BIT, MAX-PWM-L, MAX-PWM-O, MAX-PWM-S,
MAX-SAMPLE-POINT, MAX-SYNC-JUMP-WIDTH, MAX-TRCV-DELAY-COMPENSATION-OFFSET,
MIN-NUMBER-OF-TIME-QUANTA-PER-BIT, MIN-PWM-L, MIN-PWM-O, MIN-PWM-S,
MIN-SAMPLE-POINT, MIN-SYNC-JUMP-WIDTH, MIN-TRCV-DELAY-COMPENSATION-OFFSET,
TRCV-PWM-MODE-ENABLED. The class has no standalone XML element of its own; it
is consumed via the CAN-CONTROLLER-XL-REQUIREMENTS element (line 187, inside
ABSTRACT-CAN-COMMUNICATION-CONTROLLER-ATTRIBUTES) and the CAN-XL-CONFIG-REQS
element (line 16286, inside CAN-XL-PROPS) (Rule 0001.7).
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
    CanControllerConfigurationRequirements,
    CanControllerXlConfigurationRequirements,
)
from armodel.parser.arxml_parser import ARXMLParser
from tests.test_armodel.parser._helpers import _snip

XL_REQUIREMENTS_LEAF_TAGS = [
    "ERROR-SIGNALING-ENABLED",
    "MAX-NUMBER-OF-TIME-QUANTA-PER-BIT",
    "MAX-PWM-L",
    "MAX-PWM-O",
    "MAX-PWM-S",
    "MAX-SAMPLE-POINT",
    "MAX-SYNC-JUMP-WIDTH",
    "MAX-TRCV-DELAY-COMPENSATION-OFFSET",
    "MIN-NUMBER-OF-TIME-QUANTA-PER-BIT",
    "MIN-PWM-L",
    "MIN-PWM-O",
    "MIN-PWM-S",
    "MIN-SAMPLE-POINT",
    "MIN-SYNC-JUMP-WIDTH",
    "MIN-TRCV-DELAY-COMPENSATION-OFFSET",
    "TRCV-PWM-MODE-ENABLED",
]


def _read_xl_requirements(inner: str, attrs: str = "") -> CanControllerConfigurationRequirements:
    holder = CanControllerConfigurationRequirements()
    ARXMLParser().readAbstractCanCommunicationControllerAttributes(_snip(inner, attrs=attrs), holder)
    return holder


class TestReadCanControllerXlConfigurationRequirements:
    def test_reads_all_fields_with_values(self, parser):
        holder = _read_xl_requirements(
            "<CAN-CONTROLLER-XL-REQUIREMENTS>"
            "<ERROR-SIGNALING-ENABLED>true</ERROR-SIGNALING-ENABLED>"
            "<MAX-NUMBER-OF-TIME-QUANTA-PER-BIT>32</MAX-NUMBER-OF-TIME-QUANTA-PER-BIT>"
            "<MAX-PWM-L>100</MAX-PWM-L>"
            "<MAX-PWM-O>20</MAX-PWM-O>"
            "<MAX-PWM-S>30</MAX-PWM-S>"
            "<MAX-SAMPLE-POINT>0.8</MAX-SAMPLE-POINT>"
            "<MAX-SYNC-JUMP-WIDTH>0.2</MAX-SYNC-JUMP-WIDTH>"
            "<MAX-TRCV-DELAY-COMPENSATION-OFFSET>0.001</MAX-TRCV-DELAY-COMPENSATION-OFFSET>"
            "<MIN-NUMBER-OF-TIME-QUANTA-PER-BIT>16</MIN-NUMBER-OF-TIME-QUANTA-PER-BIT>"
            "<MIN-PWM-L>3</MIN-PWM-L>"
            "<MIN-PWM-O>4</MIN-PWM-O>"
            "<MIN-PWM-S>5</MIN-PWM-S>"
            "<MIN-SAMPLE-POINT>0.7</MIN-SAMPLE-POINT>"
            "<MIN-SYNC-JUMP-WIDTH>0.1</MIN-SYNC-JUMP-WIDTH>"
            "<MIN-TRCV-DELAY-COMPENSATION-OFFSET>0.0005</MIN-TRCV-DELAY-COMPENSATION-OFFSET>"
            "<TRCV-PWM-MODE-ENABLED>false</TRCV-PWM-MODE-ENABLED>"
            "</CAN-CONTROLLER-XL-REQUIREMENTS>"
        )
        req = holder.getCanControllerXlRequirements()
        assert isinstance(req, CanControllerXlConfigurationRequirements)
        assert req.getErrorSignalingEnabled().getValue() is True
        assert req.getMaxNumberOfTimeQuantaPerBit().getValue() == 32
        assert req.getMaxPwmL().getValue() == 100
        assert req.getMaxPwmO().getValue() == 20
        assert req.getMaxPwmS().getValue() == 30
        assert req.getMaxSamplePoint().getValue() == 0.8
        assert req.getMaxSyncJumpWidth().getValue() == 0.2
        assert req.getMaxTrcvDelayCompensationOffset().getValue() == 0.001
        assert req.getMinNumberOfTimeQuantaPerBit().getValue() == 16
        assert req.getMinPwmL().getValue() == 3
        assert req.getMinPwmO().getValue() == 4
        assert req.getMinPwmS().getValue() == 5
        assert req.getMinSamplePoint().getValue() == 0.7
        assert req.getMinSyncJumpWidth().getValue() == 0.1
        assert req.getMinTrcvDelayCompensationOffset().getValue() == 0.0005
        assert req.getTrcvPwmModeEnabled().getValue() is False

    def test_reads_pwm_fields_as_positive_integer(self, parser):
        holder = _read_xl_requirements(
            "<CAN-CONTROLLER-XL-REQUIREMENTS>"
            "<MAX-PWM-L>100</MAX-PWM-L>"
            "<MAX-PWM-O>20</MAX-PWM-O>"
            "<MAX-PWM-S>30</MAX-PWM-S>"
            "<MIN-PWM-L>3</MIN-PWM-L>"
            "<MIN-PWM-O>4</MIN-PWM-O>"
            "<MIN-PWM-S>5</MIN-PWM-S>"
            "</CAN-CONTROLLER-XL-REQUIREMENTS>"
        )
        req = holder.getCanControllerXlRequirements()
        assert isinstance(req.getMaxPwmL(), PositiveInteger)
        assert isinstance(req.getMaxPwmO(), PositiveInteger)
        assert isinstance(req.getMaxPwmS(), PositiveInteger)
        assert isinstance(req.getMinPwmL(), PositiveInteger)
        assert isinstance(req.getMinPwmO(), PositiveInteger)
        assert isinstance(req.getMinPwmS(), PositiveInteger)

    def test_reads_s_t_attributes_from_xl_requirements_element(self, parser):
        holder = _read_xl_requirements('<CAN-CONTROLLER-XL-REQUIREMENTS S="1234" T="2024-01-01T00:00:00Z"><MAX-PWM-L>100</MAX-PWM-L></CAN-CONTROLLER-XL-REQUIREMENTS>')
        req = holder.getCanControllerXlRequirements()
        assert req.getChecksum().getValue() == "1234"
        assert req.getTimestamp().getValue() == "2024-01-01T00:00:00Z"

    def test_reads_through_can_xl_config_reqs_consumer_element(self, parser):
        element = _snip(
            '<CAN-XL-CONFIG-REQS S="5678" T="2024-06-01T12:00:00Z">'
            "<ERROR-SIGNALING-ENABLED>true</ERROR-SIGNALING-ENABLED>"
            "<MAX-PWM-L>100</MAX-PWM-L>"
            "<MIN-SYNC-JUMP-WIDTH>0.1</MIN-SYNC-JUMP-WIDTH>"
            "</CAN-XL-CONFIG-REQS>"
        )
        req = ARXMLParser().getCanControllerXlConfigurationRequirements(element, "CAN-XL-CONFIG-REQS")
        assert isinstance(req, CanControllerXlConfigurationRequirements)
        assert req.getErrorSignalingEnabled().getValue() is True
        assert req.getMaxPwmL().getValue() == 100
        assert req.getMinSyncJumpWidth().getValue() == 0.1
        assert req.getChecksum().getValue() == "5678"
        assert req.getTimestamp().getValue() == "2024-06-01T12:00:00Z"

    def test_empty_wrapper_element_leaves_all_none(self, parser):
        holder = _read_xl_requirements("<CAN-CONTROLLER-XL-REQUIREMENTS/>")
        req = holder.getCanControllerXlRequirements()
        assert isinstance(req, CanControllerXlConfigurationRequirements)
        assert req.getErrorSignalingEnabled() is None
        assert req.getMaxNumberOfTimeQuantaPerBit() is None
        assert req.getMaxPwmL() is None
        assert req.getMaxPwmO() is None
        assert req.getMaxPwmS() is None
        assert req.getMaxSamplePoint() is None
        assert req.getMaxSyncJumpWidth() is None
        assert req.getMaxTrcvDelayCompensationOffset() is None
        assert req.getMinNumberOfTimeQuantaPerBit() is None
        assert req.getMinPwmL() is None
        assert req.getMinPwmO() is None
        assert req.getMinPwmS() is None
        assert req.getMinSamplePoint() is None
        assert req.getMinSyncJumpWidth() is None
        assert req.getMinTrcvDelayCompensationOffset() is None
        assert req.getTrcvPwmModeEnabled() is None

    def test_absent_wrapper_element_leaves_attribute_none(self, parser):
        holder = _read_xl_requirements("<OTHER/>")
        assert holder.getCanControllerXlRequirements() is None
