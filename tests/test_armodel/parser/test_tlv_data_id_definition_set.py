"""Parser tests for TlvDataIdDefinitionSet (AUTOSAR_CP_TPS_SystemTemplate, Table 7.30, p.830).

Top-level ARElement aggregated by ARPackage.element — dispatched through the
readARPackageElements ELEMENTS loop (XSD element TLV-DATA-ID-DEFINITION-SET,
AUTOSAR_00052.xsd line 5502). Member wrapper TLV-DATA-ID-DEFINITIONS holds an
unbounded choice of TLV-DATA-ID-DEFINITION elements (XSD group L124842).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import TlvDataIdDefinition, TlvDataIdDefinitionSet
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _fragment():
    return (
        "<AR-PACKAGE xmlns='%s'>"
        "<SHORT-NAME>TlvDataIdDefinitionSets</SHORT-NAME>"
        "<ELEMENTS>"
        "<TLV-DATA-ID-DEFINITION-SET>"
        "<SHORT-NAME>MySet</SHORT-NAME>"
        "<TLV-DATA-ID-DEFINITIONS>"
        "<TLV-DATA-ID-DEFINITION>"
        "<ID>7</ID>"
        '<TLV-ARGUMENT-REF DEST="ARGUMENT-DATA-PROTOTYPE">/PortInterface/op/arg</TLV-ARGUMENT-REF>'
        "</TLV-DATA-ID-DEFINITION>"
        "<TLV-DATA-ID-DEFINITION>"
        "<ID>9</ID>"
        '<TLV-RECORD-ELEMENT-REF DEST="APPLICATION-RECORD-ELEMENT">/DataType/record</TLV-RECORD-ELEMENT-REF>'
        "</TLV-DATA-ID-DEFINITION>"
        "</TLV-DATA-ID-DEFINITIONS>"
        "</TLV-DATA-ID-DEFINITION-SET>"
        "</ELEMENTS>"
        "</AR-PACKAGE>" % NS
    )


class TestTlvDataIdDefinitionSetParser:
    def test_dispatch_creates_tlv_data_id_definition_set_on_package(self):
        pkg = ARPackage(parent=AUTOSAR.getInstance(), short_name="TlvDataIdDefinitionSets")
        pkg_element = ET.fromstring(_fragment())
        ARXMLParser().readARPackageElements(pkg_element, pkg)

        created = pkg.getElement("MySet", TlvDataIdDefinitionSet)
        assert created is not None
        assert isinstance(created, TlvDataIdDefinitionSet)
        assert created.getShortName() == "MySet"

    def test_parse_asserts_member_field_values(self):
        pkg = ARPackage(parent=AUTOSAR.getInstance(), short_name="TlvDataIdDefinitionSets")
        pkg_element = ET.fromstring(_fragment())
        ARXMLParser().readARPackageElements(pkg_element, pkg)

        tlv_set = pkg.getElement("MySet", TlvDataIdDefinitionSet)
        definitions = tlv_set.getTlvDataIdDefinitions()
        assert len(definitions) == 2
        assert isinstance(definitions[0], TlvDataIdDefinition)
        assert definitions[0].getId().getValue() == 7
        assert definitions[0].getTlvArgumentRef().getValue() == "/PortInterface/op/arg"
        assert definitions[0].getTlvArgumentRef().getDest() == "ARGUMENT-DATA-PROTOTYPE"
        assert definitions[1].getId().getValue() == 9
        assert definitions[1].getTlvRecordElementRef().getValue() == "/DataType/record"
        assert definitions[1].getTlvRecordElementRef().getDest() == "APPLICATION-RECORD-ELEMENT"

    def test_parse_optional_wrapper_absent(self):
        xml = (
            "<AR-PACKAGE xmlns='%s'>"
            "<SHORT-NAME>TlvDataIdDefinitionSets</SHORT-NAME>"
            "<ELEMENTS>"
            "<TLV-DATA-ID-DEFINITION-SET><SHORT-NAME>EmptySet</SHORT-NAME></TLV-DATA-ID-DEFINITION-SET>"
            "</ELEMENTS>"
            "</AR-PACKAGE>" % NS
        )
        pkg = ARPackage(parent=AUTOSAR.getInstance(), short_name="TlvDataIdDefinitionSets")
        ARXMLParser().readARPackageElements(ET.fromstring(xml), pkg)

        tlv_set = pkg.getElement("EmptySet", TlvDataIdDefinitionSet)
        assert tlv_set is not None
        assert tlv_set.getTlvDataIdDefinitions() == []

    def test_factory_create_duplicate_returns_existing(self):
        pkg = ARPackage(parent=AUTOSAR.getInstance(), short_name="TlvDataIdDefinitionSets")
        first = pkg.createTlvDataIdDefinitionSet("MySet")
        second = pkg.createTlvDataIdDefinitionSet("MySet")

        assert first is second
        assert pkg.getTotalElement() == 1
