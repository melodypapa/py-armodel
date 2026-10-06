"""
Tests for writing AUTOSAR-PARAMETER-IREF elements — ParameterInAtomicSWCTypeInstanceRef, Table 5.36 (p.319, R23-11).

ParameterInAtomicSWCTypeInstanceRef (Base = ARObject, AtpInstanceRef) carries five own
attributes whose writer element order must follow the XSD sequenceOffset
(AUTOSAR_00052.xsd group PARAMETER-IN-ATOMIC-SWC-TYPE-INSTANCE-REF):
PORT-PROTOTYPE-REF (20) → ROOT-PARAMETER-DATA-PROTOTYPE-REF (30) →
CONTEXT-DATA-PROTOTYPE-REF (40) → TARGET-DATA-PROTOTYPE-REF (50). The `base` attribute
is atpDerived — the XSD skips it ("Association <<atpDerived>>base skipped"), so no
element is emitted. The AUTOSAR-PARAMETER-IREF wrapper is emitted by
setAutosarParameterRef; its round-trip goes through getAutosarParameterRef.

Round-trip counterpart: tests/test_armodel/parser/test_parameter_in_atomic_swc_type_instance_ref.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import AutosarParameterRef, ParameterAccess
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.InstanceRefsUsage import ParameterInAtomicSWCTypeInstanceRef
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    """Create ARXML writer instance."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLWriter()


def _ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _filled_iref():
    iref = ParameterInAtomicSWCTypeInstanceRef()
    iref.setPortPrototypeRef(_ref("/Swc/Port", "PORT-PROTOTYPE"))
    iref.setRootParameterDataPrototypeRef(_ref("/Swc/RootParameter", "PARAMETER-DATA-PROTOTYPE"))
    iref.addContextDataPrototypeRef(_ref("/Swc/ContextFirst", "APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE"))
    iref.addContextDataPrototypeRef(_ref("/Swc/ContextSecond", "APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE"))
    iref.setTargetDataPrototypeRef(_ref("/Swc/TargetElement", "PARAMETER-DATA-PROTOTYPE"))
    return iref


class TestSetParameterInAtomicSWCTypeInstanceRef:
    """Tests for setParameterInAtomicSWCTypeInstanceRef — own element field values (Table 5.36)."""

    def test_write_field_values(self, writer):
        """Test that all four ref attributes are emitted with their values read through the getters."""
        parent = ET.Element("PARENT")

        writer.setParameterInAtomicSWCTypeInstanceRef(parent, "AUTOSAR-PARAMETER-IREF", _filled_iref())

        element = parent.find("AUTOSAR-PARAMETER-IREF")
        assert element is not None
        port_ref_element = element.find("PORT-PROTOTYPE-REF")
        assert port_ref_element.text == "/Swc/Port"
        assert port_ref_element.attrib.get("DEST") == "PORT-PROTOTYPE"
        assert element.find("ROOT-PARAMETER-DATA-PROTOTYPE-REF").text == "/Swc/RootParameter"
        context_elements = element.findall("CONTEXT-DATA-PROTOTYPE-REF")
        assert [ref.text for ref in context_elements] == ["/Swc/ContextFirst", "/Swc/ContextSecond"]
        assert all(ref.attrib.get("DEST") == "APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE" for ref in context_elements)
        assert element.find("TARGET-DATA-PROTOTYPE-REF").text == "/Swc/TargetElement"

    def test_write_xsd_element_order(self, writer):
        """Test that the element order follows the XSD group sequenceOffset order (two context entries)."""
        parent = ET.Element("PARENT")

        writer.setParameterInAtomicSWCTypeInstanceRef(parent, "AUTOSAR-PARAMETER-IREF", _filled_iref())

        element = parent.find("AUTOSAR-PARAMETER-IREF")
        assert [elem.tag for elem in element] == [
            "PORT-PROTOTYPE-REF",
            "ROOT-PARAMETER-DATA-PROTOTYPE-REF",
            "CONTEXT-DATA-PROTOTYPE-REF",
            "CONTEXT-DATA-PROTOTYPE-REF",
            "TARGET-DATA-PROTOTYPE-REF",
        ]

    def test_write_none_emits_nothing(self, writer):
        """Test that a None iref emits no element at all."""
        parent = ET.Element("PARENT")

        writer.setParameterInAtomicSWCTypeInstanceRef(parent, "AUTOSAR-PARAMETER-IREF", None)

        assert len(parent) == 0

    def test_write_empty_iref_emits_empty_wrapper(self, writer):
        """Test that a default iref emits the wrapper only, with no attribute children."""
        parent = ET.Element("PARENT")

        writer.setParameterInAtomicSWCTypeInstanceRef(parent, "AUTOSAR-PARAMETER-IREF", ParameterInAtomicSWCTypeInstanceRef())

        element = parent.find("AUTOSAR-PARAMETER-IREF")
        assert element is not None
        assert len(element) == 0

    def test_write_atp_derived_base_emits_no_element(self, writer):
        """Test that the atpDerived base attribute emits no XML element."""
        parent = ET.Element("PARENT")
        iref = _filled_iref()
        iref.setBaseRef(_ref("/Swc", "ATOMIC-SWC-TYPE"))

        writer.setParameterInAtomicSWCTypeInstanceRef(parent, "AUTOSAR-PARAMETER-IREF", iref)

        element = parent.find("AUTOSAR-PARAMETER-IREF")
        assert element.find("BASE-REF") is None


