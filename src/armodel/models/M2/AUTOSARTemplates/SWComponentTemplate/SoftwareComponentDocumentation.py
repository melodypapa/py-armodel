from typing import List
from .....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class SwComponentDocumentation(ARObject):
    def __init__(self):
        super().__init__()

        self.chapters = []                              # type: List[Chapter]
        self.swCalibrationNotes = None                  # type: Chapter
        self.swCarbDoc = None                           # type: Chapter
        self.swDiagnosticsNotes = None                  # type: Chapter
        self.swFeatureDef = None                        # type: Chapter
        self.swFeatureDesc = None                       # type: Chapter
        self.swMaintenanceNotes = None                  # type: Chapter
        self.swTestDesc = None                          # type: sChapter

    def getChapters(self):
        return self.chapters

    def addChapter(self, value):
        if value is not None:
            self.chapters.append(value)
        return self

    def getSwCalibrationNotes(self):
        return self.swCalibrationNotes

    def setSwCalibrationNotes(self, value):
        if value is not None:
            self.swCalibrationNotes = value
        return self

    def getSwCarbDoc(self):
        return self.swCarbDoc

    def setSwCarbDoc(self, value):
        if value is not None:
            self.swCarbDoc = value
        return self

    def getSwDiagnosticsNotes(self):
        return self.swDiagnosticsNotes

    def setSwDiagnosticsNotes(self, value):
        if value is not None:
            self.swDiagnosticsNotes = value
        return self

    def getSwFeatureDef(self):
        return self.swFeatureDef

    def setSwFeatureDef(self, value):
        if value is not None:
            self.swFeatureDef = value
        return self

    def getSwFeatureDesc(self):
        return self.swFeatureDesc

    def setSwFeatureDesc(self, value):
        if value is not None:
            self.swFeatureDesc = value
        return self

    def getSwMaintenanceNotes(self):
        return self.swMaintenanceNotes

    def setSwMaintenanceNotes(self, value):
        if value is not None:
            self.swMaintenanceNotes = value
        return self

    def getSwTestDesc(self):
        return self.swTestDesc

    def setSwTestDesc(self, value):
        if value is not None:
            self.swTestDesc = value
        return self
