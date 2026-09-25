"""
Tests for reading NV-PROVIDE-COM-SPEC elements — NvProvideComSpec, Table 4.85 (p.195, R23-11).

NvProvideComSpec (Base = PPortComSpec) carries the optional attributes
ramBlockInitValue (RAM-BLOCK-INIT-VALUE 0..1 ValueSpecification aggregation),
romBlockInitValue (ROM-BLOCK-INIT-VALUE 0..1 ValueSpecification aggregation)
and variable (VARIABLE-REF 0..1 reference to a VariableDataPrototype). It is
aggregated by AbstractProvidedPortPrototype.providedComSpec and read through
readProvidedComSpec → getNvProvideComSpec.

Round-trip counterpart: tests/test_armodel/writer/test_nv_provide_com_spec.py
"""

import xml.etree.ElementTree as ET

from armodel.models import AUTOSAR, ApplicationSwComponentType
from armodel.models.M2.AUTOSARTemplates.CommonStructure import TextValueSpecification
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import NvProvideComSpec
from tests.test_armodel.parser._helpers import _autosar_root, _snip


class TestGetNvProvideComSpec:
    """Tests for getNvProvideComSpec — own element field values (Table 4.85)."""

    def test_own_elements_field_values(self, parser):
        """Test that all three elements are read with their field values."""
        element = _snip(
            """
            <RAM-BLOCK-INIT-VALUE>
                <TEXT-VALUE-SPECIFICATION>
                    <VALUE>0</VALUE>
                </TEXT-VALUE-SPECIFICATION>
            </RAM-BLOCK-INIT-VALUE>
            <ROM-BLOCK-INIT-VALUE>
                <TEXT-VALUE-SPECIFICATION>
                    <VALUE>255</VALUE>
                </TEXT-VALUE-SPECIFICATION>
            </ROM-BLOCK-INIT-VALUE>
            <VARIABLE-REF DEST="VARIABLE-DATA-PROTOTYPE">/pkg/NvDataInterface/Var</VARIABLE-REF>
            """,
            root_tag="NV-PROVIDE-COM-SPEC",
        )
        result = parser.getNvProvideComSpec(element)
        assert result is not None
        assert isinstance(result.getRamBlockInitValue(), TextValueSpecification)
        assert result.getRamBlockInitValue().getValue().getValue() == "0"
        assert isinstance(result.getRomBlockInitValue(), TextValueSpecification)
        assert result.getRomBlockInitValue().getValue().getValue() == "255"
        assert result.getVariableRef() is not None
        assert result.getVariableRef().getValue() == "/pkg/NvDataInterface/Var"
        assert result.getVariableRef().getDest() == "VARIABLE-DATA-PROTOTYPE"

    def test_empty_element(self, parser):
        """Test that an empty NV-PROVIDE-COM-SPEC element yields an instance with all fields None."""
        element = _snip("", root_tag="NV-PROVIDE-COM-SPEC")
        result = parser.getNvProvideComSpec(element)
        assert result is not None
        assert result.getRamBlockInitValue() is None
        assert result.getRomBlockInitValue() is None
        assert result.getVariableRef() is None

    def test_ar_object_attributes_read(self, parser):
        """Test that the ARObject base attributes (S checksum, T timestamp) are read."""
        element = ET.fromstring(
            '<NV-PROVIDE-COM-SPEC xmlns="http://autosar.org/schema/r4.0" S="abc123" T="2024-01-01T12:00:00+00:00"><VARIABLE-REF DEST="VARIABLE-DATA-PROTOTYPE">/vdp/Var</VARIABLE-REF></NV-PROVIDE-COM-SPEC>'
        )
        result = parser.getNvProvideComSpec(element)
        assert result is not None
        assert result.getChecksum() is not None
        assert result.getChecksum().getValue() == "abc123"
        assert result.getTimestamp() is not None

    def test_read_via_provided_com_spec_dispatch(self, parser):
        """Test that the AbstractProvidedPortPrototype.providedComSpec aggregation reads the com spec with field values."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        app = ApplicationSwComponentType(parent=_autosar_root(), short_name="App")
        p_port = app.createPPortPrototype("PPort")
        element = _snip(
            """
            <PROVIDED-COM-SPECS>
                <NV-PROVIDE-COM-SPEC>
                    <RAM-BLOCK-INIT-VALUE>
                        <TEXT-VALUE-SPECIFICATION>
                            <VALUE>0</VALUE>
                        </TEXT-VALUE-SPECIFICATION>
                    </RAM-BLOCK-INIT-VALUE>
                    <VARIABLE-REF DEST="VARIABLE-DATA-PROTOTYPE">/pkg/NvDataInterface/Var</VARIABLE-REF>
                </NV-PROVIDE-COM-SPEC>
            </PROVIDED-COM-SPECS>
            """
        )
        parser.readProvidedComSpec(element, p_port)
        specs = p_port.getProvidedComSpecs()
        assert len(specs) == 1
        com_spec = specs[0]
        assert isinstance(com_spec, NvProvideComSpec)
        assert isinstance(com_spec.getRamBlockInitValue(), TextValueSpecification)
        assert com_spec.getRamBlockInitValue().getValue().getValue() == "0"
        assert com_spec.getVariableRef() is not None
        assert com_spec.getVariableRef().getValue() == "/pkg/NvDataInterface/Var"
