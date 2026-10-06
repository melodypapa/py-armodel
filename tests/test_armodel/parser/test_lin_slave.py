"""Parser tests for LinSlave (Table 3.41, p.97).

XML element order per XSD LIN-SLAVE (AUTOSAR_00052.xsd line 77685): heritage
groups (SHORT-NAME via IDENTIFIABLE) first, then the LIN-SLAVE group's optional
LIN-SLAVE-VARIANTS/LIN-SLAVE-CONDITIONAL wrapper carrying the inherited
COMMUNICATION-CONTROLLER + LIN-COMMUNICATION-CONTROLLER content
(WAKE-UP-BY-CONTROLLER-SUPPORTED, PROTOCOL-VERSION) plus this class's
LIN-SLAVE-CONTENT (line 77893: ASSIGN-NAD, CONFIGURED-NAD, FUNCTION-ID,
INITIAL-NAD, LIN-ERROR-RESPONSE, NAS-TIMEOUT, SUPPLIER-ID, VARIANT-ID — the
atp.Status="removed" SAVE-CONFIGURATION is absent from the R23-11 table and not
modeled). readLinSlave dispatches the CONDITIONAL content through the reusable
readLinCommunicationController helper (exactly once, Rule 0001.7) and reads its
own attributes after it. The class is consumed as a concrete element of the
EcuInstance COMM-CONTROLLERS choice (line 50381).
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import LinSlave
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import EcuInstance
from tests.test_armodel.parser._helpers import _snip

FULL_LIN_SLAVE = (
    "<LIN-SLAVE>"
    "<SHORT-NAME>LinSlv</SHORT-NAME>"
    "<LIN-SLAVE-VARIANTS>"
    "<LIN-SLAVE-CONDITIONAL>"
    "<WAKE-UP-BY-CONTROLLER-SUPPORTED>true</WAKE-UP-BY-CONTROLLER-SUPPORTED>"
    "<PROTOCOL-VERSION>LIN 2.0</PROTOCOL-VERSION>"
    "<ASSIGN-NAD>true</ASSIGN-NAD>"
    "<CONFIGURED-NAD>3</CONFIGURED-NAD>"
    "<FUNCTION-ID>17</FUNCTION-ID>"
    "<INITIAL-NAD>1</INITIAL-NAD>"
    '<LIN-ERROR-RESPONSE S="1234" T="2024-01-01T00:00:00Z">'
    "<RESPONSE-ERROR-REF>/Pkg/ISignalTriggering</RESPONSE-ERROR-REF>"
    "</LIN-ERROR-RESPONSE>"
    "<NAS-TIMEOUT>0.1</NAS-TIMEOUT>"
    "<SUPPLIER-ID>2721</SUPPLIER-ID>"
    "<VARIANT-ID>5</VARIANT-ID>"
    "</LIN-SLAVE-CONDITIONAL>"
    "</LIN-SLAVE-VARIANTS>"
    "</LIN-SLAVE>"
)

BARE_LIN_SLAVE = "<LIN-SLAVE>" "<SHORT-NAME>LinSlv</SHORT-NAME>" "<LIN-SLAVE-VARIANTS>" "<LIN-SLAVE-CONDITIONAL>" "</LIN-SLAVE-CONDITIONAL>" "</LIN-SLAVE-VARIANTS>" "</LIN-SLAVE>"

WRAPPERLESS_LIN_SLAVE = "<LIN-SLAVE>" "<SHORT-NAME>LinSlv</SHORT-NAME>" "</LIN-SLAVE>"


def _read_lin_slave(parser, xml):
    root = _snip(xml)
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    slave = LinSlave(pkg, "LinSlv")
    parser.readLinSlave(root[0], slave)
    return slave


class TestReadLinSlave:
    def test_reads_short_name_and_inherited_levels(self, parser):
        slave = _read_lin_slave(parser, FULL_LIN_SLAVE)

        assert slave.getShortName() == "LinSlv"
        assert slave.getWakeUpByControllerSupported() is not None
        assert slave.getWakeUpByControllerSupported().getValue() is True
        assert slave.getProtocolVersion() is not None
        assert slave.getProtocolVersion().getValue() == "LIN 2.0"

    def test_reads_own_field_values(self, parser):
        slave = _read_lin_slave(parser, FULL_LIN_SLAVE)

        assert slave.getAssignNad() is not None
        assert slave.getAssignNad().getValue() is True
        assert slave.getConfiguredNad() is not None
        assert slave.getConfiguredNad().getValue() == 3
        assert slave.getFunctionId() is not None
        assert slave.getFunctionId().getValue() == 17
        assert slave.getInitialNad() is not None
        assert slave.getInitialNad().getValue() == 1
        assert slave.getLinErrorResponse() is not None
        assert slave.getLinErrorResponse().getResponseErrorRef().getValue() == "/Pkg/ISignalTriggering"
        assert slave.getLinErrorResponse().getChecksum().getValue() == "1234"
        assert slave.getLinErrorResponse().getTimestamp().getValue() == "2024-01-01T00:00:00Z"
        assert slave.getNasTimeout() is not None
        assert slave.getNasTimeout().getValue() == 0.1
        assert slave.getSupplierId() is not None
        assert slave.getSupplierId().getValue() == 2721
        assert slave.getVariantId() is not None
        assert slave.getVariantId().getValue() == 5

    def test_reads_empty_conditional_to_default_fields(self, parser):
        slave = _read_lin_slave(parser, BARE_LIN_SLAVE)

        assert slave.getShortName() == "LinSlv"
        assert slave.getProtocolVersion() is None
        assert slave.getAssignNad() is None
        assert slave.getConfiguredNad() is None
        assert slave.getFunctionId() is None
        assert slave.getInitialNad() is None
        assert slave.getLinErrorResponse() is None
        assert slave.getNasTimeout() is None
        assert slave.getSupplierId() is None
        assert slave.getVariantId() is None

    def test_reads_slave_without_variants_wrapper_to_default_fields(self, parser):
        slave = _read_lin_slave(parser, WRAPPERLESS_LIN_SLAVE)

        assert slave.getShortName() == "LinSlv"
        assert slave.getProtocolVersion() is None
        assert slave.getAssignNad() is None
        assert slave.getLinErrorResponse() is None

    def test_reads_through_ecu_instance_comm_controllers_consumer(self, parser):
        xml = "<ECU-INSTANCE>" "<SHORT-NAME>Ecu</SHORT-NAME>" "<COMM-CONTROLLERS>" + FULL_LIN_SLAVE + "<LIN-MASTER><SHORT-NAME>LinMst</SHORT-NAME></LIN-MASTER>" "</COMM-CONTROLLERS>" "</ECU-INSTANCE>"
        root = _snip(xml)
        ecu = EcuInstance(AUTOSAR.getInstance(), "Ecu")
        parser.readEcuInstanceCommControllers(root[0], ecu)

        controllers = ecu.getCommControllers()
        assert [c.getShortName() for c in controllers] == ["LinSlv", "LinMst"]
        slave = controllers[0]
        assert isinstance(slave, LinSlave)
        assert slave.getProtocolVersion().getValue() == "LIN 2.0"
        assert slave.getAssignNad().getValue() is True
        assert slave.getSupplierId().getValue() == 2721
        assert not isinstance(controllers[1], LinSlave)
