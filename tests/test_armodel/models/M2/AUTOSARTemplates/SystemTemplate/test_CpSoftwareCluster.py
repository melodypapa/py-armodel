"""
This module contains tests for the CpSoftwareCluster class
in the AUTOSAR SystemTemplate module.
"""

import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import CpSoftwareCluster, SwComponentPrototypeAssignment

SPEC_NOTE = (
    "This meta class provides the ability to define a CP Software Cluster. "
    "Each CP Software Cluster can be integrated and build individually. "
    "It defines the sub-set of hierarchical tree(s) of Software Components belonging to this CP Software Cluster. "
    "Resources required or provided by this CP Software Cluster are given in the according mappings. "
    "Tags: atp.recommendedPackage=CpSoftwareClusters"
)


class TestCpSoftwareCluster:
    def test_initialization(self):
        """Test that the concrete CpSoftwareCluster is an ARElement wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        cluster = CpSoftwareCluster(ar_root, "TestCluster")

        assert isinstance(cluster, ARElement)
        assert cluster.getShortName() == "TestCluster"

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 11.1)"""
        assert CpSoftwareCluster.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert CpSoftwareCluster.__init__.__doc__ is None

    def test_member_order_matches_spec(self):
        """Test member declaration order follows the R23-11 displayed row order"""
        source = inspect.getsource(CpSoftwareCluster.__init__)
        id_pos = source.index("self.softwareClusterId")
        assignments_pos = source.index("self.swComponentAssignments")
        refs_pos = source.index("self.swCompositionRefs")
        assert id_pos < assignments_pos < refs_pos

    def test_set_get_software_cluster_id(self):
        """Test softwareClusterId default, guarded set chaining, None no-op and typing"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        cluster = CpSoftwareCluster(ar_root, "TestId")

        assert cluster.getSoftwareClusterId() is None

        cluster_id = PositiveInteger()
        assert cluster == cluster.setSoftwareClusterId(cluster_id)
        assert cluster.getSoftwareClusterId() == cluster_id

        assert cluster == cluster.setSoftwareClusterId(None)
        assert cluster.getSoftwareClusterId() == cluster_id

        getter_hints = typing.get_type_hints(CpSoftwareCluster.getSoftwareClusterId)
        assert getter_hints.get("return") == typing.Optional[PositiveInteger]

        setter_hints = typing.get_type_hints(CpSoftwareCluster.setSoftwareClusterId)
        assert setter_hints.get("value") == typing.Optional[PositiveInteger]
        assert setter_hints.get("return") is CpSoftwareCluster

    def test_add_get_sw_component_assignments(self):
        """Test swComponentAssignments default, add chaining and typing"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        cluster = CpSoftwareCluster(ar_root, "TestAssignments")

        assert cluster.getSwComponentAssignments() == []

        assignment = SwComponentPrototypeAssignment()
        assert cluster == cluster.addSwComponentAssignment(assignment)
        assert cluster.getSwComponentAssignments() == [assignment]

        getter_hints = typing.get_type_hints(CpSoftwareCluster.getSwComponentAssignments)
        assert getter_hints.get("return") == typing.List[SwComponentPrototypeAssignment]

        adder_hints = typing.get_type_hints(CpSoftwareCluster.addSwComponentAssignment)
        assert adder_hints.get("value") is SwComponentPrototypeAssignment
        assert adder_hints.get("return") is CpSoftwareCluster

    def test_create_sw_component_assignment(self):
        """Test createSwComponentAssignment appends a new child per call (no SHORT-NAME, no duplicate protection)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        cluster = CpSoftwareCluster(ar_root, "TestCreate")

        assignment = cluster.createSwComponentAssignment()
        assert isinstance(assignment, SwComponentPrototypeAssignment)
        assert cluster.getSwComponentAssignments() == [assignment]

        assignment2 = cluster.createSwComponentAssignment()
        assert assignment2 is not assignment
        assert cluster.getSwComponentAssignments() == [assignment, assignment2]

    def test_add_get_sw_composition_refs(self):
        """Test swCompositionRefs default, guarded add chaining, None no-op and typing"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        cluster = CpSoftwareCluster(ar_root, "TestRefs")

        assert cluster.getSwCompositionRefs() == []

        ref = RefType()
        assert cluster == cluster.addSwCompositionRef(ref)
        assert cluster.getSwCompositionRefs() == [ref]

        assert cluster == cluster.addSwCompositionRef(None)
        assert cluster.getSwCompositionRefs() == [ref]

        getter_hints = typing.get_type_hints(CpSoftwareCluster.getSwCompositionRefs)
        assert getter_hints.get("return") == typing.List[RefType]

        adder_hints = typing.get_type_hints(CpSoftwareCluster.addSwCompositionRef)
        assert adder_hints.get("value") == typing.Optional[RefType]
        assert adder_hints.get("return") is CpSoftwareCluster
