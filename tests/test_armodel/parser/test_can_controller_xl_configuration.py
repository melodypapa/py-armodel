"""Parser tests for CanControllerXlConfiguration (Table 3.18, p.71).

The class models the XSD complexType CAN-CONTROLLER-XL-CONFIGURATION
(AUTOSAR_00052.xsd line 14889) whose element content is the XSD group
CAN-CONTROLLER-XL-CONFIGURATION (line 14811): ERROR-SIGNALING-ENABLED,
PROP-SEG, PWM-L, PWM-O, PWM-S, SSP-OFFSET, SYNC-JUMP-WIDTH, TIME-SEG-1,
TIME-SEG-2, TRCV-PWM-MODE-ENABLED. The class has no standalone XML element
of its own; it is consumed via the CAN-CONTROLLER-XL-ATTRIBUTES element
(line 181, inside ABSTRACT-CAN-COMMUNICATION-CONTROLLER-ATTRIBUTES) and the
CAN-XL-CONFIG element (line 16280, inside CAN-XL-PROPS) (Rule 0001.7).
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
    CanControllerConfigurationRequirements,
    CanControllerXlConfiguration,
)
from armodel.parser.arxml_parser import ARXMLParser
from tests.test_armodel.parser._helpers import _snip

XL_ATTRIBUTES_LEAF_TAGS = [
    "ERROR-SIGNALING-ENABLED",
    "PROP-SEG",
    "PWM-L",
    "PWM-O",
    "PWM-S",
    "SSP-OFFSET",
    "SYNC-JUMP-WIDTH",
    "TIME-SEG-1",
    "TIME-SEG-2",
    "TRCV-PWM-MODE-ENABLED",
]


def _read_xl_attributes(inner: str, attrs: str = "") -> CanControllerConfigurationRequirements:
    holder = CanControllerConfigurationRequirements()
    ARXMLParser().readAbstractCanCommunicationControllerAttributes(_snip(inner, attrs=attrs), holder)
    return holder


class TestReadCanControllerXlConfiguration:
    def test_reads_all_fields_with_values(self, parser):
        holder = _read_xl_attributes(
            "<CAN-CONTROLLER-XL-ATTRIBUTES>"
            "<ERROR-SIGNALING-ENABLED>true</ERROR-SIGNALING-ENABLED>"
            "<PROP-SEG>4</PROP-SEG>"
            "<PWM-L>100</PWM-L>"
            "<PWM-O>20</PWM-O>"
            "<PWM-S>30</PWM-S>"
            "<SSP-OFFSET>5</SSP-OFFSET>"
            "<SYNC-JUMP-WIDTH>1</SYNC-JUMP-WIDTH>"
            "<TIME-SEG-1>61</TIME-SEG-1>"
            "<TIME-SEG-2>14</TIME-SEG-2>"
            "<TRCV-PWM-MODE-ENABLED>false</TRCV-PWM-MODE-ENABLED>"
            "</CAN-CONTROLLER-XL-ATTRIBUTES>"
        )
        xl = holder.getCanControllerXlAttributes()
        assert isinstance(xl, CanControllerXlConfiguration)
        assert xl.getErrorSignalingEnabled().getValue() is True
        assert xl.getPropSeg().getValue() == 4
        assert xl.getPwmL().getValue() == 100
        assert xl.getPwmO().getValue() == 20
        assert xl.getPwmS().getValue() == 30
        assert xl.getSspOffset().getValue() == 5
        assert xl.getSyncJumpWidth().getValue() == 1
        assert xl.getTimeSeg1().getValue() == 61
        assert xl.getTimeSeg2().getValue() == 14
        assert xl.getTrcvPwmModeEnabled().getValue() is False

    def test_reads_positive_integer_fields_as_positive_integer(self, parser):
        holder = _read_xl_attributes("<CAN-CONTROLLER-XL-ATTRIBUTES><PROP-SEG>4</PROP-SEG></CAN-CONTROLLER-XL-ATTRIBUTES>")
        xl = holder.getCanControllerXlAttributes()
        assert isinstance(xl.getPropSeg(), PositiveInteger)

    def test_reads_s_t_attributes_from_xl_attributes_element(self, parser):
        holder = _read_xl_attributes('<CAN-CONTROLLER-XL-ATTRIBUTES S="1234" T="2024-01-01T00:00:00Z"><PROP-SEG>4</PROP-SEG></CAN-CONTROLLER-XL-ATTRIBUTES>')
        xl = holder.getCanControllerXlAttributes()
        assert xl.getChecksum().getValue() == "1234"
        assert xl.getTimestamp().getValue() == "2024-01-01T00:00:00Z"

    def test_reads_through_can_xl_config_consumer_element(self, parser):
        element = _snip("<CAN-XL-CONFIG>" "<PROP-SEG>4</PROP-SEG>" "<TIME-SEG-1>61</TIME-SEG-1>" "<TIME-SEG-2>14</TIME-SEG-2>" "<TRCV-PWM-MODE-ENABLED>true</TRCV-PWM-MODE-ENABLED>" "</CAN-XL-CONFIG>")
        xl = ARXMLParser().getCanControllerXlConfiguration(element, "CAN-XL-CONFIG")
        assert isinstance(xl, CanControllerXlConfiguration)
        assert xl.getPropSeg().getValue() == 4
        assert xl.getTimeSeg1().getValue() == 61
        assert xl.getTimeSeg2().getValue() == 14
        assert xl.getTrcvPwmModeEnabled().getValue() is True

    def test_empty_wrapper_element_leaves_all_none(self, parser):
        holder = _read_xl_attributes("<CAN-CONTROLLER-XL-ATTRIBUTES/>")
        xl = holder.getCanControllerXlAttributes()
        assert isinstance(xl, CanControllerXlConfiguration)
        assert xl.getErrorSignalingEnabled() is None
        assert xl.getPropSeg() is None
        assert xl.getPwmL() is None
        assert xl.getPwmO() is None
        assert xl.getPwmS() is None
        assert xl.getSspOffset() is None
        assert xl.getSyncJumpWidth() is None
        assert xl.getTimeSeg1() is None
        assert xl.getTimeSeg2() is None
        assert xl.getTrcvPwmModeEnabled() is None

    def test_absent_wrapper_element_leaves_attribute_none(self, parser):
        holder = _read_xl_attributes("<OTHER/>")
        assert holder.getCanControllerXlAttributes() is None
