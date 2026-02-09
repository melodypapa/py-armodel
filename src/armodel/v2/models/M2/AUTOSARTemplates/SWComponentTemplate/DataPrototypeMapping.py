from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class DataPrototypeMapping(ARObject):
    """
    Defines the mapping of two particular VariableDataPrototypes,
    ParameterDataPrototypes or Argument DataPrototypes with non-equal
    shortNames, non-equal structure (specific condition is described by
    [constr_1187]), and/or non-equal semantic (resolution or range) in context
    of two different Sender ReceiverInterface, NvDataInterface or
    ParameterInterface or Operations. If the semantic is unequal, the following
    rules apply: The textTableMapping is only applicable if the referred
    DataPrototypes are typed by AutosarDataType referring to CompuMethods of
    category TEXTTABLE, SCALE_LINEAR_AND_TEXTTABLE or BITFIELD_TEXTTABLE. In the
    case that the DataPrototypes are typed by AutosarDataType either referring
    to CompuMethods of category LINEAR, IDENTICAL or referring to no CompuMethod
    (which is similar as IDENTICAL) the linear conversion factor is calculated
    out of the factorSiToUnit and offsetSiToUnit attributes of the referred
    Units and the CompuRationalCoeffs of a compuInternalToPhys of the referred
    CompuMethods.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 125, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2014, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # First to be mapped DataPrototype in context of a Sender NvDataInterface,
        # ParameterInterface.
        self._firstData: RefType = None

    @property
    def first_data(self) -> RefType:
        """Get firstData (Pythonic accessor)."""
        return self._firstData

    @first_data.setter
    def first_data(self, value: RefType) -> None:
        """
        Set firstData with validation.

        Args:
            value: The firstData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._firstData = None
            return

        self._firstData = value
        # This reference defines the need to execute the Data <Mip>_<transformerId>
                # functions of the chain when communicating from the Data the Data also
                # specifies the reverse Data functions of chain (i.
        # e.
        # from the DataPrototype the DataPrototype the referenced Data symmetric, i.
        # e.
        # attribute Data set to.
        self._firstToSecond: Optional["DataTransformation"] = None

    @property
    def first_to_second(self) -> Optional["DataTransformation"]:
        """Get firstToSecond (Pythonic accessor)."""
        return self._firstToSecond

    @first_to_second.setter
    def first_to_second(self, value: Optional["DataTransformation"]) -> None:
        """
        Set firstToSecond with validation.

        Args:
            value: The firstToSecond to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._firstToSecond = None
            return

        if not isinstance(value, DataTransformation):
            raise TypeError(
                f"firstToSecond must be DataTransformation or None, got {type(value).__name__}"
            )
        self._firstToSecond = value
        # Second to be mapped DataPrototype in context of a NvDataInterface, Parameter
        # Operation.
        self._secondData: RefType = None

    @property
    def second_data(self) -> RefType:
        """Get secondData (Pythonic accessor)."""
        return self._secondData

    @second_data.setter
    def second_data(self, value: RefType) -> None:
        """
        Set secondData with validation.

        Args:
            value: The secondData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._secondData = None
            return

        self._secondData = value
        # This defines the need to execute the reverse Data <Mip>_Inv_<transformerId>
        # functions of transformation chain when communicating from the the Data.
        self._secondToFirst: Optional["DataTransformation"] = None

    @property
    def second_to_first(self) -> Optional["DataTransformation"]:
        """Get secondToFirst (Pythonic accessor)."""
        return self._secondToFirst

    @second_to_first.setter
    def second_to_first(self, value: Optional["DataTransformation"]) -> None:
        """
        Set secondToFirst with validation.

        Args:
            value: The secondToFirst to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._secondToFirst = None
            return

        if not isinstance(value, DataTransformation):
            raise TypeError(
                f"secondToFirst must be DataTransformation or None, got {type(value).__name__}"
            )
        self._secondToFirst = value
        # This represents the owned SubelementMapping.
        # atpSplitable.
        self._subElement: List[RefType] = []

    @property
    def sub_element(self) -> List[RefType]:
        """Get subElement (Pythonic accessor)."""
        return self._subElement
        self._textTable: RefType = None

    @property
    def text_table(self) -> RefType:
        """Get textTable (Pythonic accessor)."""
        return self._textTable

    @text_table.setter
    def text_table(self, value: RefType) -> None:
        """
        Set textTable with validation.

        Args:
            value: The textTable to set

        Raises:
            TypeError: If value type is incorrect
        """
        self._textTable = value

    def with_sub_element(self, value):
        """
        Set sub_element and return self for chaining.

        Args:
            value: The sub_element to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sub_element("value")
        """
        self.sub_element = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFirstData(self) -> RefType:
        """
        AUTOSAR-compliant getter for firstData.

        Returns:
            The firstData value

        Note:
            Delegates to first_data property (CODING_RULE_V2_00017)
        """
        return self.first_data  # Delegates to property

    def setFirstData(self, value: RefType) -> "DataPrototypeMapping":
        """
        AUTOSAR-compliant setter for firstData with method chaining.

        Args:
            value: The firstData to set

        Returns:
            self for method chaining

        Note:
            Delegates to first_data property setter (gets validation automatically)
        """
        self.first_data = value  # Delegates to property setter
        return self

    def getFirstToSecond(self) -> "DataTransformation":
        """
        AUTOSAR-compliant getter for firstToSecond.

        Returns:
            The firstToSecond value

        Note:
            Delegates to first_to_second property (CODING_RULE_V2_00017)
        """
        return self.first_to_second  # Delegates to property

    def setFirstToSecond(self, value: "DataTransformation") -> "DataPrototypeMapping":
        """
        AUTOSAR-compliant setter for firstToSecond with method chaining.

        Args:
            value: The firstToSecond to set

        Returns:
            self for method chaining

        Note:
            Delegates to first_to_second property setter (gets validation automatically)
        """
        self.first_to_second = value  # Delegates to property setter
        return self

    def getSecondData(self) -> RefType:
        """
        AUTOSAR-compliant getter for secondData.

        Returns:
            The secondData value

        Note:
            Delegates to second_data property (CODING_RULE_V2_00017)
        """
        return self.second_data  # Delegates to property

    def setSecondData(self, value: RefType) -> "DataPrototypeMapping":
        """
        AUTOSAR-compliant setter for secondData with method chaining.

        Args:
            value: The secondData to set

        Returns:
            self for method chaining

        Note:
            Delegates to second_data property setter (gets validation automatically)
        """
        self.second_data = value  # Delegates to property setter
        return self

    def getSecondToFirst(self) -> "DataTransformation":
        """
        AUTOSAR-compliant getter for secondToFirst.

        Returns:
            The secondToFirst value

        Note:
            Delegates to second_to_first property (CODING_RULE_V2_00017)
        """
        return self.second_to_first  # Delegates to property

    def setSecondToFirst(self, value: "DataTransformation") -> "DataPrototypeMapping":
        """
        AUTOSAR-compliant setter for secondToFirst with method chaining.

        Args:
            value: The secondToFirst to set

        Returns:
            self for method chaining

        Note:
            Delegates to second_to_first property setter (gets validation automatically)
        """
        self.second_to_first = value  # Delegates to property setter
        return self

    def getSubElement(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for subElement.

        Returns:
            The subElement value

        Note:
            Delegates to sub_element property (CODING_RULE_V2_00017)
        """
        return self.sub_element  # Delegates to property

    def getTextTable(self) -> RefType:
        """
        AUTOSAR-compliant getter for textTable.

        Returns:
            The textTable value

        Note:
            Delegates to text_table property (CODING_RULE_V2_00017)
        """
        return self.text_table  # Delegates to property

    def setTextTable(self, value: RefType) -> "DataPrototypeMapping":
        """
        AUTOSAR-compliant setter for textTable with method chaining.

        Args:
            value: The textTable to set

        Returns:
            self for method chaining

        Note:
            Delegates to text_table property setter (gets validation automatically)
        """
        self.text_table = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_first_data(self, value: Optional[RefType]) -> "DataPrototypeMapping":
        """
        Set firstData and return self for chaining.

        Args:
            value: The firstData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_first_data("value")
        """
        self.first_data = value  # Use property setter (gets validation)
        return self

    def with_first_to_second(self, value: Optional["DataTransformation"]) -> "DataPrototypeMapping":
        """
        Set firstToSecond and return self for chaining.

        Args:
            value: The firstToSecond to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_first_to_second("value")
        """
        self.first_to_second = value  # Use property setter (gets validation)
        return self

    def with_second_data(self, value: Optional[RefType]) -> "DataPrototypeMapping":
        """
        Set secondData and return self for chaining.

        Args:
            value: The secondData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_second_data("value")
        """
        self.second_data = value  # Use property setter (gets validation)
        return self

    def with_second_to_first(self, value: Optional["DataTransformation"]) -> "DataPrototypeMapping":
        """
        Set secondToFirst and return self for chaining.

        Args:
            value: The secondToFirst to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_second_to_first("value")
        """
        self.second_to_first = value  # Use property setter (gets validation)
        return self

    def with_text_table(self, value: RefType) -> "DataPrototypeMapping":
        """
        Set textTable and return self for chaining.

        Args:
            value: The textTable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_text_table("value")
        """
        self.text_table = value  # Use property setter (gets validation)
        return self
