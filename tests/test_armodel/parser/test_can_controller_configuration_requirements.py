"""Parser tests for CanControllerConfigurationRequirements (Table 3.15, p.65).

XML element order per XSD complexType CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS:
the ABSTRACT-CAN-COMMUNICATION-CONTROLLER-ATTRIBUTES group (FD/XL sub-
configurations) precedes the CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS leaves
(MAX-NUMBER-OF-TIME-QUANTA-PER-BIT, MAX-SAMPLE-POINT, MAX-SYNC-JUMP-WIDTH,
MIN-NUMBER-OF-TIME-QUANTA-PER-BIT, MIN-SAMPLE-POINT, MIN-SYNC-JUMP-WIDTH).
Coverage runs through the spec aggregator AbstractCanCommunicationController.
canControllerAttributes (CAN-CONTROLLER-ATTRIBUTES >
CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS dispatch). No ref/DEST attributes
exist in this class's element set (six 0..1 attr leaves only).
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Float, Integer
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
    CanCommunicationController,
    CanControllerConfigurationRequirements,
)
from armodel.parser.arxml_parser import ARXMLParser
from tests.test_armodel.parser._helpers import _autosar_root, _snip

FULL_REQUIREMENTS = (
    "<CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS>"
    "<MAX-NUMBER-OF-TIME-QUANTA-PER-BIT>32</MAX-NUMBER-OF-TIME-QUANTA-PER-BIT>"
    "<MAX-SAMPLE-POINT>0.8</MAX-SAMPLE-POINT>"
    "<MAX-SYNC-JUMP-WIDTH>0.2</MAX-SYNC-JUMP-WIDTH>"
    "<MIN-NUMBER-OF-TIME-QUANTA-PER-BIT>16</MIN-NUMBER-OF-TIME-QUANTA-PER-BIT>"
    "<MIN-SAMPLE-POINT>0.7</MIN-SAMPLE-POINT>"
    "<MIN-SYNC-JUMP-WIDTH>0.1</MIN-SYNC-JUMP-WIDTH>"
    "</CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS>"
)

FULL_CONTROLLER_ATTRS = "<CAN-CONTROLLER-ATTRIBUTES>" + FULL_REQUIREMENTS + "</CAN-CONTROLLER-ATTRIBUTES>"


def _read_controller_attrs(inner):
    controller = CanCommunicationController(parent=_autosar_root(), short_name="ctrl")
    ARXMLParser().readAbstractCanCommunicationControllerCanControllerAttributes(_snip(inner), controller)
    return controller


def _assert_full_requirements(req, max_quanta, max_sample, max_sjw, min_quanta, min_sample, min_sjw):
    assert isinstance(req, CanControllerConfigurationRequirements)

    value = req.getMaxNumberOfTimeQuantaPerBit()
    assert isinstance(value, Integer)
    assert value.getValue() == max_quanta

    value = req.getMaxSamplePoint()
    assert isinstance(value, Float)
    assert value.getValue() == max_sample

    value = req.getMaxSyncJumpWidth()
    assert isinstance(value, Float)
    assert value.getValue() == max_sjw

    value = req.getMinNumberOfTimeQuantaPerBit()
    assert isinstance(value, Integer)
    assert value.getValue() == min_quanta

    value = req.getMinSamplePoint()
    assert isinstance(value, Float)
    assert value.getValue() == min_sample

    value = req.getMinSyncJumpWidth()
    assert isinstance(value, Float)
    assert value.getValue() == min_sjw


class TestReadCanControllerConfigurationRequirements:
    def test_reads_all_six_fields_with_values_and_types(self, parser):
        controller = _read_controller_attrs(FULL_CONTROLLER_ATTRS)
        _assert_full_requirements(controller.getCanControllerAttributes(), 32, 0.8, 0.2, 16, 0.7, 0.1)

    def test_reads_empty_requirements_to_none_fields(self, parser):
        controller = _read_controller_attrs("<CAN-CONTROLLER-ATTRIBUTES><CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS/></CAN-CONTROLLER-ATTRIBUTES>")
        req = controller.getCanControllerAttributes()
        assert isinstance(req, CanControllerConfigurationRequirements)
        assert req.getMaxNumberOfTimeQuantaPerBit() is None
        assert req.getMaxSamplePoint() is None
        assert req.getMaxSyncJumpWidth() is None
        assert req.getMinNumberOfTimeQuantaPerBit() is None
        assert req.getMinSamplePoint() is None
        assert req.getMinSyncJumpWidth() is None

    def test_absent_requirements_left_none(self, parser):
        controller = _read_controller_attrs("")
        assert controller.getCanControllerAttributes() is None

    def test_reads_leaves_and_base_group_coexisting(self, parser):
        inner = (
            "<CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS>"
            "<CAN-CONTROLLER-FD-REQUIREMENTS>"
            "<MAX-SAMPLE-POINT>0.9</MAX-SAMPLE-POINT>"
            "</CAN-CONTROLLER-FD-REQUIREMENTS>"
            "<MAX-NUMBER-OF-TIME-QUANTA-PER-BIT>32</MAX-NUMBER-OF-TIME-QUANTA-PER-BIT>"
            "<MIN-SYNC-JUMP-WIDTH>0.1</MIN-SYNC-JUMP-WIDTH>"
            "</CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS>"
        )
        controller = _read_controller_attrs("<CAN-CONTROLLER-ATTRIBUTES>" + inner + "</CAN-CONTROLLER-ATTRIBUTES>")
        req = controller.getCanControllerAttributes()
        assert isinstance(req, CanControllerConfigurationRequirements)
        assert req.getMaxNumberOfTimeQuantaPerBit().getValue() == 32
        assert req.getMinSyncJumpWidth().getValue() == 0.1
        assert req.getMaxSamplePoint() is None
        fd_req = req.getCanControllerFdRequirements()
        assert fd_req is not None
        assert fd_req.getMaxSamplePoint().getValue() == 0.9
