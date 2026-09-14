import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.MSR.Documentation.BlockElements import Colspec
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import AlignEnum, TableSeparatorString
from armodel.writer.arxml_writer import ARXMLWriter


def test_write_colspec_attributes():
    colspec = Colspec()
    colspec.setAlign(AlignEnum().setValue(AlignEnum.CENTER))
    colspec.setColname(String().setValue("name"))
    colspec.setColnum(String().setValue("1"))
    colspec.setColsep(TableSeparatorString().setValue("1"))
    colspec.setColwidth(String().setValue("2*"))
    colspec.setRowsep(TableSeparatorString().setValue("0"))
    element = ET.Element("COLSPEC")

    ARXMLWriter().writeColspec(element, colspec)

    assert element.attrib == {"ALIGN": "CENTER", "COLNAME": "name", "COLNUM": "1", "COLSEP": "1", "COLWIDTH": "2*", "ROWSEP": "0"}
