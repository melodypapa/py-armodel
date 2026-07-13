"""
This module contains classes for representing AUTOSAR included data types
in software component internal behavior templates.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, RefType
from typing import List

class IncludedDataTypeSet(ARObject):
    """
    A set of data type references that are included in the context of
    a software component internal behavior.
    """
    # IncludedDataTypeSet method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] addDataTypeRef               [x] impl  [x] docstring  [ ] test
    # [ ] getDataTypeRefs              [x] impl  [x] docstring  [ ] test
    # [ ] literalPrefix                [x] impl  [x] docstring  [ ] test
    # [ ] literalPrefix                [x] impl  [x] docstring  [ ] test
    # [ ] getLiteralPrefix             [x] impl  [x] docstring  [ ] test


    def __init__(self):
        super().__init__()

        self.data_type_refs = []            # type: List[RefType]
        self.literal_prefix = None          # type: ARLiteral

    def addDataTypeRef(self, ref_type: RefType):
        """
        Adds a data type reference to the set.

        Args:
            ref_type: The data type reference to add
        """
        self.data_type_refs.append(ref_type)

    def getDataTypeRefs(self) -> List[RefType]:
        """
        Gets the list of data type references.

        Returns:
            List[RefType]: The list of data type references
        """
        return self.data_type_refs

    @property
    def literalPrefix(self) -> ARLiteral:
        """
        Gets the literal prefix for the included data types.

        Returns:
            ARLiteral: The literal prefix
        """
        return self.literal_prefix

    @literalPrefix.setter
    def literalPrefix(self, value: ARLiteral):
        """
        Sets the literal prefix for the included data types.

        Args:
            value: The literal prefix to set
        """
        self.literal_prefix = value

    def getLiteralPrefix(self) -> ARLiteral:
        """
        Gets the literal prefix for the included data types.

        Returns:
            ARLiteral: The literal prefix
        """
        return self.literal_prefix
