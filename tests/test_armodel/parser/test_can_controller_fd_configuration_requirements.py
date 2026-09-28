"""Parser tests for CanControllerFdConfigurationRequirements (Table 3.17, pp.66-67).

XML element order per XSD group CAN-CONTROLLER-FD-CONFIGURATION-REQUIREMENTS
(AUTOSAR_00052.xsd line 14724): MAX-NUMBER-OF-TIME-QUANTA-PER-BIT,
MAX-SAMPLE-POINT, MAX-SYNC-JUMP-WIDTH, MAX-TRCV-DELAY-COMPENSATION-OFFSET,
MIN-NUMBER-OF-TIME-QUANTA-PER-BIT, MIN-SAMPLE-POINT, MIN-SYNC-JUMP-WIDTH,
MIN-TRCV-DELAY-COMPENSATION-OFFSET, PADDING-VALUE, TX-BIT-RATE-SWITCH.
Coverage runs through the spec aggregator AbstractCanCommunicationAttributes
(CAN-CONTROLLER-FD-REQUIREMENTS element, AUTOSAR_00052.xsd line 175). No
ref/DEST attributes exist in this class's element set (ten 0..1 attr leaves
only).
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Float, Integer, PositiveInteger, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
    CanControllerConfigurationRequirements,
    CanControllerFdConfigurationRequirements,
)
from armodel.parser.arxml_parser import ARXMLParser
from tests.test_armodel.parser._helpers import _snip

FULL_FD_REQUIREMENTS = (
    "<CAN-CONTROLLER-FD-REQUIREMENTS>"
    "<MAX-NUMBER-OF-TIME-QUANTA-PER-BIT>32</MAX-NUMBER-OF-TIME-QUANTA-PER-BIT>"
    "<MAX-SAMPLE-POINT>0.8</MAX-SAMPLE-POINT>"
    "<MAX-SYNC-JUMP-WIDTH>0.2</MAX-SYNC-JUMP-WIDTH>"
    "<MAX-TRCV-DELAY-COMPENSATION-OFFSET>0.001</MAX-TRCV-DELAY-COMPENSATION-OFFSET>"
    "<MIN-NUMBER-OF-TIME-QUANTA-PER-BIT>16</MIN-NUMBER-OF-TIME-QUANTA-PER-BIT>"
    "<MIN-SAMPLE-POINT>0.7</MIN-SAMPLE-POINT>"
    "<MIN-SYNC-JUMP-WIDTH>0.1</MIN-SYNC-JUMP-WIDTH>"
    "<MIN-TRCV-DELAY-COMPENSATION-OFFSET>0.0005</MIN-TRCV-DELAY-COMPENSATION-OFFSET>"
    "<PADDING-VALUE>8</PADDING-VALUE>"
    "<TX-BIT-RATE-SWITCH>true</TX-BIT-RATE-SWITCH>"
    "</CAN-CONTROLLER-FD-REQUIREMENTS>"
)


def _read_fd_requirements(inner):
    holder = CanControllerConfigurationRequirements()
    ARXMLParser().readAbstractCanCommunicationControllerAttributes(_snip(inner), holder)
    return holder


def _assert_full_fd_requirements(req):
    assert isinstance(req, CanControllerFdConfigurationRequirements)

    value = req.getMaxNumberOfTimeQuantaPerBit()
    assert isinstance(value, Integer)
    assert value.getValue() == 32

    value = req.getMaxSamplePoint()
    assert isinstance(value, Float)
    assert value.getValue() == 0.8

    value = req.getMaxSyncJumpWidth()
    assert isinstance(value, Float)
    assert value.getValue() == 0.2

    value = req.getMaxTrcvDelayCompensationOffset()
    assert isinstance(value, TimeValue)
    assert value.getValue() == 0.001

    value = req.getMinNumberOfTimeQuantaPerBit()
    assert isinstance(value, Integer)
    assert value.getValue() == 16

    value = req.getMinSamplePoint()
    assert isinstance(value, Float)
    assert value.getValue() == 0.7

    value = req.getMinSyncJumpWidth()
    assert isinstance(value, Float)
    assert value.getValue() == 0.1

    value = req.getMinTrcvDelayCompensationOffset()
    assert isinstance(value, TimeValue)
    assert value.getValue() == 0.0005

    value = req.getPaddingValue()
    assert isinstance(value, PositiveInteger)
    assert value.getValue() == 8

    value = req.getTxBitRateSwitch()
    assert isinstance(value, Boolean)
    assert value.getValue() is True


class TestReadCanControllerFdConfigurationRequirements:
    def test_reads_all_ten_fields_with_values_and_types(self, parser):
        holder = _read_fd_requirements(FULL_FD_REQUIREMENTS)
        _assert_full_fd_requirements(holder.getCanControllerFdRequirements())

    def test_reads_empty_requirements_to_none_fields(self, parser):
        holder = _read_fd_requirements("<CAN-CONTROLLER-FD-REQUIREMENTS/>")
        req = holder.getCanControllerFdRequirements()
        assert isinstance(req, CanControllerFdConfigurationRequirements)
        assert req.getMaxNumberOfTimeQuantaPerBit() is None
        assert req.getMaxSamplePoint() is None
        assert req.getMaxSyncJumpWidth() is None
        assert req.getMaxTrcvDelayCompensationOffset() is None
        assert req.getMinNumberOfTimeQuantaPerBit() is None
        assert req.getMinSamplePoint() is None
        assert req.getMinSyncJumpWidth() is None
        assert req.getMinTrcvDelayCompensationOffset() is None
        assert req.getPaddingValue() is None
        assert req.getTxBitRateSwitch() is None

    def test_absent_requirements_left_none(self, parser):
        holder = _read_fd_requirements("")
        assert holder.getCanControllerFdRequirements() is None
