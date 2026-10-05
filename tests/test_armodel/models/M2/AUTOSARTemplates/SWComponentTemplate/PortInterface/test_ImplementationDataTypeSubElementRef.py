import typing

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    ImplementationDataTypeSubElementRef,
    SubElementRef,
)

SPEC_NOTE = "This meta-class represents the specialization of SubElementMapping with respect to ImplementationDataTypes."
IMPL_ELEMENT_NOTE = "This represents the referenced implementationDataTypeElement."
PARAM_ELEMENT_NOTE = "This represents the referenced ImplementationDataTypeElement."


class TestImplementationDataTypeSubElementRef:
    def test_initialization(self):
        sub_element_ref = ImplementationDataTypeSubElementRef()

        assert sub_element_ref.getImplementationDataTypeElement() is None
        assert sub_element_ref.getParameterImplementationDataTypeElement() is None

    def test_heritage(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

        sub_element_ref = ImplementationDataTypeSubElementRef()
        assert type(sub_element_ref).__bases__ == (SubElementRef,)
        for ancestor in (ImplementationDataTypeSubElementRef, SubElementRef, ARObject):
            assert isinstance(sub_element_ref, ancestor)

    def test_sub_element_ref_abstract(self):
        import pytest

        with pytest.raises(TypeError) as err:
            SubElementRef()
        assert str(err.value) == "SubElementRef is an abstract class."

    def test_class_docstring_verbatim(self):
        assert ImplementationDataTypeSubElementRef.__doc__.strip() == SPEC_NOTE

    def test_get_set_implementation_data_type_element(self):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import (
            ArVariableInImplementationDataInstanceRef,
        )

        sub_element_ref = ImplementationDataTypeSubElementRef()
        iref = ArVariableInImplementationDataInstanceRef()

        result = sub_element_ref.setImplementationDataTypeElement(iref)
        assert result is sub_element_ref
        assert sub_element_ref.getImplementationDataTypeElement() is iref
        sub_element_ref.setImplementationDataTypeElement(None)
        assert sub_element_ref.getImplementationDataTypeElement() is iref

    def test_get_set_parameter_implementation_data_type_element(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
            ArParameterInImplementationDataInstanceRef,
        )

        sub_element_ref = ImplementationDataTypeSubElementRef()
        iref = ArParameterInImplementationDataInstanceRef()

        result = sub_element_ref.setParameterImplementationDataTypeElement(iref)
        assert result is sub_element_ref
        assert sub_element_ref.getParameterImplementationDataTypeElement() is iref
        sub_element_ref.setParameterImplementationDataTypeElement(None)
        assert sub_element_ref.getParameterImplementationDataTypeElement() is iref

    def test_docstrings_verbatim(self):
        sub_element_ref = ImplementationDataTypeSubElementRef()

        def norm(doc):
            return " ".join(doc.split())

        assert norm(sub_element_ref.getImplementationDataTypeElement.__doc__) == IMPL_ELEMENT_NOTE
        assert norm(sub_element_ref.setImplementationDataTypeElement.__doc__) == (
            IMPL_ELEMENT_NOTE + " A None value is a no-op and does not overwrite an existing implementationDataTypeElement."
        )
        assert norm(sub_element_ref.getParameterImplementationDataTypeElement.__doc__) == PARAM_ELEMENT_NOTE
        assert norm(sub_element_ref.setParameterImplementationDataTypeElement.__doc__) == (
            PARAM_ELEMENT_NOTE + " A None value is a no-op and does not overwrite an existing parameterImplementationDataTypeElement."
        )

    def test_get_type_hints_pins(self):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import (
            ArVariableInImplementationDataInstanceRef,
        )
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
            ArParameterInImplementationDataInstanceRef,
        )

        hints = typing.get_type_hints(ImplementationDataTypeSubElementRef.getImplementationDataTypeElement)
        assert hints.get("return") == typing.Optional[ArVariableInImplementationDataInstanceRef]

        hints = typing.get_type_hints(ImplementationDataTypeSubElementRef.getParameterImplementationDataTypeElement)
        assert hints.get("return") == typing.Optional[ArParameterInImplementationDataInstanceRef]
