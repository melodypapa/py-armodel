"""Writer tests for TlvDataIdDefinitionSet (AUTOSAR_CP_TPS_SystemTemplate, Table 7.30, p.830).

writeARPackageElement dispatch emits TLV-DATA-ID-DEFINITION-SET (XSD element,
AUTOSAR_00052.xsd line 5502). Element order per XSD group TLV-DATA-ID-DEFINITION-SET
(L124842): SHORT-NAME (IDENTIFIABLE) then the optional TLV-DATA-ID-DEFINITIONS
wrapper (minOccurs=0, omitted when the Set is empty) holding TLV-DATA-ID-DEFINITION
choice members.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import TlvDataIdDefinition, TlvDataIdDefinitionSet
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _ref(value, dest):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _make_definition(id_value):
    tlv = TlvDataIdDefinition()
    tlv.setId(PositiveInteger().setValue(id_value))
    return tlv


def _make_package():
    pkg = ARPackage(parent=AUTOSAR.getInstance(), short_name="TlvDataIdDefinitionSets")
    tlv_set = pkg.createTlvDataIdDefinitionSet("MySet")
    first = _make_definition(7)
    first.setTlvArgumentRef(_ref("/PortInterface/op/arg", "ARGUMENT-DATA-PROTOTYPE"))
    second = _make_definition(9)
    second.setTlvRecordElementRef(_ref("/DataType/record", "APPLICATION-RECORD-ELEMENT"))
    tlv_set.addTlvDataIdDefinition(first)
    tlv_set.addTlvDataIdDefinition(second)
    return pkg


class TestTlvDataIdDefinitionSetWriter:
    def test_dispatch_emits_tlv_data_id_definition_set(self):
        pkg = _make_package()
        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(parent, pkg)

        assert len(parent) == 1
        elements_tag = parent[0]
        assert elements_tag.tag == "ELEMENTS"
        assert elements_tag[0].tag == "TLV-DATA-ID-DEFINITION-SET"

    def test_write_element_order_short_name_then_wrapper(self):
        pkg = _make_package()
        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(parent, pkg)

        tlv_set_element = parent[0][0]
        children = list(tlv_set_element)
        assert [c.tag for c in children] == ["SHORT-NAME", "TLV-DATA-ID-DEFINITIONS"]
        assert children[0].text == "MySet"

    def test_write_nested_member_values(self):
        pkg = _make_package()
        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(parent, pkg)

        wrapper = parent[0][0][1]
        definitions = list(wrapper)
        assert len(definitions) == 2
        assert all(d.tag == "TLV-DATA-ID-DEFINITION" for d in definitions)

        first_children = list(definitions[0])
        assert [c.tag for c in first_children] == ["ID", "TLV-ARGUMENT-REF"]
        assert first_children[0].text == "7"
        assert first_children[1].get("DEST") == "ARGUMENT-DATA-PROTOTYPE"
        assert first_children[1].text == "/PortInterface/op/arg"

        second_children = list(definitions[1])
        assert [c.tag for c in second_children] == ["ID", "TLV-RECORD-ELEMENT-REF"]
        assert second_children[0].text == "9"
        assert second_children[1].get("DEST") == "APPLICATION-RECORD-ELEMENT"
        assert second_children[1].text == "/DataType/record"

    def test_write_empty_set_omits_wrapper(self):
        pkg = ARPackage(parent=AUTOSAR.getInstance(), short_name="TlvDataIdDefinitionSets")
        pkg.createTlvDataIdDefinitionSet("EmptySet")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(parent, pkg)

        tlv_set_element = parent[0][0]
        assert tlv_set_element.tag == "TLV-DATA-ID-DEFINITION-SET"
        child_tags = [c.tag for c in tlv_set_element]
        assert "TLV-DATA-ID-DEFINITIONS" not in child_tags
        assert child_tags == ["SHORT-NAME"]

    def test_factory_create_duplicate_returns_existing(self):
        pkg = ARPackage(parent=AUTOSAR.getInstance(), short_name="TlvDataIdDefinitionSets")
        first = pkg.createTlvDataIdDefinitionSet("MySet")
        second = pkg.createTlvDataIdDefinitionSet("MySet")

        assert first is second
        assert isinstance(first, TlvDataIdDefinitionSet)
        assert pkg.getTotalElement() == 1

    def test_write_reparse_round_trip(self):
        pkg = _make_package()
        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(parent, pkg)
        reparsed = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<AR-PACKAGE>", "<AR-PACKAGE xmlns='%s'>" % NS, 1))

        reloaded = ARPackage(parent=AUTOSAR.getInstance(), short_name="TlvDataIdDefinitionSets")
        ARXMLParser().readARPackageElements(reparsed, reloaded)

        tlv_set = reloaded.getElement("MySet", TlvDataIdDefinitionSet)
        assert tlv_set is not None
        assert tlv_set.getShortName() == "MySet"
        definitions = tlv_set.getTlvDataIdDefinitions()
        assert len(definitions) == 2
        assert definitions[0].getId().getValue() == 7
        assert definitions[0].getTlvArgumentRef().getValue() == "/PortInterface/op/arg"
        assert definitions[0].getTlvArgumentRef().getDest() == "ARGUMENT-DATA-PROTOTYPE"
        assert definitions[1].getId().getValue() == 9
        assert definitions[1].getTlvRecordElementRef().getValue() == "/DataType/record"
        assert definitions[1].getTlvRecordElementRef().getDest() == "APPLICATION-RECORD-ELEMENT"
