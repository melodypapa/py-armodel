"""
Tests for reading PARAMETER-REQUIRE-COM-SPEC elements — ParameterRequireComSpec, Table 4.83 (p.193, R23-11).

ParameterRequireComSpec (Base = RPortComSpec) carries the optional attributes
initValue (INIT-VALUE 0..1 ValueSpecification aggregation)
and parameter (PARAMETER-REF 0..1 reference to a ParameterDataPrototype). It is
aggregated by AbstractRequiredPortPrototype.requiredComSpec and read through
readRequiredComSpec → getParameterRequireComSpec.

Round-trip counterpart: tests/test_armodel/writer/test_parameter_require_com_spec.py
"""

import xml.etree.ElementTree as ET

from armodel.models import AUTOSAR, ApplicationSwComponentType
from armodel.models.M2.AUTOSARTemplates.CommonStructure import TextValueSpecification
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import ParameterRequireComSpec
from tests.test_armodel.parser._helpers import _autosar_root, _snip


class TestGetParameterRequireComSpec:
    """Tests for getParameterRequireComSpec — own element field values (Table 4.83)."""

    def test_own_elements_field_values(self, parser):
        """Test that both elements are read with their field values."""
        element = _snip(
            """
            <INIT-VALUE>
                <TEXT-VALUE-SPECIFICATION>
                    <VALUE>0</VALUE>
                </TEXT-VALUE-SPECIFICATION>
            </INIT-VALUE>
            <PARAMETER-REF DEST="PARAMETER-DATA-PROTOTYPE">/pkg/ParamInterface/Param</PARAMETER-REF>
            """,
            root_tag="PARAMETER-REQUIRE-COM-SPEC",
        )
        result = parser.getParameterRequireComSpec(element)
        assert result is not None
        assert isinstance(result.getInitValue(), TextValueSpecification)
        assert result.getInitValue().getValue().getValue() == "0"
        assert result.getParameterRef() is not None
        assert result.getParameterRef().getValue() == "/pkg/ParamInterface/Param"
        assert result.getParameterRef().getDest() == "PARAMETER-DATA-PROTOTYPE"

    def test_empty_element(self, parser):
        """Test that an empty PARAMETER-REQUIRE-COM-SPEC element yields an instance with all fields None."""
        element = _snip("", root_tag="PARAMETER-REQUIRE-COM-SPEC")
        result = parser.getParameterRequireComSpec(element)
        assert result is not None
        assert result.getInitValue() is None
        assert result.getParameterRef() is None

    def test_ar_object_attributes_read(self, parser):
        """Test that the ARObject base attributes (S checksum, T timestamp) are read."""
        element = ET.fromstring(
            '<PARAMETER-REQUIRE-COM-SPEC xmlns="http://autosar.org/schema/r4.0" S="abc123" T="2024-01-01T12:00:00+00:00"><PARAMETER-REF DEST="PARAMETER-DATA-PROTOTYPE">/pdp/Param</PARAMETER-REF></PARAMETER-REQUIRE-COM-SPEC>'
        )
        result = parser.getParameterRequireComSpec(element)
        assert result is not None
        assert result.getChecksum() is not None
        assert result.getChecksum().getValue() == "abc123"
        assert result.getTimestamp() is not None

    def test_read_via_required_com_spec_dispatch(self, parser):
        """Test that the AbstractRequiredPortPrototype.requiredComSpec aggregation reads the com spec with field values."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        app = ApplicationSwComponentType(parent=_autosar_root(), short_name="App")
        r_port = app.createRPortPrototype("RPort")
        element = _snip(
            """
            <REQUIRED-COM-SPECS>
                <PARAMETER-REQUIRE-COM-SPEC>
                    <INIT-VALUE>
                        <TEXT-VALUE-SPECIFICATION>
                            <VALUE>0</VALUE>
                        </TEXT-VALUE-SPECIFICATION>
                    </INIT-VALUE>
                    <PARAMETER-REF DEST="PARAMETER-DATA-PROTOTYPE">/pkg/ParamInterface/Param</PARAMETER-REF>
                </PARAMETER-REQUIRE-COM-SPEC>
            </REQUIRED-COM-SPECS>
            """
        )
        parser.readRequiredComSpec(element, r_port)
        specs = r_port.getRequiredComSpecs()
        assert len(specs) == 1
        com_spec = specs[0]
        assert isinstance(com_spec, ParameterRequireComSpec)
        assert isinstance(com_spec.getInitValue(), TextValueSpecification)
        assert com_spec.getInitValue().getValue().getValue() == "0"
        assert com_spec.getParameterRef() is not None
        assert com_spec.getParameterRef().getValue() == "/pkg/ParamInterface/Param"
