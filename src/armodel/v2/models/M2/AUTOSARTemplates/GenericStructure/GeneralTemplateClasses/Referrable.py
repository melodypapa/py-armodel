"""
AUTOSAR Package - Referrable

Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Referrable
"""


from __future__ import annotations
from abc import (
    ABC,
)
from typing import (
    List,
    Optional,
    TYPE_CHECKING,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    String,
)

if TYPE_CHECKING:
    from armodel.v2.models.M2.MSR.Documentation.TextModel.MultilanguageData import (
        MultilanguageLongName,
    )
    from armodel.v2.models.M2.MSR.Documentation.TextModel.SingleLanguageData import (
        SingleLanguageLongName,
    )


class Referrable(ARObject, ABC):
    """
    Instances of this class can be referred to by their identifier (while
    adhering to namespace borders).

    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable::Referrable

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 328, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 328, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 305, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 63, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 1002, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2049, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 238, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_ARXMLSerializationRules.pdf (Page 31, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 49, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 78, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 63, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (Page 33, Foundation R23-11)
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 66, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 202, Foundation
      R23-11)
    """
    def __init__(self) -> None:
        if type(self) is Referrable:
            raise TypeError("Referrable is an abstract class.")
        super().__init__()

        # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This specifies an identifying shortName for the object.
        # It needs to be unique within its context and is intended for humans but even
        # more for technical reference.
        self._shortName: Optional["Identifier"] = None
        # This specifies how the Referrable.
        # shortName is of several shortNameFragments.
        self._shortNameFragment: List[ShortNameFragment] = []

    @property
    def short_name(self) -> Optional["Identifier"]:
        """Get shortName (Pythonic accessor)."""
        return self._shortName

    @short_name.setter
    def short_name(self, value: "Identifier") -> None:
        """
        Set shortName with validation.

        Args:
            value: The shortName to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"shortName must be Identifier or str, got {type(value).__name__}"
            )
        # Always store as Identifier instance
        if isinstance(value, str):
            identifier = Identifier()
            identifier.value = value
            self._shortName = identifier
        else:
            self._shortName = value

    @property
    def short_name_fragment(self) -> List[ShortNameFragment]:
        """Get shortNameFragment (Pythonic accessor)."""
        return self._shortNameFragment

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getShortNameFragment(self) -> List[ShortNameFragment]:
        """
        AUTOSAR-compliant getter for shortNameFragment.

        Returns:
            The shortNameFragment value

        Note:
            Delegates to short_name_fragment property (CODING_RULE_V2_00017)
        """
        return self.short_name_fragment  # Delegates to property

    def getShortName(self) -> Optional["Identifier"]:
        """
        AUTOSAR-compliant getter for shortName.

        Returns:
            The shortName value

        Note:
            Delegates to short_name property (CODING_RULE_V2_00017)
        """
        return self.short_name  # Delegates to property

    def setShortName(self, value: "Identifier") -> Referrable:
        """
        AUTOSAR-compliant setter for shortName with method chaining.

        Args:
            value: The shortName to set

        Returns:
            self for method chaining

        Note:
            Delegates to short_name property setter (gets validation automatically)
        """
        self.short_name = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_short_name(self, value: "Identifier") -> Referrable:
        """
        Set shortName and return self for chaining.

        Args:
            value: The shortName to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_short_name("value")
        """
        self.short_name = value  # Use property setter (gets validation)
        return self


class MultilanguageReferrable(Referrable, ABC):
    """
    Instances of this class can be referred to by their identifier (while
    adhering to namespace borders). They also may have a longName. But they are
    not considered to contribute substantially to the overall structure of an
    AUTOSAR description. In particular it does not contain other Referrables.

    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable::MultilanguageReferrable

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 179, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 301, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 1000, Classic
      Platform R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 48, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 75, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 63, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 197, Foundation
      R23-11)
    """
    def __init__(self) -> None:
        if type(self) is MultilanguageReferrable:
            raise TypeError("MultilanguageReferrable is an abstract class.")
        super().__init__()

        # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This specifies the long name of the object.
        # Long name is to human readers and acts like a headline.
        self._longName: Optional["MultilanguageLongName"] = None

    @property
    def long_name(self) -> Optional["MultilanguageLongName"]:
        """Get longName (Pythonic accessor)."""
        return self._longName

    @long_name.setter
    def long_name(self, value: Optional["MultilanguageLongName"]) -> None:
        """
        Set longName with validation.

        Args:
            value: The longName to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._longName = None
            return

        if value is not None and not hasattr(value, 'longName'):
            raise TypeError(
                f"longName must be MultilanguageLongName or None, got {type(value).__name__}"
            )
        self._longName = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLongName(self) -> Optional["MultilanguageLongName"]:
        """
        AUTOSAR-compliant getter for longName.

        Returns:
            The longName value

        Note:
            Delegates to long_name property (CODING_RULE_V2_00017)
        """
        return self.long_name  # Delegates to property

    def setLongName(self, value: "MultilanguageLongName") -> MultilanguageReferrable:
        """
        AUTOSAR-compliant setter for longName with method chaining.

        Args:
            value: The longName to set

        Returns:
            self for method chaining

        Note:
            Delegates to long_name property setter (gets validation automatically)
        """
        self.long_name = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_long_name(self, value: Optional["MultilanguageLongName"]) -> MultilanguageReferrable:
        """
        Set longName and return self for chaining.

        Args:
            value: The longName to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_long_name("value")
        """
        self.long_name = value  # Use property setter (gets validation)
        return self


