"""
Reader tests for SwVariableRefProxy (Table 5.57, p.370).

The XML snippets use the XSD-valid element spellings from
``autosar/R23-11/xsd/AUTOSAR_00052.xsd`` (group SW-VARIABLE-REF-PROXY:
AUTOSAR-VARIABLE typed AUTOSAR-VARIABLE-REF, then MC-DATA-INSTANCE-VAR-REF).
The group is consumed in two shapes: repeated instances inlined in the
SW-VARIABLE-REFS / SW-COMPARISON-VARIABLES wrappers, and the SW-HOST-VARIABLE
element typed by the SW-VARIABLE-REF-PROXY complexType (L116718), which carries
the AR-OBJECT attributeGroup (S/T).
"""

from tests.test_armodel.parser._helpers import _snip


class TestSwVariableRefProxyReader:
    """Tests for the SW-VARIABLE-REF-PROXY group readers (Table 5.57)."""

    def test_read_variable_refs_full_content(self, parser):
        """Each SW-VARIABLE-REFS group instance (AUTOSAR-VARIABLE? + MC-DATA-INSTANCE-VAR-REF?) becomes one proxy with both fields."""
        element = _snip(
            "<SW-VARIABLE-REFS>"
            "<AUTOSAR-VARIABLE>"
            "<LOCAL-VARIABLE-REF DEST='VARIABLE-DATA-PROTOTYPE'>/variables/temp</LOCAL-VARIABLE-REF>"
            "</AUTOSAR-VARIABLE>"
            "<MC-DATA-INSTANCE-VAR-REF DEST='MC-DATA-INSTANCE'>/mc/instances/v1</MC-DATA-INSTANCE-VAR-REF>"
            "<AUTOSAR-VARIABLE>"
            "<LOCAL-VARIABLE-REF DEST='VARIABLE-DATA-PROTOTYPE'>/variables/pressure</LOCAL-VARIABLE-REF>"
            "</AUTOSAR-VARIABLE>"
            "<MC-DATA-INSTANCE-VAR-REF DEST='MC-DATA-INSTANCE'>/mc/instances/v2</MC-DATA-INSTANCE-VAR-REF>"
            "</SW-VARIABLE-REFS>",
            root_tag="SW-AXIS-INDIVIDUAL",
        )
        props = parser.getSwAxisIndividual(element)

        refs = props.getSwVariableRefs()
        assert len(refs) == 2
        first_local = refs[0].getAutosarVariable().getLocalVariableRef()
        assert first_local.getValue() == "/variables/temp"
        assert first_local.getDest() == "VARIABLE-DATA-PROTOTYPE"
        assert refs[0].getMcDataInstanceVarRef().getValue() == "/mc/instances/v1"
        assert refs[0].getMcDataInstanceVarRef().getDest() == "MC-DATA-INSTANCE"
        second_local = refs[1].getAutosarVariable().getLocalVariableRef()
        assert second_local.getValue() == "/variables/pressure"
        assert refs[1].getMcDataInstanceVarRef().getValue() == "/mc/instances/v2"

    def test_read_autosar_variable_only_instance(self, parser):
        """A group instance with only AUTOSAR-VARIABLE yields a proxy with mcDataInstanceVarRef unset."""
        element = _snip(
            "<SW-VARIABLE-REFS>" "<AUTOSAR-VARIABLE>" "<LOCAL-VARIABLE-REF DEST='VARIABLE-DATA-PROTOTYPE'>/variables/temp</LOCAL-VARIABLE-REF>" "</AUTOSAR-VARIABLE>" "</SW-VARIABLE-REFS>",
            root_tag="SW-AXIS-INDIVIDUAL",
        )
        props = parser.getSwAxisIndividual(element)

        refs = props.getSwVariableRefs()
        assert len(refs) == 1
        assert refs[0].getAutosarVariable().getLocalVariableRef().getValue() == "/variables/temp"
        assert refs[0].getMcDataInstanceVarRef() is None

    def test_read_empty_variable_refs_wrapper(self, parser):
        """An empty SW-VARIABLE-REFS wrapper parses to an empty list."""
        element = _snip("<SW-VARIABLE-REFS></SW-VARIABLE-REFS>", root_tag="SW-AXIS-INDIVIDUAL")
        props = parser.getSwAxisIndividual(element)

        assert props.getSwVariableRefs() == []

    def test_read_sw_host_variable_element_with_ar_object_attributes(self, parser):
        """SW-HOST-VARIABLE is typed by the SW-VARIABLE-REF-PROXY complexType — its S/T attributes (AR-OBJECT attributeGroup) round-trip into the proxy alongside the group members."""
        element = _snip(
            "<SW-DATA-DEF-PROPS>"
            "<SW-DATA-DEF-PROPS-VARIANTS>"
            "<SW-DATA-DEF-PROPS-CONDITIONAL>"
            '<SW-HOST-VARIABLE S="4321" T="2024-06-01T12:00:00Z">'
            "<AUTOSAR-VARIABLE>"
            "<LOCAL-VARIABLE-REF DEST='VARIABLE-DATA-PROTOTYPE'>/variables/host</LOCAL-VARIABLE-REF>"
            "</AUTOSAR-VARIABLE>"
            "<MC-DATA-INSTANCE-VAR-REF DEST='MC-DATA-INSTANCE'>/mc/instances/host</MC-DATA-INSTANCE-VAR-REF>"
            "</SW-HOST-VARIABLE>"
            "</SW-DATA-DEF-PROPS-CONDITIONAL>"
            "</SW-DATA-DEF-PROPS-VARIANTS>"
            "</SW-DATA-DEF-PROPS>"
        )
        props = parser.getSwDataDefProps(element, "SW-DATA-DEF-PROPS")

        host_variable = props.getSwHostVariable()
        assert host_variable is not None
        assert host_variable.getChecksum() is not None
        assert host_variable.getChecksum().getValue() == "4321"
        assert host_variable.getTimestamp() is not None
        assert host_variable.getTimestamp().getValue() == "2024-06-01T12:00:00Z"
        assert host_variable.getAutosarVariable().getLocalVariableRef().getValue() == "/variables/host"
        assert host_variable.getMcDataInstanceVarRef().getValue() == "/mc/instances/host"
