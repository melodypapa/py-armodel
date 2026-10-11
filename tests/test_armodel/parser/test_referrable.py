"""
Tests for readReferrable (Referrable, Table 4.10).

Round-trip counterpart: tests/test_armodel/writer/test_referrable.py
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Referrable, ShortNameFragment
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class _Derived(Referrable):
    """
    Concrete Referrable subclass so the abstract guard does not reject the instance.
    """

    pass


class TestReadReferrable:
    """
    Test readReferrable.
    """

    def test_read_short_name_fragments(self):
        """
        readReferrable must populate shortNameFragments from the SHORT-NAME-FRAGMENTS wrapper.
        """
        element = ET.fromstring(
            f"""<ELEMENT xmlns='{NS}'>
                <SHORT-NAME-FRAGMENTS>
                    <SHORT-NAME-FRAGMENT>
                        <ROLE>prefix</ROLE>
                        <FRAGMENT>PFX</FRAGMENT>
                    </SHORT-NAME-FRAGMENT>
                </SHORT-NAME-FRAGMENTS>
            </ELEMENT>"""
        )

        referrable = _Derived(None, "App")
        ARXMLParser().readReferrable(element, referrable)

        fragments = referrable.getShortNameFragments()
        assert len(fragments) == 1
        assert isinstance(fragments[0], ShortNameFragment)
        assert fragments[0].getRole().getValue() == "prefix"
        assert fragments[0].getFragment().getValue() == "PFX"

    def test_read_short_name_fragments_empty_wrapper(self):
        """
        An empty SHORT-NAME-FRAGMENTS wrapper must leave the list empty.
        """
        element = ET.fromstring(f"<ELEMENT xmlns='{NS}'><SHORT-NAME-FRAGMENTS/></ELEMENT>")

        referrable = _Derived(None, "App")
        ARXMLParser().readReferrable(element, referrable)

        assert referrable.getShortNameFragments() == []

    def test_read_absent_wrapper_leaves_empty(self):
        """
        An element without SHORT-NAME-FRAGMENTS must leave the list empty.
        """
        element = ET.fromstring(f"<ELEMENT xmlns='{NS}'><SHORT-NAME>App</SHORT-NAME></ELEMENT>")

        referrable = _Derived(None, "App")
        ARXMLParser().readReferrable(element, referrable)

        assert referrable.getShortNameFragments() == []

    def test_read_s_and_t(self):
        """readARObject must run so the inherited S/T state is read (Rule 0025)."""
        element = ET.fromstring(f"""<ELEMENT xmlns='{NS}' S="cs-1" T="2026-10-11T10:00:00"/>""")

        referrable = _Derived(None, "App")
        ARXMLParser().readReferrable(element, referrable)

        assert referrable.getChecksum().getValue() == "cs-1"
        assert referrable.getTimestamp().getValue() == "2026-10-11T10:00:00"

    def test_read_multiple_fragments_preserves_order(self):
        """
        All SHORT-NAME-FRAGMENT children must be read, in document order.
        """
        element = ET.fromstring(
            f"""<ELEMENT xmlns='{NS}'>
                <SHORT-NAME-FRAGMENTS>
                    <SHORT-NAME-FRAGMENT><ROLE>prefix</ROLE><FRAGMENT>PFX</FRAGMENT></SHORT-NAME-FRAGMENT>
                    <SHORT-NAME-FRAGMENT><ROLE>suffix</ROLE><FRAGMENT>SFX</FRAGMENT></SHORT-NAME-FRAGMENT>
                </SHORT-NAME-FRAGMENTS>
            </ELEMENT>"""
        )

        referrable = _Derived(None, "App")
        ARXMLParser().readReferrable(element, referrable)

        fragments = referrable.getShortNameFragments()
        assert [fragment.getFragment().getValue() for fragment in fragments] == ["PFX", "SFX"]
        assert all(isinstance(fragment.getFragment(), Identifier) for fragment in fragments)
