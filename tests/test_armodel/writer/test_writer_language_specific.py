"""Reader/writer round-trip tests for the LanguageSpecific family (Table 9.97)."""

import os
import tempfile

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken, String
from armodel.models.M2.MSR.AsamHdo.AdminData import AdminData
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import EmphasisText, IndexEntry, Superscript, Tt
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LLongName, LOverviewParagraph, LPlainText
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultilanguageLongName, MultiLanguageOverviewParagraph, MultiLanguagePlainText
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestLanguageSpecificRoundTrip:
    def test_round_trip_long_name(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("AUTOSAR")
        swc = pkg.createApplicationSwComponentType("App")

        long_name = MultilanguageLongName()
        l4 = LLongName()
        l4.setL("EN")
        l4.setValue("English name")
        long_name.addL4(l4)
        swc.setLongName(long_name)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            swc_2 = document_2.getARPackages()[0].getAtomicSwComponentTypes()[0]
            l4_2 = swc_2.getLongName().getL4s()[0]
            assert l4_2.getL() == "EN"
            assert l4_2.getValue() == "English name"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_long_name_inline_content(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("AUTOSAR")
        swc = pkg.createApplicationSwComponentType("App")

        long_name = MultilanguageLongName()
        l4 = LLongName()
        l4.setL("EN")
        l4.setValue("Long name with ")
        l4.setSup(Superscript().setValue("true"))
        emphasis = EmphasisText()
        emphasis.setValue(String().setValue("emphasized"))
        l4.setE(emphasis)
        index_entry = IndexEntry()
        index_entry.setValue(String().setValue("index"))
        l4.setIe(index_entry)
        tt = Tt()
        tt.setValue(String().setValue("term"))
        tt.setType(NameToken().setValue("VARIABLE"))
        l4.setTt(tt)
        long_name.addL4(l4)
        swc.setLongName(long_name)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            swc_2 = document_2.getARPackages()[0].getAtomicSwComponentTypes()[0]
            l4_2 = swc_2.getLongName().getL4s()[0]
            assert l4_2.getL() == "EN"
            assert l4_2.getSup().getValue() == "true"
            assert l4_2.getE().getValue().getValue() == "emphasized"
            assert l4_2.getIe().getValue().getValue() == "index"
            assert l4_2.getTt().getValue().getValue() == "term"
            assert l4_2.getTt().getType().getValue() == "VARIABLE"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_overview_paragraph(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("AUTOSAR")
        swc = pkg.createApplicationSwComponentType("App")

        overview = MultiLanguageOverviewParagraph()
        l2 = LOverviewParagraph()
        l2.setL("EN")
        l2.setValue("Overview")
        overview.addL2(l2)
        swc.setDesc(overview)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            swc_2 = document_2.getARPackages()[0].getAtomicSwComponentTypes()[0]
            l2_2 = swc_2.getDesc().getL2s()[0]
            assert l2_2.getL() == "EN"
            assert l2_2.getValue() == "Overview"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_plain_text(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("AUTOSAR")
        swc = pkg.createApplicationSwComponentType("App")

        used_languages = MultiLanguagePlainText()
        l10 = LPlainText()
        l10.setL("EN")
        l10.setValue("plain text")
        used_languages.addL10(l10)
        swc.setAdminData(AdminData())
        swc.getAdminData().setUsedLanguages(used_languages)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            swc_2 = document_2.getARPackages()[0].getAtomicSwComponentTypes()[0]
            l10_2 = swc_2.getAdminData().getUsedLanguages().getL10s()[0]
            assert l10_2.getL() == "EN"
            assert l10_2.getValue() == "plain text"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
