"""
Tests for writing INSTANTIATION-DATA-DEF-PROPS elements — InstantiationDataDefProps, Table 7.41 (p.588, R23-11).

InstantiationDataDefProps (Base = ARObject) carries three own attributes whose writer element
order must follow the XSD sequence (AUTOSAR_00052.xsd group INSTANTIATION-DATA-DEF-PROPS):
PARAMETER-INSTANCE → SW-DATA-DEF-PROPS → VARIABLE-INSTANCE. The ARObject base attributes
(S checksum, T timestamp) belong to the element set via the XSD AR-OBJECT attributeGroup. The
INSTANTIATION-DATA-DEF-PROPS element is emitted inline by writeNvBlockDescriptor and
writeSwcInternalBehaviorInstantiationDataDefProps; its round-trip goes through the matching
reader call sites.

Round-trip counterpart: tests/test_armodel/parser/test_instantiation_data_def_props.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, RefType, String
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDescriptor
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import SwcInternalBehavior
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import AutosarParameterRef, AutosarVariableRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.InstanceRefsUsage import VariableInAtomicSWCTypeInstanceRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstantiationDataDefProps import InstantiationDataDefProps
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ELEMENT_ORDER = [
    "PARAMETER-INSTANCE",
    "SW-DATA-DEF-PROPS",
    "VARIABLE-INSTANCE",
]


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


def _filled_props() -> InstantiationDataDefProps:
    props = InstantiationDataDefProps()

    parameter_instance = AutosarParameterRef()
    parameter_instance.setLocalParameterRef(_ref("/Swc/LocalParameter", "PARAMETER-DATA-PROTOTYPE"))
    props.setParameterInstance(parameter_instance)

    def_props = SwDataDefProps()
    def_props.setBaseTypeRef(_ref("/DataTypes/uint8", "SW-BASE-TYPE"))
    props.setSwDataDefProps(def_props)

    variable_instance = AutosarVariableRef()
    variable_iref = VariableInAtomicSWCTypeInstanceRef()
    variable_iref.setPortPrototypeRef(_ref("/Swc/DataPort", "P-PORT-PROTOTYPE"))
    variable_instance.setAutosarVariableIRef(variable_iref)
    props.setVariableInstance(variable_instance)
    return props


class TestWriteSwcInternalBehaviorInstantiationDataDefProps:
    """Tests for writeSwcInternalBehaviorInstantiationDataDefProps — own element field values (Table 7.41)."""

    def _write(self, writer, props: InstantiationDataDefProps) -> ET.Element:
        root = AUTOSAR.getInstance().createARPackage("Pkg")
        behavior = SwcInternalBehavior(root, "behavior")
        behavior.addInstantiationDataDefProps(props)
        parent = ET.Element("ROOT")
        writer.writeSwcInternalBehaviorInstantiationDataDefProps(parent, behavior)
        return parent.find("INSTANTIATION-DATA-DEF-PROPSS")[0]

    def test_own_element_field_values(self, writer):
        """Test that all three attribute elements are emitted with their field values."""
        elem = self._write(writer, _filled_props())

        assert elem is not None
        assert elem.find("PARAMETER-INSTANCE/LOCAL-PARAMETER-REF").text == "/Swc/LocalParameter"
        assert elem.find("PARAMETER-INSTANCE/LOCAL-PARAMETER-REF").get("DEST") == "PARAMETER-DATA-PROTOTYPE"
        assert elem.find("SW-DATA-DEF-PROPS/SW-DATA-DEF-PROPS-VARIANTS/SW-DATA-DEF-PROPS-CONDITIONAL/BASE-TYPE-REF").text == "/DataTypes/uint8"
        assert elem.find("SW-DATA-DEF-PROPS/SW-DATA-DEF-PROPS-VARIANTS/SW-DATA-DEF-PROPS-CONDITIONAL/BASE-TYPE-REF").get("DEST") == "SW-BASE-TYPE"
        assert elem.find("VARIABLE-INSTANCE/AUTOSAR-VARIABLE-IREF/PORT-PROTOTYPE-REF").text == "/Swc/DataPort"
        assert elem.find("VARIABLE-INSTANCE/AUTOSAR-VARIABLE-IREF/PORT-PROTOTYPE-REF").get("DEST") == "P-PORT-PROTOTYPE"

    def test_xsd_element_order(self, writer):
        """Test that the emitted element order follows the XSD group sequence."""
        elem = self._write(writer, _filled_props())

        children = [child.tag for child in elem]
        assert children == XSD_ELEMENT_ORDER

    def test_ar_object_attributes_written(self, writer):
        """Test that the ARObject base attributes (S checksum, T timestamp) are written."""
        props = InstantiationDataDefProps()
        checksum = String()
        checksum.setValue("ck1")
        props.setChecksum(checksum)
        timestamp = DateTime()
        timestamp.setValue("2024-01-01T12:00:00+01:00")
        props.setTimestamp(timestamp)

        elem = self._write(writer, props)

        assert elem.get("S") == "ck1"
        assert elem.get("T") is not None

    def test_no_wrapper_when_aggregation_empty(self, writer):
        """Test that an empty aggregation emits no INSTANTIATION-DATA-DEF-PROPSS wrapper."""
        root = AUTOSAR.getInstance().createARPackage("Pkg")
        behavior = SwcInternalBehavior(root, "behavior")
        parent = ET.Element("ROOT")

        writer.writeSwcInternalBehaviorInstantiationDataDefProps(parent, behavior)

        assert parent.find("INSTANTIATION-DATA-DEF-PROPSS") is None

    def test_empty_props_element(self, writer):
        """Test that a props without any set field emits the element with no children."""
        elem = self._write(writer, InstantiationDataDefProps())

        assert elem is not None
        assert list(elem) == []


class TestWriteNvBlockDescriptorInstantiationDataDefProps:
    """Tests for the NvBlockDescriptor.instantiationDataDefProps write dispatch."""

    def test_dispatch_ar_object_attributes_written(self, writer):
        """Test that writeNvBlockDescriptor writes the ARObject base attributes on the props element."""
        root = AUTOSAR.getInstance().createARPackage("Pkg")
        descriptor = NvBlockDescriptor(root, "NvBlockDesc")
        props = InstantiationDataDefProps()
        checksum = String()
        checksum.setValue("ck1")
        props.setChecksum(checksum)
        descriptor.addInstantiationDataDefProps(props)

        parent = ET.Element("ROOT")
        writer.writeNvBlockDescriptor(parent, descriptor)

        props_element = parent.find("NV-BLOCK-DESCRIPTOR/INSTANTIATION-DATA-DEF-PROPSS/INSTANTIATION-DATA-DEF-PROPS")
        assert props_element is not None
        assert props_element.get("S") == "ck1"


class TestWriteReadRoundTrip:
    """Write → re-parse round-trip through the matching reader call sites."""

    def test_round_trip_field_values(self, writer):
        """Test that write and re-parse preserve every field value one level down."""
        original = _filled_props()

        root = AUTOSAR.getInstance().createARPackage("Pkg")
        behavior = SwcInternalBehavior(root, "behavior")
        behavior.addInstantiationDataDefProps(original)
        parent = ET.Element("ROOT")
        writer.writeSwcInternalBehaviorInstantiationDataDefProps(parent, behavior)
        xml = ET.tostring(parent.find("INSTANTIATION-DATA-DEF-PROPSS"), encoding="unicode")
        element = ET.fromstring(f"<ROOT xmlns='{NS}'>{xml}</ROOT>")

        parser = ARXMLParser()
        reloaded_behavior = SwcInternalBehavior(AUTOSAR.getInstance().createARPackage("Pkg2"), "behavior")
        parser.readSwcInternalBehaviorInstantiationDataDefProps(element, reloaded_behavior)

        props = reloaded_behavior.getInstantiationDataDefPropss()[0]
        parameter_instance = props.getParameterInstance()
        assert isinstance(parameter_instance, AutosarParameterRef)
        assert parameter_instance.getLocalParameterRef().getValue() == "/Swc/LocalParameter"
        assert parameter_instance.getLocalParameterRef().getDest() == "PARAMETER-DATA-PROTOTYPE"
        def_props = props.getSwDataDefProps()
        assert isinstance(def_props, SwDataDefProps)
        assert def_props.getBaseTypeRef().getValue() == "/DataTypes/uint8"
        variable_instance = props.getVariableInstance()
        assert isinstance(variable_instance, AutosarVariableRef)
        iref = variable_instance.getAutosarVariableIRef()
        assert isinstance(iref, VariableInAtomicSWCTypeInstanceRef)
        assert iref.getPortPrototypeRef().getValue() == "/Swc/DataPort"

    def test_round_trip_absent_elements(self, writer):
        """Test that absent attribute elements are not emitted and re-parse to None."""
        props = InstantiationDataDefProps()

        root = AUTOSAR.getInstance().createARPackage("Pkg")
        behavior = SwcInternalBehavior(root, "behavior")
        behavior.addInstantiationDataDefProps(props)
        parent = ET.Element("ROOT")
        writer.writeSwcInternalBehaviorInstantiationDataDefProps(parent, behavior)
        wrapper = parent.find("INSTANTIATION-DATA-DEF-PROPSS")
        elem = wrapper[0]
        assert elem.find("PARAMETER-INSTANCE") is None
        assert elem.find("SW-DATA-DEF-PROPS") is None
        assert elem.find("VARIABLE-INSTANCE") is None

        xml = ET.tostring(wrapper, encoding="unicode")
        element = ET.fromstring(f"<ROOT xmlns='{NS}'>{xml}</ROOT>")

        parser = ARXMLParser()
        reloaded_behavior = SwcInternalBehavior(AUTOSAR.getInstance().createARPackage("Pkg2"), "behavior")
        parser.readSwcInternalBehaviorInstantiationDataDefProps(element, reloaded_behavior)

        reloaded = reloaded_behavior.getInstantiationDataDefPropss()[0]
        assert reloaded.getParameterInstance() is None
        assert reloaded.getSwDataDefProps() is None
        assert reloaded.getVariableInstance() is None
