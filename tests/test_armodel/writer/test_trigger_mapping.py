"""
Tests for writing TRIGGER-MAPPING elements (TriggerMapping, Table 4.31) via
the TriggerInterfaceMapping TRIGGER-MAPPINGS wrapper.

Round-trip counterpart: tests/test_armodel/parser/test_trigger_mapping.py
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import TriggerMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import TriggerInterfaceMapping
from armodel.writer.arxml_writer import ARXMLWriter


def _ref(value: str, dest: str = "TRIGGER") -> RefType:
    ref = RefType().setValue(value)
    ref.setDest(dest)
    return ref


class TestWriteTriggerMapping:
    """
    Test TriggerMapping ref emission via writeTriggerInterfaceMapping (Table 4.31).
    """

    def _mapping_with_refs(self) -> TriggerInterfaceMapping:
        AUTOSAR.getInstance().new()
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        pims = ar_root.createPortInterfaceMappingSet("Pims")
        tim = pims.createTriggerInterfaceMapping("tim")

        trigger_mapping = TriggerMapping()
        trigger_mapping.setFirstTriggerRef(_ref("/pkg/trigger1"))
        trigger_mapping.setSecondTriggerRef(_ref("/pkg/trigger2"))
        tim.setTriggerMapping([trigger_mapping])
        return tim

    def test_write_field_values(self):
        """Test that both refs are written in XSD order with DEST and values."""
        writer = ARXMLWriter()
        tim = self._mapping_with_refs()

        element = ET.Element("PARENT")
        writer.writeTriggerInterfaceMapping(element, tim)

        tim_tag = element.find("TRIGGER-INTERFACE-MAPPING")
        assert tim_tag is not None
        assert tim_tag.find("SHORT-NAME").text == "tim"

        wrapper = tim_tag.find("TRIGGER-MAPPINGS")
        assert wrapper is not None

        children = list(wrapper)
        assert len(children) == 1
        assert children[0].tag == "TRIGGER-MAPPING"

        mapping_tag = children[0]
        ref_tags = list(mapping_tag)
        assert [t.tag for t in ref_tags] == ["FIRST-TRIGGER-REF", "SECOND-TRIGGER-REF"]
        assert ref_tags[0].attrib["DEST"] == "TRIGGER"
        assert ref_tags[0].text == "/pkg/trigger1"
        assert ref_tags[1].attrib["DEST"] == "TRIGGER"
        assert ref_tags[1].text == "/pkg/trigger2"

    def test_write_absent_refs(self):
        """Test that a TriggerMapping without refs emits a TRIGGER-MAPPING element with no ref children."""
        writer = ARXMLWriter()
        AUTOSAR.getInstance().new()
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        pims = ar_root.createPortInterfaceMappingSet("Pims")
        tim = pims.createTriggerInterfaceMapping("tim")
        tim.setTriggerMapping([TriggerMapping()])

        element = ET.Element("PARENT")
        writer.writeTriggerInterfaceMapping(element, tim)

        mapping_tag = element.find("TRIGGER-INTERFACE-MAPPING/TRIGGER-MAPPINGS/TRIGGER-MAPPING")
        assert mapping_tag is not None
        assert mapping_tag.find("FIRST-TRIGGER-REF") is None
        assert mapping_tag.find("SECOND-TRIGGER-REF") is None

    def test_write_empty_wrapper_list(self):
        """Test that no TRIGGER-MAPPINGS wrapper is written when the list is empty."""
        writer = ARXMLWriter()
        AUTOSAR.getInstance().new()
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        pims = ar_root.createPortInterfaceMappingSet("Pims")
        tim = pims.createTriggerInterfaceMapping("tim")

        element = ET.Element("PARENT")
        writer.writeTriggerInterfaceMapping(element, tim)

        tim_tag = element.find("TRIGGER-INTERFACE-MAPPING")
        assert tim_tag is not None
        assert tim_tag.find("TRIGGER-MAPPINGS") is None
