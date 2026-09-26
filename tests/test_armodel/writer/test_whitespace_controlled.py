"""Writer tests for the WhitespaceControlled xml:space serialization (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.7)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Enumerations import XmlSpaceEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken, VerbatimStringPlain
from armodel.models.M2.MSR.AsamHdo.AdminData import AdminData
from armodel.models.M2.MSR.AsamHdo.SpecialData import Sd, Sdg, SdgContents
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LPlainText, LVerbatim
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguagePlainText, MultiLanguageVerbatim
from armodel.writer.arxml_writer import ARXMLWriter

XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"


class TestWhitespaceControlledWriter:
    def test_write_l10_emits_xml_space(self):
        """The L-10 element (complexType L-PLAIN-TEXT composes the WHITESPACE-CONTROLLED attributeGroup) must carry the xml:space attribute (Table 9.7 xmlSpace row, xml.name=space xml.nsPrefix=xml)."""
        l10 = LPlainText()
        l10.setValue("preserve me")
        l10.setXmlSpace(XmlSpaceEnum().setValue(XmlSpaceEnum.PRESERVE))

        element = ET.Element("MULTI-LANGUAGE-PLAIN-TEXT")
        ARXMLWriter().setMultiLanguagePlainText(element, "MULTI-LANGUAGE-PLAIN-TEXT", MultiLanguagePlainText().addL10(l10))

        written = element.find("MULTI-LANGUAGE-PLAIN-TEXT/L-10")
        assert written is not None
        assert written.attrib[XML_SPACE] == "preserve"
        assert 'xml:space="preserve"' in ET.tostring(element, encoding="unicode")

    def test_write_l10_without_xml_space_omits_attrib(self):
        """xmlSpace is Optional in the model: None must omit the attribute entirely (writer no-op)."""
        l10 = LPlainText()
        l10.setValue("plain text")

        element = ET.Element("MULTI-LANGUAGE-PLAIN-TEXT")
        ARXMLWriter().setMultiLanguagePlainText(element, "MULTI-LANGUAGE-PLAIN-TEXT", MultiLanguagePlainText().addL10(l10))

        written = element.find("MULTI-LANGUAGE-PLAIN-TEXT/L-10")
        assert written is not None
        assert XML_SPACE not in written.attrib

    def test_write_l5_emits_xml_space(self):
        """The L-5 element (complexType L-VERBATIM composes the WHITESPACE-CONTROLLED attributeGroup) must carry the xml:space attribute."""
        l5 = LVerbatim()
        l5.setValue("verbatim text")
        l5.setXmlSpace(XmlSpaceEnum().setValue(XmlSpaceEnum.DEFAULT))

        element = ET.Element("MULTI-LANGUAGE-VERBATIM")
        ARXMLWriter().setMultiLanguageVerbatim(element, "MULTI-LANGUAGE-VERBATIM", MultiLanguageVerbatim().addL5(l5))

        written = element.find("MULTI-LANGUAGE-VERBATIM/L-5")
        assert written is not None
        assert written.attrib[XML_SPACE] == "default"
        assert 'xml:space="default"' in ET.tostring(element, encoding="unicode")

    def test_write_l5_without_xml_space_omits_attrib(self):
        l5 = LVerbatim()
        l5.setValue("verbatim text")

        element = ET.Element("MULTI-LANGUAGE-VERBATIM")
        ARXMLWriter().setMultiLanguageVerbatim(element, "MULTI-LANGUAGE-VERBATIM", MultiLanguageVerbatim().addL5(l5))

        written = element.find("MULTI-LANGUAGE-VERBATIM/L-5")
        assert written is not None
        assert XML_SPACE not in written.attrib

    def test_write_sd_emits_xml_space(self):
        """The SD element carries its optional xml:space attribute via the shared writeWhitespaceControlled helper (Sd unification)."""
        sd = Sd()
        sd.setGID(NameToken().setValue("purpose"))
        sd.setValue(VerbatimStringPlain().setValue("special   data"))
        sd.setXmlSpace(XmlSpaceEnum().setValue(XmlSpaceEnum.PRESERVE))
        sdg = Sdg()
        sdg.setGID(NameToken().setValue("demo"))
        sdg.setSdgContentsType(SdgContents())
        sdg.getSdgContentsType().addSd(sd)

        element = ET.Element("ROOT")
        ARXMLWriter().setAdminData(element, AdminData().addSdg(sdg))

        written = element.find("ADMIN-DATA/SDGS/SDG/SD")
        assert written is not None
        assert written.attrib[XML_SPACE] == "preserve"
        assert written.attrib["GID"] == "purpose"

    def test_write_sd_without_xml_space_omits_attrib(self):
        sd = Sd()
        sd.setGID(NameToken().setValue("purpose"))
        sdg = Sdg()
        sdg.setGID(NameToken().setValue("demo"))
        sdg.setSdgContentsType(SdgContents())
        sdg.getSdgContentsType().addSd(sd)

        element = ET.Element("ROOT")
        ARXMLWriter().setAdminData(element, AdminData().addSdg(sdg))

        written = element.find("ADMIN-DATA/SDGS/SDG/SD")
        assert written is not None
        assert XML_SPACE not in written.attrib
