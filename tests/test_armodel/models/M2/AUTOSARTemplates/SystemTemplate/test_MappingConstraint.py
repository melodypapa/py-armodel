import inspect
import typing

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import MappingScopeEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import ComponentInSystemInstanceRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import ComponentClustering, MappingConstraint
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock


class _ConcreteMappingConstraint(MappingConstraint):
    """Minimal concrete test double: the real subclass ComponentSeparation (Table 5.11) is still queued for its own sync pass."""

    pass


class TestMappingConstraint:
    """Test cases for MappingConstraint (Table 5.8, p.202)."""

    MEMBERS = [
        "introduction",
    ]

    def test_inheritance(self):
        assert issubclass(MappingConstraint, ARObject)
        assert issubclass(MappingConstraint, VariationPointCapable)

    def test_abstract(self):
        with pytest.raises(TypeError):
            MappingConstraint()
        constraint = _ConcreteMappingConstraint()
        assert isinstance(constraint, MappingConstraint)

    def test_class_docstring_note(self):
        expected = "Different constraints that may be used to limit the mapping of SW components to applicable ECUs, " "Partitions or Cores depending on the mappingScope attribute."
        assert inspect.cleandoc(MappingConstraint.__doc__) == expected

    def test_init_has_no_docstring(self):
        assert MappingConstraint.__init__.__doc__ is None

    def test_initialization_defaults(self):
        constraint = _ConcreteMappingConstraint()
        assert constraint.getIntroduction() is None

    def test_member_order(self):
        constraint = _ConcreteMappingConstraint()
        members = [k for k in vars(constraint) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_get_set_introduction(self):
        constraint = _ConcreteMappingConstraint()
        block = DocumentationBlock()
        result = constraint.setIntroduction(block)
        assert result is constraint
        assert constraint.getIntroduction() is block
        constraint.setIntroduction(None)
        assert constraint.getIntroduction() is block

    def test_type_hints(self):
        hints = typing.get_type_hints(MappingConstraint.getIntroduction)
        assert hints.get("return") == typing.Optional[DocumentationBlock]
        hints = typing.get_type_hints(MappingConstraint.setIntroduction)
        assert hints.get("value") == typing.Optional[DocumentationBlock]
        assert hints.get("return") is MappingConstraint


class TestComponentClustering:
    """Test cases for ComponentClustering (Table 5.9, p.203) and the abstract-base accessors through this concrete subclass."""

    MEMBERS = [
        "clusteredComponentIRefs",
        "mappingScope",
    ]

    def _mapping_scope(self, value: str = "MAPPING-SCOPE-CORE") -> MappingScopeEnum:
        scope = MappingScopeEnum(("MAPPING-SCOPE-CORE", "MAPPING-SCOPE-ECU", "MAPPING-SCOPE-PARTITION"))
        scope.setValue(value)
        return scope

    def test_inheritance(self):
        assert issubclass(ComponentClustering, MappingConstraint)
        assert issubclass(ComponentClustering, ARObject)
        assert issubclass(ComponentClustering, VariationPointCapable)

    def test_concrete(self):
        clustering = ComponentClustering()
        assert isinstance(clustering, MappingConstraint)

    def test_class_docstring_note(self):
        expected = (
            "Constraint that forces the mapping of all referenced SW component instances to the same ECU, Core, Partition "
            "depending on the defined mappingScope attribute. If mappingScope is not specified then mappingScopeEcu shall be assumed."
        )
        assert inspect.cleandoc(ComponentClustering.__doc__) == expected

    def test_init_has_no_docstring(self):
        assert ComponentClustering.__init__.__doc__ is None

    def test_initialization_defaults(self):
        clustering = ComponentClustering()
        assert clustering.getClusteredComponentIRefs() == []
        assert clustering.getMappingScope() is None

    def test_member_order(self):
        clustering = ComponentClustering()
        members = [k for k in vars(clustering) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_add_clustered_component_i_ref(self):
        clustering = ComponentClustering()
        iref = ComponentInSystemInstanceRef()
        result = clustering.addClusteredComponentIRef(iref)
        assert result is clustering
        assert clustering.getClusteredComponentIRefs() == [iref]
        iref2 = ComponentInSystemInstanceRef()
        clustering.addClusteredComponentIRef(iref2)
        assert clustering.getClusteredComponentIRefs() == [iref, iref2]

    def test_add_clustered_component_i_ref_none_no_op(self):
        clustering = ComponentClustering()
        clustering.addClusteredComponentIRef(None)
        assert clustering.getClusteredComponentIRefs() == []

    def test_get_set_mapping_scope(self):
        clustering = ComponentClustering()
        scope = self._mapping_scope("MAPPING-SCOPE-ECU")
        result = clustering.setMappingScope(scope)
        assert result is clustering
        assert clustering.getMappingScope() is scope
        assert clustering.getMappingScope().getValue() == "MAPPING-SCOPE-ECU"

    def test_set_mapping_scope_none_no_op(self):
        clustering = ComponentClustering()
        scope = self._mapping_scope("MAPPING-SCOPE-PARTITION")
        clustering.setMappingScope(scope)
        clustering.setMappingScope(None)
        assert clustering.getMappingScope() is scope

    def test_base_accessors_via_concrete_subclass(self):
        clustering = ComponentClustering()
        assert clustering.getIntroduction() is None
        block = DocumentationBlock()
        result = clustering.setIntroduction(block)
        assert result is clustering
        assert clustering.getIntroduction() is block
        clustering.setIntroduction(None)
        assert clustering.getIntroduction() is block

    def test_base_variation_point_accessor_via_concrete_subclass(self):
        clustering = ComponentClustering()
        assert clustering.getVariationPoint() is None

    def test_type_hints(self):
        hints = typing.get_type_hints(ComponentClustering.addClusteredComponentIRef)
        assert hints.get("value") == typing.Optional[ComponentInSystemInstanceRef]
        assert hints.get("return") is ComponentClustering
        hints = typing.get_type_hints(ComponentClustering.getClusteredComponentIRefs)
        assert hints.get("return") == typing.List[ComponentInSystemInstanceRef]
        hints = typing.get_type_hints(ComponentClustering.getMappingScope)
        assert hints.get("return") == typing.Optional[MappingScopeEnum]
        hints = typing.get_type_hints(ComponentClustering.setMappingScope)
        assert hints.get("value") == typing.Optional[MappingScopeEnum]
        assert hints.get("return") is ComponentClustering
