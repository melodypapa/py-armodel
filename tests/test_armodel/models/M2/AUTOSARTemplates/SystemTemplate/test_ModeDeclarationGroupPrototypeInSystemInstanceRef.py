"""Reader tests for the ModeDeclarationGroupPrototypeInSystemInstanceRef class.

The class is XSD-only (no own table in the repo corpus); the member set and the
xml.sequenceOffset order derive from the MODE-DECLARATION-GROUP-PROTOTYPE-IN-SYSTEM-INSTANCE-REF
group (AUTOSAR_00052.xsd l.82093, complexType l.82151).
"""

import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import ModeDeclarationGroupPrototypeInSystemInstanceRef


def _ref(value: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    return ref


class TestModeDeclarationGroupPrototypeInSystemInstanceRef:
    """Test cases for ModeDeclarationGroupPrototypeInSystemInstanceRef (AUTOSAR_00052.xsd l.82151)."""

    MEMBERS = [
        "contextCompositionRef",
        "contextComponentRefs",
        "contextPortRef",
        "targetModeDeclarationGroupPrototypeRef",
    ]

    def test_inheritance(self):
        assert issubclass(ModeDeclarationGroupPrototypeInSystemInstanceRef, AtpInstanceRef)

    def test_initialization_defaults(self):
        instance_ref = ModeDeclarationGroupPrototypeInSystemInstanceRef()
        assert instance_ref.getBaseRef() is None
        assert instance_ref.getContextComponentRefs() == []
        assert instance_ref.getContextCompositionRef() is None
        assert instance_ref.getContextPortRef() is None
        assert instance_ref.getTargetModeDeclarationGroupPrototypeRef() is None

    def test_member_order(self):
        instance_ref = ModeDeclarationGroupPrototypeInSystemInstanceRef()
        members = [k for k in vars(instance_ref) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_get_set_base_ref(self):
        instance_ref = ModeDeclarationGroupPrototypeInSystemInstanceRef()
        result = instance_ref.setBaseRef(_ref("/Root"))
        assert result is instance_ref
        assert instance_ref.getBaseRef().getValue() == "/Root"
        instance_ref.setBaseRef(None)
        assert instance_ref.getBaseRef().getValue() == "/Root"

    def test_add_context_component_ref(self):
        instance_ref = ModeDeclarationGroupPrototypeInSystemInstanceRef()
        result = instance_ref.addContextComponentRef(_ref("/SwcA"))
        assert result is instance_ref
        instance_ref.addContextComponentRef(_ref("/SwcB"))
        assert [ref.getValue() for ref in instance_ref.getContextComponentRefs()] == ["/SwcA", "/SwcB"]
        instance_ref.addContextComponentRef(None)
        assert len(instance_ref.getContextComponentRefs()) == 2

    def test_get_set_context_composition_ref(self):
        instance_ref = ModeDeclarationGroupPrototypeInSystemInstanceRef()
        instance_ref.setContextCompositionRef(_ref("/Root"))
        assert instance_ref.getContextCompositionRef().getValue() == "/Root"
        instance_ref.setContextCompositionRef(None)
        assert instance_ref.getContextCompositionRef().getValue() == "/Root"

    def test_get_set_context_port_ref(self):
        instance_ref = ModeDeclarationGroupPrototypeInSystemInstanceRef()
        instance_ref.setContextPortRef(_ref("/Port"))
        assert instance_ref.getContextPortRef().getValue() == "/Port"
        instance_ref.setContextPortRef(None)
        assert instance_ref.getContextPortRef().getValue() == "/Port"

    def test_get_set_target_mode_declaration_group_prototype_ref(self):
        instance_ref = ModeDeclarationGroupPrototypeInSystemInstanceRef()
        instance_ref.setTargetModeDeclarationGroupPrototypeRef(_ref("/ModeGroup"))
        assert instance_ref.getTargetModeDeclarationGroupPrototypeRef().getValue() == "/ModeGroup"
        instance_ref.setTargetModeDeclarationGroupPrototypeRef(None)
        assert instance_ref.getTargetModeDeclarationGroupPrototypeRef().getValue() == "/ModeGroup"

    def test_type_hints(self):
        hints = typing.get_type_hints(ModeDeclarationGroupPrototypeInSystemInstanceRef.getBaseRef)
        assert hints["return"] == typing.Optional[RefType]
        hints = typing.get_type_hints(ModeDeclarationGroupPrototypeInSystemInstanceRef.getContextComponentRefs)
        assert hints["return"] == typing.List[RefType]
        hints = typing.get_type_hints(ModeDeclarationGroupPrototypeInSystemInstanceRef.getTargetModeDeclarationGroupPrototypeRef)
        assert hints["return"] == typing.Optional[RefType]
