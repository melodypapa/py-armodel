"""
This module contains tests for the SoftwareComponentDocumentation module in SWComponentTemplate.
"""

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SoftwareComponentDocumentation import (
    SwComponentDocumentation,
)


class TestSwComponentDocumentation:
    """Test class for SwComponentDocumentation class."""

    def test_sw_component_documentation_initialization(self):
        doc = SwComponentDocumentation()
        assert doc.getChapters() == []
        assert doc.getSwCalibrationNotes() is None
        assert doc.getSwCarbDoc() is None
        assert doc.getSwDiagnosticsNotes() is None
        assert doc.getSwFeatureDef() is None
        assert doc.getSwFeatureDesc() is None
        assert doc.getSwMaintenanceNotes() is None
        assert doc.getSwTestDesc() is None

    def test_create_get_predefined_chapters(self):
        doc = SwComponentDocumentation()

        feature_def = doc.createSwFeatureDef("FeatureDef")
        assert feature_def.getShortName() == "FeatureDef"
        assert doc.getSwFeatureDef() is feature_def
        assert doc.createSwFeatureDef("FeatureDef") is feature_def

        feature_desc = doc.createSwFeatureDesc("FeatureDesc")
        assert feature_desc.getShortName() == "FeatureDesc"
        assert doc.getSwFeatureDesc() is feature_desc
        assert doc.createSwFeatureDesc("FeatureDesc") is feature_desc

        test_desc = doc.createSwTestDesc("TestDesc")
        assert test_desc.getShortName() == "TestDesc"
        assert doc.getSwTestDesc() is test_desc
        assert doc.createSwTestDesc("TestDesc") is test_desc

        calibration_notes = doc.createSwCalibrationNotes("CalibrationNotes")
        assert calibration_notes.getShortName() == "CalibrationNotes"
        assert doc.getSwCalibrationNotes() is calibration_notes
        assert doc.createSwCalibrationNotes("CalibrationNotes") is calibration_notes

        maintenance_notes = doc.createSwMaintenanceNotes("MaintenanceNotes")
        assert maintenance_notes.getShortName() == "MaintenanceNotes"
        assert doc.getSwMaintenanceNotes() is maintenance_notes
        assert doc.createSwMaintenanceNotes("MaintenanceNotes") is maintenance_notes

        diagnostics_notes = doc.createSwDiagnosticsNotes("DiagnosticsNotes")
        assert diagnostics_notes.getShortName() == "DiagnosticsNotes"
        assert doc.getSwDiagnosticsNotes() is diagnostics_notes
        assert doc.createSwDiagnosticsNotes("DiagnosticsNotes") is diagnostics_notes

        carb_doc = doc.createSwCarbDoc("CarbDoc")
        assert carb_doc.getShortName() == "CarbDoc"
        assert doc.getSwCarbDoc() is carb_doc
        assert doc.createSwCarbDoc("CarbDoc") is carb_doc

    def test_create_get_chapters(self):
        doc = SwComponentDocumentation()
        chapter_a = doc.createChapter("ChapterA")
        assert chapter_a.getShortName() == "ChapterA"
        chapter_b = doc.createChapter("ChapterB")
        assert doc.getChapters() == [chapter_a, chapter_b]
        assert doc.createChapter("ChapterA") is chapter_a
        assert doc.getChapters() == [chapter_a, chapter_b]
