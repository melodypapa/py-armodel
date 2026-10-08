"""Writer round-trip test for the DATA-EXCHANGE-POINT element chain."""

import re
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DataExchangePoint
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import Baseline, DataFormatTailoring, SpecificationScope
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ConcreteClassTailoring, SpecificationDocumentScope, ConstraintTailoring
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DataExchangePointKind, String
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestWriteDataExchangePoint:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_write_and_round_trip_chain(self):
        dep = DataExchangePoint(self._parent(), "Dep")
        kind = DataExchangePointKind()
        kind.setValue(DataExchangePointKind.AGREED)
        dep.setKind(kind)
        baseline = Baseline()
        revision = String()
        revision.setValue("R23-11")
        baseline.addStandardRevision(revision)
        dep.setReferencedBaseline(baseline)
        spec_scope = SpecificationScope()
        doc_scope = SpecificationDocumentScope(spec_scope, "DocScope")
        spec_scope.addSpecificationDocumentScope(doc_scope)
        dep.setSpecificationScope(spec_scope)
        dft = DataFormatTailoring()
        dft.addConstraintTailoring(ConstraintTailoring(dft, "ConstraintTailoring"))
        dft.addClassTailoring(ConcreteClassTailoring(dft, "ClassTailoring"))
        dep.setDataFormatTailoring(dft)

        container = ET.Element("ELEMENTS")
        ARXMLWriter().writeDataExchangePoint(container, dep)
        element = container.find("DATA-EXCHANGE-POINT")

        assert element.find("SHORT-NAME").text == "Dep"
        assert element.find("KIND").text == "AGREED"
        assert element.find("REFERENCED-BASELINE/STANDARD-REVISIONS/STANDARD-REVISION").text == "R23-11"
        assert element.find("SPECIFICATION-SCOPE/SPECIFICATION-DOCUMENT-SCOPES/SPECIFICATION-DOCUMENT-SCOPE/SHORT-NAME").text == "DocScope"
        assert element.find("DATA-FORMAT-TAILORING/CLASS-TAILORINGS/CONCRETE-CLASS-TAILORING/SHORT-NAME").text == "ClassTailoring"
        assert element.find("DATA-FORMAT-TAILORING/CONSTRAINT-TAILORINGS/CONSTRAINT-TAILORING/SHORT-NAME").text == "ConstraintTailoring"

        xml_str = ET.tostring(element).decode()
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + ' xmlns="http://autosar.org/schema/r4.0"' + xml_str[idx:]

        parsed_parent = self._parent()
        parsed = ARXMLParser().readDataExchangePoint(ET.fromstring(xml_str), parsed_parent.createDataExchangePoint("Dep"))
        assert parsed.getKind().getValue() == "AGREED"
        assert parsed.getReferencedBaseline().getStandardRevisions()[0].getValue() == "R23-11"
        assert len(parsed.getDataFormatTailoring().getClassTailorings()) == 1
        assert len(parsed.getDataFormatTailoring().getConstraintTailorings()) == 1
