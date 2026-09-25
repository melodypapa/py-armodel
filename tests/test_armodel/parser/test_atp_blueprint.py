"""
Regression tests for AtpBlueprint (R23-11 AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate,
Table D.11, p.305) reader/writer coverage.

AtpBlueprint is abstract and its only own attribute blueprintPolicy (BlueprintPolicy, *)
is aggregated. BlueprintPolicy itself is implemented (R23-11 Table C.18, attributeName
modeled), but its concrete XML-bearing subclasses (BlueprintPolicyList/-NotModifiable/
-Single -- they own the BLUEPRINT-POLICY-* elements, XSD 00052 group ATP-BLUEPRINT) are
not yet synced, so the blueprintPolicy aggregation's serialization is deferred until
those types land (Rule 0001.10 blocker owned by the subclasses). AtpBlueprint therefore
owns no dedicated XML dispatch of its own (no readAtpBlueprint/writeAtpBlueprint) and
inherited members arrive through the shared readIdentifiable/writeIdentifiable helpers
(Table D.11 Base closure = {ARObject, Identifiable, MultilanguageReferrable, Referrable}).
Steps 5/6 are N/A for a dedicated dispatch; these tests pin that deferral contract.
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
from armodel.models.M2.MSR.AsamHdo.AdminData import AdminData
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
        The inherited Identifiable members (shortName, adminData) round-trip through the
        shared readIdentifiable/writeIdentifiable helpers.
        """
        AUTOSAR.getInstance().new()
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        src = ConcreteAtpBlueprint(parent, "MyBlueprint")
        admin_data = AdminData()
        src.setAdminData(admin_data)

        writer = _make_writer()
        element = ET.Element("AR-ELEMENT")
        element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
        writer.writeIdentifiable(element, src)

        reparsed = ET.fromstring(ET.tostring(element))
        dst = ConcreteAtpBlueprint(AUTOSAR.getInstance().getARPackages()[0], "MyBlueprint")
        _make_parser().readIdentifiable(reparsed, dst)

        assert dst.getShortName() == "MyBlueprint"
        assert dst.getAdminData() is not None
        assert dst.getAdminData() is not admin_data

    def test_blueprint_policy_aggregation_deferred(self):
        """
        Rule 0001.10 deferral: the blueprintPolicy aggregation is typed with the
        implemented abstract BlueprintPolicy (List[BlueprintPolicy], R23-11 Table C.18)
        but is not serialized (no BLUEPRINT-POLICYS reader/writer) until the concrete
        XML-bearing subclasses (BlueprintPolicyList/-NotModifiable/-Single) land.
        """
        AUTOSAR.getInstance().new()
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        src = ConcreteAtpBlueprint(parent, "MyBlueprint")
        assert src.blueprintPolicys == []
        assert src.getBlueprintPolicys() == []
