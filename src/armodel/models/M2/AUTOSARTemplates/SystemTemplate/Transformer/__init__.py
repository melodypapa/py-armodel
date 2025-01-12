from typing import List
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement

class DataTransformationSet(ARElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.dataTransformations = []                       # type: List[DataTransformation]
        self.transformationTechnology = []                  # type: List[TransformationTechnology]

    def getDataTransformations(self):
        return self.dataTransformations

    def setDataTransformations(self, value):
        if value is not None:
            self.dataTransformations = value
        return self

    def getTransformationTechnology(self):
        return self.transformationTechnology

    def setTransformationTechnology(self, value):
        if value is not None:
            self.transformationTechnology = value
        return self
