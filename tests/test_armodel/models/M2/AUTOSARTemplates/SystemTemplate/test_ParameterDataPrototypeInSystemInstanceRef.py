"""Reader tests for the ParameterDataPrototypeInSystemInstanceRef class.

The class is XSD-only (no own table in the repo corpus); the member set and the
xml.sequenceOffset order derive from the PARAMETER-DATA-PROTOTYPE-IN-SYSTEM-INSTANCE-REF
group (AUTOSAR_00052.xsd l.87933, complexType l.87991).
"""

import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import ParameterDataPrototypeInSystemInstanceRef


def _ref(value: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    return ref


class TestParameterDataPrototypeInSystemInstanceRef:
    """Test cases for ParameterDataPrototypeInSystemInstanceRef (AUTOSAR_00052.xsd l.87991)."""

    MEMBERS = [
        "contextCompositionRef",
        "contextComponentRefs",
        "contextPortRef",
        "targetParameterDataPrototypeRef",
    ]

    def test_inheritance(self):
        assert issubclass(ParameterDataPrototypeInSystemInstanceRef, AtpInstanceRef)

    def test_initialization_defaults(self):
        instance_ref = ParameterDataPrototypeInSystemInstanceRef()
        assert instance_ref.getBaseRef() is None
        assert instance_ref.getContextComponentRefs() == []
        assert instance_ref.getContextCompositionRef() is None
        assert instance_ref.getContextPortRef() is None
        assert instance_ref.getTargetParameterDataPrototypeRef() is None

    def test_member_order(self):
        instance_ref = ParameterDataPrototypeInSystemInstanceRef()
        members = [k for k in vars(instance_ref) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_get_set_base_ref(self):
        instance_ref = ParameterDataPrototypeInSystemInstanceRef()
        result = instance_ref.setBaseRef(_ref("/Root"))
        assert result is instance_ref
        assert instance_ref.getBaseRef().getValue() == "/Root"
        instance_ref.setBaseRef(None)
        assert instance_ref.getBaseRef().getValue() == "/Root"

    def test_add_context_component_ref(self):
        instance_ref = ParameterDataPrototypeInSystemInstanceRef()
        result = instance_ref.addContextComponentRef(_ref("/SwcA"))
        assert result is instance_ref
        instance_ref.addContextComponentRef(_ref("/SwcB"))
        assert [ref.getValue() for ref in instance_ref.getContextComponentRefs()] == ["/SwcA", "/SwcB"]
        instance_ref.addContextComponentRef(None)
        assert len(instance_ref.getContextComponentRefs()) == 2

    def test_get_set_context_composition_ref(self):
        instance_ref = ParameterDataPrototypeInSystemInstanceRef()
        instance_ref.setContextCompositionRef(_ref("/Root"))
        assert instance_ref.getContextCompositionRef().getValue() == "/Root"
        instance_ref.setContextCompositionRef(None)
        assert instance_ref.getContextCompositionRef().getValue() == "/Root"

    def test_get_set_context_port_ref(self):
        instance_ref = ParameterDataPrototypeInSystemInstanceRef()
        instance_ref.setContextPortRef(_ref("/Port"))
        assert instance_ref.getContextPortRef().getValue() == "/Port"
        instance_ref.setContextPortRef(None)
        assert instance_ref.getContextPortRef().getValue() == "/Port"

    def test_get_set_target_parameter_data_prototype_ref(self):
        instance_ref = ParameterDataPrototypeInSystemInstanceRef()
        instance_ref.setTargetParameterDataPrototypeRef(_ref("/Parameter"))
        assert instance_ref.getTargetParameterDataPrototypeRef().getValue() == "/Parameter"
        instance_ref.setTargetParameterDataPrototypeRef(None)
        assert instance_ref.getTargetParameterDataPrototypeRef().getValue() == "/Parameter"

    def test_type_hints(self):
        hints = typing.get_type_hints(ParameterDataPrototypeInSystemInstanceRef.getBaseRef)
        assert hints["return"] == typing.Optional[RefType]
        hints = typing.get_type_hints(ParameterDataPrototypeInSystemInstanceRef.getContextComponentRefs)
        assert hints["return"] == typing.List[RefType]
        hints = typing.get_type_hints(ParameterDataPrototypeInSystemInstanceRef.getTargetParameterDataPrototypeRef)
        assert hints["return"] == typing.Optional[RefType]
