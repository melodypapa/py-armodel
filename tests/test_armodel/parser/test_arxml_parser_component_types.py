"""Tests for the AtomicSwComponentType subclass parser handlers.

Covers the reader handlers for EcuAbstractionSwComponentType,
ComplexDeviceDriverSwComponentType, SensorActuatorSwComponentType,
NvBlockSwComponentType and ServiceProxySwComponentType plus their
ARPackage-level dispatch.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

NS = "http://autosar.org/schema/r4.0"


def _snip(inner: str, root_tag: str = "ROOT") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


def _dispatch(parser, parent, inner_xml: str) -> None:
    xml = f"<AR-PACKAGE xmlns='{NS}'><SHORT-NAME>Pkg</SHORT-NAME><ELEMENTS>{inner_xml}</ELEMENTS></AR-PACKAGE>"
    parser.readARPackageElements(ET.fromstring(xml), parent)


class TestEcuAbstractionSwComponentTypeHandlers:
    """Exercise the EcuAbstractionSwComponentType reader handler."""

    def test_read_hardware_element_refs_full(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import EcuAbstractionSwComponentType

        root = AUTOSAR.getInstance().createARPackage("Pkg")
        swc = EcuAbstractionSwComponentType(root, "EcuAbstraction")
        element = _snip(
            "<SHORT-NAME>EcuAbstraction</SHORT-NAME>" "<HARDWARE-ELEMENT-REFS><HARDWARE-ELEMENT-REF DEST='HW-DESCRIPTION-ENTITY'>/Hw/Ecu</HARDWARE-ELEMENT-REF></HARDWARE-ELEMENT-REFS>",
            root_tag="ECU-ABSTRACTION-SW-COMPONENT-TYPE",
        )
        parser.readEcuAbstractionSwComponentType(element, swc)
        refs = swc.getHardwareElementRefs()
        assert len(refs) == 1
        assert refs[0].getValue() == "/Hw/Ecu"
        assert refs[0].getDest() == "HW-DESCRIPTION-ENTITY"

    def test_read_hardware_element_refs_minimal(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import EcuAbstractionSwComponentType

        root = AUTOSAR.getInstance().createARPackage("Pkg")
        swc = EcuAbstractionSwComponentType(root, "EcuAbstraction")
        parser.readEcuAbstractionSwComponentType(_snip("<SHORT-NAME>EcuAbstraction</SHORT-NAME>"), swc)
        assert swc.getHardwareElementRefs() == []

    def test_dispatch(self, parser):
        parent = AUTOSAR.getInstance().createARPackage("Pkg")
        _dispatch(parser, parent, "<ECU-ABSTRACTION-SW-COMPONENT-TYPE><SHORT-NAME>E1</SHORT-NAME></ECU-ABSTRACTION-SW-COMPONENT-TYPE>")
        assert len(parent.getSwComponentTypes()) == 1


class TestComplexDeviceDriverSwComponentTypeHandlers:
    """Exercise the ComplexDeviceDriverSwComponentType reader handler."""

    def test_read_hardware_element_refs_full(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import ComplexDeviceDriverSwComponentType

        root = AUTOSAR.getInstance().createARPackage("Pkg")
        swc = ComplexDeviceDriverSwComponentType(root, "Cdd")
        element = _snip(
            "<SHORT-NAME>Cdd</SHORT-NAME>" "<HARDWARE-ELEMENT-REFS><HARDWARE-ELEMENT-REF DEST='HW-DESCRIPTION-ENTITY'>/Hw/Cdd</HARDWARE-ELEMENT-REF></HARDWARE-ELEMENT-REFS>",
            root_tag="COMPLEX-DEVICE-DRIVER-SW-COMPONENT-TYPE",
        )
        parser.readComplexDeviceDriverSwComponentType(element, swc)
        refs = swc.getHardwareElementRefs()
        assert len(refs) == 1
        assert refs[0].getValue() == "/Hw/Cdd"

    def test_dispatch(self, parser):
        parent = AUTOSAR.getInstance().createARPackage("Pkg")
        _dispatch(parser, parent, "<COMPLEX-DEVICE-DRIVER-SW-COMPONENT-TYPE><SHORT-NAME>CDD1</SHORT-NAME></COMPLEX-DEVICE-DRIVER-SW-COMPONENT-TYPE>")
        assert len(parent.getComplexDeviceDriverSwComponentTypes()) == 1


class TestSensorActuatorSwComponentTypeHandlers:
    """Exercise the SensorActuatorSwComponentType reader handler."""

    def test_read_sensor_actuator_ref_full(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import SensorActuatorSwComponentType

        root = AUTOSAR.getInstance().createARPackage("Pkg")
        swc = SensorActuatorSwComponentType(root, "Sensor")
        element = _snip(
            "<SHORT-NAME>Sensor</SHORT-NAME>" "<SENSOR-ACTUATOR-REF DEST='HW-DESCRIPTION-ENTITY'>/Hw/Sensor</SENSOR-ACTUATOR-REF>",
            root_tag="SENSOR-ACTUATOR-SW-COMPONENT-TYPE",
        )
        parser.readSensorActuatorSwComponentType(element, swc)
        ref = swc.getSensorActuatorRef()
        assert ref is not None
        assert ref.getValue() == "/Hw/Sensor"
        assert ref.getDest() == "HW-DESCRIPTION-ENTITY"

    def test_read_sensor_actuator_ref_minimal(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import SensorActuatorSwComponentType

        root = AUTOSAR.getInstance().createARPackage("Pkg")
        swc = SensorActuatorSwComponentType(root, "Sensor")
        parser.readSensorActuatorSwComponentType(_snip("<SHORT-NAME>Sensor</SHORT-NAME>"), swc)
        assert swc.getSensorActuatorRef() is None

    def test_dispatch(self, parser):
        parent = AUTOSAR.getInstance().createARPackage("Pkg")
        _dispatch(parser, parent, "<SENSOR-ACTUATOR-SW-COMPONENT-TYPE><SHORT-NAME>SA1</SHORT-NAME></SENSOR-ACTUATOR-SW-COMPONENT-TYPE>")
        assert len(parent.getSensorActuatorSwComponentType()) == 1


class TestServiceProxySwComponentTypeHandlers:
    """Exercise the ServiceProxySwComponentType reader handler and dispatch."""

    def test_dispatch(self, parser):
        parent = AUTOSAR.getInstance().createARPackage("Pkg")
        _dispatch(parser, parent, "<SERVICE-PROXY-SW-COMPONENT-TYPE><SHORT-NAME>SP1</SHORT-NAME></SERVICE-PROXY-SW-COMPONENT-TYPE>")
        assert len(parent.getSwComponentTypes()) == 1
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import ServiceProxySwComponentType

        assert isinstance(parent.getSwComponentTypes()[0], ServiceProxySwComponentType)


class TestNvBlockSwComponentTypeHandlers:
    """Exercise the NvBlockSwComponentType reader handler and dispatch."""

    def test_read_full(self, parser):
        root = AUTOSAR.getInstance().createARPackage("Pkg")
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import NvBlockSwComponentType

        swc = NvBlockSwComponentType(root, "NvBlockComp")
        element = _snip(
            "<SHORT-NAME>NvBlockComp</SHORT-NAME>"
            "<BULK-NV-DATA-DESCRIPTORS><BULK-NV-DATA-DESCRIPTOR><SHORT-NAME>BulkDesc</SHORT-NAME></BULK-NV-DATA-DESCRIPTOR></BULK-NV-DATA-DESCRIPTORS>"
            "<NV-BLOCK-DESCRIPTORS><NV-BLOCK-DESCRIPTOR><SHORT-NAME>BlockDesc</SHORT-NAME><SUPPORT-DIRTY-FLAG>true</SUPPORT-DIRTY-FLAG></NV-BLOCK-DESCRIPTOR></NV-BLOCK-DESCRIPTORS>",
            root_tag="NV-BLOCK-SW-COMPONENT-TYPE",
        )
        parser.readNvBlockSwComponentType(element, swc)
        bulk_descriptors = swc.getBulkNvDataDescriptors()
        assert len(bulk_descriptors) == 1
        assert bulk_descriptors[0].getShortName() == "BulkDesc"
        nv_descriptors = swc.getNvBlockDescriptors()
        assert len(nv_descriptors) == 1
        assert nv_descriptors[0].getShortName() == "BlockDesc"
        assert nv_descriptors[0].getSupportDirtyFlag().getValue() is True

    def test_read_minimal(self, parser):
        root = AUTOSAR.getInstance().createARPackage("Pkg")
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import NvBlockSwComponentType

        swc = NvBlockSwComponentType(root, "NvBlockComp")
        parser.readNvBlockSwComponentType(_snip("<SHORT-NAME>NvBlockComp</SHORT-NAME>"), swc)
        assert swc.getBulkNvDataDescriptors() == []
        assert swc.getNvBlockDescriptors() == []

    def test_dispatch(self, parser):
        parent = AUTOSAR.getInstance().createARPackage("Pkg")
        _dispatch(
            parser,
            parent,
            "<NV-BLOCK-SW-COMPONENT-TYPE><SHORT-NAME>NV1</SHORT-NAME>"
            "<NV-BLOCK-DESCRIPTORS><NV-BLOCK-DESCRIPTOR><SHORT-NAME>D1</SHORT-NAME></NV-BLOCK-DESCRIPTOR></NV-BLOCK-DESCRIPTORS>"
            "</NV-BLOCK-SW-COMPONENT-TYPE>",
        )
        assert len(parent.getSwComponentTypes()) == 1
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import NvBlockSwComponentType

        swc = parent.getSwComponentTypes()[0]
        assert isinstance(swc, NvBlockSwComponentType)
        assert len(swc.getNvBlockDescriptors()) == 1
