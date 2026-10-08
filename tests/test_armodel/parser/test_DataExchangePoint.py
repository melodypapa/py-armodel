"""Parser round-trip test for the DATA-EXCHANGE-POINT element chain."""

import re
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DataExchangePoint
from armodel.parser.arxml_parser import ARXMLParser


def _parent():
    document = AUTOSAR.getInstance()
    document.clear()
    document.setARRelease("R23-11")
    return document.createARPackage("AUTOSAR")


def _round_trip(element: ET.Element) -> ET.Element:
    xml_str = ET.tostring(element).decode()
    xml_str = re.sub(r"^(<[A-Za-z][\w.-]*)", r'\1 xmlns="http://autosar.org/schema/r4.0"', xml_str)
    return ET.fromstring(xml_str)


class TestReadDataExchangePoint:
    def test_read_chain(self):
        element = ET.Element("DATA-EXCHANGE-POINT")
        ET.SubElement(element, "SHORT-NAME").text = "Dep"
        ET.SubElement(element, "KIND").text = "AGREED"
        baseline = ET.SubElement(element, "REFERENCED-BASELINE")
        revisions_tag = ET.SubElement(baseline, "STANDARD-REVISIONS")
        ET.SubElement(revisions_tag, "STANDARD-REVISION").text = "R23-11"
        spec_scope = ET.SubElement(element, "SPECIFICATION-SCOPE")
        doc_scopes_tag = ET.SubElement(spec_scope, "SPECIFICATION-DOCUMENT-SCOPES")
        doc_scope = ET.SubElement(doc_scopes_tag, "SPECIFICATION-DOCUMENT-SCOPE")
        ET.SubElement(doc_scope, "SHORT-NAME").text = "DocScope"
        dft = ET.SubElement(element, "DATA-FORMAT-TAILORING")
        ct_tag = ET.SubElement(dft, "CONSTRAINT-TAILORINGS")
        ct = ET.SubElement(ct_tag, "CONSTRAINT-TAILORING")
        ET.SubElement(ct, "SHORT-NAME").text = "ConstraintTailoring"

        parent = _parent()
        obj = ARXMLParser().readDataExchangePoint(_round_trip(element), parent.createDataExchangePoint("Dep"))
        assert obj.getShortName() == "Dep"
        assert obj.getKind() is not None
        assert obj.getKind().getValue() == "AGREED"
        assert obj.getReferencedBaseline() is not None
        assert len(obj.getReferencedBaseline().getStandardRevisions()) == 1
        assert obj.getReferencedBaseline().getStandardRevisions()[0].getValue() == "R23-11"
        assert obj.getSpecificationScope() is not None
        assert len(obj.getSpecificationScope().getSpecificationDocumentScopes()) == 1
        assert obj.getSpecificationScope().getSpecificationDocumentScopes()[0].getShortName() == "DocScope"
        assert obj.getDataFormatTailoring() is not None
        assert len(obj.getDataFormatTailoring().getConstraintTailorings()) == 1
        assert obj.getDataFormatTailoring().getConstraintTailorings()[0].getShortName() == "ConstraintTailoring"
