"""Unit tests for the Fibex CddSupport module (UserDefinedCluster, UserDefinedPhysicalChannel).

Table 3.129 (p.179) is a page-split table whose fragment A renders the
Class/Package/Note/Base/Aggregated by rows before the caption and carries NO
Attribute rows — the class adds no own fields or accessors beyond its
CommunicationCluster base (Rule 0001.3); the XSD own group USER-DEFINED-CLUSTER
(AUTOSAR_00052.xsd lines 128516-128536) holds only the atpVariation
USER-DEFINED-CLUSTER-VARIANTS/USER-DEFINED-CLUSTER-CONDITIONAL wrapper.
Table 3.130 (p.179) is the page-split sibling whose fragment renders before its
caption and likewise carries NO Attribute rows — UserDefinedPhysicalChannel adds
no own fields or accessors beyond its PhysicalChannel base; the XSD own group
USER-DEFINED-PHYSICAL-CHANNEL (AUTOSAR_00052.xsd lines 128980-128988) is an empty
sequence (no atpVariation wrapper).
Spec placement per Rule 0007: M2::AUTOSARTemplates::SystemTemplate::Fibex::CddSupport.
"""

import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    PositiveUnlimitedInteger,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.CddSupport import UserDefinedCluster, UserDefinedPhysicalChannel
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanPhysicalChannel
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import FibexElement
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import ISignalTriggering, PduTriggering
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationCluster, PhysicalChannel


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


USER_DEFINED_CLUSTER_CLASS_NOTE = (
    "This element allows the modeling of arbitrary Communication Clusters (e.g. bus systems that are not supported by AUTOSAR). Tags: atp.recommendedPackage=CommunicationClusters"
)


class TestUserDefinedCluster:
    """Test cases for UserDefinedCluster (Table 3.129, p.179)."""

    def test_inheritance(self):
        assert issubclass(UserDefinedCluster, CommunicationCluster)
        assert issubclass(UserDefinedCluster, FibexElement)
        assert issubclass(UserDefinedCluster, ARObject)

    def test_concrete_instantiation(self):
        cluster = UserDefinedCluster(MockParent(), "cluster")  # Table 3.129 carries no abstract stereotype

        assert isinstance(cluster, CommunicationCluster)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(UserDefinedCluster.__doc__) == USER_DEFINED_CLUSTER_CLASS_NOTE

    def test_init_docless(self):
        assert UserDefinedCluster.__init__.__doc__ is None

    def test_no_own_members(self):
        # Table 3.129's Attribute rows render none — UserDefinedCluster adds no fields or accessors beyond its bases (Rule 0001.3)
        own = [name for name, value in vars(UserDefinedCluster).items() if not name.startswith("_")]
        assert own == []

    def test_initialization_defaults(self):
        cluster = UserDefinedCluster(MockParent(), "cluster")

        for getter in ["getBaudrate", "getProtocolName", "getProtocolVersion"]:
            assert getattr(cluster, getter)() is None, getter
        assert cluster.getPhysicalChannels() == []

    def test_inherited_accessors_round_trip(self):
        cluster = UserDefinedCluster(MockParent(), "cluster")
        baudrate = PositiveUnlimitedInteger().setValue("500000")
        protocol_name = ARLiteral().setValue("USER-DEFINED")
        protocol_version = ARLiteral().setValue("1.0")

        assert cluster == cluster.setBaudrate(baudrate)
        assert cluster.getBaudrate() is baudrate
        assert cluster.getBaudrate().getValue() == 500000
        assert cluster == cluster.setBaudrate(None)  # None no-op
        assert cluster.getBaudrate() is baudrate  # unchanged

        assert cluster == cluster.setProtocolName(protocol_name)
        assert cluster.getProtocolName() is protocol_name
        assert cluster == cluster.setProtocolName(None)  # None no-op
        assert cluster.getProtocolName() is protocol_name  # unchanged

        assert cluster == cluster.setProtocolVersion(protocol_version)
        assert cluster.getProtocolVersion() is protocol_version
        assert cluster == cluster.setProtocolVersion(None)  # None no-op
        assert cluster.getProtocolVersion() is protocol_version  # unchanged

    def test_inherited_create_physical_channel(self):
        cluster = UserDefinedCluster(MockParent(), "cluster")

        channel = cluster.createCanPhysicalChannel("Channel")
        assert isinstance(channel, CanPhysicalChannel)
        assert cluster.getPhysicalChannels() == [channel]

        duplicate = cluster.createCanPhysicalChannel("Channel")
        assert duplicate is channel
        assert len(cluster.getPhysicalChannels()) == 1


