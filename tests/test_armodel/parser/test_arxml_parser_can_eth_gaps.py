"""Tests for CAN FD and CouplingPort handler gaps."""
import logging
import xml.etree.ElementTree as ET
import pytest
from armodel.models import AUTOSAR
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


@pytest.fixture
def warning_parser():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser(options={"warning": True})


def _snip(inner: str, root_tag: str = "ROOT") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


def _autosar_root():
    return AUTOSAR.getInstance()


# ==================== CanControllerFdConfiguration ====================


class TestCanControllerFdConfiguration:
    """getCanControllerFdConfiguration (L4743-4749) - has TODO/incomplete impl."""

    def test_returns_none_when_child_absent(self, parser):
        from armodel.models import CanControllerFdConfiguration
        element = _snip("<OTHER/>")
        result = parser.getCanControllerFdConfiguration(
            element, "CAN-CONTROLLER-FD-CONFIGURATION"
        )
        assert result is None

    def test_returns_config_when_child_present(self, parser):
        from armodel.models import CanControllerFdConfiguration
        element = _snip(
            "<CAN-CONTROLLER-FD-CONFIGURATION>"
            "<PADDING-VALUE>10</PADDING-VALUE>"
            "</CAN-CONTROLLER-FD-CONFIGURATION>"
        )
        result = parser.getCanControllerFdConfiguration(
            element, "CAN-CONTROLLER-FD-CONFIGURATION"
        )
        # Implementation is incomplete (TODO) but still returns an instance.
        assert isinstance(result, CanControllerFdConfiguration)


# ==================== CanControllerFdConfigurationRequirements ====================


class TestCanControllerFdConfigurationRequirements:
    """getCanControllerFdConfigurationRequirements (L4751-4765)."""

    def test_returns_none_when_child_absent(self, parser):
        element = _snip("<OTHER/>")
        result = parser.getCanControllerFdConfigurationRequirements(
            element, "CAN-CONTROLLER-FD-REQUIREMENTS"
        )
        assert result is None

    def test_sets_all_fields(self, parser):
        element = _snip(
            "<CAN-CONTROLLER-FD-REQUIREMENTS>"
            "<MAX-NUMBER-OF-TIME-QUANTA-PER-BIT>32</MAX-NUMBER-OF-TIME-QUANTA-PER-BIT>"
            "<MAX-SAMPLE-POINT>0.8</MAX-SAMPLE-POINT>"
            "<MAX-SYNC-JUMP-WIDTH>0.2</MAX-SYNC-JUMP-WIDTH>"
            "<MAX-TRCV-DELAY-COMPENSATION-OFFSET>0.0001</MAX-TRCV-DELAY-COMPENSATION-OFFSET>"
            "<MIN-NUMBER-OF-TIME-QUANTA-PER-BIT>16</MIN-NUMBER-OF-TIME-QUANTA-PER-BIT>"
            "<MIN-SAMPLE-POINT>0.7</MIN-SAMPLE-POINT>"
            "<MIN-SYNC-JUMP-WIDTH>0.1</MIN-SYNC-JUMP-WIDTH>"
            "<MIN-TRCV-DELAY-COMPENSATION-OFFSET>0.00005</MIN-TRCV-DELAY-COMPENSATION-OFFSET>"
            "<TX-BIT-RATE-SWITCH>true</TX-BIT-RATE-SWITCH>"
            "</CAN-CONTROLLER-FD-REQUIREMENTS>"
        )
        result = parser.getCanControllerFdConfigurationRequirements(
            element, "CAN-CONTROLLER-FD-REQUIREMENTS"
        )
        assert result is not None
        assert result.getMaxNumberOfTimeQuantaPerBit().getValue() == 32
        assert result.getMaxSamplePoint().getValue() == 0.8
        assert result.getMaxSyncJumpWidth().getValue() == 0.2
        assert result.getMaxTrcvDelayCompensationOffset().getValue() == 0.0001
        assert result.getMinNumberOfTimeQuantaPerBit().getValue() == 16
        assert result.getMinSamplePoint().getValue() == 0.7
        assert result.getMinSyncJumpWidth().getValue() == 0.1
        assert result.getMinTrcvDelayCompensationOffset().getValue() == 0.00005
        assert result.getTxBitRateSwitch().getValue() is True


