"""
Spec-contract tests for PassThroughSwConnector (SWC TPS Table 3.15, p.83).
"""

import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition import PassThroughSwConnector, SwConnector

PASS_THROUGH_SW_CONNECTOR_CLASS_NOTE = "This kind of SwConnector can be used inside a CompositionSwComponentType to connect two delegation PortPrototypes."

PASS_THROUGH_SW_CONNECTOR_MEMBER_NOTES = {
    "providedOuterPort": "This represents the provided outer delegation Port Prototype of the PassThroughSwConnector.",
    "requiredOuterPort": "This represents the required outer delegation Port Prototype of the PassThroughSwConnector.",
}


class TestPassThroughSwConnector:
    """Spec-contract tests for PassThroughSwConnector."""

    def test_is_concrete_sw_connector(self):
        connector = PassThroughSwConnector(None, "pass")
        assert isinstance(connector, SwConnector)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(PassThroughSwConnector.__doc__) == PASS_THROUGH_SW_CONNECTOR_CLASS_NOTE

    def test_init_docless(self):
        assert PassThroughSwConnector.__init__.__doc__ is None

    def test_initialization_defaults(self):
        connector = PassThroughSwConnector(None, "pass")
        assert connector.getProvidedOuterPortRef() is None
        assert connector.getRequiredOuterPortRef() is None

    def test_member_order(self):
        connector = PassThroughSwConnector(None, "pass")
        members = [k for k in vars(connector) if k in ("mappingRef", "providedOuterPortRef", "requiredOuterPortRef")]
        assert members == ["mappingRef", "providedOuterPortRef", "requiredOuterPortRef"]

    def test_get_set_provided_outer_port_ref(self):
        connector = PassThroughSwConnector(None, "pass")
        ref = RefType().setValue("/Pkg/Comp/OuterProvided")
        assert connector.setProvidedOuterPortRef(ref) is connector
        assert connector.getProvidedOuterPortRef() is ref
        assert connector.setProvidedOuterPortRef(None) is connector
        assert connector.getProvidedOuterPortRef() is ref

    def test_get_set_required_outer_port_ref(self):
        connector = PassThroughSwConnector(None, "pass")
        ref = RefType().setValue("/Pkg/Comp/OuterRequired")
        assert connector.setRequiredOuterPortRef(ref) is connector
        assert connector.getRequiredOuterPortRef() is ref
        assert connector.setRequiredOuterPortRef(None) is connector
        assert connector.getRequiredOuterPortRef() is ref

    def test_docstrings_verbatim(self):
        for attr, method_get, method_set in (
            ("providedOuterPort", PassThroughSwConnector.getProvidedOuterPortRef, PassThroughSwConnector.setProvidedOuterPortRef),
            ("requiredOuterPort", PassThroughSwConnector.getRequiredOuterPortRef, PassThroughSwConnector.setRequiredOuterPortRef),
        ):
            note = PASS_THROUGH_SW_CONNECTOR_MEMBER_NOTES[attr]
            for method in (method_get, method_set):
                assert method.__doc__ is not None, method.__name__
                assert method.__doc__.strip().split("\n")[0] == note, method.__name__
        assert "A None value is a no-op and does not overwrite an existing reference." in PassThroughSwConnector.setProvidedOuterPortRef.__doc__
        assert "A None value is a no-op and does not overwrite an existing reference." in PassThroughSwConnector.setRequiredOuterPortRef.__doc__

    def test_type_hints(self):
        import typing

        hints = typing.get_type_hints(PassThroughSwConnector.setProvidedOuterPortRef)
        assert hints["value"] == typing.Optional[RefType]
        assert hints["return"] is PassThroughSwConnector
        hints = typing.get_type_hints(PassThroughSwConnector.getProvidedOuterPortRef)
        assert hints["return"] == typing.Optional[RefType]
        hints = typing.get_type_hints(PassThroughSwConnector.setRequiredOuterPortRef)
        assert hints["value"] == typing.Optional[RefType]
        assert hints["return"] is PassThroughSwConnector
        hints = typing.get_type_hints(PassThroughSwConnector.getRequiredOuterPortRef)
        assert hints["return"] == typing.Optional[RefType]
