"""Reader tests for ValueSpecification (Swc TPS Table 5.109, p.433).

readValueSpecification populates the abstract base level via the mutators: readARObject
(Rule 0025 base-helper call), then SHORT-LABEL (0..1 Identifier) via setShortLabel. The
concrete subclass element keeps its own dispatch (getValueSpecification); here the base
attribute coverage is pinned on a NUMERICAL-VALUE-SPECIFICATION carrier.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import NumericalValueSpecification
from tests.test_armodel.parser._helpers import _snip


class TestValueSpecificationReader:
    def test_read_short_label_full_field_values(self, parser):
        element = _snip(
            """
            <NUMERICAL-VALUE-SPECIFICATION>
                <SHORT-LABEL>field1</SHORT-LABEL>
                <VALUE>42</VALUE>
            </NUMERICAL-VALUE-SPECIFICATION>
            """,
        )
        value_spec = parser.getValueSpecification(element[0], "NUMERICAL-VALUE-SPECIFICATION")

        assert isinstance(value_spec, NumericalValueSpecification)
        assert value_spec.getShortLabel() is not None
        assert value_spec.getShortLabel().getValue() == "field1"
        assert value_spec.getValue() is not None
        assert value_spec.getValue().getValue() == 42

    def test_read_absent_short_label_is_none(self, parser):
        element = _snip(
            """
            <NUMERICAL-VALUE-SPECIFICATION>
                <VALUE>42</VALUE>
            </NUMERICAL-VALUE-SPECIFICATION>
            """,
        )
        value_spec = parser.getValueSpecification(element[0], "NUMERICAL-VALUE-SPECIFICATION")

        assert isinstance(value_spec, NumericalValueSpecification)
        assert value_spec.getShortLabel() is None
        assert value_spec.getValue().getValue() == 42
