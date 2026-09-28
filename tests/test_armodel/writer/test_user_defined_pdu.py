"""Writer tests for UserDefinedPdu (AUTOSAR_CP_TPS_SystemTemplate, Table 6.27, p.345).

writeUserDefinedPdu emits the XSD complexType USER-DEFINED-PDU
(00052.xsd line 128955): the PDU group via the writePdu base helper first
(LENGTH from the PDU group), then the own group's CDD-TYPE (String, 0..1,
omitted when None); no VARIATION-POINT.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR as AutosarDocument
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import UserDefinedPdu
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _length(value):
    number = Integer()
    number.setValue(value)
    return number


def _cdd_type(value):
    text = String()
    text.setValue(value)
    return text


def _new_package(with_cdd_type=True):
    pkg = ARPackage(parent=AutosarDocument.getInstance(), short_name="Pdus")
    pdu = pkg.createUserDefinedPdu("UDPdu")
    pdu.setLength(_length(8))
    if with_cdd_type:
        pdu.setCddType(_cdd_type("ComplexDriverCdd"))
    return pkg


class TestUserDefinedPduWriter:
    def test_write_content_in_xsd_order(self):
        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(parent, _new_package())

        node = parent.find("ELEMENTS/USER-DEFINED-PDU")
        assert node is not None
        children = [child.tag for child in node]
        assert children.index("LENGTH") < children.index("CDD-TYPE")
        assert node.find("SHORT-NAME").text == "UDPdu"
        assert node.find("LENGTH").text == "8"
        assert node.find("CDD-TYPE").text == "ComplexDriverCdd"

    def test_write_none_cdd_type_is_omitted(self):
        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(parent, _new_package(with_cdd_type=False))

        node = parent.find("ELEMENTS/USER-DEFINED-PDU")
        assert node.find("CDD-TYPE") is None
        assert node.find("LENGTH").text == "8"

    def test_write_reparse_round_trip_preserves_values(self):
        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(parent, _new_package())
        reparsed = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<AR-PACKAGE>", "<AR-PACKAGE xmlns='%s'>" % NS, 1))

        reloaded = ARPackage(parent=AutosarDocument.getInstance(), short_name="Pdus")
        ARXMLParser().readARPackageElements(reparsed, reloaded)

        pdu = reloaded.getElement("UDPdu", UserDefinedPdu)
        assert pdu is not None
        assert pdu.getLength().getValue() == 8
        assert pdu.getCddType().getValue() == "ComplexDriverCdd"
