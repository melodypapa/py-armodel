"""Writer/parser round-trip tests for the SWC composition connectors and
instantiation RTE event props (CP_TPS_SoftwareComponentTemplate).

Covers Table 3.17 InstantiationRTEEventProps (p.85), Table 3.16 InstantiationTimingEventProps
(p.85), Table 3.12 SwConnector (p.80) and Table 3.15 PassThroughSwConnector (p.83).

XML element order per the XSD groups INSTANTIATION-RTE-EVENT-PROPS / INSTANTIATION-TIMING-EVENT-PROPS /
SW-CONNECTOR / PASS-THROUGH-SW-CONNECTOR (AUTOSAR_00052.xsd): REFINED-EVENT-IREF, SHORT-LABEL,
PERIOD; MAPPING-REF; PROVIDED-OUTER-PORT-REF, REQUIRED-OUTER-PORT-REF.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition import InstantiationTimingEventProps
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import InstanceEventInCompositionInstanceRef
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


class TestPassThroughSwConnectorRoundTrip:
    def test_round_trip_field_values_and_element_order(self):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        composition = pkg.createCompositionSwComponentType("Comp")
        connector = composition.createPassThroughSwConnector("Pass")
        connector.setRequiredOuterPortRef(_ref("/Pkg/Comp/OuterRequired", "R-PORT-PROTOTYPE"))
        connector.setProvidedOuterPortRef(_ref("/Pkg/Comp/OuterProvided", "P-PORT-PROTOTYPE"))

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(parent, composition.parent)
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner))

        connector_tag = root.find("{%s}AR-PACKAGE/{%s}ELEMENTS/{%s}COMPOSITION-SW-COMPONENT-TYPE/{%s}CONNECTORS/{%s}PASS-THROUGH-SW-CONNECTOR" % tuple([NS] * 5))
        assert [child.tag.split("}")[-1] for child in connector_tag] == ["SHORT-NAME", "PROVIDED-OUTER-PORT-REF", "REQUIRED-OUTER-PORT-REF"]

        parser = ARXMLParser(options={"warning": True})
        parsed_pkg = AUTOSAR.getInstance().createARPackage("Parsed")
        parser.readARPackageElements(root.find("{%s}AR-PACKAGE" % NS), parsed_pkg)

        parsed = parsed_pkg.getCompositionSwComponentTypes()[0].getPassThroughSwConnectors()[0]
        assert parsed.getProvidedOuterPortRef().getValue() == "/Pkg/Comp/OuterProvided"
        assert parsed.getProvidedOuterPortRef().getDest() == "P-PORT-PROTOTYPE"
        assert parsed.getRequiredOuterPortRef().getValue() == "/Pkg/Comp/OuterRequired"
        assert parsed.getRequiredOuterPortRef().getDest() == "R-PORT-PROTOTYPE"

    def test_empty_connector_has_no_ref_elements(self):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        composition = pkg.createCompositionSwComponentType("Comp")
        composition.createPassThroughSwConnector("Pass")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(parent, composition.parent)
        raw = ET.tostring(parent).decode("utf-8")
        assert "PROVIDED-OUTER-PORT-REF" not in raw
        assert "REQUIRED-OUTER-PORT-REF" not in raw


class TestSwConnectorBaseRoundTrip:
    def test_mapping_ref_round_trip(self):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        composition = pkg.createCompositionSwComponentType("Comp")
        connector = composition.createPassThroughSwConnector("Pass")
        connector.setMappingRef(_ref("/Pkg/PortInterfaceMappings/Map1", "PORT-INTERFACE-MAPPING"))

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(parent, composition.parent)
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner))
        parser = ARXMLParser(options={"warning": True})
        parsed_pkg = AUTOSAR.getInstance().createARPackage("Parsed")
        parser.readARPackageElements(root.find("{%s}AR-PACKAGE" % NS), parsed_pkg)

        parsed_connectors = parsed_pkg.getCompositionSwComponentTypes()[0].getSwConnectors()
        assert len(parsed_connectors) == 1
        parsed = parsed_connectors[0]
        assert parsed.getMappingRef() is not None
        assert parsed.getMappingRef().getValue() == "/Pkg/PortInterfaceMappings/Map1"
        assert parsed.getMappingRef().getDest() == "PORT-INTERFACE-MAPPING"

    def test_connector_without_mapping_has_no_mapping_ref_element(self):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        composition = pkg.createCompositionSwComponentType("Comp")
        composition.createPassThroughSwConnector("Pass")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(parent, composition.parent)
        raw = ET.tostring(parent).decode("utf-8")
        assert "MAPPING-REF" not in raw


class TestInstantiationRTEEventPropsRoundTrip:
    def _build(self):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        composition = pkg.createCompositionSwComponentType("Comp")
        props = InstantiationTimingEventProps()
        iref = InstanceEventInCompositionInstanceRef()
        iref.addContextComponentPrototypeRef(_ref("/Pkg/Comp/Swc1", "SW-COMPONENT-PROTOTYPE"))
        iref.setTargetEventRef(_ref("/Pkg/App/Ib/TimingEvent1", "TIMING-EVENT"))
        props.setRefinedEventIRef(iref)
        props.setShortLabel(Identifier().setValue("splitKey1"))
        composition.addInstantiationRTEEventProps(props)
        return composition, props

    def test_round_trip_field_values(self):
        composition, props = self._build()

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(parent, composition.parent)
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner))
        parser = ARXMLParser(options={"warning": True})
        parsed_pkg = AUTOSAR.getInstance().createARPackage("Parsed")
        parser.readARPackageElements(root.find("{%s}AR-PACKAGE" % NS), parsed_pkg)

        parsed_composition = parsed_pkg.getCompositionSwComponentTypes()[0]
        parsed_props = parsed_composition.getInstantiationRTEEventProps()
        assert len(parsed_props) == 1
        parsed = parsed_props[0]
        assert isinstance(parsed, InstantiationTimingEventProps)

        parsed_iref = parsed.getRefinedEventIRef()
        assert parsed_iref is not None
        assert [ref.getValue() for ref in parsed_iref.getContextComponentPrototypeRefs()] == ["/Pkg/Comp/Swc1"]
        assert parsed_iref.getTargetEventRef().getValue() == "/Pkg/App/Ib/TimingEvent1"
        assert parsed_iref.getTargetEventRef().getDest() == "TIMING-EVENT"
        assert props.getShortLabel().getValue() == "splitKey1"

    def test_period_round_trip_and_element_order(self):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        composition = pkg.createCompositionSwComponentType("Comp")
        props = InstantiationTimingEventProps()
        props.setPeriod(TimeValue().setValue("0.02"))
        composition.addInstantiationRTEEventProps(props)

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(parent, composition.parent)
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner))
        parser = ARXMLParser(options={"warning": True})
        parsed_pkg = AUTOSAR.getInstance().createARPackage("Parsed")
        parser.readARPackageElements(root.find("{%s}AR-PACKAGE" % NS), parsed_pkg)

        props_tag = root.find("{%s}AR-PACKAGE/{%s}ELEMENTS/{%s}COMPOSITION-SW-COMPONENT-TYPE/{%s}INSTANTIATION-RTE-EVENT-PROPSS/{%s}INSTANTIATION-TIMING-EVENT-PROPS" % tuple([NS] * 5))
        assert [child.tag.split("}")[-1] for child in props_tag] == ["PERIOD"]
        parsed_props = parsed_pkg.getCompositionSwComponentTypes()[0].getInstantiationRTEEventProps()[0]
        assert parsed_props.getPeriod().getValue() == 0.02

    def test_empty_instantiation_props_wrapper_not_written(self):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        composition = pkg.createCompositionSwComponentType("Comp")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(parent, composition.parent)
        raw = ET.tostring(parent).decode("utf-8")
        assert "INSTANTIATION-RTE-EVENT-PROPSS" not in raw

    def test_no_variation_point_written(self):
        composition, _ = self._build()

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(parent, composition.parent)
        raw = ET.tostring(parent).decode("utf-8")
        assert "VARIATION-POINT" not in raw

    def test_incoming_variation_point_ignored(self):
        parser = ARXMLParser(options={"warning": True})
        snippet = (
            "<INSTANTIATION-TIMING-EVENT-PROPS xmlns='%s'>"
            "<REFINED-EVENT-IREF><TARGET-EVENT-REF DEST='TIMING-EVENT'>/Pkg/App/Ib/E1</TARGET-EVENT-REF></REFINED-EVENT-IREF>"
            "<SHORT-LABEL>K1</SHORT-LABEL>"
            "<VARIATION-POINT><DEVIATION-ATTRIBUTE><VARIATION-POINT-CLASS>I</VARIATION-POINT-CLASS></DEVIATION-ATTRIBUTE></VARIATION-POINT>"
            "</INSTANTIATION-TIMING-EVENT-PROPS>" % NS
        )
        element = ET.fromstring(snippet)
        props = InstantiationTimingEventProps()
        parser.readInstantiationRTEEventProps(element, props)

        assert props.getShortLabel().getValue() == "K1"
        assert props.getRefinedEventIRef().getTargetEventRef().getValue() == "/Pkg/App/Ib/E1"