# ==================== AbstractCanCommunicationControllerCanControllerAttributes ====================


class TestAbstractCanCommunicationControllerCanControllerAttributes:
    """readAbstractCanCommunicationControllerCanControllerAttributes (L4780-4788)."""

    def test_sets_requirements_branch(self, parser):
        from armodel.models import CanCommunicationController
        controller = CanCommunicationController(
            parent=_autosar_root(), short_name="ctrl"
        )
        element = _snip(
            "<CAN-CONTROLLER-ATTRIBUTES>"
            "<CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS>"
            "<MAX-NUMBER-OF-TIME-QUANTA-PER-BIT>32</MAX-NUMBER-OF-TIME-QUANTA-PER-BIT>"
            "</CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS>"
            "</CAN-CONTROLLER-ATTRIBUTES>"
        )
        parser.readAbstractCanCommunicationControllerCanControllerAttributes(
            element, controller
        )
        attrs = controller.getCanControllerAttributes()
        assert attrs is not None
        assert attrs.getMaxNumberOfTimeQuantaPerBit().getValue() == 32

    def test_unsupported_branch_raises_by_default(self, parser):
        from armodel.models import CanCommunicationController
        controller = CanCommunicationController(
            parent=_autosar_root(), short_name="ctrl"
        )
        element = _snip(
            "<CAN-CONTROLLER-ATTRIBUTES>"
            "<UNKNOWN-ATTRS/>"
            "</CAN-CONTROLLER-ATTRIBUTES>"
        )
        with pytest.raises(NotImplementedError):
            parser.readAbstractCanCommunicationControllerCanControllerAttributes(
                element, controller
            )

    def test_unsupported_branch_logs_warning(self, warning_parser, caplog):
        from armodel.models import CanCommunicationController
        controller = CanCommunicationController(
            parent=_autosar_root(), short_name="ctrl"
        )
        element = _snip(
            "<CAN-CONTROLLER-ATTRIBUTES>"
            "<UNKNOWN-ATTRS/>"
            "</CAN-CONTROLLER-ATTRIBUTES>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readAbstractCanCommunicationControllerCanControllerAttributes(
                element, controller
            )
        assert any(
            "Unsupported CanControllerAttributes" in rec.getMessage()
            for rec in caplog.records
        )


# ==================== CouplingPortDetailsCouplingPortStructuralElements ====================


class TestCouplingPortDetailsCouplingPortStructuralElements:
    """readCouplingPortDetailsCouplingPortStructuralElements (L4811-4821)."""

    def test_creates_fifo(self, parser):
        from armodel.models import CouplingPortDetails
        details = CouplingPortDetails()
        element = _snip(
            "<COUPLING-PORT-STRUCTURAL-ELEMENTS>"
            "<COUPLING-PORT-FIFO>"
            "<SHORT-NAME>fifo1</SHORT-NAME>"
            "</COUPLING-PORT-FIFO>"
            "</COUPLING-PORT-STRUCTURAL-ELEMENTS>"
        )
        parser.readCouplingPortDetailsCouplingPortStructuralElements(element, details)
        elements = details.getCouplingPortStructuralElements()
        assert len(elements) == 1
        from armodel.models import CouplingPortFifo
        assert isinstance(elements[0], CouplingPortFifo)
        assert elements[0].getShortName() == "fifo1"

    def test_creates_scheduler(self, parser):
        from armodel.models import CouplingPortDetails
        details = CouplingPortDetails()
        element = _snip(
            "<COUPLING-PORT-STRUCTURAL-ELEMENTS>"
            "<COUPLING-PORT-SCHEDULER>"
            "<SHORT-NAME>sched1</SHORT-NAME>"
            "<PORT-SCHEDULER>WEIGHTED_ROUND_ROBIN</PORT-SCHEDULER>"
            "</COUPLING-PORT-SCHEDULER>"
            "</COUPLING-PORT-STRUCTURAL-ELEMENTS>"
        )
        parser.readCouplingPortDetailsCouplingPortStructuralElements(element, details)
        elements = details.getCouplingPortStructuralElements()
        assert len(elements) == 1
        from armodel.models import CouplingPortScheduler
        assert isinstance(elements[0], CouplingPortScheduler)
        assert elements[0].getShortName() == "sched1"
        assert elements[0].getPortScheduler() is not None

    def test_unsupported_branch_raises_by_default(self, parser):
        from armodel.models import CouplingPortDetails
        details = CouplingPortDetails()
        element = _snip(
            "<COUPLING-PORT-STRUCTURAL-ELEMENTS>"
            "<UNKNOWN-ELEMENT/>"
            "</COUPLING-PORT-STRUCTURAL-ELEMENTS>"
        )
        with pytest.raises(NotImplementedError):
            parser.readCouplingPortDetailsCouplingPortStructuralElements(
                element, details
            )

    def test_unsupported_branch_logs_warning(self, warning_parser, caplog):
        from armodel.models import CouplingPortDetails
        details = CouplingPortDetails()
        element = _snip(
            "<COUPLING-PORT-STRUCTURAL-ELEMENTS>"
            "<UNKNOWN-ELEMENT/>"
            "</COUPLING-PORT-STRUCTURAL-ELEMENTS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readCouplingPortDetailsCouplingPortStructuralElements(
                element, details
            )
        assert any(
            "Unsupported CouplingPortStructuralElement" in rec.getMessage()
            for rec in caplog.records
        )


