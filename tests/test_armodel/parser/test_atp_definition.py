"""
Regression tests for AtpDefinition (Table 11.3) reader/writer coverage.

AtpDefinition is abstract and Table 11.3 lists no Attribute rows; it owns no XML
element of its own and has no dedicated readAtpDefinition/writeAtpDefinition -
inherited members are reached through the shared readReferrable/writeReferrable
helpers (Table 11.3 Base closure = {ARObject, Referrable}).
Steps 5/6 are N/A; these tests pin that N/A contract and cover the heritage
regression (the class re-parented Identifiable -> Referrable, so every inherited
member now arrives through Referrable instead of Identifiable).
"""

import logging
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.RolesAndRights import AtpDefinition
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class ConcreteAtpDefinition(AtpDefinition):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)


def _make_writer() -> ARXMLWriter:
    writer = ARXMLWriter.__new__(ARXMLWriter)
    writer.logger = logging.getLogger("test.writer")
    writer.nsmap = {"xmlns": "http://autosar.org/schema/r4.0"}
    return writer


def _make_parser() -> ARXMLParser:
    return ARXMLParser(options={"warning": True})


class TestAtpDefinitionReaderWriter:
    """Confirm AtpDefinition has no own XML element mapping."""

    def test_no_dedicated_reader_writer_methods(self):
        assert not hasattr(ARXMLParser, "readAtpDefinition")
        assert not hasattr(ARXMLWriter, "writeAtpDefinition")

    def test_identifiable_not_in_heritage(self):
        """Table 11.3 Base closure excludes Identifiable."""
        assert Identifiable not in AtpDefinition.__mro__

    def test_round_trip_inherited_members_through_referrable(self):
        """
        The heritage re-parent to Referrable must still round-trip the inherited
        Referrable member (shortName) through the shared helpers.
        """
        AUTOSAR.getInstance().new()
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        src = ConcreteAtpDefinition(parent, "MyDefinition")

        writer = _make_writer()
        element = ET.Element("AR-ELEMENT")
        element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
        writer.writeReferrable(element, src)

        reparsed = ET.fromstring(ET.tostring(element))
        dst = ConcreteAtpDefinition(AUTOSAR.getInstance().getARPackages()[0], "MyDefinition")
        _make_parser().readReferrable(reparsed, dst)

        assert dst.getShortName() == "MyDefinition"
