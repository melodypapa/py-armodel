"""Reader/writer round-trip tests for the Referrable.shortNameFragment aggregation."""

import os
import tempfile

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ShortNameFragment
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier
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
        fragment.setRole("prefix")
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
            assert fragments[0].getRole() == "prefix"
            assert isinstance(fragments[0].getFragment(), Identifier)
            assert fragments[0].getFragment().getValue() == "PFX"
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
