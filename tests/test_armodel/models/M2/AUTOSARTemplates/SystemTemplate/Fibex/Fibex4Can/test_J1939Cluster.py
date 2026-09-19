"""
This module contains tests for the J1939Cluster class
in the AUTOSAR SystemTemplate Fibex4Can module.
"""

import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import J1939Cluster
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import AbstractCanCluster, CommunicationCluster

SPEC_NOTE = (
    "J1939 specific cluster attributes. Tags: atp.recommendedPackage=CommunicationClusters\n"
    "\n"
    "[constr_3050] J1939Cluster uses exactly one CanPhysicalChannel: A J1939Cluster shall aggregate exactly one CanPhysicalChannel.\n"
    "\n"
    "[constr_1463] Applicable values for J1939Cluster.networkId: The values of the attribute J1939Cluster.networkId shall always be within the interval 1..4."
)


class TestJ1939Cluster:
    def test_initialization(self):
        """Test that the concrete J1939Cluster is an AbstractCanCluster wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        cluster = J1939Cluster(ar_root, "TestJ1939Cluster")

        assert isinstance(cluster, AbstractCanCluster)
        assert isinstance(cluster, CommunicationCluster)
        assert cluster.getShortName() == "TestJ1939Cluster"

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 3.28)"""
        assert inspect.cleandoc(J1939Cluster.__doc__).strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert J1939Cluster.__init__.__doc__ is None

    def test_member_order_matches_spec(self):
        """Test member declaration order follows the R23-11 displayed row order"""
        source = inspect.getsource(J1939Cluster.__init__)
        network_id_pos = source.index("self.networkId")
        request2_support_pos = source.index("self.request2Support")
        uses_address_arbitration_pos = source.index("self.usesAddressArbitration")
        assert network_id_pos < request2_support_pos < uses_address_arbitration_pos

    def test_get_set_network_id(self):
        """Test networkId default, guarded set chaining, None no-op and typing"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        cluster = J1939Cluster(ar_root, "TestNetworkId")

        assert cluster.getNetworkId() is None

        network_id = PositiveInteger()
        network_id.setValue("2")
        assert cluster == cluster.setNetworkId(network_id)
        assert cluster.getNetworkId() == network_id

        assert cluster == cluster.setNetworkId(None)
        assert cluster.getNetworkId() == network_id

        getter_hints = typing.get_type_hints(J1939Cluster.getNetworkId)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(J1939Cluster.setNetworkId)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is J1939Cluster

    def test_get_set_request2_support(self):
        """Test request2Support default, guarded set chaining, None no-op and typing"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        cluster = J1939Cluster(ar_root, "TestRequest2Support")

        assert cluster.getRequest2Support() is None

        request2_support = Boolean()
        request2_support.setValue("true")
        assert cluster == cluster.setRequest2Support(request2_support)
        assert cluster.getRequest2Support() == request2_support

        assert cluster == cluster.setRequest2Support(None)
        assert cluster.getRequest2Support() == request2_support

        getter_hints = typing.get_type_hints(J1939Cluster.getRequest2Support)
        assert getter_hints.get("return") == typing.Optional[Boolean]

        setter_hints = typing.get_type_hints(J1939Cluster.setRequest2Support)
        assert setter_hints.get("value") == typing.Optional[Boolean]
        assert setter_hints.get("return") is J1939Cluster

    def test_get_set_uses_address_arbitration(self):
        """Test usesAddressArbitration default, guarded set chaining, None no-op and typing"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        cluster = J1939Cluster(ar_root, "TestUsesAddressArbitration")

        assert cluster.getUsesAddressArbitration() is None

        uses_address_arbitration = Boolean()
        uses_address_arbitration.setValue("false")
        assert cluster == cluster.setUsesAddressArbitration(uses_address_arbitration)
        assert cluster.getUsesAddressArbitration() == uses_address_arbitration

        assert cluster == cluster.setUsesAddressArbitration(None)
        assert cluster.getUsesAddressArbitration() == uses_address_arbitration

        getter_hints = typing.get_type_hints(J1939Cluster.getUsesAddressArbitration)
        assert getter_hints.get("return") == typing.Optional[Boolean]

        setter_hints = typing.get_type_hints(J1939Cluster.setUsesAddressArbitration)
        assert setter_hints.get("value") == typing.Optional[Boolean]
        assert setter_hints.get("return") is J1939Cluster

    def test_ar_package_create_j1939_cluster(self):
        """Test ARPackage.createJ1939Cluster factory with type-qualified duplicate protection"""
        parent = AUTOSAR.getInstance()
        ar_package = parent.createARPackage("AUTOSAR")
        assert isinstance(ar_package, ARPackage)

        cluster = ar_package.createJ1939Cluster("J1939ClusterA")
        assert isinstance(cluster, J1939Cluster)
        assert cluster.getShortName() == "J1939ClusterA"

        cluster2 = ar_package.createJ1939Cluster("J1939ClusterA")
        assert cluster2 is cluster
