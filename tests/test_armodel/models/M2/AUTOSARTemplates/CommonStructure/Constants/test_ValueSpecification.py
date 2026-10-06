from typing import Optional, get_type_hints

import pytest

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import TextValueSpecification, ValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier


class TestValueSpecification:
    def test_abstract_instantiation_raises(self):
        """Table 5.109 marks ValueSpecification (abstract): direct instantiation must raise."""
        with pytest.raises(TypeError):
            ValueSpecification()

    def test_concrete_subclass_inheritance(self):
        """Base accessors are exercised through a concrete subclass (Rule 0006)."""
        spec = TextValueSpecification()
        assert isinstance(spec, ValueSpecification)
        assert spec.getShortLabel() is None

    def test_base_properties(self):
        """shortLabel (Table 5.109, 0..1 attr): default, chaining round-trip, None no-op."""
        spec = TextValueSpecification()
        assert spec.getShortLabel() is None

        label = Identifier().setValue("field1")
        assert spec.setShortLabel(label) is spec
        assert spec.getShortLabel() is label

        spec.setShortLabel(None)
        assert spec.getShortLabel() is label

    def test_get_set_short_label_type_hints(self):
        """Rule 0003: annotation names resolve at runtime (Python 3.8 get_type_hints pin)."""
        hints = get_type_hints(ValueSpecification.setShortLabel)
        assert hints["value"] == Optional[Identifier]
        assert hints["return"] is ValueSpecification
