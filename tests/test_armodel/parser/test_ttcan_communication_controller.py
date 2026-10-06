"""Parser tests for TtcanCommunicationController (Table 3.25, p.77).

XML element order per XSD TTCAN-COMMUNICATION-CONTROLLER (AUTOSAR_00052.xsd
line 127016): heritage groups (SHORT-NAME via IDENTIFIABLE) first, then the
TTCAN-COMMUNICATION-CONTROLLER group's optional TTCAN-COMMUNICATION-CONTROLLER-VARIANTS/
TTCAN-COMMUNICATION-CONTROLLER-CONDITIONAL wrapper carrying the inherited
COMMUNICATION-CONTROLLER + ABSTRACT-CAN-COMMUNICATION-CONTROLLER content
(WAKE-UP-BY-CONTROLLER-SUPPORTED, CAN-CONTROLLER-ATTRIBUTES) plus this class's
TTCAN-COMMUNICATION-CONTROLLER-CONTENT (line 127068: APPL-WATCHDOG-LIMIT,
EXPECTED-TX-TRIGGER, EXTERNAL-CLOCK-SYNCHRONISATION, INITIAL-REF-OFFSET, MASTER,
TIME-MASTER-PRIORITY, TIME-TRIGGERED-CAN-LEVEL, TX-ENABLE-WINDOW-LENGTH).
readTtcanCommunicationController dispatches the conditional content through the
reusable readAbstractCanCommunicationController helper (exactly once) and reads
its own attributes after it. The class is consumed as a concrete element of the
EcuInstance COMM-CONTROLLERS choice (line 50382, Rule 0001.7).
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
    CanControllerConfigurationRequirements,
    TtcanCommunicationController,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import EcuInstance
from tests.test_armodel.parser._helpers import _snip

OWN_CONDITIONAL = (
    "<APPL-WATCHDOG-LIMIT>100</APPL-WATCHDOG-LIMIT>"
    "<EXPECTED-TX-TRIGGER>8</EXPECTED-TX-TRIGGER>"
    "<EXTERNAL-CLOCK-SYNCHRONISATION>true</EXTERNAL-CLOCK-SYNCHRONISATION>"
    "<INITIAL-REF-OFFSET>3</INITIAL-REF-OFFSET>"
    "<MASTER>true</MASTER>"
    "<TIME-MASTER-PRIORITY>5</TIME-MASTER-PRIORITY>"
    "<TIME-TRIGGERED-CAN-LEVEL>2</TIME-TRIGGERED-CAN-LEVEL>"
    "<TX-ENABLE-WINDOW-LENGTH>12</TX-ENABLE-WINDOW-LENGTH>"
)

FULL_TTCAN_CONTROLLER = (
    "<TTCAN-COMMUNICATION-CONTROLLER>"
    "<SHORT-NAME>TtcanCtl</SHORT-NAME>"
    "<TTCAN-COMMUNICATION-CONTROLLER-VARIANTS>"
    "<TTCAN-COMMUNICATION-CONTROLLER-CONDITIONAL>"
    "<WAKE-UP-BY-CONTROLLER-SUPPORTED>true</WAKE-UP-BY-CONTROLLER-SUPPORTED>"
    "<CAN-CONTROLLER-ATTRIBUTES>"
    "<CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS>"
    "<MIN-NUMBER-OF-TIME-QUANTA-PER-BIT>4</MIN-NUMBER-OF-TIME-QUANTA-PER-BIT>"
    "</CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS>"
    "</CAN-CONTROLLER-ATTRIBUTES>" + OWN_CONDITIONAL + "</TTCAN-COMMUNICATION-CONTROLLER-CONDITIONAL>"
    "</TTCAN-COMMUNICATION-CONTROLLER-VARIANTS>"
    "</TTCAN-COMMUNICATION-CONTROLLER>"
)

BARE_TTCAN_CONTROLLER = (
    "<TTCAN-COMMUNICATION-CONTROLLER>"
    "<SHORT-NAME>TtcanCtl</SHORT-NAME>"
    "<TTCAN-COMMUNICATION-CONTROLLER-VARIANTS>"
    "<TTCAN-COMMUNICATION-CONTROLLER-CONDITIONAL>"
    "</TTCAN-COMMUNICATION-CONTROLLER-CONDITIONAL>"
    "</TTCAN-COMMUNICATION-CONTROLLER-VARIANTS>"
    "</TTCAN-COMMUNICATION-CONTROLLER>"
)

WRAPPERLESS_TTCAN_CONTROLLER = "<TTCAN-COMMUNICATION-CONTROLLER>" "<SHORT-NAME>TtcanCtl</SHORT-NAME>" "</TTCAN-COMMUNICATION-CONTROLLER>"


def _new_controller(name="TtcanCtl"):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    return TtcanCommunicationController(pkg, name)


def _read_ttcan_controller(parser, xml):
    root = _snip(xml)
    controller = _new_controller()
    parser.readTtcanCommunicationController(root[0], controller)
    return controller


class TestReadTtcanCommunicationController:
    def test_reads_short_name_and_inherited_levels(self, parser):
        controller = _read_ttcan_controller(parser, FULL_TTCAN_CONTROLLER)

        assert controller.getShortName() == "TtcanCtl"
        assert controller.getWakeUpByControllerSupported().getValue() is True
        attributes = controller.getCanControllerAttributes()
        assert isinstance(attributes, CanControllerConfigurationRequirements)
        assert attributes.getMinNumberOfTimeQuantaPerBit().getValue() == 4

    def test_reads_own_field_values(self, parser):
        controller = _read_ttcan_controller(parser, FULL_TTCAN_CONTROLLER)

        assert controller.getApplWatchdogLimit().getValue() == 100
        assert controller.getExpectedTxTrigger().getValue() == 8
        assert controller.getExternalClockSynchronisation().getValue() is True
        assert controller.getInitialRefOffset().getValue() == 3
        assert controller.getMaster().getValue() is True
        assert controller.getTimeMasterPriority().getValue() == 5
        assert controller.getTimeTriggeredCanLevel().getValue() == 2
        assert controller.getTxEnableWindowLength().getValue() == 12

    def test_reads_empty_conditional_to_none_fields(self, parser):
        controller = _read_ttcan_controller(parser, BARE_TTCAN_CONTROLLER)

        assert controller.getShortName() == "TtcanCtl"
        assert controller.getWakeUpByControllerSupported() is None
        assert controller.getCanControllerAttributes() is None
        assert controller.getApplWatchdogLimit() is None
        assert controller.getExpectedTxTrigger() is None
        assert controller.getExternalClockSynchronisation() is None
        assert controller.getInitialRefOffset() is None
        assert controller.getMaster() is None
        assert controller.getTimeMasterPriority() is None
        assert controller.getTimeTriggeredCanLevel() is None
        assert controller.getTxEnableWindowLength() is None

    def test_reads_controller_without_variants_wrapper_to_none_fields(self, parser):
        controller = _read_ttcan_controller(parser, WRAPPERLESS_TTCAN_CONTROLLER)

        assert controller.getShortName() == "TtcanCtl"
        assert controller.getApplWatchdogLimit() is None
        assert controller.getExpectedTxTrigger() is None
        assert controller.getExternalClockSynchronisation() is None
        assert controller.getInitialRefOffset() is None
        assert controller.getMaster() is None
        assert controller.getTimeMasterPriority() is None
        assert controller.getTimeTriggeredCanLevel() is None
        assert controller.getTxEnableWindowLength() is None

    def test_reads_through_ecu_instance_comm_controllers_consumer(self, parser):
        xml = (
            "<ECU-INSTANCE>"
            "<SHORT-NAME>Ecu</SHORT-NAME>"
            "<COMM-CONTROLLERS>" + FULL_TTCAN_CONTROLLER + "<CAN-COMMUNICATION-CONTROLLER><SHORT-NAME>CanCtl</SHORT-NAME></CAN-COMMUNICATION-CONTROLLER>"
            "</COMM-CONTROLLERS>"
            "</ECU-INSTANCE>"
        )
        root = _snip(xml)
        ecu = EcuInstance(AUTOSAR.getInstance(), "Ecu")
        parser.readEcuInstanceCommControllers(root[0], ecu)

        controllers = ecu.getCommControllers()
        assert [c.getShortName() for c in controllers] == ["TtcanCtl", "CanCtl"]
        ttcan_controller = controllers[0]
        assert isinstance(ttcan_controller, TtcanCommunicationController)
        assert ttcan_controller.getApplWatchdogLimit().getValue() == 100
        assert ttcan_controller.getTimeTriggeredCanLevel().getValue() == 2
        assert not isinstance(controllers[1], TtcanCommunicationController)
