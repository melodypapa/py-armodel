"""Parser tests for AbstractCanCommunicationControllerAttributes (Table 3.13, p.64).

XML element order per XSD group ABSTRACT-CAN-COMMUNICATION-CONTROLLER-ATTRIBUTES
(AUTOSAR_00052.xsd line 160): CAN-CONTROLLER-FD-ATTRIBUTES (line 169, type
CAN-CONTROLLER-FD-CONFIGURATION), CAN-CONTROLLER-FD-REQUIREMENTS (line 175, type
CAN-CONTROLLER-FD-CONFIGURATION-REQUIREMENTS), CAN-CONTROLLER-XL-ATTRIBUTES
(line 181, type CAN-CONTROLLER-XL-CONFIGURATION), CAN-CONTROLLER-XL-REQUIREMENTS
(line 187, type CAN-CONTROLLER-XL-CONFIGURATION-REQUIREMENTS). The class is a pure
XSD element group with no own element; it is consumed inline by
CAN-CONTROLLER-CONFIGURATION and CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS
(Rule 0001.7).
"""

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
    CanControllerConfigurationRequirements,
    CanControllerFdConfiguration,
    CanControllerFdConfigurationRequirements,
    CanControllerXlConfiguration,
    CanControllerXlConfigurationRequirements,
)
from armodel.parser.arxml_parser import ARXMLParser
from tests.test_armodel.parser._helpers import _snip


def _read_into(inner: str, attrs: str = "") -> CanControllerConfigurationRequirements:
    holder = CanControllerConfigurationRequirements()
    ARXMLParser().readAbstractCanCommunicationControllerAttributes(_snip(inner, attrs=attrs), holder)
    return holder


