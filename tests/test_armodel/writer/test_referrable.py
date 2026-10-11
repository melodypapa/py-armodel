"""
Tests for writeReferrable (Referrable, Table 4.10).

Round-trip counterpart: tests/test_armodel/parser/test_referrable.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Referrable, ShortNameFragment
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, Identifier, String
from armodel.writer.arxml_writer import ARXMLWriter


class _Derived(Referrable):
    """
    Concrete Referrable subclass so the abstract guard does not reject the instance.
    """

    pass


class TestWriteReferrable:
    """
    Test writeReferrable.
    """

    def test_write_short_name(self):
        """
        writeReferrable must emit SHORT-NAME from getShortName().
        """
        referrable = _Derived(None, "App")

        writer = ARXMLWriter()
        element = ET.Element("ELEMENT")
        writer.writeReferrable(element, referrable)

        assert element.find("SHORT-NAME").text == "App"

    def test_write_short_name_fragments(self):
        """
        writeReferrable must emit the SHORT-NAME-FRAGMENTS wrapper and one SHORT-NAME-FRAGMENT per fragment.
        """
        referrable = _Derived(None, "App")
        fragment = ShortNameFragment()
        fragment.setRole(String().setValue("prefix"))
        fragment.setFragment(Identifier().setValue("PFX"))
        referrable.addShortNameFragment(fragment)

        writer = ARXMLWriter()
        element = ET.Element("ELEMENT")
        writer.writeReferrable(element, referrable)

        wrapper = element.find("SHORT-NAME-FRAGMENTS")
        assert wrapper is not None
        children = list(wrapper)
        assert [child.tag for child in children] == ["SHORT-NAME-FRAGMENT"]
        assert children[0].find("ROLE").text == "prefix"
        assert children[0].find("FRAGMENT").text == "PFX"

    def test_write_omits_wrapper_when_empty(self):
        """
        An unset aggregation must emit no SHORT-NAME-FRAGMENTS wrapper.
        """
        referrable = _Derived(None, "App")

        writer = ARXMLWriter()
        element = ET.Element("ELEMENT")
        writer.writeReferrable(element, referrable)

        assert element.find("SHORT-NAME-FRAGMENTS") is None

    def test_write_s_and_t(self):
        """writeARObject must run so the inherited S/T state is emitted (Rule 0025)."""
        referrable = _Derived(None, "App")
        referrable.setChecksum(String().setValue("cs-1"))
        referrable.setTimestamp(DateTime().setValue("2026-10-11T10:00:00Z"))

        writer = ARXMLWriter()
        element = ET.Element("ELEMENT")
        writer.writeReferrable(element, referrable)

        assert element.attrib["S"] == "cs-1"
        assert element.attrib["T"] == "2026-10-11T10:00:00Z"

    def test_write_element_order_short_name_before_fragments(self):
        """
        SHORT-NAME must precede SHORT-NAME-FRAGMENTS (XSD group REFERRABLE sequence, AUTOSAR_00052.xsd l.96601).
        """
        referrable = _Derived(None, "App")
        fragment = ShortNameFragment()
        fragment.setRole(String().setValue("prefix"))
        fragment.setFragment(Identifier().setValue("PFX"))
        referrable.addShortNameFragment(fragment)

        writer = ARXMLWriter()
        element = ET.Element("ELEMENT")
        writer.writeReferrable(element, referrable)

        assert [child.tag for child in element] == ["SHORT-NAME", "SHORT-NAME-FRAGMENTS"]


class TestReferrableRoundTrip:
    """
    Test the document-level write -> read round-trip of the Referrable group.

    Goes through a real save/load (not an in-memory element hand-off): the writer emits
    children under the document's AUTOSAR namespace declaration while the parser resolves
    them through its namespace map, so a bare in-memory element cannot exercise both sides.
    """

    def test_round_trip(self):
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
        from armodel.parser.arxml_parser import ARXMLParser

        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("AUTOSAR")
        swc = pkg.createApplicationSwComponentType("App")
        swc.setChecksum(String().setValue("cs-1"))
        swc.setTimestamp(DateTime().setValue("2026-10-11T10:00:00Z"))

        fragment = ShortNameFragment()
        fragment.setRole(String().setValue("prefix"))
        fragment.setFragment(Identifier().setValue("PFX"))
        swc.addShortNameFragment(fragment)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            swc_2 = document_2.getARPackages()[0].getAtomicSwComponentTypes()[0]
            assert swc_2.getShortName() == "App"
            assert swc_2.getChecksum().getValue() == "cs-1"
            assert swc_2.getTimestamp().getValue() == "2026-10-11T10:00:00Z"
            fragments = swc_2.getShortNameFragments()
            assert len(fragments) == 1
            assert fragments[0].getRole().getValue() == "prefix"
            assert fragments[0].getFragment().getValue() == "PFX"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
