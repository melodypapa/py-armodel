"""Writer tests for the Xref inline text element."""

from xml.etree import ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, String
from armodel.models.M2.MSR.Documentation.TextModel.InlineAttributeEnums import ResolutionPolicyEnum, ShowContentEnum
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import Xref
from armodel.models.M2.MSR.Documentation.TextModel.SingleLanguageData import SingleLanguageLongName
from armodel.writer.arxml_writer import ARXMLWriter


class TestXrefWriter:
    def test_set_xref_writes_nested_members_and_attributes(self):
        xref = Xref()
        xref.setLabel1(SingleLanguageLongName().setValue(String().setValue("Replacement")))
        xref.setReferrableRef(RefType().setValue("/A/B").setDest("AR-PACKAGE"))
        xref.setResolutionPolicy(ResolutionPolicyEnum().setValue("SLOPPY"))
        xref.setShowContent(ShowContentEnum().setValue("SHOW-CONTENT"))

        parent = ET.Element("PARENT")
        ARXMLWriter().setXref(parent, "XREF", xref)
        written = parent.find("XREF")

        assert written.find("LABEL-1").text == "Replacement"
        assert written.find("REFERRABLE-REF").text == "/A/B"
        assert written.find("REFERRABLE-REF").attrib["DEST"] == "AR-PACKAGE"
        assert written.attrib["RESOLUTION-POLICY"] == "SLOPPY"
        assert written.attrib["SHOW-CONTENT"] == "SHOW-CONTENT"
