"""Reader tests for ReferenceValueSpecification (Swc TPS Table 5.115, p.437).

getReferenceValueSpecification populates the model via the mutators: readValueSpecification
(the inherited ValueSpecification level, Rule 0025 base-helper call) plus REFERENCE-VALUE-REF
(0..1, DEST = DATA-PROTOTYPE per the XSD group REFERENCE-VALUE-SPECIFICATION) via
setReferenceValueRef.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import ReferenceValueSpecification
from tests.test_armodel.parser._helpers import _snip


class TestReferenceValueSpecificationReader:
    def test_read_full_field_values(self, parser):
        root = _snip(
            """
            <REFERENCE-VALUE-SPECIFICATION>
                <REFERENCE-VALUE-REF DEST="DATA-PROTOTYPE">/DataTypes/PointerTarget</REFERENCE-VALUE-REF>
            </REFERENCE-VALUE-SPECIFICATION>
            """,
            root_tag="PARENT",
        )
        value_spec = parser.getValueSpecification(root[0], "REFERENCE-VALUE-SPECIFICATION")

        assert isinstance(value_spec, ReferenceValueSpecification)
        ref = value_spec.getReferenceValueRef()
        assert ref is not None
        assert ref.getDest() == "DATA-PROTOTYPE"
        assert ref.getValue() == "/DataTypes/PointerTarget"

    def test_read_absent_ref_is_none(self, parser):
        root = _snip("<REFERENCE-VALUE-SPECIFICATION/>", root_tag="PARENT")
        value_spec = parser.getValueSpecification(root[0], "REFERENCE-VALUE-SPECIFICATION")

        assert isinstance(value_spec, ReferenceValueSpecification)
        assert value_spec.getReferenceValueRef() is None
