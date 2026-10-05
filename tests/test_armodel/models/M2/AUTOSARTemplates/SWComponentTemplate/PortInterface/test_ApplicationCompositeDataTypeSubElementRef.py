import typing

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    ApplicationCompositeDataTypeSubElementRef,
    SubElementRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.InstanceRefs import (
    ApplicationCompositeElementInPortInterfaceInstanceRef,
)

SPEC_NOTE = "This meta-class represents the specialization of SubElementMapping with respect to ApplicationCompositeDataTypes."
ELEMENT_NOTE = (
    "This represents the referenced ApplicationCompositeDataPrototype. InstanceRef implemented by: "
    "ApplicationCompositeElementInPortInterfaceInstanceRef"
)


class TestApplicationCompositeDataTypeSubElementRef:
    def test_initialization(self):
        sub_element_ref = ApplicationCompositeDataTypeSubElementRef()

        assert sub_element_ref.getApplicationCompositeElementIRef() is None

    def test_heritage(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

        sub_element_ref = ApplicationCompositeDataTypeSubElementRef()
        assert type(sub_element_ref).__bases__ == (SubElementRef,)
        for ancestor in (ApplicationCompositeDataTypeSubElementRef, SubElementRef, ARObject):
            assert isinstance(sub_element_ref, ancestor)

    def test_sub_element_ref_abstract_guard(self):
        import pytest

        with pytest.raises(TypeError) as err:
            SubElementRef()
        assert str(err.value) == "SubElementRef is an abstract class."

    def test_class_docstring_verbatim(self):
        assert ApplicationCompositeDataTypeSubElementRef.__doc__.strip() == SPEC_NOTE

    def test_get_set_application_composite_element_iref(self):
        sub_element_ref = ApplicationCompositeDataTypeSubElementRef()
        iref = ApplicationCompositeElementInPortInterfaceInstanceRef()

        result = sub_element_ref.setApplicationCompositeElementIRef(iref)
        assert result is sub_element_ref
        assert sub_element_ref.getApplicationCompositeElementIRef() is iref
        sub_element_ref.setApplicationCompositeElementIRef(None)
        assert sub_element_ref.getApplicationCompositeElementIRef() is iref

    def test_docstrings_verbatim(self):
        sub_element_ref = ApplicationCompositeDataTypeSubElementRef()

        def norm(doc):
            return " ".join(doc.split())

        assert norm(sub_element_ref.getApplicationCompositeElementIRef.__doc__) == ELEMENT_NOTE
        assert norm(sub_element_ref.setApplicationCompositeElementIRef.__doc__) == (
            ELEMENT_NOTE + " A None value is a no-op and does not overwrite an existing applicationCompositeElementIRef."
        )

    def test_get_type_hints_pins(self):
        hints = typing.get_type_hints(ApplicationCompositeDataTypeSubElementRef.getApplicationCompositeElementIRef)
        assert hints.get("return") == typing.Optional[ApplicationCompositeElementInPortInterfaceInstanceRef]

        hints = typing.get_type_hints(ApplicationCompositeDataTypeSubElementRef.setApplicationCompositeElementIRef)
        assert hints.get("value") == typing.Optional[ApplicationCompositeElementInPortInterfaceInstanceRef]
        assert hints.get("return") is ApplicationCompositeDataTypeSubElementRef
