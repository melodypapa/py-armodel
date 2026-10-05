"""Parser tests for LinMaster (Table 3.38, p.94).

XML element order per XSD LIN-MASTER (AUTOSAR_00052.xsd line 77381): heritage
groups (SHORT-NAME via IDENTIFIABLE) first, then the LIN-MASTER group's optional
LIN-MASTER-VARIANTS/LIN-MASTER-CONDITIONAL wrapper carrying the inherited
COMMUNICATION-CONTROLLER + LIN-COMMUNICATION-CONTROLLER content
(WAKE-UP-BY-CONTROLLER-SUPPORTED, PROTOCOL-VERSION) plus this class's
LIN-MASTER-CONTENT (line 77433: LIN-SLAVES wrapper of unbounded LIN-SLAVE-CONFIG,
TIME-BASE, TIME-BASE-JITTER). readLinMaster dispatches the CONDITIONAL content
through the reusable readLinCommunicationController helper (exactly once,
Rule 0001.7) and reads its own attributes after it. The class is consumed as a
concrete element of the EcuInstance COMM-CONTROLLERS choice (line 50380).
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import LinMaster
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import EcuInstance
from tests.test_armodel.parser._helpers import _snip

FULL_LIN_MASTER = (
    "<LIN-MASTER>"
    "<SHORT-NAME>LinMst</SHORT-NAME>"
    "<LIN-MASTER-VARIANTS>"
    "<LIN-MASTER-CONDITIONAL>"
    "<WAKE-UP-BY-CONTROLLER-SUPPORTED>true</WAKE-UP-BY-CONTROLLER-SUPPORTED>"
    "<PROTOCOL-VERSION>LIN 2.0</PROTOCOL-VERSION>"
    "<LIN-SLAVES>"
    "<LIN-SLAVE-CONFIG>"
    "<IDENT><SHORT-NAME>SlaveA</SHORT-NAME></IDENT>"
    "<INITIAL-NAD>1</INITIAL-NAD>"
    "</LIN-SLAVE-CONFIG>"
    "<LIN-SLAVE-CONFIG>"
    "<IDENT><SHORT-NAME>SlaveB</SHORT-NAME></IDENT>"
    "<INITIAL-NAD>2</INITIAL-NAD>"
    "</LIN-SLAVE-CONFIG>"
    "</LIN-SLAVES>"
    "<TIME-BASE>0.01</TIME-BASE>"
    "<TIME-BASE-JITTER>0.001</TIME-BASE-JITTER>"
    "</LIN-MASTER-CONDITIONAL>"
    "</LIN-MASTER-VARIANTS>"
    "</LIN-MASTER>"
)

BARE_LIN_MASTER = "<LIN-MASTER>" "<SHORT-NAME>LinMst</SHORT-NAME>" "<LIN-MASTER-VARIANTS>" "<LIN-MASTER-CONDITIONAL>" "</LIN-MASTER-CONDITIONAL>" "</LIN-MASTER-VARIANTS>" "</LIN-MASTER>"

WRAPPERLESS_LIN_MASTER = "<LIN-MASTER>" "<SHORT-NAME>LinMst</SHORT-NAME>" "</LIN-MASTER>"


def _read_lin_master(parser, xml):
    root = _snip(xml)
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    master = LinMaster(pkg, "LinMst")
    parser.readLinMaster(root[0], master)
    return master


class TestReadLinMaster:
    def test_reads_short_name_and_inherited_levels(self, parser):
        master = _read_lin_master(parser, FULL_LIN_MASTER)

        assert master.getShortName() == "LinMst"
        assert master.getWakeUpByControllerSupported() is not None
        assert master.getWakeUpByControllerSupported().getValue() is True
        assert master.getProtocolVersion() is not None
        assert master.getProtocolVersion().getValue() == "LIN 2.0"

    def test_reads_own_field_values(self, parser):
        master = _read_lin_master(parser, FULL_LIN_MASTER)

        slaves = master.getLinSlaves()
        assert len(slaves) == 2
        assert slaves[0].getIdent().getShortName() == "SlaveA"
        assert slaves[0].getInitialNad().getValue() == 1
        assert slaves[1].getIdent().getShortName() == "SlaveB"
        assert slaves[1].getInitialNad().getValue() == 2

        assert master.getTimeBase() is not None
        assert master.getTimeBase().getValue() == 0.01
        assert master.getTimeBaseJitter() is not None
        assert master.getTimeBaseJitter().getValue() == 0.001

    def test_reads_empty_conditional_to_default_fields(self, parser):
        master = _read_lin_master(parser, BARE_LIN_MASTER)

        assert master.getShortName() == "LinMst"
        assert master.getProtocolVersion() is None
        assert master.getLinSlaves() == []
        assert master.getTimeBase() is None
        assert master.getTimeBaseJitter() is None

    def test_reads_master_without_variants_wrapper_to_default_fields(self, parser):
        master = _read_lin_master(parser, WRAPPERLESS_LIN_MASTER)

        assert master.getShortName() == "LinMst"
        assert master.getProtocolVersion() is None
        assert master.getLinSlaves() == []
        assert master.getTimeBase() is None
        assert master.getTimeBaseJitter() is None

    def test_reads_through_ecu_instance_comm_controllers_consumer(self, parser):
        xml = (
            "<ECU-INSTANCE>"
            "<SHORT-NAME>Ecu</SHORT-NAME>"
            "<COMM-CONTROLLERS>" + FULL_LIN_MASTER + "<CAN-COMMUNICATION-CONTROLLER><SHORT-NAME>CanCtl</SHORT-NAME></CAN-COMMUNICATION-CONTROLLER>"
            "</COMM-CONTROLLERS>"
            "</ECU-INSTANCE>"
        )
        root = _snip(xml)
        ecu = EcuInstance(AUTOSAR.getInstance(), "Ecu")
        parser.readEcuInstanceCommControllers(root[0], ecu)

        controllers = ecu.getCommControllers()
        assert [c.getShortName() for c in controllers] == ["LinMst", "CanCtl"]
        master = controllers[0]
        assert isinstance(master, LinMaster)
        assert master.getProtocolVersion().getValue() == "LIN 2.0"
        assert len(master.getLinSlaves()) == 2
        assert master.getTimeBaseJitter().getValue() == 0.001
        assert not isinstance(controllers[1], LinMaster)
