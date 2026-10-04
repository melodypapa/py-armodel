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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType
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
        assert parsed.getShortLabel().getValue() == "splitKey1"

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
