"""
This module contains tests for the SwComponentDocumentation class
(spec AUTOSAR CP_TPS_SoftwareComponentTemplate, Table 12.1, p.698).
"""

import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SoftwareComponentDocumentation import SwComponentDocumentation
from armodel.models.M2.MSR.Documentation.Chapters import Chapter


class TestSwComponentDocumentation:

    def test_initialization(self):
        documentation = SwComponentDocumentation()
        assert isinstance(documentation, ARObject)
        assert isinstance(documentation, VariationPointCapable)
        assert documentation.getChapters() == []
        assert documentation.getSwCalibrationNotes() is None
        assert documentation.getSwCarbDoc() is None
        assert documentation.getSwDiagnosticsNotes() is None
        assert documentation.getSwFeatureDef() is None
        assert documentation.getSwFeatureDesc() is None
        assert documentation.getSwMaintenanceNotes() is None
        assert documentation.getSwTestDesc() is None
        assert documentation.getVariationPoint() is None

    def test_create_get_chapters(self):
        documentation = SwComponentDocumentation()
        chapter_a = documentation.createChapter("ChapterA")
        assert isinstance(chapter_a, Chapter)
        assert chapter_a.getShortName() == "ChapterA"
        assert documentation.getChapters() == [chapter_a]
        chapter_b = documentation.createChapter("ChapterB")
        assert documentation.getChapters() == [chapter_a, chapter_b]
        assert documentation.createChapter("ChapterA") is chapter_a
        assert documentation.getChapters() == [chapter_a, chapter_b]

    def test_create_get_predefined_chapters(self):
        documentation = SwComponentDocumentation()
        feature_def = documentation.createSwFeatureDef("FeatureDef")
        assert isinstance(feature_def, Chapter)
        assert feature_def.getShortName() == "FeatureDef"
        assert documentation.getSwFeatureDef() is feature_def
        assert documentation.createSwFeatureDef("FeatureDef") is feature_def
        feature_desc = documentation.createSwFeatureDesc("FeatureDesc")
        assert feature_desc.getShortName() == "FeatureDesc"
        assert documentation.getSwFeatureDesc() is feature_desc
        assert documentation.createSwFeatureDesc("FeatureDesc") is feature_desc
        test_desc = documentation.createSwTestDesc("TestDesc")
        assert test_desc.getShortName() == "TestDesc"
        assert documentation.getSwTestDesc() is test_desc
        assert documentation.createSwTestDesc("TestDesc") is test_desc
        calibration_notes = documentation.createSwCalibrationNotes("CalibrationNotes")
        assert calibration_notes.getShortName() == "CalibrationNotes"
        assert documentation.getSwCalibrationNotes() is calibration_notes
        assert documentation.createSwCalibrationNotes("CalibrationNotes") is calibration_notes
        maintenance_notes = documentation.createSwMaintenanceNotes("MaintenanceNotes")
        assert maintenance_notes.getShortName() == "MaintenanceNotes"
        assert documentation.getSwMaintenanceNotes() is maintenance_notes
        assert documentation.createSwMaintenanceNotes("MaintenanceNotes") is maintenance_notes
        diagnostics_notes = documentation.createSwDiagnosticsNotes("DiagnosticsNotes")
        assert diagnostics_notes.getShortName() == "DiagnosticsNotes"
        assert documentation.getSwDiagnosticsNotes() is diagnostics_notes
        assert documentation.createSwDiagnosticsNotes("DiagnosticsNotes") is diagnostics_notes
        carb_doc = documentation.createSwCarbDoc("CarbDoc")
        assert carb_doc.getShortName() == "CarbDoc"
        assert documentation.getSwCarbDoc() is carb_doc
        assert documentation.createSwCarbDoc("CarbDoc") is carb_doc

    def test_get_set_variation_point(self):
        documentation = SwComponentDocumentation()
        variation_point = VariationPoint()

        assert documentation == documentation.setVariationPoint(None)
        assert documentation.getVariationPoint() is None

        assert documentation == documentation.setVariationPoint(variation_point)
        assert documentation.getVariationPoint() == variation_point

        assert documentation == documentation.setVariationPoint(None)  # None no-op
        assert documentation.getVariationPoint() == variation_point

    def test_type_hints(self):
        assert typing.get_type_hints(SwComponentDocumentation.createChapter).get("return") is Chapter
        assert typing.get_type_hints(SwComponentDocumentation.createChapter).get("short_name") is str
        assert typing.get_type_hints(SwComponentDocumentation.getChapters).get("return") == typing.List[Chapter]
        assert typing.get_type_hints(SwComponentDocumentation.getSwCalibrationNotes).get("return") == typing.Optional[Chapter]
        assert typing.get_type_hints(SwComponentDocumentation.getSwTestDesc).get("return") == typing.Optional[Chapter]
