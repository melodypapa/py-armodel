"""
Spec-contract tests for SwConnector (SWC TPS Table 3.12, p.80).
"""

import inspect

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition import (
    PassThroughSwConnector,
    SwConnector,
)

SW_CONNECTOR_CLASS_NOTE = "The base class for connectors between ports. Connectors have to be identifiable to allow references from the system constraint template."

SW_CONNECTOR_MEMBER_NOTES = {
    "mapping": "Reference to a PortInterfaceMapping specifying the mapping of unequal named PortInterface elements of the two different PortInterfaces typing the two PortPrototypes which are referenced by the ConnectorPrototype.",
}


class TestSwConnector:
    """Spec-contract tests for the abstract SwConnector base."""

    def _make(self, name="conn"):
        return PassThroughSwConnector(None, name)

    def test_base_class(self):
        assert issubclass(SwConnector, AtpStructureElement)

    def test_abstract_guard(self):
        with pytest.raises(TypeError, match="SwConnector is an abstract class"):
            SwConnector(None, "abstract")

    def test_class_docstring_note(self):
        assert inspect.cleandoc(SwConnector.__doc__) == SW_CONNECTOR_CLASS_NOTE

    def test_init_docless(self):
        assert SwConnector.__init__.__doc__ is None

    def test_initialization_defaults(self):
        connector = self._make()
        assert connector.getMappingRef() is None

    def test_not_variation_point_capable(self):
        assert not hasattr(SwConnector, "setVariationPoint")

    def test_get_set_mapping_ref(self):
        connector = self._make()
        ref = RefType().setValue("/Pkg/PortInterfaceMappingSet/Mapping1")
        assert connector.setMappingRef(ref) is connector
        assert connector.getMappingRef() is ref
        assert connector.setMappingRef(None) is connector
        assert connector.getMappingRef() is ref

    def test_base_accessors_via_concrete_subclass(self):
        connector = self._make()
        ref = RefType().setValue("/Pkg/M1")
        connector.setMappingRef(ref)
        assert connector.getMappingRef().getValue() == "/Pkg/M1"
        connector.setMappingRef(None)
        assert connector.getMappingRef() is ref

    def test_docstrings_verbatim(self):
        note = SW_CONNECTOR_MEMBER_NOTES["mapping"]
        for method in (SwConnector.getMappingRef, SwConnector.setMappingRef):
            assert method.__doc__ is not None, method.__name__
            assert method.__doc__.strip().split("\n")[0] == note, method.__name__
        assert "A None value is a no-op and does not overwrite an existing reference." in SwConnector.setMappingRef.__doc__

    def test_type_hints(self):
        import typing

        hints = typing.get_type_hints(SwConnector.setMappingRef)
        assert hints["value"] == typing.Optional[RefType]
        assert hints["return"] is SwConnector
        hints = typing.get_type_hints(SwConnector.getMappingRef)
        assert hints["return"] == typing.Optional[RefType]
