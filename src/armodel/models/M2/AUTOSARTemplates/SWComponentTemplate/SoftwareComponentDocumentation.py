"""
This module contains the SwComponentDocumentation class for AUTOSAR software
component templates (spec M2::AUTOSARTemplates::SWComponentTemplate::SoftwareComponentDocumentation).

The Chapter family it aggregates (Chapter, ChapterModel, ChapterContent,
ChapterOrMsrQuery, TopicOrMsrQuery) lives in its own package
M2::MSR::Documentation::Chapters (see src/armodel/models/M2/MSR/Documentation/Chapters.py).
"""

from __future__ import annotations
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.MSR.Documentation.Chapters import Chapter


class SwComponentDocumentation(ARObject, VariationPointCapable):
    """
    This class specifies the ability to write dedicated documentation to a component type according to ASAM FSX.
    """

    # SwComponentDocumentation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 12.1, p.698
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createChapter            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getChapters              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createSwCalibrationNotes [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwCalibrationNotes    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createSwCarbDoc          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwCarbDoc             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createSwDiagnosticsNotes [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwDiagnosticsNotes    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createSwFeatureDef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwFeatureDef          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createSwFeatureDesc      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwFeatureDesc         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createSwMaintenanceNotes [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwMaintenanceNotes    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createSwTestDesc         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwTestDesc            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # These chapters provide additional information about the software component that do not fit in the other chapters. Note that this is subject to variation because Chapter aggregations in the role chapter are variant within the documentation in general. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=chapter.shortName, chapter.variationPoint.shortLabel vh.latestBindingTime=postBuild xml.roleElement=true xml.roleWrapperElement=false xml.sequenceOffset=100 xml.typeElement=false
        self.chapters: List[Chapter] = []

        # This element contains calibration instructions and hints for a calibration engineer. Tags: xml.roleElement=true xml.sequenceOffset=60 xml.typeElement=false
        self.swCalibrationNotes: Optional[Chapter] = None

        # This element records the documentation requested by CARB. Tags: xml.roleElement=true xml.sequenceOffset=80 xml.typeElement=false
        self.swCarbDoc: Optional[Chapter] = None

        # This element contains general information about diagnostics issues within the component. Tags: xml.roleElement=true xml.sequenceOffset=75 xml.typeElement=false
        self.swDiagnosticsNotes: Optional[Chapter] = None

        # This element contains the definition of the physical functionality of this software component. This definition is more or less formal and is intended to be delivered from modeling tools. Tags: xml.roleElement=true xml.sequenceOffset=20 xml.typeElement=false
        self.swFeatureDef: Optional[Chapter] = None

        # This element contains the textual description of the software functionality of this software component. Expert should write this description. Tags: xml.roleElement=true xml.sequenceOffset=30 xml.typeElement=false
        self.swFeatureDesc: Optional[Chapter] = None

        # This element contains information regarding the software maintenance of the component. Tags: xml.roleElement=true xml.sequenceOffset=70 xml.typeElement=false
        self.swMaintenanceNotes: Optional[Chapter] = None

        # This element contains suggestions and hints for the test of the software functionality of this software component. Tags: xml.roleElement=true xml.sequenceOffset=50 xml.typeElement=false
        self.swTestDesc: Optional[Chapter] = None

    def createChapter(self, short_name: str) -> Chapter:
        """
        These chapters provide additional information about the software component that do not fit in the other chapters. Note that this is subject to variation because Chapter aggregations in the role chapter are variant within the documentation in general. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=chapter.shortName, chapter.variationPoint.shortLabel vh.latestBindingTime=postBuild xml.roleElement=true xml.roleWrapperElement=false xml.sequenceOffset=100 xml.typeElement=false
        """
        for chapter in self.chapters:
            if chapter.getShortName() == short_name:
                return chapter
        chapter = Chapter(self, short_name)
        self.chapters.append(chapter)
        return chapter

    def getChapters(self) -> List[Chapter]:
        """
        These chapters provide additional information about the software component that do not fit in the other chapters. Note that this is subject to variation because Chapter aggregations in the role chapter are variant within the documentation in general. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=chapter.shortName, chapter.variationPoint.shortLabel vh.latestBindingTime=postBuild xml.roleElement=true xml.roleWrapperElement=false xml.sequenceOffset=100 xml.typeElement=false
        """
        return self.chapters

    def createSwCalibrationNotes(self, short_name: str) -> Chapter:
        """
        This element contains calibration instructions and hints for a calibration engineer. Tags: xml.roleElement=true xml.sequenceOffset=60 xml.typeElement=false
        """
        if self.swCalibrationNotes is None:
            self.swCalibrationNotes = Chapter(self, short_name)
        return self.swCalibrationNotes

    def getSwCalibrationNotes(self) -> Optional[Chapter]:
        """
        This element contains calibration instructions and hints for a calibration engineer. Tags: xml.roleElement=true xml.sequenceOffset=60 xml.typeElement=false
        """
        return self.swCalibrationNotes

    def createSwCarbDoc(self, short_name: str) -> Chapter:
        """
        This element records the documentation requested by CARB. Tags: xml.roleElement=true xml.sequenceOffset=80 xml.typeElement=false
        """
        if self.swCarbDoc is None:
            self.swCarbDoc = Chapter(self, short_name)
        return self.swCarbDoc

    def getSwCarbDoc(self) -> Optional[Chapter]:
        """
        This element records the documentation requested by CARB. Tags: xml.roleElement=true xml.sequenceOffset=80 xml.typeElement=false
        """
        return self.swCarbDoc

    def createSwDiagnosticsNotes(self, short_name: str) -> Chapter:
        """
        This element contains general information about diagnostics issues within the component. Tags: xml.roleElement=true xml.sequenceOffset=75 xml.typeElement=false
        """
        if self.swDiagnosticsNotes is None:
            self.swDiagnosticsNotes = Chapter(self, short_name)
        return self.swDiagnosticsNotes

    def getSwDiagnosticsNotes(self) -> Optional[Chapter]:
        """
        This element contains general information about diagnostics issues within the component. Tags: xml.roleElement=true xml.sequenceOffset=75 xml.typeElement=false
        """
        return self.swDiagnosticsNotes

    def createSwFeatureDef(self, short_name: str) -> Chapter:
        """
        This element contains the definition of the physical functionality of this software component. This definition is more or less formal and is intended to be delivered from modeling tools. Tags: xml.roleElement=true xml.sequenceOffset=20 xml.typeElement=false
        """
        if self.swFeatureDef is None:
            self.swFeatureDef = Chapter(self, short_name)
        return self.swFeatureDef

    def getSwFeatureDef(self) -> Optional[Chapter]:
        """
        This element contains the definition of the physical functionality of this software component. This definition is more or less formal and is intended to be delivered from modeling tools. Tags: xml.roleElement=true xml.sequenceOffset=20 xml.typeElement=false
        """
        return self.swFeatureDef

    def createSwFeatureDesc(self, short_name: str) -> Chapter:
        """
        This element contains the textual description of the software functionality of this software component. Expert should write this description. Tags: xml.roleElement=true xml.sequenceOffset=30 xml.typeElement=false
        """
        if self.swFeatureDesc is None:
            self.swFeatureDesc = Chapter(self, short_name)
        return self.swFeatureDesc

    def getSwFeatureDesc(self) -> Optional[Chapter]:
        """
        This element contains the textual description of the software functionality of this software component. Expert should write this description. Tags: xml.roleElement=true xml.sequenceOffset=30 xml.typeElement=false
        """
        return self.swFeatureDesc

    def createSwMaintenanceNotes(self, short_name: str) -> Chapter:
        """
        This element contains information regarding the software maintenance of the component. Tags: xml.roleElement=true xml.sequenceOffset=70 xml.typeElement=false
        """
        if self.swMaintenanceNotes is None:
            self.swMaintenanceNotes = Chapter(self, short_name)
        return self.swMaintenanceNotes

    def getSwMaintenanceNotes(self) -> Optional[Chapter]:
        """
        This element contains information regarding the software maintenance of the component. Tags: xml.roleElement=true xml.sequenceOffset=70 xml.typeElement=false
        """
        return self.swMaintenanceNotes

    def createSwTestDesc(self, short_name: str) -> Chapter:
        """
        This element contains suggestions and hints for the test of the software functionality of this software component. Tags: xml.roleElement=true xml.sequenceOffset=50 xml.typeElement=false
        """
        if self.swTestDesc is None:
            self.swTestDesc = Chapter(self, short_name)
        return self.swTestDesc

    def getSwTestDesc(self) -> Optional[Chapter]:
        """
        This element contains suggestions and hints for the test of the software functionality of this software component. Tags: xml.roleElement=true xml.sequenceOffset=50 xml.typeElement=false
        """
        return self.swTestDesc
