"""Writer tests for the XrefTarget inline text element."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import XrefTarget
from armodel.models.M2.MSR.Documentation.TextModel.SingleLanguageData import SingleLanguageLongName
from armodel.writer.arxml_writer import ARXMLWriter


class TestXrefTargetWriter:
    def test_write_xref_target_emits_inherited_content(self):
        target = XrefTarget(None, "TARGET")
        target.setLongName1(SingleLanguageLongName().setValue(String().setValue("Target label")))
        parent = ET.Element("PARENT")

        ARXMLWriter().setXrefTarget(parent, "XREF-TARGET", target)

        written = parent.find("XREF-TARGET")
        assert written is not None
        assert written.find("SHORT-NAME").text == "TARGET"
        assert written.find("LONG-NAME-1").text == "Target label"

    def test_write_xref_target_omits_none(self):
        parent = ET.Element("PARENT")

        ARXMLWriter().setXrefTarget(parent, "XREF-TARGET", None)

        assert parent.find("XREF-TARGET") is None
