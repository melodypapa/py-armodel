import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, NameTokens
from armodel.models.M2.MSR.Documentation.BlockElements import FrameEnum, Row, Table, Tbody, Tgroup
from armodel.models.M2.MSR.Documentation.Chapters import TopicContent
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LParagraph
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageParagraph
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestTopicContent:
    def test_write_topic_content(self):
        topic_content = TopicContent()
        block = DocumentationBlock()
        paragraph = MultiLanguageParagraph()
        l1 = LParagraph()
        l1.setL("EN")
        l1.setValue("cell text")
        paragraph.addL1(l1)
        block.addP(paragraph)
        topic_content.setBlockLevelContent(block)
        table = Table()
        table.setFrame(FrameEnum().setValue(FrameEnum.TOP))
        table.addTgroup(Tgroup().setCols(Integer().setValue(2)).setTbody(Tbody().addRow(Row())))
        topic_content.setTable(table)
        topic_content.createTraceableTable("tt")
        root = ET.Element("ROOT")

        ARXMLWriter().writeTopicContent(root, topic_content)
        element = root.find("TOPIC-CONTENT")

        assert element is not None
        assert element.find("DOCUMENTATION-BLOCK/P/L-1").text == "cell text"
        assert element.find("DOCUMENTATION-BLOCK/P/L-1").attrib["L"] == "EN"
        assert element.find("TABLE").attrib["FRAME"] == "TOP"
        assert element.find("TABLE/TGROUP") is not None
        assert element.find("TRACEABLE-TABLE/SHORT-NAME").text == "tt"
        assert [child.tag for child in element] == ["DOCUMENTATION-BLOCK", "TABLE", "TRACEABLE-TABLE"]

    def test_write_topic_content_without_optional_content(self):
        root = ET.Element("ROOT")

        ARXMLWriter().writeTopicContent(root, TopicContent())
        element = root.find("TOPIC-CONTENT")

        assert element is not None
        assert element.find("DOCUMENTATION-BLOCK") is None
        assert element.find("TABLE") is None
        assert element.find("TRACEABLE-TABLE") is None

    def test_write_then_read_roundtrip(self):
        topic_content = TopicContent()
        block = DocumentationBlock()
        paragraph = MultiLanguageParagraph()
        l1 = LParagraph()
        l1.setL("EN")
        l1.setValue("cell text")
        paragraph.addL1(l1)
        block.addP(paragraph)
        topic_content.setBlockLevelContent(block)
        table = Table()
        table.setFrame(FrameEnum().setValue(FrameEnum.TOP))
        table.addTgroup(Tgroup().setCols(Integer().setValue(2)).setTbody(Tbody().addRow(Row())))
        topic_content.setTable(table)
        traceable_table = topic_content.createTraceableTable("tt")
        traceable_table.setSi(NameTokens().setValue("semantic"))
        root = ET.Element("ROOT")
        ARXMLWriter().writeTopicContent(root, topic_content)

        wrapped = '<ROOT xmlns="http://autosar.org/schema/r4.0">' + ET.tostring(root.find("TOPIC-CONTENT"), encoding="unicode") + "</ROOT>"
        reparsed = ARXMLParser().readTopicContent(ET.fromstring(wrapped).find("{http://autosar.org/schema/r4.0}TOPIC-CONTENT"), None)

        assert reparsed.getBlockLevelContent().getPs()[0].getL1s()[0].getValue() == "cell text"
        assert reparsed.getBlockLevelContent().getPs()[0].getL1s()[0].getL() == "EN"
        assert reparsed.getTable().getFrame().getValue() == "TOP"
        assert reparsed.getTable().getTgroups()[0].getCols().getValue() == 2
        assert reparsed.getTraceableTable().getShortName() == "tt"
        assert reparsed.getTraceableTable().getSi().getValue() == "semantic"
