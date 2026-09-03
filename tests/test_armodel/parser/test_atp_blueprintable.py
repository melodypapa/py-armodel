"""
Regression tests for AtpBlueprintable (R23-11 AUTOSAR_FO_TPS_StandardizationTemplate,
Table C.14, p.162) reader/writer coverage.

AtpBlueprintable is abstract and owns no attribute of its own (Table C.14 Attribute
column is empty), so it has no dedicated XML dispatch of its own (no
readAtpBlueprintable/writeAtpBlueprintable). Its only content arrives through the
shared readIdentifiable/writeIdentifiable helpers (Table C.14 Base closure =
{ARObject, Identifiable, MultilanguageReferrable, Referrable}). The heritage fix
re-parented AtpBlueprintable from PackageableElement to Identifiable; since
PackageableElement/CollectableElement are empty markers and the `element` aggregation
lives on Identifiable, no reader/writer change is required. Steps 5/6 are N/A for a
dedicated dispatch; these tests pin that N/A contract.
"""

import logging
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import (
    AtpBlueprintable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    PackageableElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class ConcreteAtpBlueprintable(AtpBlueprintable):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)


def _make_writer() -> ARXMLWriter:
    writer = ARXMLWriter.__new__(ARXMLWriter)
    writer.logger = logging.getLogger("test.writer")
    writer.nsmap = {"xmlns": "http://autosar.org/schema/r4.0"}
    return writer


def _make_parser() -> ARXMLParser:
    return ARXMLParser(options={"warning": True})


class TestAtpBlueprintableReaderWriter:
    """Confirm AtpBlueprintable has no own XML element mapping of its own."""

    def test_no_dedicated_reader_writer_methods(self):
        assert not hasattr(ARXMLParser, "readAtpBlueprintable")
        assert not hasattr(ARXMLWriter, "writeAtpBlueprintable")

    def test_identifiable_in_heritage(self):
        """Table C.14 Base closure includes Identifiable (most-derived base)."""
        assert Identifiable in AtpBlueprintable.__mro__

    def test_not_packageable_element(self):
        """
        Heritage fix: AtpBlueprintable is a direct Identifiable, not a
        PackageableElement. This assertion is Red on the pre-fix code
        (AtpBlueprintable(PackageableElement)) and Green after the re-parent.
        """
        assert PackageableElement not in AtpBlueprintable.__mro__

    def test_round_trip_inherited_members_through_identifiable(self):
        """
        The inherited Identifiable member (shortName) round-trips through the shared
        readIdentifiable/writeIdentifiable helpers.
        """
        AUTOSAR.getInstance().new()
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        src = ConcreteAtpBlueprintable(parent, "MyBlueprintable")

        writer = _make_writer()
        element = ET.Element("AR-ELEMENT")
        element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
        writer.writeIdentifiable(element, src)

        reparsed = ET.fromstring(ET.tostring(element))
        dst = ConcreteAtpBlueprintable(AUTOSAR.getInstance().getARPackages()[0], "MyBlueprintable")
        _make_parser().readIdentifiable(reparsed, dst)

        assert dst.getShortName() == "MyBlueprintable"