class TestReadAbstractCanCommunicationControllerAttributes:
    def test_reads_fd_attributes_with_values(self, parser):
        attributes = _read_into(
            "<CAN-CONTROLLER-FD-ATTRIBUTES>" "<PADDING-VALUE>8</PADDING-VALUE>" "<PROP-SEG>4</PROP-SEG>" "<TX-BIT-RATE-SWITCH>true</TX-BIT-RATE-SWITCH>" "</CAN-CONTROLLER-FD-ATTRIBUTES>"
        )
        fd = attributes.getCanControllerFdAttributes()
        assert isinstance(fd, CanControllerFdConfiguration)
        assert fd.getPaddingValue().getValue() == 8
        assert fd.getPropSeg().getValue() == 4
        assert fd.getTxBitRateSwitch().getValue() is True
        assert attributes.getCanControllerFdRequirements() is None
        assert attributes.getCanControllerXlAttributes() is None
        assert attributes.getCanControllerXlRequirements() is None

    def test_reads_fd_requirements_with_values(self, parser):
        attributes = _read_into(
            "<CAN-CONTROLLER-FD-REQUIREMENTS>"
            "<MAX-NUMBER-OF-TIME-QUANTA-PER-BIT>32</MAX-NUMBER-OF-TIME-QUANTA-PER-BIT>"
            "<MIN-NUMBER-OF-TIME-QUANTA-PER-BIT>16</MIN-NUMBER-OF-TIME-QUANTA-PER-BIT>"
            "<TX-BIT-RATE-SWITCH>false</TX-BIT-RATE-SWITCH>"
            "</CAN-CONTROLLER-FD-REQUIREMENTS>"
        )
        fd_req = attributes.getCanControllerFdRequirements()
        assert isinstance(fd_req, CanControllerFdConfigurationRequirements)
        assert fd_req.getMaxNumberOfTimeQuantaPerBit().getValue() == 32
        assert fd_req.getMinNumberOfTimeQuantaPerBit().getValue() == 16
        assert fd_req.getTxBitRateSwitch().getValue() is False
        assert attributes.getCanControllerFdAttributes() is None

    def test_reads_xl_attributes_with_values(self, parser):
        attributes = _read_into(
            "<CAN-CONTROLLER-XL-ATTRIBUTES>"
            "<ERROR-SIGNALING-ENABLED>true</ERROR-SIGNALING-ENABLED>"
            "<PROP-SEG>6</PROP-SEG>"
            "<PWM-L>2</PWM-L>"
            "<TRCV-PWM-MODE-ENABLED>false</TRCV-PWM-MODE-ENABLED>"
            "</CAN-CONTROLLER-XL-ATTRIBUTES>"
        )
        xl = attributes.getCanControllerXlAttributes()
        assert isinstance(xl, CanControllerXlConfiguration)
        assert xl.getErrorSignalingEnabled().getValue() is True
        assert xl.getPropSeg().getValue() == 6
        assert xl.getPwmL().getValue() == 2
        assert xl.getTrcvPwmModeEnabled().getValue() is False
        assert attributes.getCanControllerXlRequirements() is None

    def test_reads_xl_requirements_with_values(self, parser):
        attributes = _read_into("<CAN-CONTROLLER-XL-REQUIREMENTS>" "<MAX-PWM-L>4</MAX-PWM-L>" "<MIN-PWM-L>1</MIN-PWM-L>" "</CAN-CONTROLLER-XL-REQUIREMENTS>")
        xl_req = attributes.getCanControllerXlRequirements()
        assert isinstance(xl_req, CanControllerXlConfigurationRequirements)
        assert xl_req.getMaxPwmL().getValue() == 4
        assert xl_req.getMinPwmL().getValue() == 1
        assert attributes.getCanControllerXlAttributes() is None

    def test_reads_arobject_s_t_from_consumer_element(self, parser):
        attributes = _read_into(
            "<CAN-CONTROLLER-FD-ATTRIBUTES><PADDING-VALUE>8</PADDING-VALUE></CAN-CONTROLLER-FD-ATTRIBUTES>",
            attrs=' S="1234" T="2024-01-01T00:00:00Z"',
        )
        assert attributes.getChecksum().getValue() == "1234"
        assert attributes.getTimestamp().getValue() == "2024-01-01T00:00:00Z"

    def test_reads_full_group_in_xsd_order(self, parser):
        attributes = _read_into(
            "<CAN-CONTROLLER-FD-ATTRIBUTES><PADDING-VALUE>8</PADDING-VALUE></CAN-CONTROLLER-FD-ATTRIBUTES>"
            "<CAN-CONTROLLER-FD-REQUIREMENTS><MAX-NUMBER-OF-TIME-QUANTA-PER-BIT>32</MAX-NUMBER-OF-TIME-QUANTA-PER-BIT></CAN-CONTROLLER-FD-REQUIREMENTS>"
            "<CAN-CONTROLLER-XL-ATTRIBUTES><PROP-SEG>6</PROP-SEG></CAN-CONTROLLER-XL-ATTRIBUTES>"
            "<CAN-CONTROLLER-XL-REQUIREMENTS><MAX-PWM-L>4</MAX-PWM-L></CAN-CONTROLLER-XL-REQUIREMENTS>"
        )
        assert isinstance(attributes.getCanControllerFdAttributes(), CanControllerFdConfiguration)
        assert isinstance(attributes.getCanControllerFdRequirements(), CanControllerFdConfigurationRequirements)
        assert isinstance(attributes.getCanControllerXlAttributes(), CanControllerXlConfiguration)
        assert isinstance(attributes.getCanControllerXlRequirements(), CanControllerXlConfigurationRequirements)
        assert attributes.getCanControllerFdAttributes().getPaddingValue().getValue() == 8
        assert attributes.getCanControllerFdRequirements().getMaxNumberOfTimeQuantaPerBit().getValue() == 32
        assert attributes.getCanControllerXlAttributes().getPropSeg().getValue() == 6
        assert attributes.getCanControllerXlRequirements().getMaxPwmL().getValue() == 4

    def test_empty_group_leaves_all_none(self, parser):
        attributes = _read_into("<OTHER/>")
        assert attributes.getCanControllerFdAttributes() is None
        assert attributes.getCanControllerFdRequirements() is None
        assert attributes.getCanControllerXlAttributes() is None
        assert attributes.getCanControllerXlRequirements() is None
        assert attributes.getChecksum() is None
        assert attributes.getTimestamp() is None
