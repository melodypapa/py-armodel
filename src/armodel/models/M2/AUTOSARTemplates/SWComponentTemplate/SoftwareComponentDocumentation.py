"""
This module contains classes for representing AUTOSAR software component documentation
elements in software component templates.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class SwComponentDocumentation(ARObject):
    """
    Documentation for a software component including chapters, calibration
    notes, diagnostics notes, feature descriptions, and test descriptions.
    """

    def __init__(self):
        super().__init__()

        self.chapters = []
        self.swCalibrationNotes = None
        self.swCarbDoc = None
        self.swDiagnosticsNotes = None
        self.swFeatureDef = None
        self.swFeatureDesc = None
        self.swMaintenanceNotes = None
        self.swTestDesc = None

    def getChapters(self):
        """
        Gets the list of documentation chapters.

        Returns:
            The list of chapters
        """
        return self.chapters

    def addChapter(self, value):
        """
        Adds a documentation chapter.

        Args:
            value: The chapter to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.chapters.append(value)
        return self

    def getSwCalibrationNotes(self):
        """
        Gets the software calibration notes.

        Returns:
            The software calibration notes
        """
        return self.swCalibrationNotes

    def setSwCalibrationNotes(self, value):
        """
        Sets the software calibration notes.

        Args:
            value: The calibration notes to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.swCalibrationNotes = value
        return self

    def getSwCarbDoc(self):
        """
        Gets the software carbon documentation.

        Returns:
            The software carbon documentation
        """
        return self.swCarbDoc

    def setSwCarbDoc(self, value):
        """
        Sets the software carbon documentation.

        Args:
            value: The carbon documentation to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.swCarbDoc = value
        return self

    def getSwDiagnosticsNotes(self):
        """
        Gets the software diagnostics notes.

        Returns:
            The software diagnostics notes
        """
        return self.swDiagnosticsNotes

    def setSwDiagnosticsNotes(self, value):
        """
        Sets the software diagnostics notes.

        Args:
            value: The diagnostics notes to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.swDiagnosticsNotes = value
        return self

    def getSwFeatureDef(self):
        """
        Gets the software feature definition.

        Returns:
            The software feature definition
        """
        return self.swFeatureDef

    def setSwFeatureDef(self, value):
        """
        Sets the software feature definition.

        Args:
            value: The feature definition to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.swFeatureDef = value
        return self

    def getSwFeatureDesc(self):
        """
        Gets the software feature description.

        Returns:
            The software feature description
        """
        return self.swFeatureDesc

    def setSwFeatureDesc(self, value):
        """
        Sets the software feature description.

        Args:
            value: The feature description to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.swFeatureDesc = value
        return self

    def getSwMaintenanceNotes(self):
        """
        Gets the software maintenance notes.

        Returns:
            The software maintenance notes
        """
        return self.swMaintenanceNotes

    def setSwMaintenanceNotes(self, value):
        """
        Sets the software maintenance notes.

        Args:
            value: The maintenance notes to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.swMaintenanceNotes = value
        return self

    def getSwTestDesc(self):
        """
        Gets the software test description.

        Returns:
            The software test description
        """
        return self.swTestDesc

    def setSwTestDesc(self, value):
        """
        Sets the software test description.

        Args:
            value: The test description to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.swTestDesc = value
        return self
