"""Parser tests for SenderReceiverInterface (SWCT Table 4.1)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    MetaDataItemSet,
    SenderReceiverInterface,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser()


def _sr_interface() -> SenderReceiverInterface:
    AUTOSAR.getInstance().new()
    ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
    return SenderReceiverInterface(ar_root, "sr_iface")


class TestReadSenderReceiverInterface:
    def test_read_all_three_aggregations(self, parser):
        sr_interface = _sr_interface()
        element = ET.fromstring(
            f"""<SENDER-RECEIVER-INTERFACE xmlns='{NS}'>
                <SHORT-NAME>SR</SHORT-NAME>
                <DATA-ELEMENTS>
                    <VARIABLE-DATA-PROTOTYPE>
                        <SHORT-NAME>de1</SHORT-NAME>
                    </VARIABLE-DATA-PROTOTYPE>
                </DATA-ELEMENTS>
                <INVALIDATION-POLICYS>
                    <INVALIDATION-POLICY>
                        <DATA-ELEMENT-REF DEST='VARIABLE-DATA-PROTOTYPE'>/AUTOSAR/SR/de1</DATA-ELEMENT-REF>
                        <HANDLE-INVALID>DISABLE</HANDLE-INVALID>
                    </INVALIDATION-POLICY>
                </INVALIDATION-POLICYS>
                <META-DATA-ITEM-SETS>
                    <META-DATA-ITEM-SET>
                        <DATA-ELEMENT-REFS>
                            <DATA-ELEMENT-REF DEST='VARIABLE-DATA-PROTOTYPE'>/AUTOSAR/SR/de1</DATA-ELEMENT-REF>
                        </DATA-ELEMENT-REFS>
                    </META-DATA-ITEM-SET>
                </META-DATA-ITEM-SETS>
            </SENDER-RECEIVER-INTERFACE>"""
        )

        parser.readSenderReceiverInterface(element, sr_interface)

        elements = sr_interface.getDataElements()
        assert len(elements) == 1
        assert elements[0].getShortName() == "de1"

        policies = sr_interface.getInvalidationPolicies()
        assert len(policies) == 1
        assert policies[0].getDataElementRef().getValue() == "/AUTOSAR/SR/de1"
        assert policies[0].getHandleInvalid().getValue() == "DISABLE"

        sets = sr_interface.getMetaDataItemSets()
        assert len(sets) == 1
        assert isinstance(sets[0], MetaDataItemSet)
        assert sets[0].getDataElementRefs()[0].getValue() == "/AUTOSAR/SR/de1"

    def test_read_empty_wrapper_list(self, parser):
        sr_interface = _sr_interface()
        element = ET.fromstring(f"<SENDER-RECEIVER-INTERFACE xmlns='{NS}'><SHORT-NAME>SR</SHORT-NAME></SENDER-RECEIVER-INTERFACE>")

        parser.readSenderReceiverInterface(element, sr_interface)

        assert sr_interface.getDataElements() == []
        assert sr_interface.getInvalidationPolicies() == []
        assert sr_interface.getMetaDataItemSets() == []
