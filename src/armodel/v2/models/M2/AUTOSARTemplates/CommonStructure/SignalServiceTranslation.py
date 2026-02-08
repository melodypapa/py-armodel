from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.SignalServiceTranslation.SignalServiceTranslationControlEnum import (
    SignalServiceTranslationControlEnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class SignalServiceTranslationProps(ARObject):
    """
    Package: M2::AUTOSARTemplates::CommonStructure::SignalServiceTranslation
    Represents signal service translation properties in AUTOSAR.
    Defines properties for signal service translation.
    """


    def __init__(self) -> None:
        """
        Initializes the SignalServiceTranslationProps with default values.
        """
        super().__init__()
        self.translationControl: Union[Union[SignalServiceTranslationControlEnum, None] , None] = None

    def getTranslationControl(self) -> Union[SignalServiceTranslationControlEnum, None]:
        """
        Gets the translation control type.

        Returns:
            Signal service translation control enum value
        """
        return self.translationControl

    def setTranslationControl(self, value: SignalServiceTranslationControlEnum) -> "SignalServiceTranslationProps":
        """
        Sets the translation control type.

        Args:
            value: Signal service translation control enum value to set

        Returns:
            self for method chaining
        """
        self.translationControl = value
        return self

from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class SignalServiceTranslationPropsSet(ARObject):
    """
    Package: M2::AUTOSARTemplates::CommonStructure::SignalServiceTranslation
    Represents a set of signal service translation properties in AUTOSAR.
    Defines a collection of signal service translation property sets.
    """


    def __init__(self) -> None:
        """
        Initializes the SignalServiceTranslationPropsSet with default values.
        """
        super().__init__()
        self.translationProps: List[str] = []

    def addTranslationProp(self, prop: str) -> "SignalServiceTranslationPropsSet":
        """
        Adds a translation property to this set.

        Args:
            prop: The translation property to add

        Returns:
            self for method chaining
        """
        self.translationProps.append(prop)
        return self

    def getTranslationProps(self) -> List[str]:
        """
        Gets the list of translation properties.

        Returns:
            List of translation properties
        """
        return self.translationProps

from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class SignalServiceTranslationEventProps(Identifiable):
    """
    This element allows to define the properties which are applicable for the
    signal/service translation event.

    Package: M2::AUTOSARTemplates::CommonStructure::SignalServiceTranslation

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 731, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines properties for a single translated element.
        self._elementProps: List["SignalService"] = []

    @property
    def element_props(self) -> List["SignalService"]:
        """Get elementProps (Pythonic accessor)."""
        return self._elementProps
        # Defined whether the translation shall happen in a safe.
        self._safeTranslation: Optional["Boolean"] = None

    @property
    def safe_translation(self) -> Optional["Boolean"]:
        """Get safeTranslation (Pythonic accessor)."""
        return self._safeTranslation

    @safe_translation.setter
    def safe_translation(self, value: Optional["Boolean"]) -> None:
        """
        Set safeTranslation with validation.

        Args:
            value: The safeTranslation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._safeTranslation = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"safeTranslation must be Boolean or None, got {type(value).__name__}"
            )
        self._safeTranslation = value
        # Defined whether the translation shall happen in a secure.
        self._secure: Optional["Boolean"] = None

    @property
    def secure(self) -> Optional["Boolean"]:
        """Get secure (Pythonic accessor)."""
        return self._secure

    @secure.setter
    def secure(self, value: Optional["Boolean"]) -> None:
        """
        Set secure with validation.

        Args:
            value: The secure to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._secure = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"secure must be Boolean or None, got {type(value).__name__}"
            )
        self._secure = value
        # of signal/service translation.
        # by: VariableDataPrototypeIn.
        self._translation: RefType = None

    @property
    def translation(self) -> RefType:
        """Get translation (Pythonic accessor)."""
        return self._translation

    @translation.setter
    def translation(self, value: RefType) -> None:
        """
        Set translation with validation.

        Args:
            value: The translation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._translation = None
            return

        self._translation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getElementProps(self) -> List["SignalService"]:
        """
        AUTOSAR-compliant getter for elementProps.

        Returns:
            The elementProps value

        Note:
            Delegates to element_props property (CODING_RULE_V2_00017)
        """
        return self.element_props  # Delegates to property

    def getSafeTranslation(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for safeTranslation.

        Returns:
            The safeTranslation value

        Note:
            Delegates to safe_translation property (CODING_RULE_V2_00017)
        """
        return self.safe_translation  # Delegates to property

    def setSafeTranslation(self, value: "Boolean") -> "SignalServiceTranslationEventProps":
        """
        AUTOSAR-compliant setter for safeTranslation with method chaining.

        Args:
            value: The safeTranslation to set

        Returns:
            self for method chaining

        Note:
            Delegates to safe_translation property setter (gets validation automatically)
        """
        self.safe_translation = value  # Delegates to property setter
        return self

    def getSecure(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for secure.

        Returns:
            The secure value

        Note:
            Delegates to secure property (CODING_RULE_V2_00017)
        """
        return self.secure  # Delegates to property

    def setSecure(self, value: "Boolean") -> "SignalServiceTranslationEventProps":
        """
        AUTOSAR-compliant setter for secure with method chaining.

        Args:
            value: The secure to set

        Returns:
            self for method chaining

        Note:
            Delegates to secure property setter (gets validation automatically)
        """
        self.secure = value  # Delegates to property setter
        return self

    def getTranslation(self) -> RefType:
        """
        AUTOSAR-compliant getter for translation.

        Returns:
            The translation value

        Note:
            Delegates to translation property (CODING_RULE_V2_00017)
        """
        return self.translation  # Delegates to property

    def setTranslation(self, value: RefType) -> "SignalServiceTranslationEventProps":
        """
        AUTOSAR-compliant setter for translation with method chaining.

        Args:
            value: The translation to set

        Returns:
            self for method chaining

        Note:
            Delegates to translation property setter (gets validation automatically)
        """
        self.translation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_safe_translation(self, value: Optional["Boolean"]) -> "SignalServiceTranslationEventProps":
        """
        Set safeTranslation and return self for chaining.

        Args:
            value: The safeTranslation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_safe_translation("value")
        """
        self.safe_translation = value  # Use property setter (gets validation)
        return self

    def with_secure(self, value: Optional["Boolean"]) -> "SignalServiceTranslationEventProps":
        """
        Set secure and return self for chaining.

        Args:
            value: The secure to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_secure("value")
        """
        self.secure = value  # Use property setter (gets validation)
        return self

    def with_translation(self, value: Optional[RefType]) -> "SignalServiceTranslationEventProps":
        """
        Set translation and return self for chaining.

        Args:
            value: The translation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_translation("value")
        """
        self.translation = value  # Use property setter (gets validation)
        return self

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class SignalServiceTranslationElementProps(Identifiable):
    """
    Defined translation properties for individual mapped elements.

    Package: M2::AUTOSARTemplates::CommonStructure::SignalServiceTranslation

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 735, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the leaf element the SignalService apply to.
        self._element: RefType = None

    @property
    def element(self) -> RefType:
        """Get element (Pythonic accessor)."""
        return self._element

    @element.setter
    def element(self, value: RefType) -> None:
        """
        Set element with validation.

        Args:
            value: The element to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._element = None
            return

        self._element = value
        # Defines an optional filter to be applied during translation.
        self._filter: Optional["DataFilter"] = None

    @property
    def filter(self) -> Optional["DataFilter"]:
        """Get filter (Pythonic accessor)."""
        return self._filter

    @filter.setter
    def filter(self, value: Optional["DataFilter"]) -> None:
        """
        Set filter with validation.

        Args:
            value: The filter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._filter = None
            return

        if not isinstance(value, DataFilter):
            raise TypeError(
                f"filter must be DataFilter or None, got {type(value).__name__}"
            )
        self._filter = value
        # Defines whether the source element (which is mapped to referenced element)
        # triggers the sending of the.
        self._transmission: Optional["Boolean"] = None

    @property
    def transmission(self) -> Optional["Boolean"]:
        """Get transmission (Pythonic accessor)."""
        return self._transmission

    @transmission.setter
    def transmission(self, value: Optional["Boolean"]) -> None:
        """
        Set transmission with validation.

        Args:
            value: The transmission to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transmission = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"transmission must be Boolean or None, got {type(value).__name__}"
            )
        self._transmission = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getElement(self) -> RefType:
        """
        AUTOSAR-compliant getter for element.

        Returns:
            The element value

        Note:
            Delegates to element property (CODING_RULE_V2_00017)
        """
        return self.element  # Delegates to property

    def setElement(self, value: RefType) -> "SignalServiceTranslationElementProps":
        """
        AUTOSAR-compliant setter for element with method chaining.

        Args:
            value: The element to set

        Returns:
            self for method chaining

        Note:
            Delegates to element property setter (gets validation automatically)
        """
        self.element = value  # Delegates to property setter
        return self

    def getFilter(self) -> "DataFilter":
        """
        AUTOSAR-compliant getter for filter.

        Returns:
            The filter value

        Note:
            Delegates to filter property (CODING_RULE_V2_00017)
        """
        return self.filter  # Delegates to property

    def setFilter(self, value: "DataFilter") -> "SignalServiceTranslationElementProps":
        """
        AUTOSAR-compliant setter for filter with method chaining.

        Args:
            value: The filter to set

        Returns:
            self for method chaining

        Note:
            Delegates to filter property setter (gets validation automatically)
        """
        self.filter = value  # Delegates to property setter
        return self

    def getTransmission(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for transmission.

        Returns:
            The transmission value

        Note:
            Delegates to transmission property (CODING_RULE_V2_00017)
        """
        return self.transmission  # Delegates to property

    def setTransmission(self, value: "Boolean") -> "SignalServiceTranslationElementProps":
        """
        AUTOSAR-compliant setter for transmission with method chaining.

        Args:
            value: The transmission to set

        Returns:
            self for method chaining

        Note:
            Delegates to transmission property setter (gets validation automatically)
        """
        self.transmission = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_element(self, value: Optional[RefType]) -> "SignalServiceTranslationElementProps":
        """
        Set element and return self for chaining.

        Args:
            value: The element to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_element("value")
        """
        self.element = value  # Use property setter (gets validation)
        return self

    def with_filter(self, value: Optional["DataFilter"]) -> "SignalServiceTranslationElementProps":
        """
        Set filter and return self for chaining.

        Args:
            value: The filter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_filter("value")
        """
        self.filter = value  # Use property setter (gets validation)
        return self

    def with_transmission(self, value: Optional["Boolean"]) -> "SignalServiceTranslationElementProps":
        """
        Set transmission and return self for chaining.

        Args:
            value: The transmission to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_transmission("value")
        """
        self.transmission = value  # Use property setter (gets validation)
        return self
