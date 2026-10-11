"""Reader/writer round-trip tests for AnyInstanceRef (Table 9.57, XSD group ANY-INSTANCE-REF).

XML element order per the XSD group (AUTOSAR_00052.xsd l.2206): CONTEXT-ELEMENT-REF*,
TARGET-REF, then VARIATION-POINT (xml.sequenceOffset="10000", so it is always last).
The `base` association is <<atpDerived>> and the XSD group skips it
(`<!-- Association <<atpDerived>>base skipped -->`), so BASE-REF carries no XSD element;
it is still read/written here to match the stamped instance-ref family precedent
(Group5/Group7 AnyInstanceRef Table 9.57 family) and is recorded as an atpDerived deviation.

Table 9.57 has no own `variationPoint` attribute row — capability comes from the
VariationPointCapable mixin (Rule 0020), and the reader/writer must therefore round-trip
the XSD-declared VARIATION-POINT element (Rule 0025).
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import AnyInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken, RefType, String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _ns_wrap(parent):
    """Serialize the dummy PARENT's child under the AUTOSAR namespace and return that child."""
    return ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, ET.tostring(parent).decode("utf-8")))[0][0]


def _full_instance_ref():
    iref = AnyInstanceRef()
    iref.setBaseRef(RefType().setValue("/Pkg/Base").setDest("SW-COMPONENT-PROTOTYPE"))
    iref.addContextElementRef(RefType().setValue("/Pkg/Base/Step1").setDest("SW-COMPONENT-PROTOTYPE"))
    iref.addContextElementRef(RefType().setValue("/Pkg/Base/Step2").setDest("SW-COMPONENT-PROTOTYPE"))
    iref.setTargetRef(RefType().setValue("/Pkg/Target").setDest("R-PORT-PROTOTYPE"))
    return iref


class TestAnyInstanceRefReadWrite:
    def test_all_table_9_57_attributes_round_trip(self, writer, parser):
        """Every Table 9.57 attribute survives a write/read cycle with its field values."""
        iref = _full_instance_ref()

        parent = ET.Element("PARENT")
        iref_element = ET.SubElement(parent, "VALUE-IREF")
        writer.writeAnyInstanceRef(iref_element, iref)

        assert [child.tag for child in iref_element] == ["BASE-REF", "CONTEXT-ELEMENT-REF", "CONTEXT-ELEMENT-REF", "TARGET-REF"]

        reloaded = AnyInstanceRef()
        parser.readAnyInstanceRef(_ns_wrap(parent), reloaded)

        assert reloaded.getBaseRef().getValue() == "/Pkg/Base"
        assert reloaded.getBaseRef().getDest() == "SW-COMPONENT-PROTOTYPE"
        assert [ref.getValue() for ref in reloaded.getContextElementRefs()] == ["/Pkg/Base/Step1", "/Pkg/Base/Step2"]
        assert reloaded.getTargetRef().getValue() == "/Pkg/Target"
        assert reloaded.getTargetRef().getDest() == "R-PORT-PROTOTYPE"

    def test_minimal_instance_ref_round_trip(self, writer, parser):
        """A target-only instance ref round-trips its field values and leaves the rest unset."""
        iref = AnyInstanceRef()
        iref.setTargetRef(RefType().setValue("/Pkg/Target").setDest("R-PORT-PROTOTYPE"))

        parent = ET.Element("PARENT")
        iref_element = ET.SubElement(parent, "VALUE-IREF")
        writer.writeAnyInstanceRef(iref_element, iref)
        assert [child.tag for child in iref_element] == ["TARGET-REF"]

        reloaded = AnyInstanceRef()
        parser.readAnyInstanceRef(_ns_wrap(parent), reloaded)
        assert reloaded.getTargetRef().getValue() == "/Pkg/Target"
        assert reloaded.getBaseRef() is None
        assert reloaded.getContextElementRefs() == []
        assert reloaded.getVariationPoint() is None

    def test_ar_object_attributes_survive(self, writer, parser):
        """S/T checksum/timestamp owned by the ARObject level survive (Rule 0025)."""
        iref = _full_instance_ref()
        iref.setChecksum(String().setValue("csum-1"))

        parent = ET.Element("PARENT")
        iref_element = ET.SubElement(parent, "VALUE-IREF")
        writer.writeAnyInstanceRef(iref_element, iref)
        assert iref_element.attrib.get("S") == "csum-1"

        reloaded = AnyInstanceRef()
        parser.readAnyInstanceRef(_ns_wrap(parent), reloaded)
        assert reloaded.getChecksum().getValue() == "csum-1"

    def test_variation_point_round_trips(self, writer, parser):
        """The XSD-declared VARIATION-POINT survives in both directions (Rule 0020 + Rule 0025)."""
        iref = _full_instance_ref()
        variation_point = VariationPoint()
        variation_point.setShortLabel(NameToken().setValue("VP"))
        iref.setVariationPoint(variation_point)

        parent = ET.Element("PARENT")
        iref_element = ET.SubElement(parent, "VALUE-IREF")
        writer.writeAnyInstanceRef(iref_element, iref)

        serialized = ET.tostring(parent).decode("utf-8")
        assert "<VARIATION-POINT" in serialized
        # sequenceOffset 10000 keeps VARIATION-POINT last
        assert [child.tag for child in iref_element][-1] == "VARIATION-POINT"

        reloaded = AnyInstanceRef()
        parser.readAnyInstanceRef(_ns_wrap(parent), reloaded)
        assert reloaded.getVariationPoint() is not None
        assert reloaded.getVariationPoint().getShortLabel().getValue() == "VP"

    def test_no_variation_point_emitted_when_unset(self, writer, parser):
        """An unset variationPoint emits no element and re-parses as None."""
        iref = _full_instance_ref()

        parent = ET.Element("PARENT")
        iref_element = ET.SubElement(parent, "VALUE-IREF")
        writer.writeAnyInstanceRef(iref_element, iref)
        assert "<VARIATION-POINT" not in ET.tostring(parent).decode("utf-8")

        reloaded = AnyInstanceRef()
        parser.readAnyInstanceRef(_ns_wrap(parent), reloaded)
        assert reloaded.getVariationPoint() is None

    def test_incoming_variation_point_is_read(self, parser):
        """A VARIATION-POINT arriving on the wire is stored, not dropped."""
        raw = (
            "<AUTOSAR xmlns='%s'><VALUE-IREF><BASE-REF DEST='SW-COMPONENT-PROTOTYPE'>/Pkg/Base</BASE-REF>"
            "<TARGET-REF DEST='R-PORT-PROTOTYPE'>/Pkg/Target</TARGET-REF>"
            "<VARIATION-POINT><SHORT-LABEL>VP</SHORT-LABEL></VARIATION-POINT></VALUE-IREF></AUTOSAR>" % NS
        )
        reloaded = AnyInstanceRef()
        parser.readAnyInstanceRef(ET.fromstring(raw)[0], reloaded)
        assert reloaded.getVariationPoint() is not None
        assert reloaded.getVariationPoint().getShortLabel().getValue() == "VP"
