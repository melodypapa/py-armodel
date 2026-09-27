"""Parser tests for CanControllerConfiguration (Table 3.14, p.64).

XML element order per XSD group CAN-CONTROLLER-CONFIGURATION: PROP-SEG,
SYNC-JUMP-WIDTH, TIME-SEG-1, TIME-SEG-2; the ABSTRACT-CAN-COMMUNICATION-
CONTROLLER-ATTRIBUTES group (FD/XL sub-configurations) precedes the leaves.
Coverage runs through both spec aggregators: CanXlProps.canConfig (CAN-CONFIG)
and AbstractCanCommunicationController.canControllerAttributes
(CAN-CONTROLLER-ATTRIBUTES > CAN-CONTROLLER-CONFIGURATION dispatch).
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanCommunicationController, CanControllerConfiguration, CanXlProps
from armodel.parser.arxml_parser import ARXMLParser
from tests.test_armodel.parser._helpers import _autosar_root, _snip

FULL_CONFIG = "<CAN-CONFIG>" "<PROP-SEG>8</PROP-SEG>" "<SYNC-JUMP-WIDTH>1</SYNC-JUMP-WIDTH>" "<TIME-SEG-1>13</TIME-SEG-1>" "<TIME-SEG-2>2</TIME-SEG-2>" "</CAN-CONFIG>"

FULL_CONTROLLER_ATTRS = (
    "<CAN-CONTROLLER-ATTRIBUTES>"
    "<CAN-CONTROLLER-CONFIGURATION>"
    "<PROP-SEG>4</PROP-SEG>"
    "<SYNC-JUMP-WIDTH>2</SYNC-JUMP-WIDTH>"
    "<TIME-SEG-1>6</TIME-SEG-1>"
    "<TIME-SEG-2>3</TIME-SEG-2>"
    "</CAN-CONTROLLER-CONFIGURATION>"
    "</CAN-CONTROLLER-ATTRIBUTES>"
)


def _read_props(inner):
    props = CanXlProps(_autosar_root(), "Props")
    ARXMLParser().readCanXlProps(_snip(inner), props)
    return props


def _read_controller_attrs(inner):
    controller = CanCommunicationController(parent=_autosar_root(), short_name="ctrl")
    ARXMLParser().readAbstractCanCommunicationControllerCanControllerAttributes(_snip(inner), controller)
    return controller


def _assert_full_config(config, prop_seg, sync_jump_width, time_seg1, time_seg2):
    assert isinstance(config, CanControllerConfiguration)

    value = config.getPropSeg()
    assert isinstance(value, Integer)
    assert value.getValue() == prop_seg

    value = config.getSyncJumpWidth()
    assert isinstance(value, Integer)
    assert value.getValue() == sync_jump_width

    value = config.getTimeSeg1()
    assert isinstance(value, Integer)
    assert value.getValue() == time_seg1

    value = config.getTimeSeg2()
    assert isinstance(value, Integer)
    assert value.getValue() == time_seg2


class TestReadCanControllerConfiguration:
    def test_returns_none_when_can_config_absent(self, parser):
        props = _read_props("<CAN-BAUDRATE>2000000</CAN-BAUDRATE>")
        assert props.getCanConfig() is None

    def test_reads_all_four_fields_with_values_and_types(self, parser):
        props = _read_props(FULL_CONFIG)
        _assert_full_config(props.getCanConfig(), 8, 1, 13, 2)

    def test_reads_empty_can_config_to_none_fields(self, parser):
        props = _read_props("<CAN-CONFIG/>")
        config = props.getCanConfig()
        assert isinstance(config, CanControllerConfiguration)
        assert config.getPropSeg() is None
        assert config.getSyncJumpWidth() is None
        assert config.getTimeSeg1() is None
        assert config.getTimeSeg2() is None

    def test_reads_config_through_controller_attributes_dispatch(self, parser):
        controller = _read_controller_attrs(FULL_CONTROLLER_ATTRS)
        _assert_full_config(controller.getCanControllerAttributes(), 4, 2, 6, 3)

    def test_can_config_and_fd_config_coexist_on_props(self, parser):
        props = _read_props(FULL_CONFIG + "<CAN-FD-CONFIG/>")
        assert isinstance(props.getCanConfig(), CanControllerConfiguration)
        assert props.getCanConfig().getPropSeg().getValue() == 8
        assert props.getCanFdConfig() is not None
