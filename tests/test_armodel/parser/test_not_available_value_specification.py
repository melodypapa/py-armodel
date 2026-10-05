"""Reader tests for NotAvailableValueSpecification (Swc TPS Table 5.116, p.440).

getNotAvailableValueSpecification populates the model via the mutators: readValueSpecification
(the inherited ValueSpecification level, Rule 0025 base-helper call) plus DEFAULT-PATTERN
(0..1 PositiveInteger per the XSD group NOT-AVAILABLE-VALUE-SPECIFICATION) via
setDefaultPattern.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import NotAvailableValueSpecification
from tests.test_armodel.parser._helpers import _snip


class TestNotAvailableValueSpecificationReader:
    def test_read_full_field_values(self, parser):
        root = _snip(
            """
            <NOT-AVAILABLE-VALUE-SPECIFICATION>
                <DEFAULT-PATTERN>255</DEFAULT-PATTERN>
            </NOT-AVAILABLE-VALUE-SPECIFICATION>
            """,
            root_tag="PARENT",
        )
        value_spec = parser.getValueSpecification(root[0], "NOT-AVAILABLE-VALUE-SPECIFICATION")

        assert isinstance(value_spec, NotAvailableValueSpecification)
        assert value_spec.getDefaultPattern() is not None
        assert value_spec.getDefaultPattern().getValue() == 255

    def test_read_absent_pattern_is_none(self, parser):
        root = _snip("<NOT-AVAILABLE-VALUE-SPECIFICATION/>", root_tag="PARENT")
        value_spec = parser.getValueSpecification(root[0], "NOT-AVAILABLE-VALUE-SPECIFICATION")

        assert isinstance(value_spec, NotAvailableValueSpecification)
        assert value_spec.getDefaultPattern() is None
