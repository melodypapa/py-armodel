"""
This module contains the SwComponentDocumentation class for AUTOSAR software
component templates (spec M2::AUTOSARTemplates::SWComponentTemplate::SoftwareComponentDocumentation).

The Chapter family it aggregates (Chapter, ChapterModel, ChapterContent,
ChapterOrMsrQuery, TopicOrMsrQuery) lives in its own package
M2::MSR::Documentation::Chapters (see src/armodel/models/M2/MSR/Documentation/Chapters.py).
"""

from __future__ import annotations
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.MSR.Documentation.Chapters import Chapter


class SwComponentDocumentation(ARObject, VariationPointCapable):
    """
    This class specifies the ability to write dedicated documentation to a component type according to ASAM FSX.
    """

    # SwComponentDocumentation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 12.1, p.698
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] createChapter            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getChapters              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createSwCalibrationNotes [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwCalibrationNotes    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createSwCarbDoc          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwCarbDoc             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createSwDiagnosticsNotes [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwDiagnosticsNotes    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createSwFeatureDef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwFeatureDef          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createSwFeatureDesc      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwFeatureDesc         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createSwMaintenanceNotes [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwMaintenanceNotes    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createSwTestDesc         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwTestDesc            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self):
        super().__init__()

        # These chapters provide additional information about the software component that do not fit in the other chapters. Note that this is subject to variation because Chapter aggregations in the role chapter are variant within the documentation in general.
        self.chapters: List[Chapter] = []

        # This element contains calibration instructions and hints for a calibration engineer.
        self.swCalibrationNotes: Optional[Chapter] = None

        # This element records the documentation requested by CARB.
        self.swCarbDoc: Optional[Chapter] = None

        # This element contains general information about diagnostics issues within the component.
        self.swDiagnosticsNotes: Optional[Chapter] = None

        # This element contains the definition of the physical functionality of this software component. This definition is more or less formal and is intended to be delivered from modeling tools.
        self.swFeatureDef: Optional[Chapter] = None

        # This element contains the textual description of the software functionality of this software component. Expert should write this description.
        self.swFeatureDesc: Optional[Chapter] = None

        # This element contains information regarding the software maintenance of the component.
        self.swMaintenanceNotes: Optional[Chapter] = None

        # This element contains suggestions and hints for the test of the software functionality of this software component.
        self.swTestDesc: Optional[Chapter] = None

    def createChapter(self, short_name: str) -> Chapter:
        """
        These chapters provide additional information about the software component that do not fit in the other chapters. Note that this is subject to variation because Chapter aggregations in the role chapter are variant within the documentation in general.

        Creates a new Chapter for the chapter attribute with the given short name, or returns the existing one if it already exists.

        Args:
            short_name: The short name for the new Chapter

        Returns:
            The created (or existing) Chapter
        """
        for chapter in self.chapters:
            if chapter.getShortName() == short_name:
                return chapter
        chapter = Chapter(self, short_name)
        self.chapters.append(chapter)
        return chapter

    def getChapters(self) -> List[Chapter]:
        """
        These chapters provide additional information about the software component that do not fit in the other chapters. Note that this is subject to variation because Chapter aggregations in the role chapter are variant within the documentation in general.

        Returns:
            List of Chapter instances
        """
        return self.chapters

    def createSwCalibrationNotes(self, short_name: str) -> Chapter:
        """
        This element contains calibration instructions and hints for a calibration engineer.

        Creates a new Chapter for the swCalibrationNotes attribute with the given short name, or returns the existing one if already set.

        Args:
            short_name: The short name for the new Chapter

        Returns:
            The created (or existing) Chapter
        """
        if self.swCalibrationNotes is None:
            self.swCalibrationNotes = Chapter(self, short_name)
        return self.swCalibrationNotes

    def getSwCalibrationNotes(self) -> Optional[Chapter]:
        """
        This element contains calibration instructions and hints for a calibration engineer.

        Returns:
            Chapter, or None if not set
        """
        return self.swCalibrationNotes

    def createSwCarbDoc(self, short_name: str) -> Chapter:
        """
        This element records the documentation requested by CARB.

        Creates a new Chapter for the swCarbDoc attribute with the given short name, or returns the existing one if already set.

        Args:
            short_name: The short name for the new Chapter

        Returns:
            The created (or existing) Chapter
        """
        if self.swCarbDoc is None:
            self.swCarbDoc = Chapter(self, short_name)
        return self.swCarbDoc

    def getSwCarbDoc(self) -> Optional[Chapter]:
        """
        This element records the documentation requested by CARB.

        Returns:
            Chapter, or None if not set
        """
        return self.swCarbDoc

    def createSwDiagnosticsNotes(self, short_name: str) -> Chapter:
        """
        This element contains general information about diagnostics issues within the component.

        Creates a new Chapter for the swDiagnosticsNotes attribute with the given short name, or returns the existing one if already set.

        Args:
            short_name: The short name for the new Chapter

        Returns:
            The created (or existing) Chapter
        """
        if self.swDiagnosticsNotes is None:
            self.swDiagnosticsNotes = Chapter(self, short_name)
        return self.swDiagnosticsNotes

    def getSwDiagnosticsNotes(self) -> Optional[Chapter]:
        """
        This element contains general information about diagnostics issues within the component.

        Returns:
            Chapter, or None if not set
        """
        return self.swDiagnosticsNotes

    def createSwFeatureDef(self, short_name: str) -> Chapter:
        """
        This element contains the definition of the physical functionality of this software component. This definition is more or less formal and is intended to be delivered from modeling tools.

        Creates a new Chapter for the swFeatureDef attribute with the given short name, or returns the existing one if already set.

        Args:
            short_name: The short name for the new Chapter

        Returns:
            The created (or existing) Chapter
        """
        if self.swFeatureDef is None:
            self.swFeatureDef = Chapter(self, short_name)
        return self.swFeatureDef

    def getSwFeatureDef(self) -> Optional[Chapter]:
        """
        This element contains the definition of the physical functionality of this software component. This definition is more or less formal and is intended to be delivered from modeling tools.

        Returns:
            Chapter, or None if not set
        """
        return self.swFeatureDef

    def createSwFeatureDesc(self, short_name: str) -> Chapter:
        """
        This element contains the textual description of the software functionality of this software component. Expert should write this description.

        Creates a new Chapter for the swFeatureDesc attribute with the given short name, or returns the existing one if already set.

        Args:
            short_name: The short name for the new Chapter

        Returns:
            The created (or existing) Chapter
        """
        if self.swFeatureDesc is None:
            self.swFeatureDesc = Chapter(self, short_name)
        return self.swFeatureDesc

    def getSwFeatureDesc(self) -> Optional[Chapter]:
        """
        This element contains the textual description of the software functionality of this software component. Expert should write this description.

        Returns:
            Chapter, or None if not set
        """
        return self.swFeatureDesc

    def createSwMaintenanceNotes(self, short_name: str) -> Chapter:
        """
        This element contains information regarding the software maintenance of the component.

        Creates a new Chapter for the swMaintenanceNotes attribute with the given short name, or returns the existing one if already set.

        Args:
            short_name: The short name for the new Chapter

        Returns:
            The created (or existing) Chapter
        """
        if self.swMaintenanceNotes is None:
            self.swMaintenanceNotes = Chapter(self, short_name)
        return self.swMaintenanceNotes

    def getSwMaintenanceNotes(self) -> Optional[Chapter]:
        """
        This element contains information regarding the software maintenance of the component.

        Returns:
            Chapter, or None if not set
        """
        return self.swMaintenanceNotes

    def createSwTestDesc(self, short_name: str) -> Chapter:
        """
        This element contains suggestions and hints for the test of the software functionality of this software component.

        Creates a new Chapter for the swTestDesc attribute with the given short name, or returns the existing one if already set.

        Args:
            short_name: The short name for the new Chapter

        Returns:
            The created (or existing) Chapter
        """
        if self.swTestDesc is None:
            self.swTestDesc = Chapter(self, short_name)
        return self.swTestDesc

    def getSwTestDesc(self) -> Optional[Chapter]:
        """
        This element contains suggestions and hints for the test of the software functionality of this software component.

        Returns:
            Chapter, or None if not set
        """
        return self.swTestDesc