class SingleLanguageReferrable(Referrable, ABC):
    """
    Instances of this class can be referred to by their identifier (while
    adhering to namespace borders). They also may have a longName but in one
    language only. Specializations of this class only occur as inline elements
    in one particular language. Therefore they aggregate But they are not
    considered to contribute substantially to the overall structure of an
    AUTOSAR description. In particular it does not contain other Referrables.

    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable::SingleLanguageReferrable

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 64, Foundation
      R23-11)
    """
    def __init__(self) -> None:
        if type(self) is SingleLanguageReferrable:
            raise TypeError("SingleLanguageReferrable is an abstract class.")
        super().__init__()

        # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This specifies the long name of the object.
        # The role is for compatibiilty to ASAM FSX.
        self._longName1: Optional["SingleLanguageLongName"] = None

    @property
    def long_name1(self) -> Optional["SingleLanguageLongName"]:
        """Get longName1 (Pythonic accessor)."""
        return self._longName1

    @long_name1.setter
    def long_name1(self, value: Optional["SingleLanguageLongName"]) -> None:
        """
        Set longName1 with validation.

        Args:
            value: The longName1 to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._longName1 = None
            return

        if value is not None and not hasattr(value, 'longName1'):
            raise TypeError(
                f"longName1 must be SingleLanguageLongName or None, got {type(value).__name__}"
            )
        self._longName1 = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLongName1(self) -> Optional["SingleLanguageLongName"]:
        """
        AUTOSAR-compliant getter for longName1.

        Returns:
            The longName1 value

        Note:
            Delegates to long_name1 property (CODING_RULE_V2_00017)
        """
        return self.long_name1  # Delegates to property

    def setLongName1(self, value: "SingleLanguageLongName") -> SingleLanguageReferrable:
        """
        AUTOSAR-compatible setter for longName1 with method chaining.

        Args:
            value: The longName1 to set

        Returns:
            self for method chaining

        Note:
            Delegates to long_name1 property setter (gets validation automatically)
        """
        self.long_name1 = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_long_name1(self, value: Optional["SingleLanguageLongName"]) -> SingleLanguageReferrable:
        """
        Set longName1 and return self for chaining.

        Args:
            value: The longName1 to set

        Returns:
            self for chaining

        Example:
            >>> obj.with_long_name1("value")
        """
        self.long_name1 = value  # Use property setter (gets validation)
        return self


class ShortNameFragment(ARObject):
    """
    This class describes how the Referrable.shortName is composed of several
    shortNameFragments.

    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable::ShortNameFragment

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 64, Foundation R23-11)
    """
    def __init__(self) -> None:
        super().__init__()

        # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This specifies a single shortName (fragment) which is the composed shortName.
        self._fragment: Optional["Identifier"] = None
        # This specifies the role of fragment to define e.
        # g.
        # the order fragments.
        self._role: Optional["String"] = None

    @property
    def fragment(self) -> Optional["Identifier"]:
        """Get fragment (Pythonic accessor)."""
        return self._fragment

    @fragment.setter
    def fragment(self, value: "Identifier") -> None:
        """
        Set fragment with validation.

        Args:
            value: The fragment to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"fragment must be Identifier or str, got {type(value).__name__}"
            )
        self._fragment = value

    @property
    def role(self) -> Optional["String"]:
        """Get role (Pythonic accessor)."""
        return self._role

    @role.setter
    def role(self, value: "String") -> None:
        """
        Set role with validation.

        Args:
            value: The role to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (String, str)):
            raise TypeError(
                f"role must be String or str, got {type(value).__name__}"
            )
        self._role = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFragment(self) -> Optional["Identifier"]:
        """
        AUTOSAR-compliant getter for fragment.

        Returns:
            The fragment value

        Note:
            Delegates to fragment property (CODING_RULE_V2_00017)
        """
        return self.fragment  # Delegates to property

    def setFragment(self, value: "Identifier") -> ShortNameFragment:
        """
        AUTOSAR-compliant setter for fragment with method chaining.

        Args:
            value: The fragment to set

        Returns:
            self for method chaining

        Note:
            Delegates to fragment property setter (gets validation automatically)
        """
        self.fragment = value  # Delegates to property setter
        return self

    def getRole(self) -> Optional["String"]:
        """
        AUTOSAR-compatible getter for role.

        Returns:
            The role value

        Note:
            Delegates to role property (CODING_RULE_V2_00017)
        """
        return self.role  # Delegates to property

    def setRole(self, value: "String") -> ShortNameFragment:
        """
        AUTOSAR-compliant setter for role with method chaining.

        Args:
            value: The role to set

        Returns:
            self for method chaining

        Note:
            Delegates to role property setter (gets validation automatically)
        """
        self.role = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_fragment(self, value: "Identifier") -> ShortNameFragment:
        """
        Set fragment and return self for chaining.

        Args:
            value: The fragment to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_fragment("value")
        """
        self.fragment = value  # Use property setter (gets validation)
        return self

    def with_role(self, value: "String") -> ShortNameFragment:
        """
        Set role and return self for chaining.

        Args:
            value: The role to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_role("value")
        """
        self.role = value  # Use property setter (gets validation)
        return self


# Export all classes
__all__ = [
    "Referrable",
    "MultilanguageReferrable",
    "SingleLanguageReferrable",
    "ShortNameFragment",
]