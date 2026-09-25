"""
Tests for reading NV-REQUIRE-COM-SPEC elements — NvRequireComSpec, Table 4.84 (p.194, R23-11).

NvRequireComSpec (Base = RPortComSpec) carries the optional attributes
initValue (INIT-VALUE 0..1 ValueSpecification aggregation)
and variable (VARIABLE-REF 0..1 reference to a VariableDataPrototype). It is
aggregated by AbstractRequiredPortPrototype.requiredComSpec and read through
readRequiredComSpec → getNvRequireComSpec.

Round-trip counterpart: tests/test_armodel/writer/test_nv_require_com_spec.py
"""

import xml.etree.ElementTree as ET

from armodel.models import AUTOSAR, ApplicationSwComponentType
from armodel.models.M2.AUTOSARTemplates.CommonStructure import TextValueSpecification
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import NvRequireComSpec
from tests.test_armodel.parser._helpers import _autosar_root, _snip


class TestGetNvRequireComSpec:
    """Tests for getNvRequireComSpec — own element field values (Table 4.84)."""

    def test_own_elements_field_values(self, parser):
        """Test that both elements are read with their field values."""
        element = _snip(
            """
            <INIT-VALUE>
                <TEXT-VALUE-SPECIFICATION>
                    <VALUE>0</VALUE>
                </TEXT-VALUE-SPECIFICATION>
            </INIT-VALUE>
            <VARIABLE-REF DEST="VARIABLE-DATA-PROTOTYPE">/pkg/NvDataInterface/Var</VARIABLE-REF>
            """,
            root_tag="NV-REQUIRE-COM-SPEC",
        )
        result = parser.getNvRequireComSpec(element)
        assert result is not None
        assert isinstance(result.getInitValue(), TextValueSpecification)
        assert result.getInitValue().getValue().getValue() == "0"
        assert result.getVariableRef() is not None
        assert result.getVariableRef().getValue() == "/pkg/NvDataInterface/Var"
        assert result.getVariableRef().getDest() == "VARIABLE-DATA-PROTOTYPE"

    def test_empty_element(self, parser):
        """Test that an empty NV-REQUIRE-COM-SPEC element yields an instance with all fields None."""
        element = _snip("", root_tag="NV-REQUIRE-COM-SPEC")
        result = parser.getNvRequireComSpec(element)
        assert result is not None
        assert result.getInitValue() is None
        assert result.getVariableRef() is None

    def test_ar_object_attributes_read(self, parser):
        """Test that the ARObject base attributes (S checksum, T timestamp) are read."""
        element = ET.fromstring(
            '<NV-REQUIRE-COM-SPEC xmlns="http://autosar.org/schema/r4.0" S="abc123" T="2024-01-01T12:00:00+00:00"><VARIABLE-REF DEST="VARIABLE-DATA-PROTOTYPE">/vdp/Var</VARIABLE-REF></NV-REQUIRE-COM-SPEC>'
        )
        result = parser.getNvRequireComSpec(element)
        assert result is not None
        assert result.getChecksum() is not None
        assert result.getChecksum().getValue() == "abc123"
        assert result.getTimestamp() is not None

    def test_read_via_required_com_spec_dispatch(self, parser):
        """Test that the AbstractRequiredPortPrototype.requiredComSpec aggregation reads the com spec with field values."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        app = ApplicationSwComponentType(parent=_autosar_root(), short_name="App")
        r_port = app.createRPortPrototype("RPort")
        element = _snip("""
            <REQUIRED-COM-SPECS>
                <NV-REQUIRE-COM-SPEC>
                    <INIT-VALUE>
                        <TEXT-VALUE-SPECIFICATION>
                            <VALUE>0</VALUE>
                        </TEXT-VALUE-SPECIFICATION>
                    </INIT-VALUE>
                    <VARIABLE-REF DEST="VARIABLE-DATA-PROTOTYPE">/pkg/NvDataInterface/Var</VARIABLE-REF>
                </NV-REQUIRE-COM-SPEC>
            </REQUIRED-COM-SPECS>
            """)
        parser.readRequiredComSpec(element, r_port)
        specs = r_port.getRequiredComSpecs()
        assert len(specs) == 1
        com_spec = specs[0]
        assert isinstance(com_spec, NvRequireComSpec)
        assert isinstance(com_spec.getInitValue(), TextValueSpecification)
        assert com_spec.getInitValue().getValue().getValue() == "0"
        assert com_spec.getVariableRef() is not None
        assert com_spec.getVariableRef().getValue() == "/pkg/NvDataInterface/Var"