# ==================== CouplingPortDetailsEthernetPriorityRegenerations ====================


class TestCouplingPortDetailsEthernetPriorityRegenerations:
    """readCouplingPortDetailsEthernetPriorityRegenerations (L4827-4834)."""

    def test_creates_regeneration(self, parser):
        from armodel.models import CouplingPortDetails
        details = CouplingPortDetails()
        element = _snip(
            "<ETHERNET-PRIORITY-REGENERATIONS>"
            "<ETHERNET-PRIORITY-REGENERATION>"
            "<SHORT-NAME>regen1</SHORT-NAME>"
            "<INGRESS-PRIORITY>1</INGRESS-PRIORITY>"
            "<REGENERATED-PRIORITY>2</REGENERATED-PRIORITY>"
            "</ETHERNET-PRIORITY-REGENERATION>"
            "</ETHERNET-PRIORITY-REGENERATIONS>"
        )
        parser.readCouplingPortDetailsEthernetPriorityRegenerations(element, details)
        regens = details.getEthernetPriorityRegenerations()
        assert len(regens) == 1
        assert regens[0].getShortName() == "regen1"
        assert regens[0].getIngressPriority().getValue() == 1
        assert regens[0].getRegeneratedPriority().getValue() == 2

    def test_unsupported_branch_raises_by_default(self, parser):
        from armodel.models import CouplingPortDetails
        details = CouplingPortDetails()
        element = _snip(
            "<ETHERNET-PRIORITY-REGENERATIONS>"
            "<UNKNOWN-REGEN/>"
            "</ETHERNET-PRIORITY-REGENERATIONS>"
        )
        with pytest.raises(NotImplementedError):
            parser.readCouplingPortDetailsEthernetPriorityRegenerations(
                element, details
            )

    def test_unsupported_branch_logs_warning(self, warning_parser, caplog):
        from armodel.models import CouplingPortDetails
        details = CouplingPortDetails()
        element = _snip(
            "<ETHERNET-PRIORITY-REGENERATIONS>"
            "<UNKNOWN-REGEN/>"
            "</ETHERNET-PRIORITY-REGENERATIONS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readCouplingPortDetailsEthernetPriorityRegenerations(
                element, details
            )
        assert any(
            "Unsupported EthernetPriorityRegeneration" in rec.getMessage()
            for rec in caplog.records
        )


# ==================== CouplingPortDetails (getCouplingPortDetails) ====================


