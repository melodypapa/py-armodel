import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameTokens, ViewTokens
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import DocumentViewSelectable
from armodel.writer.arxml_writer import ARXMLWriter


class ConcreteSelectable(DocumentViewSelectable):
    def __init__(self):
        super().__init__()


def test_write_document_view_selectable_attributes():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    selectable = ConcreteSelectable()
    selectable.setSi(NameTokens().setValue("INTERNAL"))
    selectable.setView(ViewTokens().setValue("DETAILED"))
    element = ET.Element("SELECTABLE")

    ARXMLWriter().writeDocumentViewSelectable(element, selectable)

    assert element.attrib["SI"] == "INTERNAL"
    assert element.attrib["VIEW"] == "DETAILED"


def test_write_document_view_selectable_without_optional_view():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    selectable = ConcreteSelectable().setSi(NameTokens().setValue("INTERNAL"))
    element = ET.Element("SELECTABLE")

    ARXMLWriter().writeDocumentViewSelectable(element, selectable)

    assert element.attrib == {"SI": "INTERNAL"}
