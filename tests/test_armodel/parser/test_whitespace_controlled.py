"""Reader tests for the WhitespaceControlled xml:space deserialization (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.7)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Enumerations import XmlSpaceEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken, VerbatimStringPlain
from armodel.models.M2.MSR.AsamHdo.AdminData import AdminData
from armodel.models.M2.MSR.AsamHdo.SpecialData import Sd, Sdg, SdgContents
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LPlainText, LVerbatim
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguagePlainText, MultiLanguageVerbatim
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestWhitespaceControlledParser:
    def test_read_l10_reads_xml_space(self):
        """The xml:space attribute on L-10 (complexType L-PLAIN-TEXT composes the WHITESPACE-CONTROLLED attributeGroup) must parse into xmlSpace (Table 9.7 xmlSpace row)."""
        parser = ARXMLParser()
        element = ET.fromstring(
            '<ROOT xmlns="http://autosar.org/schema/r4.0">' "<MULTI-LANGUAGE-PLAIN-TEXT>" '<L-10 L="EN" xml:space="preserve">plain text</L-10>' "</MULTI-LANGUAGE-PLAIN-TEXT>" "</ROOT>"
        )

        paragraph = parser.getMultiLanguagePlainText(element, "MULTI-LANGUAGE-PLAIN-TEXT")

        l10 = paragraph.getL10s()[0]
        assert l10.getXmlSpace() is not None
        assert l10.getXmlSpace().getValue() == "preserve"
        assert l10.getValue() == "plain text"

    def test_read_l5_reads_xml_space(self):
        """The xml:space attribute on L-5 (complexType L-VERBATIM composes the WHITESPACE-CONTROLLED attributeGroup) must parse into xmlSpace."""
        parser = ARXMLParser()
        element = ET.fromstring(
            '<ROOT xmlns="http://autosar.org/schema/r4.0">' "<MULTI-LANGUAGE-VERBATIM>" '<L-5 L="EN" xml:space="default">verbatim text</L-5>' "</MULTI-LANGUAGE-VERBATIM>" "</ROOT>"
        )

        verbatim = parser.getMultiLanguageVerbatim(element, "MULTI-LANGUAGE-VERBATIM")

        l5 = verbatim.getL5s()[0]
        assert l5.getXmlSpace() is not None
        assert l5.getXmlSpace().getValue() == "default"
        assert l5.getValue() == "verbatim text"

    def test_read_without_xml_space_defaults_none(self):
        """Elements without the attribute keep xmlSpace None (Optional model field)."""
        parser = ARXMLParser()
        element = ET.fromstring('<ROOT xmlns="http://autosar.org/schema/r4.0">' "<MULTI-LANGUAGE-PLAIN-TEXT>" '<L-10 L="EN">plain text</L-10>' "</MULTI-LANGUAGE-PLAIN-TEXT>" "</ROOT>")

        paragraph = parser.getMultiLanguagePlainText(element, "MULTI-LANGUAGE-PLAIN-TEXT")

        assert paragraph.getL10s()[0].getXmlSpace() is None

    def test_round_trip_preserves_xml_space(self):
        """writeL10/xml:space -> parse must return the same enum value on both consumer elements (writer/parser helper-pair contract)."""
        l10 = LPlainText()
        l10.setL("EN")
        l10.setValue("plain text")
        l10.setXmlSpace(XmlSpaceEnum().setValue(XmlSpaceEnum.PRESERVE))

        element = ET.Element("ROOT")
        ARXMLWriter().setMultiLanguagePlainText(element, "MULTI-LANGUAGE-PLAIN-TEXT", MultiLanguagePlainText().addL10(l10))
        element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
        parsed = ET.fromstring(ET.tostring(element, encoding="unicode"))

        result = ARXMLParser().getMultiLanguagePlainText(parsed, "MULTI-LANGUAGE-PLAIN-TEXT")
        assert result.getL10s()[0].getXmlSpace().getValue() == "preserve"

    def test_round_trip_l5_preserves_xml_space(self):
        l5 = LVerbatim()
        l5.setL("DE")
        l5.setValue("verbatim text")
        l5.setXmlSpace(XmlSpaceEnum().setValue(XmlSpaceEnum.DEFAULT))

        element = ET.Element("ROOT")
        ARXMLWriter().setMultiLanguageVerbatim(element, "MULTI-LANGUAGE-VERBATIM", MultiLanguageVerbatim().addL5(l5))
        element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
        parsed = ET.fromstring(ET.tostring(element, encoding="unicode"))

        result = ARXMLParser().getMultiLanguageVerbatim(parsed, "MULTI-LANGUAGE-VERBATIM")
        assert result.getL5s()[0].getXmlSpace().getValue() == "default"

    def test_read_sd_reads_xml_space(self):
        """The optional xml:space attribute of the SD attributeGroup (Sd, XSD 00052 SD attributeGroup) must parse into xmlSpace — readSd drops it otherwise (writeSds has always written it)."""
        parser = ARXMLParser()
        element = ET.fromstring(
            '<ROOT xmlns="http://autosar.org/schema/r4.0">' '<ADMIN-DATA><SDGS><SDG GID="demo">' '<SD GID="purpose" xml:space="preserve">special   data</SD>' "</SDG></SDGS></ADMIN-DATA>" "</ROOT>"
        )

        admin_data = parser.getAdminData(element, "ADMIN-DATA")

        sd = admin_data.getSdgs()[0].getSdgContentsType().getSds()[0]
        assert sd.getXmlSpace().getValue() == "preserve"
        assert sd.getValue().getValue() == "special   data"

    def test_round_trip_sd_preserves_xml_space(self):
        """SD xml:space write -> parse round-trip (readSd/writeSds helper-pair contract via the shared WhitespaceControlled helpers)."""
        sd = Sd()
        sd.setGID(NameToken().setValue("purpose"))
        sd.setValue(VerbatimStringPlain().setValue("special   data"))
        sd.setXmlSpace(XmlSpaceEnum().setValue(XmlSpaceEnum.PRESERVE))
        sdg = Sdg()
        sdg.setGID(NameToken().setValue("demo"))
        sdg.setSdgContentsType(SdgContents())
        sdg.getSdgContentsType().addSd(sd)

        admin_data = AdminData()
        admin_data.addSdg(sdg)
        element = ET.Element("ROOT")
        ARXMLWriter().setAdminData(element, admin_data)
        element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
        parsed = ET.fromstring(ET.tostring(element, encoding="unicode"))

        result = ARXMLParser().getAdminData(parsed, "ADMIN-DATA")
        assert result.getSdgs()[0].getSdgContentsType().getSds()[0].getXmlSpace().getValue() == "preserve"
