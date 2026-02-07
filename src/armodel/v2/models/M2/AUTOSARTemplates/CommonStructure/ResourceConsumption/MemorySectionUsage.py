"""
This module contains the MemorySection class for representing
memory section usage in AUTOSAR resource consumption models.
"""

from typing import List, Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    RefType,
)


class MemorySection(Identifiable):
    """
    Represents a memory section in AUTOSAR models.
    This class defines memory section properties including alignment, size, and addressing methods.
    """

    def __init__(self, parent: ARObject, short_name: str) -> None:
        """
        Initializes the MemorySection with a parent and short name.

        Args:
            parent: The parent ARObject that contains this memory section
            short_name: The unique short name of this memory section
        """
        super().__init__(parent, short_name)

        # Private alignment value for this memory section
        self._alignment: Union[Union[ARLiteral, None] , None] = None
        # Memory class symbol for this memory section
        self.memClassSymbol: Union[Union[ARLiteral, None] , None] = None
        # Size of this memory section
        self.size = None
        # List of options for this memory section
        self.options: List[ARLiteral] = []
        # Reference to the software address method for this memory section
        self.swAddrMethodRef: Union[Union[RefType, None] , None] = None
        # Symbol name for this memory section
        self.symbol: Union[Union[ARLiteral, None] , None] = None

    def getAlignment(self):
        """
        Gets the alignment value for this memory section through the property getter.

        Returns:
            ARLiteral: Alignment value
        """
        return self.alignment

    def setAlignment(self, value):
        """
        Sets the alignment value for this memory section through the property setter.

        Args:
            value: The alignment value to set

        Returns:
            self for method chaining
        """
        self.alignment = value
        return self

    def getMemClassSymbol(self):
        """
        Gets the memory class symbol for this memory section.

        Returns:
            ARLiteral: Memory class symbol
        """
        return self.memClassSymbol

    def setMemClassSymbol(self, value):
        """
        Sets the memory class symbol for this memory section.

        Args:
            value: The memory class symbol to set

        Returns:
            self for method chaining
        """
        self.memClassSymbol = value
        return self

    def getSize(self):
        """
        Gets the size of this memory section.

        Returns:
            Size value of the memory section
        """
        return self.size

    def setSize(self, value):
        """
        Sets the size of this memory section.

        Args:
            value: The size value to set

        Returns:
            self for method chaining
        """
        self.size = value
        return self

    def getSwAddrMethodRef(self):
        """
        Gets the reference to the software address method for this memory section.

        Returns:
            RefType: Reference to the software address method
        """
        return self.swAddrMethodRef

    def setSwAddrMethodRef(self, value):
        """
        Sets the reference to the software address method for this memory section.

        Args:
            value: The reference to the software address method to set

        Returns:
            self for method chaining
        """
        self.swAddrMethodRef = value
        return self

    def getSymbol(self):
        """
        Gets the symbol name for this memory section.

        Returns:
            ARLiteral: Symbol name
        """
        return self.symbol

    def setSymbol(self, value):
        """
        Sets the symbol name for this memory section.

        Args:
            value: The symbol name to set

        Returns:
            self for method chaining
        """
        self.symbol = value
        return self

    @property
    def alignment(self) -> ARLiteral:
        """
        Gets the alignment value for this memory section.

        Returns:
            ARLiteral: Alignment value
        """
        return self._alignment

    @alignment.setter
    def alignment(self, value: ARLiteral) -> None:
        """
        Sets the alignment value for this memory section with validation.
        Note: The validation code is commented out but kept for reference.

        Args:
            value: The alignment value to set
        """
        r'''
        if value is not None and value.getValue() != "":
            match = False
            if value.getValue() in ("UNKNOWN", "UNSPECIFIED", "BOOLEAN", "PTR"):
                self._alignment = value
                match = True
            else:
                m = re.match(r'^\d+', value.value)
                if m:
                    self._alignment = value
                    match = True

            if not match:
                raise ValueError("Invalid alignment <%s> of memory section <%s>" % (value, self.getShortName()))
        '''
        if value is not None:
            self._alignment = value

    def addOption(self, option: ARLiteral) -> None:
        """
        Adds an option to the list of options for this memory section.

        Args:
            option: The option to add
        """
        self.options.append(option)

    def getOptions(self) -> List[ARLiteral]:
        """
        Gets the list of options for this memory section.

        Returns:
            List of ARLiteral options
        """
        return self.options


class SectionNamePrefix(ARObject):
    """
    Represents a section name prefix in AUTOSAR memory section usage.
    Defines a prefix for memory section names.
    """


    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        """
        Initializes the SectionNamePrefix with default values.
        """
        super().__init__()
        self.prefix: Union[str, None] = None

    def getPrefix(self) -> str:
        """
        Gets the section name prefix.

        Returns:
            String representing the prefix
        """
        return self.prefix

    def setPrefix(self, value: str):
        """
        Sets the section name prefix.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.prefix = value
        return self
