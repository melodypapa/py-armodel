"""Reader/writer round-trip tests for the Referrable.shortNameFragment aggregation."""

import os
import tempfile
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ShortNameFragment
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, String
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestShortNameFragmentsRoundTrip:
    def test_round_trip(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("AUTOSAR")
        swc = pkg.createApplicationSwComponentType("App")

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
            fragments = swc_2.getShortNameFragments()
            assert len(fragments) == 1
            assert isinstance(fragments[0].getRole(), String)
            assert fragments[0].getRole().getValue() == "prefix"
            assert isinstance(fragments[0].getFragment(), Identifier)
            assert fragments[0].getFragment().getValue() == "PFX"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_multiple_fragments(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("AUTOSAR")
        swc = pkg.createApplicationSwComponentType("App")

        fragment_1 = ShortNameFragment()
        fragment_1.setRole(String().setValue("prefix"))
        fragment_1.setFragment(Identifier().setValue("PFX"))
        swc.addShortNameFragment(fragment_1)

        fragment_2 = ShortNameFragment()
        fragment_2.setRole(String().setValue("suffix"))
        fragment_2.setFragment(Identifier().setValue("SFX"))
        swc.addShortNameFragment(fragment_2)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            swc_2 = document_2.getARPackages()[0].getAtomicSwComponentTypes()[0]
            fragments = swc_2.getShortNameFragments()
            assert len(fragments) == 2
            assert [fragment.getRole().getValue() for fragment in fragments] == ["prefix", "suffix"]
            assert [fragment.getFragment().getValue() for fragment in fragments] == ["PFX", "SFX"]
            assert all(isinstance(fragment.getRole(), String) for fragment in fragments)
            assert all(isinstance(fragment.getFragment(), Identifier) for fragment in fragments)
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_written_element_order_role_before_fragment(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("AUTOSAR")
        swc = pkg.createApplicationSwComponentType("App")

        fragment = ShortNameFragment()
        fragment.setRole(String().setValue("prefix"))
        fragment.setFragment(Identifier().setValue("PFX"))
        swc.addShortNameFragment(fragment)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            tree = ET.parse(file_path)
            fragment_element = next(element for element in tree.iter() if element.tag.endswith("SHORT-NAME-FRAGMENT"))
            assert [child.tag.split("}")[-1] for child in fragment_element] == ["ROLE", "FRAGMENT"]
            assert [child.text for child in fragment_element if child.tag.endswith("ROLE")][0] == "prefix"
            assert [child.text for child in fragment_element if child.tag.endswith("FRAGMENT")][0] == "PFX"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty_fragments(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("AUTOSAR")
        pkg.createApplicationSwComponentType("App")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            swc_2 = document_2.getARPackages()[0].getAtomicSwComponentTypes()[0]
            assert swc_2.getShortNameFragments() == []
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
