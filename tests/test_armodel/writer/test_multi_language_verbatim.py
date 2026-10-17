"""Round-trip tests for MultiLanguageVerbatim (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.5).

The class inherits DocumentViewSelectable/Paginateable (SI/VIEW/BREAK/KEEP-WITH-PREVIOUS)
and the VariationPointCapable mixin (VARIATION-POINT); the reader/writer entry points must
dispatch both, not just the bare ARObject state.
"""

import os
import tempfile

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Enumerations import XmlSpaceEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken, NameTokens, String, ViewTokens
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.MSR.Documentation.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import FloatEnum, PgwideEnum
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import ChapterEnumBreak, KeepWithPreviousEnum
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LVerbatim
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageVerbatim
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestMultiLanguageVerbatimRoundTrip:
    def _build(self, document):
        pkg = document.createARPackage("AUTOSAR")
        swc = pkg.createApplicationSwComponentType("App")

        verbatim = MultiLanguageVerbatim()
        verbatim.setSi(NameTokens().setValue("SIVAL"))
        verbatim.setView(ViewTokens().setValue("VIEWVAL"))
        verbatim.setBreak(ChapterEnumBreak().setValue(ChapterEnumBreak.BREAK))
        verbatim.setKeepWithPrevious(KeepWithPreviousEnum().setValue(KeepWithPreviousEnum.KEEP))
        verbatim.setVariationPoint(VariationPoint())
        verbatim.setAllowBreak(NameToken().setValue("0"))
        verbatim.setFloat(FloatEnum().setValue(FloatEnum.NO_FLOAT))
        verbatim.setHelpEntry(String().setValue("help-entry"))
        verbatim.setPgwide(PgwideEnum().setValue(PgwideEnum.PGWIDE))
        l5 = LVerbatim()
        l5.setL("EN")
        l5.setValue("verbatim text")
        l5.setXmlSpace(XmlSpaceEnum().setValue(XmlSpaceEnum.PRESERVE))
        verbatim.addL5(l5)

        intro = DocumentationBlock()
        intro.setVerbatim(verbatim)
        swc.setIntroduction(intro)
        return swc

    def test_round_trip(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        self._build(document)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            swc_2 = document_2.getARPackages()[0].getAtomicSwComponentTypes()[0]
            verbatim = swc_2.getIntroduction().getVerbatim()

            assert verbatim is not None
            assert verbatim.getSi().getValue() == "SIVAL"
            assert verbatim.getView().getValue() == "VIEWVAL"
            assert verbatim.getBreak().getValue() == ChapterEnumBreak.BREAK
            assert verbatim.getKeepWithPrevious().getValue() == KeepWithPreviousEnum.KEEP
            assert verbatim.getVariationPoint() is not None
            assert verbatim.getAllowBreak().getValue() == "0"
            assert verbatim.getFloat().getValue() == FloatEnum.NO_FLOAT
            assert verbatim.getHelpEntry().getValue() == "help-entry"
            assert verbatim.getPgwide().getValue() == PgwideEnum.PGWIDE
            assert verbatim.getL5s()[0].getValue() == "verbatim text"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