USER_DEFINED_PHYSICAL_CHANNEL_CLASS_NOTE = "This element allows the modeling of arbitrary Physical Channels."


class TestUserDefinedPhysicalChannel:
    """Test cases for UserDefinedPhysicalChannel (Table 3.130, p.179)."""

    def test_inheritance(self):
        assert issubclass(UserDefinedPhysicalChannel, PhysicalChannel)
        assert issubclass(UserDefinedPhysicalChannel, Identifiable)
        assert issubclass(UserDefinedPhysicalChannel, ARObject)

    def test_concrete_instantiation(self):
        channel = UserDefinedPhysicalChannel(MockParent(), "channel")  # Table 3.130 carries no abstract stereotype

        assert isinstance(channel, PhysicalChannel)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(UserDefinedPhysicalChannel.__doc__) == USER_DEFINED_PHYSICAL_CHANNEL_CLASS_NOTE

    def test_init_docless(self):
        assert UserDefinedPhysicalChannel.__init__.__doc__ is None

    def test_no_own_members(self):
        # Table 3.130's Attribute rows render none — UserDefinedPhysicalChannel adds no fields or accessors beyond its PhysicalChannel base (Rule 0001.3)
        own = [name for name, value in vars(UserDefinedPhysicalChannel).items() if not name.startswith("_")]
        assert own == []

    def test_initialization_defaults(self):
        channel = UserDefinedPhysicalChannel(MockParent(), "channel")

        assert channel.getCommConnectorRefs() == []
        assert channel.getFrameTriggerings() == []
        assert channel.getISignalTriggerings() == []
        assert channel.getManagedPhysicalChannelRefs() == []
        assert channel.getPduTriggerings() == []

    def test_inherited_accessors_round_trip(self):
        channel = UserDefinedPhysicalChannel(MockParent(), "channel")
        comm_connector_ref = RefType()
        comm_connector_ref.setValue("/ECU/CONN")
        managed_channel_ref = RefType()
        managed_channel_ref.setValue("/CLUSTER/MANAGED_CH")

        assert channel == channel.addCommConnectorRef(comm_connector_ref)
        assert channel.getCommConnectorRefs() == [comm_connector_ref]
        assert channel == channel.addCommConnectorRef(None)  # None no-op
        assert channel.getCommConnectorRefs() == [comm_connector_ref]  # unchanged

        assert channel == channel.addManagedPhysicalChannelRef(managed_channel_ref)
        assert channel.getManagedPhysicalChannelRefs() == [managed_channel_ref]
        assert channel == channel.addManagedPhysicalChannelRef(None)  # None no-op
        assert channel.getManagedPhysicalChannelRefs() == [managed_channel_ref]  # unchanged

        triggering = channel.createISignalTriggering("ISignalTriggering")
        assert isinstance(triggering, ISignalTriggering)
        assert channel.getISignalTriggerings() == [triggering]

        pdu_triggering = channel.createPduTriggering("PduTriggering")
        assert isinstance(pdu_triggering, PduTriggering)
        assert channel.getPduTriggerings() == [pdu_triggering]
        assert channel.getFrameTriggerings() == []

        assert channel.createISignalTriggering("ISignalTriggering") is triggering
        assert channel.createPduTriggering("PduTriggering") is pdu_triggering
        assert len(channel.getISignalTriggerings()) == 1
        assert len(channel.getPduTriggerings()) == 1

    def test_cluster_factory_creates_and_appends(self):
        cluster = UserDefinedCluster(MockParent(), "cluster")

        channel = cluster.createUserDefinedPhysicalChannel("Channel")
        assert isinstance(channel, UserDefinedPhysicalChannel)
        assert cluster.getPhysicalChannels() == [channel]

        duplicate = cluster.createUserDefinedPhysicalChannel("Channel")
        assert duplicate is channel
        assert len(cluster.getPhysicalChannels()) == 1
