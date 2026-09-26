"""
Tests for writing ARPackage PORT-INTERFACE-MAPPING-SET elements — Table 4.19 (portInterfaceMapping aggr).

Round-trip counterpart: tests/test_armodel/parser/test_ar_package_port_interface_mapping_set.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeDeclarationGroupPrototypeMapping
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import TriggerMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    ClientServerApplicationErrorMapping,
    ClientServerInterfaceMapping,
    ClientServerOperationMapping,
    DataPrototypeMapping,
    PortInterfaceMappingSet,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    """Create ARXML writer instance."""
    AUTOSAR.getInstance().new()
    return ARXMLWriter()


def _mapping_set() -> PortInterfaceMappingSet:
    AUTOSAR.getInstance().new()
    ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
    return PortInterfaceMappingSet(ar_root, "pims")


def _ref(value: str) -> RefType:
    return RefType().setValue(value)


class TestWritePortInterfaceMappingSet:
    """
    Test writePortInterfaceMappingSet (ARPackage.element, Table 4.19).
    """

    def test_write_field_values(self, writer):
        """
        Test that each created mapping is written under PORT-INTERFACE-MAPPINGS
        with its own tag and SHORT-NAME, in list order.
        """
        mapping_set = _mapping_set()
        mapping_set.createVariableAndParameterInterfaceMapping("vpm")
        mapping_set.createClientServerInterfaceMapping("csim")
        mapping_set.createModeInterfaceMapping("mim")

        element = ET.Element("PARENT")
        writer.writePortInterfaceMappingSet(element, mapping_set)

        set_tag = element.find("PORT-INTERFACE-MAPPING-SET")
        assert set_tag is not None
        assert set_tag.find("SHORT-NAME").text == "pims"

        wrapper = set_tag.find("PORT-INTERFACE-MAPPINGS")
        assert wrapper is not None
        children = list(wrapper)
        assert [c.tag for c in children] == [
            "VARIABLE-AND-PARAMETER-INTERFACE-MAPPING",
            "CLIENT-SERVER-INTERFACE-MAPPING",
            "MODE-INTERFACE-MAPPING",
        ]
        assert [c.find("SHORT-NAME").text for c in children] == ["vpm", "csim", "mim"]

    def test_write_trigger_mapping(self, writer):
        """
        Test that a TriggerInterfaceMapping in the list is written as a
        TRIGGER-INTERFACE-MAPPING element with its TRIGGER-MAPPINGS refs.
        """
        mapping_set = _mapping_set()
        tim = mapping_set.createTriggerInterfaceMapping("tim")

        trigger_mapping = TriggerMapping()
        trigger_mapping.setFirstTriggerRef(_ref("/pkg/trigger1"))
        trigger_mapping.setSecondTriggerRef(_ref("/pkg/trigger2"))
        tim.addTriggerMapping(trigger_mapping)

        element = ET.Element("PARENT")
        writer.writePortInterfaceMappingSet(element, mapping_set)

        wrapper = element.find("PORT-INTERFACE-MAPPING-SET/PORT-INTERFACE-MAPPINGS")
        assert wrapper is not None
        tim_tag = wrapper.find("TRIGGER-INTERFACE-MAPPING")
        assert tim_tag is not None
        assert tim_tag.find("SHORT-NAME").text == "tim"

        trigger_mapping_tag = tim_tag.find("TRIGGER-MAPPINGS/TRIGGER-MAPPING")
        assert trigger_mapping_tag is not None
        assert trigger_mapping_tag.find("FIRST-TRIGGER-REF").text == "/pkg/trigger1"
        assert trigger_mapping_tag.find("SECOND-TRIGGER-REF").text == "/pkg/trigger2"

    def test_write_empty_wrapper_list(self, writer):
        """
        Test that no PORT-INTERFACE-MAPPINGS wrapper is written when the
        mapping list is empty.
        """
        mapping_set = _mapping_set()

        element = ET.Element("PARENT")
        writer.writePortInterfaceMappingSet(element, mapping_set)

        set_tag = element.find("PORT-INTERFACE-MAPPING-SET")
        assert set_tag is not None
        assert set_tag.find("PORT-INTERFACE-MAPPINGS") is None


class TestWriteModeInterfaceMappingModeMapping:
    """
    Test the MODE-MAPPING child of MODE-INTERFACE-MAPPING —
    ModeDeclarationGroupPrototypeMapping (SWC TPS Table 4.27, all attrs 0..1 refs).
    """

    @staticmethod
    def _mode_mapping() -> ModeDeclarationGroupPrototypeMapping:
        mm = ModeDeclarationGroupPrototypeMapping()
        mm.setFirstModeGroupRef(RefType().setValue("/pkg/first").setDest("MODE-GROUP"))
        mm.setModeDeclarationMappingSetRef(RefType().setValue("/pkg/set1").setDest("MODE-DECLARATION-MAPPING-SET"))
        mm.setSecondModeGroupRef(RefType().setValue("/pkg/second").setDest("MODE-GROUP"))
        return mm

    def test_write_mode_mapping_field_values(self, writer):
        """
        Test that all three refs are written with value and DEST, in XSD
        element order (FIRST, MODE-DECLARATION-MAPPING-SET, SECOND).
        """
        mapping_set = _mapping_set()
        mim = mapping_set.createModeInterfaceMapping("mim")
        mim.setModeMapping(self._mode_mapping())

        element = ET.Element("PARENT")
        writer.writePortInterfaceMappingSet(element, mapping_set)

        mm_tag = element.find("PORT-INTERFACE-MAPPING-SET/PORT-INTERFACE-MAPPINGS/MODE-INTERFACE-MAPPING/MODE-MAPPING")
        assert mm_tag is not None
        children = list(mm_tag)
        assert [c.tag for c in children] == [
            "FIRST-MODE-GROUP-REF",
            "MODE-DECLARATION-MAPPING-SET-REF",
            "SECOND-MODE-GROUP-REF",
        ]
        assert children[0].text == "/pkg/first"
        assert children[0].attrib["DEST"] == "MODE-GROUP"
        assert children[1].text == "/pkg/set1"
        assert children[1].attrib["DEST"] == "MODE-DECLARATION-MAPPING-SET"
        assert children[2].text == "/pkg/second"
        assert children[2].attrib["DEST"] == "MODE-GROUP"

    def test_write_mode_mapping_absent_refs(self, writer):
        """
        Test that unset refs emit no elements (0..1) and no MODE-MAPPING is
        written when the mapping itself is absent.
        """
        mapping_set = _mapping_set()
        mim = mapping_set.createModeInterfaceMapping("mim")
        mm = ModeDeclarationGroupPrototypeMapping()
        mm.setFirstModeGroupRef(RefType().setValue("/pkg/first").setDest("MODE-GROUP"))
        mim.setModeMapping(mm)

        mapping_set.createModeInterfaceMapping("mim2")

        element = ET.Element("PARENT")
        writer.writePortInterfaceMappingSet(element, mapping_set)

        wrapper = element.find("PORT-INTERFACE-MAPPING-SET/PORT-INTERFACE-MAPPINGS")
        mim_tag = wrapper.find("MODE-INTERFACE-MAPPING")
        mm_tag = mim_tag.find("MODE-MAPPING")
        assert mm_tag is not None
        assert [c.tag for c in mm_tag] == ["FIRST-MODE-GROUP-REF"]
        assert mm_tag.find("FIRST-MODE-GROUP-REF").text == "/pkg/first"

        mim2_tag = list(wrapper)[1]
        assert mim2_tag.find("MODE-MAPPING") is None

    def test_round_trip_field_values(self, writer):
        """
        Test write → read round-trip preserves all three ref values and DESTs.
        """
        mapping_set = _mapping_set()
        mim = mapping_set.createModeInterfaceMapping("mim")
        mim.setModeMapping(self._mode_mapping())

        parent = ET.Element("PARENT")
        writer.writeModeInterfaceMapping(parent, mim)

        xml_text = ET.tostring(parent, encoding="unicode")
        reparsed = ET.fromstring(xml_text.replace("PARENT", "PARENT xmlns='%s'" % NS, 1))

        mapping_set2 = _mapping_set()
        mim2 = mapping_set2.createModeInterfaceMapping("mim")
        ARXMLParser().readModeInterfaceMapping(reparsed[0], mim2)

        mm2 = mim2.getModeMapping()
        assert isinstance(mm2, ModeDeclarationGroupPrototypeMapping)
        assert mm2.getFirstModeGroupRef().getValue() == "/pkg/first"
        assert mm2.getFirstModeGroupRef().getDest() == "MODE-GROUP"
        assert mm2.getModeDeclarationMappingSetRef().getValue() == "/pkg/set1"
        assert mm2.getModeDeclarationMappingSetRef().getDest() == "MODE-DECLARATION-MAPPING-SET"
        assert mm2.getSecondModeGroupRef().getValue() == "/pkg/second"
        assert mm2.getSecondModeGroupRef().getDest() == "MODE-GROUP"


class TestWriteClientServerInterfaceMappingErrorMappings:
    """
    Test the ERROR-MAPPINGS children of CLIENT-SERVER-INTERFACE-MAPPING —
    ClientServerApplicationErrorMapping (SWC TPS Table 4.25, all attrs 0..1 refs).
    """

    @staticmethod
    def _error_mapping() -> ClientServerApplicationErrorMapping:
        em = ClientServerApplicationErrorMapping()
        em.setFirstApplicationErrorRef(RefType().setValue("/ifc1/err1").setDest("APPLICATION-ERROR"))
        em.setSecondApplicationErrorRef(RefType().setValue("/ifc2/err2").setDest("APPLICATION-ERROR"))
        return em

    def test_write_error_mappings_field_values(self, writer):
        """
        Test that both refs are written with value and DEST, in XSD element
        order (FIRST-APPLICATION-ERROR-REF, SECOND-APPLICATION-ERROR-REF).
        """
        mapping_set = _mapping_set()
        csim = mapping_set.createClientServerInterfaceMapping("csim")
        csim.addErrorMapping(self._error_mapping())

        element = ET.Element("PARENT")
        writer.writePortInterfaceMappingSet(element, mapping_set)

        em_tag = element.find("PORT-INTERFACE-MAPPING-SET/PORT-INTERFACE-MAPPINGS/CLIENT-SERVER-INTERFACE-MAPPING/ERROR-MAPPINGS/CLIENT-SERVER-APPLICATION-ERROR-MAPPING")
        assert em_tag is not None
        children = list(em_tag)
        assert [c.tag for c in children] == [
            "FIRST-APPLICATION-ERROR-REF",
            "SECOND-APPLICATION-ERROR-REF",
        ]
        assert children[0].text == "/ifc1/err1"
        assert children[0].attrib["DEST"] == "APPLICATION-ERROR"
        assert children[1].text == "/ifc2/err2"
        assert children[1].attrib["DEST"] == "APPLICATION-ERROR"

    def test_write_error_mappings_absent_refs(self, writer):
        """
        Test that unset refs emit no elements (0..1) and no ERROR-MAPPINGS
        wrapper is written when the mapping list is empty.
        """
        mapping_set = _mapping_set()
        csim = mapping_set.createClientServerInterfaceMapping("csim")
        em = ClientServerApplicationErrorMapping()
        em.setFirstApplicationErrorRef(RefType().setValue("/ifc1/err1").setDest("APPLICATION-ERROR"))
        csim.addErrorMapping(em)

        mapping_set.createClientServerInterfaceMapping("csim2")

        element = ET.Element("PARENT")
        writer.writePortInterfaceMappingSet(element, mapping_set)

        wrapper = element.find("PORT-INTERFACE-MAPPING-SET/PORT-INTERFACE-MAPPINGS")
        csim_tag = wrapper.find("CLIENT-SERVER-INTERFACE-MAPPING")
        em_tag = csim_tag.find("ERROR-MAPPINGS/CLIENT-SERVER-APPLICATION-ERROR-MAPPING")
        assert em_tag is not None
        assert [c.tag for c in em_tag] == ["FIRST-APPLICATION-ERROR-REF"]
        assert em_tag.find("FIRST-APPLICATION-ERROR-REF").text == "/ifc1/err1"

        csim2_tag = list(wrapper)[1]
        assert csim2_tag.find("ERROR-MAPPINGS") is None

    def test_round_trip_field_values(self, writer):
        """
        Test write → read round-trip preserves both ref values and DESTs.
        """
        mapping_set = _mapping_set()
        csim = mapping_set.createClientServerInterfaceMapping("csim")
        csim.addErrorMapping(self._error_mapping())

        parent = ET.Element("PARENT")
        writer.writeClientServerInterfaceMapping(parent, csim)

        xml_text = ET.tostring(parent, encoding="unicode")
        reparsed = ET.fromstring(xml_text.replace("PARENT", "PARENT xmlns='%s'" % NS, 1))

        mapping_set2 = _mapping_set()
        csim2 = mapping_set2.createClientServerInterfaceMapping("csim")
        ARXMLParser().readClientServerInterfaceMapping(reparsed[0], csim2)

        error_mappings = csim2.getErrorMappings()
        assert len(error_mappings) == 1
        em2 = error_mappings[0]
        assert isinstance(em2, ClientServerApplicationErrorMapping)
        assert em2.getFirstApplicationErrorRef().getValue() == "/ifc1/err1"
        assert em2.getFirstApplicationErrorRef().getDest() == "APPLICATION-ERROR"
        assert em2.getSecondApplicationErrorRef().getValue() == "/ifc2/err2"
        assert em2.getSecondApplicationErrorRef().getDest() == "APPLICATION-ERROR"


class TestWriteClientServerInterfaceMappingOperationMappings:
    """
    Test the OPERATION-MAPPINGS children of CLIENT-SERVER-INTERFACE-MAPPING —
    ClientServerOperationMapping (SWC TPS Table 4.24; argumentMapping `*` aggr
    under the ARGUMENT-MAPPINGS wrapper + three 0..1 refs).
    """

    @staticmethod
    def _argument_mapping(first: str, second: str) -> DataPrototypeMapping:
        am = DataPrototypeMapping()
        am.setFirstDataPrototypeRef(RefType().setValue(first).setDest("ARGUMENT-DATA-PROTOTYPE"))
        am.setSecondDataPrototypeRef(RefType().setValue(second).setDest("ARGUMENT-DATA-PROTOTYPE"))
        return am

    @staticmethod
    def _operation_mapping() -> ClientServerOperationMapping:
        om = ClientServerOperationMapping()
        om.addArgumentMapping(TestWriteClientServerInterfaceMappingOperationMappings._argument_mapping("/ifc1/op1/arg1", "/ifc2/op2/arg2"))
        om.setFirstOperationRef(RefType().setValue("/ifc1/op1").setDest("CLIENT-SERVER-OPERATION"))
        om.setFirstToSecondDataTransformationRef(RefType().setValue("/pkg/trans1").setDest("DATA-TRANSFORMATION"))
        om.setSecondOperationRef(RefType().setValue("/ifc2/op2").setDest("CLIENT-SERVER-OPERATION"))
        return om

    def test_write_operation_mapping_field_values(self, writer):
        """
        Test that the ARGUMENT-MAPPINGS items and all three refs are written with
        value and DEST, in XSD element order (ARGUMENT-MAPPINGS, FIRST-OPERATION-REF,
        FIRST-TO-SECOND-DATA-TRANSFORMATION-REF, SECOND-OPERATION-REF).
        """
        mapping_set = _mapping_set()
        csim = mapping_set.createClientServerInterfaceMapping("csim")
        csim.addOperationMapping(self._operation_mapping())

        element = ET.Element("PARENT")
        writer.writePortInterfaceMappingSet(element, mapping_set)

        om_tag = element.find("PORT-INTERFACE-MAPPING-SET/PORT-INTERFACE-MAPPINGS/CLIENT-SERVER-INTERFACE-MAPPING/OPERATION-MAPPINGS/CLIENT-SERVER-OPERATION-MAPPING")
        assert om_tag is not None
        children = [c.tag for c in om_tag]
        assert children == [
            "ARGUMENT-MAPPINGS",
            "FIRST-OPERATION-REF",
            "FIRST-TO-SECOND-DATA-TRANSFORMATION-REF",
            "SECOND-OPERATION-REF",
        ]
        items = om_tag.find("ARGUMENT-MAPPINGS").findall("DATA-PROTOTYPE-MAPPING")
        assert len(items) == 1
        assert items[0].find("FIRST-DATA-PROTOTYPE-REF").text == "/ifc1/op1/arg1"
        assert items[0].find("FIRST-DATA-PROTOTYPE-REF").attrib["DEST"] == "ARGUMENT-DATA-PROTOTYPE"
        assert items[0].find("SECOND-DATA-PROTOTYPE-REF").text == "/ifc2/op2/arg2"
        assert om_tag.find("FIRST-OPERATION-REF").text == "/ifc1/op1"
        assert om_tag.find("FIRST-OPERATION-REF").attrib["DEST"] == "CLIENT-SERVER-OPERATION"
        assert om_tag.find("FIRST-TO-SECOND-DATA-TRANSFORMATION-REF").text == "/pkg/trans1"
        assert om_tag.find("FIRST-TO-SECOND-DATA-TRANSFORMATION-REF").attrib["DEST"] == "DATA-TRANSFORMATION"
        assert om_tag.find("SECOND-OPERATION-REF").text == "/ifc2/op2"
        assert om_tag.find("SECOND-OPERATION-REF").attrib["DEST"] == "CLIENT-SERVER-OPERATION"

    def test_write_operation_mappings_absent_refs(self, writer):
        """
        Test that unset refs emit no elements (0..1), no ARGUMENT-MAPPINGS wrapper
        is written when the list is empty, and no OPERATION-MAPPINGS wrapper is
        written when the mapping list is empty.
        """
        mapping_set = _mapping_set()
        csim = mapping_set.createClientServerInterfaceMapping("csim")
        om = ClientServerOperationMapping()
        om.setFirstOperationRef(RefType().setValue("/ifc1/op1").setDest("CLIENT-SERVER-OPERATION"))
        csim.addOperationMapping(om)

        mapping_set.createClientServerInterfaceMapping("csim2")

        element = ET.Element("PARENT")
        writer.writePortInterfaceMappingSet(element, mapping_set)

        wrapper = element.find("PORT-INTERFACE-MAPPING-SET/PORT-INTERFACE-MAPPINGS")
        csim_tag = wrapper.find("CLIENT-SERVER-INTERFACE-MAPPING")
        om_tag = csim_tag.find("OPERATION-MAPPINGS/CLIENT-SERVER-OPERATION-MAPPING")
        assert om_tag is not None
        assert [c.tag for c in om_tag] == ["FIRST-OPERATION-REF"]
        assert om_tag.find("ARGUMENT-MAPPINGS") is None
        assert om_tag.find("FIRST-OPERATION-REF").text == "/ifc1/op1"

        csim2_tag = list(wrapper)[1]
        assert csim2_tag.find("OPERATION-MAPPINGS") is None

    def test_round_trip_field_values(self, writer):
        """
        Test write → read round-trip preserves the argument mappings and all
        three ref values and DESTs.
        """
        mapping_set = _mapping_set()
        csim = mapping_set.createClientServerInterfaceMapping("csim")
        csim.addOperationMapping(self._operation_mapping())

        parent = ET.Element("PARENT")
        writer.writeClientServerInterfaceMapping(parent, csim)

        xml_text = ET.tostring(parent, encoding="unicode")
        reparsed = ET.fromstring(xml_text.replace("PARENT", "PARENT xmlns='%s'" % NS, 1))

        mapping_set2 = _mapping_set()
        csim2 = mapping_set2.createClientServerInterfaceMapping("csim")
        ARXMLParser().readClientServerInterfaceMapping(reparsed[0], csim2)

        operation_mappings = csim2.getOperationMappings()
        assert len(operation_mappings) == 1
        om2 = operation_mappings[0]
        assert isinstance(om2, ClientServerOperationMapping)
        argument_mappings = om2.getArgumentMappings()
        assert len(argument_mappings) == 1
        assert isinstance(argument_mappings[0], DataPrototypeMapping)
        assert argument_mappings[0].getFirstDataPrototypeRef().getValue() == "/ifc1/op1/arg1"
        assert argument_mappings[0].getFirstDataPrototypeRef().getDest() == "ARGUMENT-DATA-PROTOTYPE"
        assert argument_mappings[0].getSecondDataPrototypeRef().getValue() == "/ifc2/op2/arg2"
        assert om2.getFirstOperationRef().getValue() == "/ifc1/op1"
        assert om2.getFirstOperationRef().getDest() == "CLIENT-SERVER-OPERATION"
        assert om2.getFirstToSecondDataTransformationRef().getValue() == "/pkg/trans1"
        assert om2.getFirstToSecondDataTransformationRef().getDest() == "DATA-TRANSFORMATION"
        assert om2.getSecondOperationRef().getValue() == "/ifc2/op2"
        assert om2.getSecondOperationRef().getDest() == "CLIENT-SERVER-OPERATION"


class TestWriteClientServerInterfaceMapping:
    """Class-level orchestrator (Table 4.23): wrappers in XSD order, SHORT-NAME, omission when empty, round-trip."""

    def _make_mapping(self):
        mapping_set = _mapping_set()
        csim = mapping_set.createClientServerInterfaceMapping("csim")

        error_mapping = ClientServerApplicationErrorMapping()
        first_error = RefType()
        first_error.setDest("APPLICATION-ERROR")
        first_error.setValue("/Ifc1/E1")
        error_mapping.setFirstApplicationErrorRef(first_error)
        second_error = RefType()
        second_error.setDest("APPLICATION-ERROR")
        second_error.setValue("/Ifc2/E2")
        error_mapping.setSecondApplicationErrorRef(second_error)
        csim.addErrorMapping(error_mapping)

        operation_mapping = ClientServerOperationMapping()
        first_op = RefType()
        first_op.setDest("CLIENT-SERVER-OPERATION")
        first_op.setValue("/Ifc1/Op1")
        operation_mapping.setFirstOperationRef(first_op)
        second_op = RefType()
        second_op.setDest("CLIENT-SERVER-OPERATION")
        second_op.setValue("/Ifc2/Op2")
        operation_mapping.setSecondOperationRef(second_op)
        csim.addOperationMapping(operation_mapping)
        return mapping_set, csim

    def test_write_field_values_in_xsd_order(self, writer):
        _, csim = self._make_mapping()

        element = ET.Element("PARENT")
        ARXMLWriter().writeClientServerInterfaceMapping(element, csim)

        written = element.find("CLIENT-SERVER-INTERFACE-MAPPING")
        assert written is not None
        assert written.find("SHORT-NAME").text == "csim"
        children = [child.tag for child in written]
        assert children.index("ERROR-MAPPINGS") < children.index("OPERATION-MAPPINGS")
        assert written.find("ERROR-MAPPINGS/CLIENT-SERVER-APPLICATION-ERROR-MAPPING/FIRST-APPLICATION-ERROR-REF").text == "/Ifc1/E1"
        assert written.find("ERROR-MAPPINGS/CLIENT-SERVER-APPLICATION-ERROR-MAPPING/SECOND-APPLICATION-ERROR-REF").text == "/Ifc2/E2"
        assert written.find("OPERATION-MAPPINGS/CLIENT-SERVER-OPERATION-MAPPING/FIRST-OPERATION-REF").text == "/Ifc1/Op1"
        assert written.find("OPERATION-MAPPINGS/CLIENT-SERVER-OPERATION-MAPPING/SECOND-OPERATION-REF").text == "/Ifc2/Op2"

    def test_write_empty_mapping_omits_wrappers(self, writer):
        mapping_set = _mapping_set()
        csim = mapping_set.createClientServerInterfaceMapping("csim")

        element = ET.Element("PARENT")
        ARXMLWriter().writeClientServerInterfaceMapping(element, csim)

        written = element.find("CLIENT-SERVER-INTERFACE-MAPPING")
        assert written is not None
        assert written.find("ERROR-MAPPINGS") is None
        assert written.find("OPERATION-MAPPINGS") is None

    def test_round_trip_field_values(self, writer):
        mapping_set, _ = self._make_mapping()

        element = ET.Element("PARENT")
        ARXMLWriter().writeClientServerInterfaceMapping(element, mapping_set.getPortInterfaceMappings()[0])

        xml_str = ET.tostring(element).decode().replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1)
        reparsed = ET.fromstring(xml_str)

        read_back = ClientServerInterfaceMapping(mapping_set, "csim")
        ARXMLParser().readClientServerInterfaceMapping(reparsed.find("{%s}CLIENT-SERVER-INTERFACE-MAPPING" % NS), read_back)

        assert read_back.getShortName() == "csim"
        assert len(read_back.getErrorMappings()) == 1
        assert read_back.getErrorMappings()[0].getFirstApplicationErrorRef().getValue() == "/Ifc1/E1"
        assert len(read_back.getOperationMappings()) == 1
        assert read_back.getOperationMappings()[0].getSecondOperationRef().getValue() == "/Ifc2/Op2"
