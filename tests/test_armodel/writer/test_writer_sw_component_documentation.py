"""Writer tests for SwComponentDocumentation (Swc TPS Table 12.1, p.698).

writeSwComponentDocumentationElement emits the own group in XSD order
(AUTOSAR_00052.xsd line 114911): SW-FEATURE-DEF, SW-FEATURE-DESC,
SW-TEST-DESC, SW-CALIBRATION-NOTES, SW-MAINTENANCE-NOTES,
SW-DIAGNOSTICS-NOTES, SW-CARB-DOC, CHAPTER, VARIATION-POINT — with the
inherited AR:AR-OBJECT S/T attributes written through writeARObject
(Rule 0025: base helper called exactly once).
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, Identifier, String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SoftwareComponentDocumentation import SwComponentDocumentation
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _make_documentation() -> SwComponentDocumentation:
    documentation = SwComponentDocumentation()
    documentation.createSwFeatureDef("FeatureDef")
    documentation.createSwFeatureDesc("FeatureDesc")
    documentation.createSwTestDesc("TestDesc")
    documentation.createSwCalibrationNotes("CalibrationNotes")
    documentation.createSwMaintenanceNotes("MaintenanceNotes")
    documentation.createSwDiagnosticsNotes("DiagnosticsNotes")
    documentation.createSwCarbDoc("CarbDoc")
    documentation.createChapter("FreeChapter1")
    documentation.createChapter("FreeChapter2")

    variation_point = VariationPoint()
    short_label = Identifier()
    short_label.setValue("vpLabel")
    variation_point.setShortLabel(short_label)
    documentation.setVariationPoint(variation_point)

    checksum = String()
    checksum.setValue("chk-1")
    documentation.setChecksum(checksum)
    timestamp = DateTime()
    timestamp.setValue("2009-07-23T13:38:00Z")
    documentation.setTimestamp(timestamp)
    return documentation


class TestWriteSwComponentDocumentation:
    def test_write_empty_documentation_emits_nothing(self):
        """A documentation with nothing set emits no CHAPTER slots and no VARIATION-POINT."""
        document = AUTOSAR.getInstance()
        document.clear()
        package = document.createARPackage("Pkg")
        swc = package.createApplicationSwComponentType("Swc")
        swc.setSwComponentDocumentation(SwComponentDocumentation())
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSwComponentTypeSwComponentDocumentation(parent, swc)
        child = parent.find("SW-COMPONENT-DOCUMENTATION")
        assert child is not None
        assert len(list(child)) == 0

    def test_write_own_group_in_xsd_order(self):
        document = AUTOSAR.getInstance()
        document.clear()
        package = document.createARPackage("Pkg")
        swc = package.createApplicationSwComponentType("Swc")
        swc.setSwComponentDocumentation(_make_documentation())
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSwComponentTypeSwComponentDocumentation(parent, swc)

        child = parent.find("SW-COMPONENT-DOCUMENTATION")
        tags = [c.tag for c in child]
        assert tags == [
            "SW-FEATURE-DEF",
            "SW-FEATURE-DESC",
            "SW-TEST-DESC",
            "SW-CALIBRATION-NOTES",
            "SW-MAINTENANCE-NOTES",
            "SW-DIAGNOSTICS-NOTES",
            "SW-CARB-DOC",
            "CHAPTER",
            "CHAPTER",
            "VARIATION-POINT",
        ]
        assert child.attrib.get("S") == "chk-1"
        assert child.attrib.get("T") == "2009-07-23T13:38:00Z"
        assert child.find("SW-FEATURE-DEF/SHORT-NAME").text == "FeatureDef"
        assert child.find("SW-CARB-DOC/SHORT-NAME").text == "CarbDoc"
        chapters = child.findall("CHAPTER")
        assert [c.find("SHORT-NAME").text for c in chapters] == ["FreeChapter1", "FreeChapter2"]
        assert child.find("VARIATION-POINT/SHORT-LABEL").text == "vpLabel"

    def test_round_trip_field_values(self):
        """Set -> save -> reload: every own attribute survives with its field value."""
        document = AUTOSAR.getInstance()
        document.clear()
        package = document.createARPackage("Pkg")
        swc = package.createApplicationSwComponentType("Swc")
        swc.setSwComponentDocumentation(_make_documentation())

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            swc_2 = document_2.getARPackages()[0].getSwComponentTypes()[0]
            documentation_2 = swc_2.getSwComponentDocumentation()
            assert documentation_2 is not None

            assert documentation_2.getChecksum() is not None
            assert documentation_2.getChecksum().getValue() == "chk-1"
            assert documentation_2.getTimestamp() is not None
            assert documentation_2.getTimestamp().getValue() == "2009-07-23T13:38:00Z"

            assert documentation_2.getSwFeatureDef().getShortName() == "FeatureDef"
            assert documentation_2.getSwFeatureDesc().getShortName() == "FeatureDesc"
            assert documentation_2.getSwTestDesc().getShortName() == "TestDesc"
            assert documentation_2.getSwCalibrationNotes().getShortName() == "CalibrationNotes"
            assert documentation_2.getSwMaintenanceNotes().getShortName() == "MaintenanceNotes"
            assert documentation_2.getSwDiagnosticsNotes().getShortName() == "DiagnosticsNotes"
            assert documentation_2.getSwCarbDoc().getShortName() == "CarbDoc"

            chapters = documentation_2.getChapters()
            assert [c.getShortName() for c in chapters] == ["FreeChapter1", "FreeChapter2"]

            variation_point = documentation_2.getVariationPoint()
            assert variation_point is not None
            assert variation_point.getShortLabel().getValue() == "vpLabel"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
