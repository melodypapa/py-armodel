"""
This module defines BSW scheduler name prefix in AUTOSAR.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class BswSchedulerNamePrefix(ARObject):
    """
    Represents a BSW scheduler name prefix in AUTOSAR.
    This class defines the prefix used for scheduler names.
    """
    # BswSchedulerNamePrefix method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test
    # [ ] getPrefix                    [x] impl  [ ] docstring  [ ] test
    # [ ] setPrefix                    [x] impl  [ ] docstring  [ ] test


    def __init__(self):
        """
        Initializes the BswSchedulerNamePrefix with default values.
        """
        super().__init__()
        self.prefix: str = None

    def getPrefix(self):
        return self.prefix

    def setPrefix(self, value):
        self.prefix = value
        return self
