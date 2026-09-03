"""
Regression tests for AtpBlueprint (R23-11 AUTOSAR_FO_TPS_StandardizationTemplate,
Table C.12) reader/writer coverage.

AtpBlueprint is abstract and its only own attribute blueprintPolicy (BlueprintPolicy, *)
is aggregated; BlueprintPolicy itself is NOT implemented in this repo (Rule 0001.10
referenced-class placeholder), so the BLUEPRINT-POLICY aggregation is deferred until
that type lands. AtpBlueprint therefore owns no dedicated XML dispatch of its own
(no readAtpBlueprint/writeAtpBlueprint) and inherited members arrive through the
shared readIdentifiable/writeIdentifiable helpers (Table C.12 Base closure =
{ARObject, Identifiable, MultilanguageReferrable, Referrable}).
Steps 5/6 are N/A for a dedicated dispatch; these tests pin that N/A contract.
"""

import logging
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import (
    AtpBlueprint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class ConcreteAtpBlueprint(AtpBlueprint):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)


def _make_writer() -> ARXMLWriter:
    writer = ARXMLWriter.__new__(ARXMLWriter)
    writer.logger = logging.getLogger("test.writer")
    writer.nsmap = {"xmlns": "http://autosar.org/schema/r4.0"}
    return writer


def _make_parser() -> ARXMLParser:
    return ARXMLParser(options={"warning": True})


class TestAtpBlueprintReaderWriter:
    """Confirm AtpBlueprint has no own XML element mapping of its own."""

    def test_no_dedicated_reader_writer_methods(self):
        assert not hasattr(ARXMLParser, "readAtpBlueprint")
        assert not hasattr(ARXMLWriter, "writeAtpBlueprint")

    def test_identifiable_in_heritage(self):
        """Table C.12 Base closure includes Identifiable (most-derived base)."""
        assert Identifiable in AtpBlueprint.__mro__

    def test_round_trip_inherited_members_through_identifiable(self):
        """
        The inherited Identifiable member (shortName) round-trips through the shared
        readIdentifiable/writeIdentifiable helpers.
        """
        AUTOSAR.getInstance().new()
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        src = ConcreteAtpBlueprint(parent, "MyBlueprint")

        writer = _make_writer()
        element = ET.Element("AR-ELEMENT")
        element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
        writer.writeIdentifiable(element, src)

        reparsed = ET.fromstring(ET.tostring(element))
        dst = ConcreteAtpBlueprint(AUTOSAR.getInstance().getARPackages()[0], "MyBlueprint")
        _make_parser().readIdentifiable(reparsed, dst)

        assert dst.getShortName() == "MyBlueprint"

    def test_blueprint_policy_aggregation_deferred(self):
        """
        Rule 0001.10 placeholder: the blueprintPolicy aggregation is kept on the model
        as a List[ARObject] placeholder (BlueprintPolicy unimplemented), but is not
        serialized (no BLUEPRINT-POLICY reader/writer) until BlueprintPolicy lands.
        """
        AUTOSAR.getInstance().new()
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        src = ConcreteAtpBlueprint(parent, "MyBlueprint")
        assert src.blueprintPolicys == []
        assert src.getBlueprintPolicys() == []
