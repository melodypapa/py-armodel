"""
Regression tests for BlueprintPolicy (R23-11 AUTOSAR_FO_TPS_StandardizationTemplate,
Table C.18, p.164) reader/writer coverage.

BlueprintPolicy is abstract (Base = ARObject only) and owns one attribute
attributeName (String, 1, attr). It has NO own XML element: the XSD BLUEPRINT-POLICY
group (AUTOSAR_00052.xsd l.9211) is substituted by the concrete subclasses
BLUEPRINT-POLICY-LIST / -NOT-MODIFIABLE / -SINGLE, which carry the ATTRIBUTE-NAME
element. Those concrete subclasses are not in this sync's queue, so BlueprintPolicy
itself owns no dedicated XML dispatch (no readBlueprintPolicy/writeBlueprintPolicy)
and attributeName is serialized through the concrete-subclass reader/writer (deferred).
Steps 5/6 are N/A for a dedicated dispatch; these tests pin that N/A contract.
"""

from abc import ABC

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import (
    BlueprintPolicy,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class ConcreteBlueprintPolicy(BlueprintPolicy):
    def __init__(self):
        super().__init__()


class TestBlueprintPolicyReaderWriter:
    """Confirm BlueprintPolicy has no own XML element mapping of its own."""

    def test_no_dedicated_reader_writer_methods(self):
        assert not hasattr(ARXMLParser, "readBlueprintPolicy")
        assert not hasattr(ARXMLWriter, "writeBlueprintPolicy")

    def test_abstract_class(self):
        """Table C.18: BlueprintPolicy is abstract (Base = ARObject only)."""
        assert issubclass(BlueprintPolicy, ABC)
        try:
            _obj = BlueprintPolicy()
            assert False, "BlueprintPolicy should not be instantiable"
        except TypeError as e:
            assert "abstract" in str(e).lower()

    def test_attribute_name_field(self):
        """The single spec attribute attributeName (String, 1, attr) is modeled and defaults to None."""
        obj = ConcreteBlueprintPolicy()
        assert obj.getAttributeName() is None
