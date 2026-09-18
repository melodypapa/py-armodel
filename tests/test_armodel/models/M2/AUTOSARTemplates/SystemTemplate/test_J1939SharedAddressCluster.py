"""
This module contains tests for the J1939SharedAddressCluster class
in the AUTOSAR SystemTemplate module.
"""

import typing

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import J1939SharedAddressCluster

SPEC_NOTE = "This meta-class represents the ability to identify several J1939Clusters that share a common address space for the routing of messages"


class TestJ1939SharedAddressCluster:
    def test_initialization(self):
        """Test that the concrete J1939SharedAddressCluster is an Identifiable wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        cluster = J1939SharedAddressCluster(ar_root, "TestJ1939SharedAddressCluster")

        assert isinstance(cluster, Identifiable)
        assert isinstance(cluster, VariationPointCapable)
        assert cluster.getShortName() == "TestJ1939SharedAddressCluster"

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 6.324)"""
        assert J1939SharedAddressCluster.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert J1939SharedAddressCluster.__init__.__doc__ is None

    def test_get_set_participating_j1939_cluster_refs(self):
        """Test participatingJ1939ClusterRefs default, add chaining, None no-op and typing"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        cluster = J1939SharedAddressCluster(ar_root, "TestRefs")

        assert cluster.getParticipatingJ1939ClusterRefs() == []
        assert cluster.getVariationPoint() is None

        ref = RefType()
        ref.setValue("/Systems/J1939Cluster")
        ref.setDest("J1939CLUSTER")
        assert cluster == cluster.addParticipatingJ1939ClusterRef(ref)
        assert cluster.getParticipatingJ1939ClusterRefs() == [ref]

        assert cluster == cluster.addParticipatingJ1939ClusterRef(None)
        assert cluster.getParticipatingJ1939ClusterRefs() == [ref]

        getter_hints = typing.get_type_hints(J1939SharedAddressCluster.getParticipatingJ1939ClusterRefs)
        assert getter_hints.get("return") == typing.List[RefType]

        setter_hints = typing.get_type_hints(J1939SharedAddressCluster.addParticipatingJ1939ClusterRef)
        assert setter_hints.get("value") == typing.Optional[RefType]
        assert setter_hints.get("return") is J1939SharedAddressCluster
