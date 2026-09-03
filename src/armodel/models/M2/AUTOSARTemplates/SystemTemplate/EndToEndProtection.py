# This module contains the EndToEndProtection package classes for SystemTemplate
# (M2::AUTOSARTemplates::SystemTemplate::EndToEndProtection).

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, RefType


class EndToEndProtectionISignalIPdu(ARObject, VariationPointCapable):
    """
    Defines to which ISignalIPdu-ISignalGroup pair an EndToEndProtection
    applies.
    """

    # EndToEndProtectionISignalIPdu method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDataOffset                [x] impl  [x] docstring  [ ] test
    # [ ] setDataOffset                [x] impl  [x] docstring  [ ] test
    # [ ] getISignalGroupRef           [x] impl  [x] docstring  [ ] test
    # [ ] setISignalGroupRef           [x] impl  [x] docstring  [ ] test
    # [ ] getISignalIPduRef            [x] impl  [x] docstring  [ ] test
    # [ ] setISignalIPduRef            [x] impl  [x] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.dataOffset: Integer = None
        self.iSignalGroupRef: RefType = None
        self.iSignalIPduRef: RefType = None

    def getDataOffset(self):
        """
        Gets the data offset.

        Returns:
            Integer: The data offset
        """
        return self.dataOffset

    def setDataOffset(self, value):
        """
        Sets the data offset.

        Args:
            value: The data offset to set

        Returns:
            self for method chaining
        """
        self.dataOffset = value
        return self

    def getISignalGroupRef(self):
        """
        Gets the ISignalGroup reference.

        Returns:
            RefType: The ISignalGroup reference
        """
        return self.iSignalGroupRef

    def setISignalGroupRef(self, value):
        """
        Sets the ISignalGroup reference.

        Args:
            value: The ISignalGroup reference to set

        Returns:
            self for method chaining
        """
        self.iSignalGroupRef = value
        return self

    def getISignalIPduRef(self):
        """
        Gets the ISignalIPdu reference.

        Returns:
            RefType: The ISignalIPdu reference
        """
        return self.iSignalIPduRef

    def setISignalIPduRef(self, value):
        """
        Sets the ISignalIPdu reference.

        Args:
            value: The ISignalIPdu reference to set

        Returns:
            self for method chaining
        """
        self.iSignalIPduRef = value
        return self
