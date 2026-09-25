"""
Tests for the BlueprintMapping class (R23-11 FO_TPS_StandardizationTemplate Table C.17).

BlueprintMapping is a concrete specialization of the abstract AtpBlueprintMapping
(Base row "ARObject , AtpBlueprintMapping") with the two ref attributes blueprint
and derivedObject (XSD 00052 group BLUEPRINT-MAPPING: BLUEPRINT-REF ->
DERIVED-OBJECT-REF). BlueprintMappingSet lives in the same source module and is
tested in test_BlueprintMappingSet.py.
"""

import inspect
import re

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import (
    AtpBlueprintMapping,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintMapping import (
    BlueprintMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestBlueprintMapping:
    """
    Functional tests for BlueprintMapping.
    """

    def test_initialization(self):
        mapping = BlueprintMapping()
        assert isinstance(mapping, BlueprintMapping)
        assert isinstance(mapping, AtpBlueprintMapping)
        assert isinstance(mapping, ARObject)
        assert mapping.getBlueprintRef() is None
        assert mapping.getDerivedObjectRef() is None

    def test_get_set_blueprint_ref(self):
        mapping = BlueprintMapping()
        ref = RefType()
        ref.setDest("ECUC-MODULE-DEF")
        ref.setValue("/Pkg/Blueprint")
        assert mapping.setBlueprintRef(ref) is mapping
        assert mapping.getBlueprintRef() is ref
        assert mapping.setBlueprintRef(None) is mapping
        assert mapping.getBlueprintRef() is ref

    def test_get_set_derived_object_ref(self):
        mapping = BlueprintMapping()
        ref = RefType()
        ref.setDest("COMPU-METHOD")
        ref.setValue("/Pkg/Derived")
        assert mapping.setDerivedObjectRef(ref) is mapping
        assert mapping.getDerivedObjectRef() is ref
        assert mapping.setDerivedObjectRef(None) is mapping
        assert mapping.getDerivedObjectRef() is ref


class TestBlueprintMappingSpecContract:
    """
    Spec-contract pins for R23-11 Table C.17 (field-to-spec cross-check in both
    directions; docstrings = spec Note verbatim; Rule 0003/0005/0008/0011 pins).
    """

    def test_exact_own_field_set(self):
        """Rule 0001.1/0001.3: exactly the two C.17 attributes as own fields, no extras."""
        src = inspect.getsource(BlueprintMapping.__init__)
        assert re.findall(r"self\.(\w+)\s*:", src) == ["blueprintRef", "derivedObjectRef"]

    def test_pep526_annotated_members(self):
        """Rule 0003: PEP 526 annotated assignments, no trailing `# type:` comments."""
        src = inspect.getsource(BlueprintMapping)
        assert re.search(r"self\.blueprintRef:\s*Optional\[RefType\]\s*=\s*None", src)
        assert re.search(r"self\.derivedObjectRef:\s*Optional\[RefType\]\s*=\s*None", src)
        assert "# type:" not in src

    def test_most_derived_base(self):
        """Rule 0001.2: Base row "ARObject , AtpBlueprintMapping" -> most-derived AtpBlueprintMapping."""
        assert BlueprintMapping.__bases__ == (AtpBlueprintMapping,)

    def test_accessor_order_matches_displayed_rows(self):
        """Rule 0001.11: accessors in displayed row order blueprint -> derivedObject, get->set pairs."""
        src = inspect.getsource(BlueprintMapping)
        defs = re.findall(r"def (\w+)\(", src)
        assert defs == [
            "__init__",
            "getBlueprintRef",
            "setBlueprintRef",
            "getDerivedObjectRef",
            "setDerivedObjectRef",
        ]

    def test_class_docstring_verbatim(self):
        """Rule 0012: class docstring = the C.17 Note verbatim (spec typo "two an" kept)."""
        assert inspect.getdoc(BlueprintMapping) == ("This meta-class represents the ability to map two an object and its blueprint.")

    def test_get_blueprint_ref_docstring_verbatim(self):
        assert inspect.getdoc(BlueprintMapping.getBlueprintRef) == "This represents the mapped blueprint."

    def test_set_blueprint_ref_docstring_verbatim(self):
        assert inspect.getdoc(BlueprintMapping.setBlueprintRef) == ("This represents the mapped blueprint. A None value is a no-op and is not set.")

    def test_get_derived_object_ref_docstring_verbatim(self):
        assert inspect.getdoc(BlueprintMapping.getDerivedObjectRef) == ("This represents the object which was derived from the blueprint.")

    def test_set_derived_object_ref_docstring_verbatim(self):
        assert inspect.getdoc(BlueprintMapping.setDerivedObjectRef) == ("This represents the object which was derived from the blueprint. A None value is a no-op and is not set.")
