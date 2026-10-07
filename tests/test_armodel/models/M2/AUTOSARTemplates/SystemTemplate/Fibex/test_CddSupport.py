"""Unit tests for the Fibex CddSupport module (UserDefinedCluster).

Table 3.129 (p.179) is a page-split table whose fragment A renders the
Class/Package/Note/Base/Aggregated by rows before the caption and carries NO
Attribute rows — the class adds no own fields or accessors beyond its
CommunicationCluster base (Rule 0001.3); the XSD own group USER-DEFINED-CLUSTER
(AUTOSAR_00052.xsd lines 128516-128536) holds only the atpVariation
USER-DEFINED-CLUSTER-VARIANTS/USER-DEFINED-CLUSTER-CONDITIONAL wrapper.
Spec placement per Rule 0007: M2::AUTOSARTemplates::SystemTemplate::Fibex::CddSupport.
"""

import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, PositiveUnlimitedInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.CddSupport import UserDefinedCluster
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanPhysicalChannel
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import FibexElement
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationCluster


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
