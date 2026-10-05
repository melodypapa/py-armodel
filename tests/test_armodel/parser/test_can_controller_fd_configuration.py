"""Parser tests for CanControllerFdConfiguration (Table 3.16, p.66).

The class models the XSD complexType CAN-CONTROLLER-FD-CONFIGURATION
(AUTOSAR_00052.xsd line 14711) whose element content is the XSD group
CAN-CONTROLLER-FD-CONFIGURATION (line 14649): PADDING-VALUE, PROP-SEG,
SSP-OFFSET, SYNC-JUMP-WIDTH, TIME-SEG-1, TIME-SEG-2,
TRCV-DELAY-COMPENSATION-OFFSET (atp.Status="removed" — not in the R23-11
PDF table, Rule 0015), TX-BIT-RATE-SWITCH. The class has no standalone
XML element of its own; it is consumed via the CAN-CONTROLLER-FD-ATTRIBUTES
element (line 169, inside ABSTRACT-CAN-COMMUNICATION-CONTROLLER-ATTRIBUTES)
and the CAN-FD-CONFIG element (line 16268, inside CAN-XL-PROPS)
(Rule 0001.7).
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
    CanControllerConfigurationRequirements,
    CanControllerFdConfiguration,
)
from armodel.parser.arxml_parser import ARXMLParser
from tests.test_armodel.parser._helpers import _snip

FD_ATTRIBUTES_LEAF_TAGS = [
    "PADDING-VALUE",
    "PROP-SEG",
    "SSP-OFFSET",
    "SYNC-JUMP-WIDTH",
    "TIME-SEG-1",
    "TIME-SEG-2",
    "TX-BIT-RATE-SWITCH",
]


def _read_fd_attributes(inner: str, attrs: str = "") -> CanControllerConfigurationRequirements:
    holder = CanControllerConfigurationRequirements()
    ARXMLParser().readAbstractCanCommunicationControllerAttributes(_snip(inner, attrs=attrs), holder)
    return holder


class TestReadCanControllerFdConfiguration:
    def test_reads_all_fields_with_values(self, parser):
        holder = _read_fd_attributes(
            "<CAN-CONTROLLER-FD-ATTRIBUTES>"
            "<PADDING-VALUE>8</PADDING-VALUE>"
            "<PROP-SEG>4</PROP-SEG>"
            "<SSP-OFFSET>5</SSP-OFFSET>"
            "<SYNC-JUMP-WIDTH>1</SYNC-JUMP-WIDTH>"
            "<TIME-SEG-1>13</TIME-SEG-1>"
            "<TIME-SEG-2>2</TIME-SEG-2>"
            "<TX-BIT-RATE-SWITCH>true</TX-BIT-RATE-SWITCH>"
            "</CAN-CONTROLLER-FD-ATTRIBUTES>"
        )
        fd = holder.getCanControllerFdAttributes()
        assert isinstance(fd, CanControllerFdConfiguration)
        assert fd.getPaddingValue().getValue() == 8
        assert fd.getPropSeg().getValue() == 4
        assert fd.getSspOffset().getValue() == 5
        assert fd.getSyncJumpWidth().getValue() == 1
        assert fd.getTimeSeg1().getValue() == 13
        assert fd.getTimeSeg2().getValue() == 2
        assert fd.getTxBitRateSwitch().getValue() is True

    def test_reads_positive_integer_fields_as_positive_integer(self, parser):
        holder = _read_fd_attributes("<CAN-CONTROLLER-FD-ATTRIBUTES><PADDING-VALUE>8</PADDING-VALUE></CAN-CONTROLLER-FD-ATTRIBUTES>")
        fd = holder.getCanControllerFdAttributes()
        assert isinstance(fd.getPaddingValue(), PositiveInteger)

    def test_reads_s_t_attributes_from_fd_attributes_element(self, parser):
        holder = _read_fd_attributes('<CAN-CONTROLLER-FD-ATTRIBUTES S="1234" T="2024-01-01T00:00:00Z"><PADDING-VALUE>8</PADDING-VALUE></CAN-CONTROLLER-FD-ATTRIBUTES>')
        fd = holder.getCanControllerFdAttributes()
        assert fd.getChecksum().getValue() == "1234"
        assert fd.getTimestamp().getValue() == "2024-01-01T00:00:00Z"

    def test_reads_through_can_fd_config_consumer_element(self, parser):
        element = _snip("<CAN-FD-CONFIG>" "<PADDING-VALUE>8</PADDING-VALUE>" "<TX-BIT-RATE-SWITCH>false</TX-BIT-RATE-SWITCH>" "</CAN-FD-CONFIG>")
        fd = ARXMLParser().getCanControllerFdConfiguration(element, "CAN-FD-CONFIG")
        assert isinstance(fd, CanControllerFdConfiguration)
        assert fd.getPaddingValue().getValue() == 8
        assert fd.getTxBitRateSwitch().getValue() is False

    def test_empty_wrapper_element_leaves_all_none(self, parser):
        holder = _read_fd_attributes("<CAN-CONTROLLER-FD-ATTRIBUTES/>")
        fd = holder.getCanControllerFdAttributes()
        assert isinstance(fd, CanControllerFdConfiguration)
        assert fd.getPaddingValue() is None
        assert fd.getPropSeg() is None
        assert fd.getSspOffset() is None
        assert fd.getSyncJumpWidth() is None
        assert fd.getTimeSeg1() is None
        assert fd.getTimeSeg2() is None
        assert fd.getTxBitRateSwitch() is None

    def test_absent_wrapper_element_leaves_attribute_none(self, parser):
        holder = _read_fd_attributes("<OTHER/>")
        assert holder.getCanControllerFdAttributes() is None
