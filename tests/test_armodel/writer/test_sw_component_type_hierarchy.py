"""Writer/parser round-trip tests for the SwComponentType hierarchy (CP_TPS_SoftwareComponentTemplate).

Covers Table 3.1 SwComponentType (p.65), Table 2.1 ParameterSwComponentType (p.41),
Table 3.8 AtomicSwComponentType (p.70) and Table 3.9 ApplicationSwComponentType (p.71).

XML element order per the XSD groups SW-COMPONENT-TYPE / PARAMETER-SW-COMPONENT-TYPE /
ATOMIC-SW-COMPONENT-TYPE (AUTOSAR_00052.xsd): SW-COMPONENT-DOCUMENTATIONS (sequenceOffset
-10), CONSISTENCY-NEEDSS, PORTS, PORT-GROUPS, SWC-MAPPING-CONSTRAINT-REFS,
UNIT-GROUP-REFS; then INTERNAL-BEHAVIORS / SYMBOL-PROPS (atomic) and
CONSTANT-MAPPING-REFS / DATA-TYPE-MAPPING-REFS / INSTANTIATION-DATA-DEF-PROPSS
(parameter). The base-class coverage runs through APPLICATION-SW-COMPONENT-TYPE,
a concrete dispatchable subclass.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
    ApplicationSwComponentType,
    PPortPrototype,
    PRPortPrototype,
    RPortPrototype,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _ref(value, dest=None):
    ref = RefType()
    ref.setValue(value)
    if dest is not None:
        ref.dest = dest
    return ref


class TestSwComponentTypeBaseRoundTrip:
    def _build(self, with_base_content=True):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        swc = pkg.createApplicationSwComponentType("App")
        if with_base_content:
            swc.createPPortPrototype("P1")
            swc.createRPortPrototype("R1")
            swc.createPRPortPrototype("PR1")
            group = swc.createPortGroup("G1")
            group.addOuterPortRef(_ref("/Pkg/App/P1", "PORT-PROTOTYPE"))
            swc.addSwcMappingConstraintRef(_ref("/Pkg/Constraints/C1", "SW-COMPONENT-MAPPING-CONSTRAINTS"))
            swc.addUnitGroupRef(_ref("/Pkg/Units/U1", "UNIT-GROUP"))
        return swc

    def _write_read(self, swc):
        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(parent, swc.parent)
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner))
        parsed_pkg = AUTOSAR.getInstance().createARPackage("Parsed")
        ARXMLParser().readARPackageElements(root[0], parsed_pkg)
        return parsed_pkg

    def test_round_trip_base_content(self):
        swc = self._build()
        parsed_pkg = self._write_read(swc)
        parsed = parsed_pkg.getReferrableElement("App", ApplicationSwComponentType)
        assert parsed is not None
        ports = parsed.getPorts()
        assert [p.short_name for p in ports] == ["P1", "R1", "PR1"]
        assert isinstance(ports[0], PPortPrototype)
        assert isinstance(ports[1], RPortPrototype)
        assert isinstance(ports[2], PRPortPrototype)
        groups = parsed.getPortGroups()
        assert len(groups) == 1
        outer_refs = groups[0].getOuterPortRefs()
        assert len(outer_refs) == 1
        assert outer_refs[0].getValue() == "/Pkg/App/P1"
        assert outer_refs[0].dest == "PORT-PROTOTYPE"
        mapping_refs = parsed.getSwcMappingConstraintsRefs()
        assert len(mapping_refs) == 1
        assert mapping_refs[0].getValue() == "/Pkg/Constraints/C1"
        assert mapping_refs[0].dest == "SW-COMPONENT-MAPPING-CONSTRAINTS"
        unit_refs = parsed.getUnitGroupRefs()
        assert len(unit_refs) == 1
        assert unit_refs[0].getValue() == "/Pkg/Units/U1"
        assert unit_refs[0].dest == "UNIT-GROUP"

    def test_xsd_element_order(self):
        swc = self._build()
        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(parent, swc.parent)
        swc_tag = parent.find("ELEMENTS/APPLICATION-SW-COMPONENT-TYPE")
        children = [child.tag for child in swc_tag]
        assert children.index("SHORT-NAME") < children.index("PORTS")
        assert children.index("PORTS") < children.index("PORT-GROUPS")
        assert children.index("PORT-GROUPS") < children.index("SWC-MAPPING-CONSTRAINT-REFS")
        assert children.index("SWC-MAPPING-CONSTRAINT-REFS") < children.index("UNIT-GROUP-REFS")

    def test_round_trip_empty_component(self):
        swc = self._build(with_base_content=False)
        parsed_pkg = self._write_read(swc)
        parsed = parsed_pkg.getReferrableElement("App", ApplicationSwComponentType)
        assert parsed is not None
        assert parsed.getPorts() == []
        assert parsed.getPortGroups() == []
        assert parsed.getSwcMappingConstraintsRefs() == []
        assert parsed.getUnitGroupRefs() == []
        assert parsed.getConsistencyNeeds() == []
        assert parsed.getSwComponentDocumentation() is None
        wrapper = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(wrapper, swc.parent)
        swc_tag = wrapper.find("ELEMENTS/APPLICATION-SW-COMPONENT-TYPE")
        assert swc_tag.find("PORTS") is None
        assert swc_tag.find("PORT-GROUPS") is None
        assert swc_tag.find("SWC-MAPPING-CONSTRAINT-REFS") is None
        assert swc_tag.find("UNIT-GROUP-REFS") is None
        assert swc_tag.find("CONSISTENCY-NEEDSS") is None
        assert swc_tag.find("SW-COMPONENT-DOCUMENTATIONS") is None
