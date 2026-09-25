"""
Tests for reading INSTANTIATION-DATA-DEF-PROPS elements — InstantiationDataDefProps, Table 7.41 (p.588, R23-11).

InstantiationDataDefProps (Base = ARObject) carries three own attributes whose reader element set
follows the XSD group INSTANTIATION-DATA-DEF-PROPS (AUTOSAR_00052.xsd): PARAMETER-INSTANCE (type
AUTOSAR-PARAMETER-REF), SW-DATA-DEF-PROPS (type SW-DATA-DEF-PROPS) and VARIABLE-INSTANCE (type
AUTOSAR-VARIABLE-REF) — each 0..1, order-independent on read. The ARObject base attributes
(S checksum, T timestamp) belong to the element set via the XSD AR-OBJECT attributeGroup. The
class is aggregated by NvBlockDescriptor.instantiationDataDefProps and
SwcInternalBehavior.instantiationDataDefProps, and read at each call site (readNvBlockDescriptor /
readSwcInternalBehaviorInstantiationDataDefProps).

Round-trip counterpart: tests/test_armodel/writer/test_instantiation_data_def_props.py
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDescriptor
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import SwcInternalBehavior
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import AutosarParameterRef, AutosarVariableRef
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from tests.test_armodel.parser._helpers import NS

PROPS_CONTENT = (
    "<PARAMETER-INSTANCE>"
    "<LOCAL-PARAMETER-REF DEST='PARAMETER-DATA-PROTOTYPE'>/Swc/LocalParameter</LOCAL-PARAMETER-REF>"
    "</PARAMETER-INSTANCE>"
    "<SW-DATA-DEF-PROPS>"
    "<SW-DATA-DEF-PROPS-VARIANTS><SW-DATA-DEF-PROPS-CONDITIONAL>"
    "<BASE-TYPE-REF DEST='SW-BASE-TYPE'>/DataTypes/uint8</BASE-TYPE-REF>"
    "</SW-DATA-DEF-PROPS-CONDITIONAL></SW-DATA-DEF-PROPS-VARIANTS>"
    "</SW-DATA-DEF-PROPS>"
    "<VARIABLE-INSTANCE>"
    "<AUTOSAR-VARIABLE-IREF>"
    "<PORT-PROTOTYPE-REF DEST='P-PORT-PROTOTYPE'>/Swc/DataPort</PORT-PROTOTYPE-REF>"
    "</AUTOSAR-VARIABLE-IREF>"
    "</VARIABLE-INSTANCE>"
)

WRAPPER_XML = f"<INSTANTIATION-DATA-DEF-PROPSS><INSTANTIATION-DATA-DEF-PROPS>{PROPS_CONTENT}</INSTANTIATION-DATA-DEF-PROPS></INSTANTIATION-DATA-DEF-PROPSS>"


def _wrap(inner: str) -> ET.Element:
    """Wrap the fragment in a namespaced root element."""
    return ET.fromstring(f"<ROOT xmlns='{NS}'>{inner}</ROOT>")


class TestReadSwcInternalBehaviorInstantiationDataDefProps:
    """Tests for the SwcInternalBehavior.instantiationDataDefProps dispatch."""

    def test_dispatch_field_values(self, parser):
        """Test that the aggregation children are read with their field values."""
        root = AUTOSAR.getInstance().createARPackage("Pkg")
        behavior = SwcInternalBehavior(root, "behavior")
        element = _wrap(WRAPPER_XML)

        parser.readSwcInternalBehaviorInstantiationDataDefProps(element, behavior)

        props_list = behavior.getInstantiationDataDefPropss()
        assert len(props_list) == 1
        props = props_list[0]
        parameter_instance = props.getParameterInstance()
        assert isinstance(parameter_instance, AutosarParameterRef)
        assert parameter_instance.getLocalParameterRef().getValue() == "/Swc/LocalParameter"
        assert parameter_instance.getLocalParameterRef().getDest() == "PARAMETER-DATA-PROTOTYPE"
        def_props = props.getSwDataDefProps()
        assert isinstance(def_props, SwDataDefProps)
        assert def_props.getBaseTypeRef().getValue() == "/DataTypes/uint8"
        assert def_props.getBaseTypeRef().getDest() == "SW-BASE-TYPE"
        variable_instance = props.getVariableInstance()
        assert isinstance(variable_instance, AutosarVariableRef)
        assert variable_instance.getAutosarVariableIRef().getPortPrototypeRef().getValue() == "/Swc/DataPort"

    def test_dispatch_empty_wrapper(self, parser):
        """Test that an empty INSTANTIATION-DATA-DEF-PROPS element yields an instance with all fields unset."""
        root = AUTOSAR.getInstance().createARPackage("Pkg")
        behavior = SwcInternalBehavior(root, "behavior")
        element = _wrap("<INSTANTIATION-DATA-DEF-PROPSS><INSTANTIATION-DATA-DEF-PROPS></INSTANTIATION-DATA-DEF-PROPS></INSTANTIATION-DATA-DEF-PROPSS>")

        parser.readSwcInternalBehaviorInstantiationDataDefProps(element, behavior)

        props = behavior.getInstantiationDataDefPropss()[0]
        assert props.getParameterInstance() is None
        assert props.getSwDataDefProps() is None
        assert props.getVariableInstance() is None

    def test_dispatch_absent_wrapper(self, parser):
        """Test that a behavior without INSTANTIATION-DATA-DEF-PROPSS leaves the aggregation empty."""
        root = AUTOSAR.getInstance().createARPackage("Pkg")
        behavior = SwcInternalBehavior(root, "behavior")
        element = _wrap("<SHORT-NAME>behavior</SHORT-NAME>")

        parser.readSwcInternalBehaviorInstantiationDataDefProps(element, behavior)

        assert behavior.getInstantiationDataDefPropss() == []

    def test_dispatch_ar_object_attributes_read(self, parser):
        """Test that the ARObject base attributes (S checksum, T timestamp) are read."""
        root = AUTOSAR.getInstance().createARPackage("Pkg")
        behavior = SwcInternalBehavior(root, "behavior")
        element = _wrap("<INSTANTIATION-DATA-DEF-PROPSS><INSTANTIATION-DATA-DEF-PROPS S='ck1' T='2024-01-01T12:00:00+00:00'></INSTANTIATION-DATA-DEF-PROPS></INSTANTIATION-DATA-DEF-PROPSS>")

        parser.readSwcInternalBehaviorInstantiationDataDefProps(element, behavior)

        props = behavior.getInstantiationDataDefPropss()[0]
        assert props.getChecksum() is not None
        assert props.getChecksum().getValue() == "ck1"
        assert props.getTimestamp() is not None


class TestReadNvBlockDescriptorInstantiationDataDefProps:
    """Tests for the NvBlockDescriptor.instantiationDataDefProps dispatch."""

    def test_dispatch_field_values(self, parser):
        """Test that readNvBlockDescriptor reads the aggregation children with their field values."""
        root = AUTOSAR.getInstance().createARPackage("Pkg")
        descriptor = NvBlockDescriptor(root, "NvBlockDesc")
        element = ET.fromstring(f"<ROOT xmlns='{NS}'>{WRAPPER_XML}</ROOT>")

        parser.readNvBlockDescriptor(element, descriptor)

        props_list = descriptor.getInstantiationDataDefPropss()
        assert len(props_list) == 1
        props = props_list[0]
        assert props.getParameterInstance().getLocalParameterRef().getValue() == "/Swc/LocalParameter"
        assert props.getSwDataDefProps().getBaseTypeRef().getValue() == "/DataTypes/uint8"
        assert props.getVariableInstance().getAutosarVariableIRef().getPortPrototypeRef().getValue() == "/Swc/DataPort"

    def test_dispatch_absent_wrapper(self, parser):
        """Test that an NvBlockDescriptor without INSTANTIATION-DATA-DEF-PROPSS leaves the aggregation empty."""
        root = AUTOSAR.getInstance().createARPackage("Pkg")
        descriptor = NvBlockDescriptor(root, "NvBlockDesc")
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><SHORT-NAME>NvBlockDesc</SHORT-NAME></ROOT>")

        parser.readNvBlockDescriptor(element, descriptor)

        assert descriptor.getInstantiationDataDefPropss() == []