class TestParameterInAtomicSWCTypeInstanceRefRoundTrip:
    """Tests for the aggregation round-trips."""

    def _reparse(self, parent_element, root_tag):
        xml_text = ET.tostring(parent_element, encoding="unicode")
        return ET.fromstring(xml_text.replace(root_tag, f"{root_tag} xmlns='{NS}'", 1))

    def test_round_trip_via_parameter_access(self, writer):
        """Test the parameter access aggregation round-trip with field values."""
        root = AUTOSAR.getInstance().createARPackage("Pkg")
        access = ParameterAccess(root, "Pa1")
        parameter = AutosarParameterRef()
        parameter.setAutosarParameterIRef(_filled_iref())
        access.setAccessedParameter(parameter)

        parent = ET.Element("PARENT")
        writer.writeParameterAccess(parent, access)

        element = parent.find("PARAMETER-ACCESS")
        assert element is not None
        reloaded_element = self._reparse(element, "PARAMETER-ACCESS")

        root2 = AUTOSAR.getInstance().createARPackage("Pkg2")
        reloaded = ParameterAccess(root2, "OtherName")
        ARXMLParser().readParameterAccess(reloaded_element, reloaded)

        reloaded_parameter = reloaded.getAccessedParameter()
        assert isinstance(reloaded_parameter, AutosarParameterRef)
        iref = reloaded_parameter.getAutosarParameterIRef()
        assert isinstance(iref, ParameterInAtomicSWCTypeInstanceRef)
        assert iref.getPortPrototypeRef().getValue() == "/Swc/Port"
        assert iref.getPortPrototypeRef().getDest() == "PORT-PROTOTYPE"
        assert iref.getRootParameterDataPrototypeRef().getValue() == "/Swc/RootParameter"
        assert [ref.getValue() for ref in iref.getContextDataPrototypeRefs()] == ["/Swc/ContextFirst", "/Swc/ContextSecond"]
        assert all(ref.getDest() == "APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE" for ref in iref.getContextDataPrototypeRefs())
        assert iref.getTargetDataPrototypeRef().getValue() == "/Swc/TargetElement"
        assert iref.getTargetDataPrototypeRef().getDest() == "PARAMETER-DATA-PROTOTYPE"

    def test_round_trip_empty_wrapper(self, writer):
        """Test that an empty wrapper round-trips to an instance with all fields unset."""
        parent = ET.Element("PARENT")
        writer.setParameterInAtomicSWCTypeInstanceRef(parent, "AUTOSAR-PARAMETER-IREF", ParameterInAtomicSWCTypeInstanceRef())

        reloaded_element = self._reparse(parent, "PARENT")
        reloaded = ARXMLParser().getParameterInAtomicSWCTypeInstanceRef(reloaded_element, "AUTOSAR-PARAMETER-IREF")

        assert isinstance(reloaded, ParameterInAtomicSWCTypeInstanceRef)
        assert reloaded.getBaseRef() is None
        assert reloaded.getContextDataPrototypeRefs() == []
        assert reloaded.getPortPrototypeRef() is None
        assert reloaded.getRootParameterDataPrototypeRef() is None
        assert reloaded.getTargetDataPrototypeRef() is None
