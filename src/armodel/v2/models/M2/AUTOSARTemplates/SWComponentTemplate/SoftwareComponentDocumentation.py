"""
This module contains classes for representing AUTOSAR software component documentation
elements in software component templates.
"""

from typing import List, Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.MSR.Documentation.Chapters import Chapter


class SwComponentDocumentation(ARObject):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.chapters: List[Chapter] = []
        self.swCalibrationNotes: Union[Chapter, None] = None
        self.swCarbDoc: Union[Chapter, None] = None
        self.swDiagnosticsNotes: Union[Chapter, None] = None
        self.swFeatureDef: Union[Chapter, None] = None
        self.swFeatureDesc: Union[Chapter, None] = None
        self.swMaintenanceNotes: Union[Chapter, None] = None
        self.swTestDesc: Union[Chapter, None] = None

    def getChapters(self) -> List[Chapter]:
        return self.chapters

    def addChapter(self, value: Chapter):
        if value is not None:
            self.chapters.append(value)
        return self

    def getSwCalibrationNotes(self) -> Union[Chapter, None]:
        return self.swCalibrationNotes

    def setSwCalibrationNotes(self, value: Chapter):
        if value is not None:
            self.swCalibrationNotes = value
        return self

    def getSwCarbDoc(self) -> Union[Chapter, None]:
        return self.swCarbDoc

    def setSwCarbDoc(self, value: Chapter):
        if value is not None:
            self.swCarbDoc = value
        return self

    def getSwDiagnosticsNotes(self) -> Union[Chapter, None]:
        return self.swDiagnosticsNotes

    def setSwDiagnosticsNotes(self, value: Chapter):
        if value is not None:
            self.swDiagnosticsNotes = value
        return self

    def getSwFeatureDef(self) -> Union[Chapter, None]:
        return self.swFeatureDef

    def setSwFeatureDef(self, value: Chapter):
        if value is not None:
            self.swFeatureDef = value
        return self

    def getSwFeatureDesc(self) -> Union[Chapter, None]:
        return self.swFeatureDesc

    def setSwFeatureDesc(self, value: Chapter):
        if value is not None:
            self.swFeatureDesc = value
        return self

    def getSwMaintenanceNotes(self) -> Union[Chapter, None]:
        return self.swMaintenanceNotes

    def setSwMaintenanceNotes(self, value: Chapter):
        if value is not None:
            self.swMaintenanceNotes = value
        return self

    def getSwTestDesc(self) -> Union[Chapter, None]:
        return self.swTestDesc

    def setSwTestDesc(self, value: Chapter):
        if value is not None:
            self.swTestDesc = value
        return self
