"""Reader tests for ConstantSpecificationMapping (Swc TPS Table 5.118, p.443).

getConstantSpecificationMapping populates the model via the mutators: readARObject
(Rule 0025 base-helper call — the spec Base chain is ARObject only) plus APPL-CONSTANT-REF
and IMPL-CONSTANT-REF (0..1 refs, DEST = CONSTANT-SPECIFICATION per the XSD group
CONSTANT-SPECIFICATION-MAPPING) via setApplConstantRef/setImplConstantRef.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import ConstantSpecificationMapping
from tests.test_armodel.parser._helpers import _snip


class TestConstantSpecificationMappingReader:
    def test_read_full_field_values(self, parser):
        root = _snip(
            """
            <CONSTANT-SPECIFICATION-MAPPING>
                <APPL-CONSTANT-REF DEST="CONSTANT-SPECIFICATION">/Consts/ApplConst</APPL-CONSTANT-REF>
                <IMPL-CONSTANT-REF DEST="CONSTANT-SPECIFICATION">/Consts/ImplConst</IMPL-CONSTANT-REF>
            </CONSTANT-SPECIFICATION-MAPPING>
            """,
            root_tag="PARENT",
        )
        mapping = parser.getConstantSpecificationMapping(root[0])

        assert isinstance(mapping, ConstantSpecificationMapping)
        assert mapping.getApplConstantRef() is not None
        assert mapping.getApplConstantRef().getDest() == "CONSTANT-SPECIFICATION"
        assert mapping.getApplConstantRef().getValue() == "/Consts/ApplConst"
        assert mapping.getImplConstantRef() is not None
        assert mapping.getImplConstantRef().getDest() == "CONSTANT-SPECIFICATION"
        assert mapping.getImplConstantRef().getValue() == "/Consts/ImplConst"

    def test_read_absent_refs_are_none(self, parser):
        root = _snip("<CONSTANT-SPECIFICATION-MAPPING/>", root_tag="PARENT")
        mapping = parser.getConstantSpecificationMapping(root[0])

        assert isinstance(mapping, ConstantSpecificationMapping)
        assert mapping.getApplConstantRef() is None
        assert mapping.getImplConstantRef() is None