class TestGetCouplingPortDetails:
    """getCouplingPortDetails (L4836-4844)."""

    def test_returns_none_when_child_absent(self, parser):
        element = _snip("<OTHER/>")
        result = parser.getCouplingPortDetails(element, "COUPLING-PORT-DETAILS")
        assert result is None

    def test_reads_full_details(self, parser):
        from armodel.models import CouplingPortDetails
        element = _snip(
            "<COUPLING-PORT-DETAILS>"
            "<COUPLING-PORT-STRUCTURAL-ELEMENTS>"
            "<COUPLING-PORT-FIFO>"
            "<SHORT-NAME>fifo1</SHORT-NAME>"
            "</COUPLING-PORT-FIFO>"
            "</COUPLING-PORT-STRUCTURAL-ELEMENTS>"
            "<ETHERNET-PRIORITY-REGENERATIONS>"
            "<ETHERNET-PRIORITY-REGENERATION>"
            "<SHORT-NAME>regen1</SHORT-NAME>"
            "<INGRESS-PRIORITY>1</INGRESS-PRIORITY>"
            "<REGENERATED-PRIORITY>2</REGENERATED-PRIORITY>"
            "</ETHERNET-PRIORITY-REGENERATION>"
            "</ETHERNET-PRIORITY-REGENERATIONS>"
            "<LAST-EGRESS-SCHEDULER-REF DEST=\"COUPLING-PORT-SCHEDULER\">"
            "/pkg/sched1"
            "</LAST-EGRESS-SCHEDULER-REF>"
            "</COUPLING-PORT-DETAILS>"
        )
        result = parser.getCouplingPortDetails(element, "COUPLING-PORT-DETAILS")
        assert isinstance(result, CouplingPortDetails)
        assert len(result.getCouplingPortStructuralElements()) == 1
        assert len(result.getEthernetPriorityRegenerations()) == 1
        ref = result.getLastEgressSchedulerRef()
        assert ref is not None
        assert ref.getDest() == "COUPLING-PORT-SCHEDULER"
        assert ref.getValue() == "/pkg/sched1"


# ==================== VlanMembership & CouplingPortVlanMemberships ====================


class TestVlanMembership:
    """readVlanMembership (L4846-4848)."""

    def test_sets_send_activity_and_vlan_ref(self, parser):
        from armodel.models import VlanMembership
        membership = VlanMembership()
        element = _snip(
            "<SEND-ACTIVITY>TAGGED</SEND-ACTIVITY>"
            "<VLAN-REF DEST=\"VLAN\">/pkg/vlan1</VLAN-REF>",
            root_tag="VLAN-MEMBERSHIP",
        )
        parser.readVlanMembership(element, membership)
        assert membership.getSendActivity() is not None
        assert membership.getSendActivity().getValue() == "TAGGED"
        ref = membership.getVlanRef()
        assert ref is not None
        assert ref.getDest() == "VLAN"
        assert ref.getValue() == "/pkg/vlan1"


class TestCouplingPortVlanMemberships:
    """readCouplingPortVlanMemberships (L4850-4857)."""

    def test_creates_membership(self, parser):
        from armodel.models import CouplingPort
        port = CouplingPort(parent=_autosar_root(), short_name="cp")
        element = _snip(
            "<VLAN-MEMBERSHIPS>"
            "<VLAN-MEMBERSHIP>"
            "<SEND-ACTIVITY>TAGGED</SEND-ACTIVITY>"
            "<VLAN-REF DEST=\"VLAN\">/pkg/vlan1</VLAN-REF>"
            "</VLAN-MEMBERSHIP>"
            "</VLAN-MEMBERSHIPS>"
        )
        parser.readCouplingPortVlanMemberships(element, port)
        memberships = port.getVlanMemberships()
        assert len(memberships) == 1
        assert memberships[0].getSendActivity().getValue() == "TAGGED"
        assert memberships[0].getVlanRef().getValue() == "/pkg/vlan1"

    def test_unsupported_branch_raises_by_default(self, parser):
        from armodel.models import CouplingPort
        port = CouplingPort(parent=_autosar_root(), short_name="cp")
        element = _snip(
            "<VLAN-MEMBERSHIPS>"
            "<UNKNOWN-MEMBERSHIP/>"
            "</VLAN-MEMBERSHIPS>"
        )
        with pytest.raises(NotImplementedError):
            parser.readCouplingPortVlanMemberships(element, port)

    def test_unsupported_branch_logs_warning(self, warning_parser, caplog):
        from armodel.models import CouplingPort
        port = CouplingPort(parent=_autosar_root(), short_name="cp")
        element = _snip(
            "<VLAN-MEMBERSHIPS>"
            "<UNKNOWN-MEMBERSHIP/>"
            "</VLAN-MEMBERSHIPS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readCouplingPortVlanMemberships(element, port)
        assert any(
            "Unsupported VlanMembership" in rec.getMessage()
            for rec in caplog.records
        )
