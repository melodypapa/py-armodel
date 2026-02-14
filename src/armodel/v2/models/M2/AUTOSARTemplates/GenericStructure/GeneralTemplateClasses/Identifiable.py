"""
AUTOSAR Package - Identifiable

Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable
"""


from __future__ import annotations

from abc import (
    ABC,
)
from typing import (
    TYPE_CHECKING,
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CategoryString,
    Identifier,
    String,
)

# TYPE_CHECKING block to resolve circular imports
# Reason: These imports trigger a circular dependency chain:
#         Identifiable.py -> AdminData.py -> MultilanguageData.py -> BlockElements
#         -> RequirementsTracing.py -> Identifiable.py (trying to import MultilanguageReferrable)
# Solution: Import these classes only for type checking, not at runtime.
if TYPE_CHECKING:
    from armodel.v2.models.M2.MSR.AsamHdo.AdminData import (
        AdminData,
    )
    from armodel.v2.models.M2.MSR.Documentation.Annotation import (
        Annotation,
    )
    from armodel.v2.models.M2.MSR.Documentation.BlockElements import (
        DocumentationBlock,
    )
    from armodel.v2.models.M2.MSR.Documentation.TextModel.MultilanguageData import (
        MultiLanguageOverview,
    )


# Helper functions to import classes at runtime for validation
# These are called only when needed (e.g., in property setters)
def _get_admin_data_class():
    from armodel.v2.models.M2.MSR.AsamHdo.AdminData import AdminData
    return AdminData


def _get_annotation_class():
    from armodel.v2.models.M2.MSR.Documentation.Annotation import Annotation
    return Annotation


def _get_documentation_block_class():
    from armodel.v2.models.M2.MSR.Documentation.BlockElements import (
        DocumentationBlock,
    )
    return DocumentationBlock


def _get_multi_language_overview_class():
    from armodel.v2.models.M2.MSR.Documentation.TextModel.MultilanguageData import (
        MultiLanguageOverview,
    )
    return MultiLanguageOverview


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
    def short_name(self, value: Identifier) -> None:
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

    def setShortName(self, value: Identifier) -> Referrable:
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

    def with_short_name(self, value: Identifier) -> Referrable:
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

    def setLongName(self, value: MultilanguageLongName) -> MultilanguageReferrable:
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

    def setLongName1(self, value: SingleLanguageLongName) -> SingleLanguageReferrable:
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
    def fragment(self, value: Identifier) -> None:
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
    def role(self, value: String) -> None:
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

    def setFragment(self, value: Identifier) -> ShortNameFragment:
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

    def setRole(self, value: String) -> ShortNameFragment:
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

    def with_fragment(self, value: Identifier) -> ShortNameFragment:
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

    def with_role(self, value: String) -> ShortNameFragment:
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


class Describable(ARObject, ABC):
    """
    This meta-class represents the ability to add a descriptive documentation to
    non identifiable elements.

    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable::Describable

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 312, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 293, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 60, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 981, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2016, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 437, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is Describable:
            raise TypeError("Describable is an abstract class.")
        super().__init__()

        # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the administrative data for the.
        self._adminData: Optional[AdminData] = None
        # The category is a keyword that specializes the semantics Describable.
        # It affects the expected existence of the applicability of constraints.
        self._category: Optional[CategoryString] = None
        # This represents a general but brief (one paragraph) what the object in
                # question is about.
        # It is only Desc is intended to be collected into This property helps a human
                # reader to object in question.
        # documentation, (in particular how the built or used) should go to
                # "introduction".
        self._desc: Optional["MultiLanguageOverview"] = None
        # This represents more information about how the object in built or is used.
        # Therefore it is a.
        self._introduction: Optional[DocumentationBlock] = None

    @property
    def admin_data(self) -> Optional["AdminData"]:
        """Get adminData (Pythonic accessor)."""
        return self._adminData

    @admin_data.setter
    def admin_data(self, value: Optional["AdminData"]) -> None:
        """
        Set adminData with validation.

        Args:
            value: The adminData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._adminData = None
            return

        AdminData = _get_admin_data_class()
        if not isinstance(value, AdminData):
            raise TypeError(
                f"adminData must be AdminData or None, got {type(value).__name__}"
            )
        self._adminData = value

    @property
    def category(self) -> Optional[CategoryString]:
        """Get category (Pythonic accessor)."""
        return self._category

    @category.setter
    def category(self, value: Optional[CategoryString]) -> None:
        """
        Set category with validation.

        Args:
            value: The category to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._category = None
            return

        if not isinstance(value, CategoryString):
            raise TypeError(
                f"category must be CategoryString or None, got {type(value).__name__}"
            )
        self._category = value

    @property
    def desc(self) -> Optional["MultiLanguageOverview"]:
        """Get desc (Pythonic accessor)."""
        return self._desc

    @desc.setter
    def desc(self, value: Optional["MultiLanguageOverview"]) -> None:
        """
        Set desc with validation.

        Args:
            value: The desc to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._desc = None
            return

        # Skip type check for MultiLanguageOverview (missing from class-package.json)
        self._desc = value

    @property
    def introduction(self) -> Optional[DocumentationBlock]:
        """Get introduction (Pythonic accessor)."""
        return self._introduction

    @introduction.setter
    def introduction(self, value: Optional[DocumentationBlock]) -> None:
        """
        Set introduction with validation.

        Args:
            value: The introduction to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._introduction = None
            return

        from armodel.v2.models.M2.MSR.Documentation.BlockElements import (
            DocumentationBlock,
        )
        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"introduction must be DocumentationBlock or None, got {type(value).__name__}"
            )
        self._introduction = value

    def with_short_name_fragment(self, value):
        """
        Set short_name_fragment and return self for chaining.

        Args:
            value: The short_name_fragment to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_short_name_fragment("value")
        """
        self.short_name_fragment = value  # Use property setter (gets validation)
        return self

    def with_annotation(self, value):
        """
        Set annotation and return self for chaining.

        Args:
            value: The annotation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_annotation("value")
        """
        self.annotation = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAdminData(self) -> AdminData:
        """
        AUTOSAR-compliant getter for adminData.

        Returns:
            The adminData value

        Note:
            Delegates to admin_data property (CODING_RULE_V2_00017)
        """
        return self.admin_data  # Delegates to property

    def setAdminData(self, value: AdminData) -> Describable:
        """
        AUTOSAR-compliant setter for adminData with method chaining.

        Args:
            value: The adminData to set

        Returns:
            self for method chaining

        Note:
            Delegates to admin_data property setter (gets validation automatically)
        """
        self.admin_data = value  # Delegates to property setter
        return self

    def getCategory(self) -> CategoryString:
        """
        AUTOSAR-compliant getter for category.

        Returns:
            The category value

        Note:
            Delegates to category property (CODING_RULE_V2_00017)
        """
        return self.category  # Delegates to property

    def setCategory(self, value: CategoryString) -> Describable:
        """
        AUTOSAR-compliant setter for category with method chaining.

        Args:
            value: The category to set

        Returns:
            self for method chaining

        Note:
            Delegates to category property setter (gets validation automatically)
        """
        self.category = value  # Delegates to property setter
        return self

    def getDesc(self) -> "MultiLanguageOverview":
        """
        AUTOSAR-compliant getter for desc.

        Returns:
            The desc value

        Note:
            Delegates to desc property (CODING_RULE_V2_00017)
        """
        return self.desc  # Delegates to property

    def setDesc(self, value: "MultiLanguageOverview") -> Describable:
        """
        AUTOSAR-compliant setter for desc with method chaining.

        Args:
            value: The desc to set

        Returns:
            self for method chaining

        Note:
            Delegates to desc property setter (gets validation automatically)
        """
        self.desc = value  # Delegates to property setter
        return self

    def getIntroduction(self) -> DocumentationBlock:
        """
        AUTOSAR-compliant getter for introduction.

        Returns:
            The introduction value

        Note:
            Delegates to introduction property (CODING_RULE_V2_00017)
        """
        return self.introduction  # Delegates to property

    def setIntroduction(self, value: DocumentationBlock) -> Describable:
        """
        AUTOSAR-compliant setter for introduction with method chaining.

        Args:
            value: The introduction to set

        Returns:
            self for method chaining

        Note:
            Delegates to introduction property setter (gets validation automatically)
        """
        self.introduction = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_admin_data(self, value: Optional[AdminData]) -> Describable:
        """
        Set adminData and return self for chaining.

        Args:
            value: The adminData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_admin_data("value")
        """
        self.admin_data = value  # Use property setter (gets validation)
        return self

    def with_category(self, value: Optional[CategoryString]) -> Describable:
        """
        Set category and return self for chaining.

        Args:
            value: The category to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_category("value")
        """
        self.category = value  # Use property setter (gets validation)
        return self

    def with_desc(self, value: Optional["MultiLanguageOverview"]) -> Describable:
        """
        Set desc and return self for chaining.

        Args:
            value: The desc to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_desc("value")
        """
        self.desc = value  # Use property setter (gets validation)
        return self

    def with_introduction(self, value: Optional[DocumentationBlock]) -> Describable:
        """
        Set introduction and return self for chaining.

        Args:
            value: The introduction to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_introduction("value")
        """
        self.introduction = value  # Use property setter (gets validation)
        return self



class Identifiable(MultilanguageReferrable, ABC):
    """
    Instances of this class can be referred to by their identifier (within the
    namespace borders). In addition to this, Identifiables are objects which
    contribute significantly to the overall structure of an AUTOSAR description.
    In particular, Identifiables might contain Identifiables.

    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable::Identifiable

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 318, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 317, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 296, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 60, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 995, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2027, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 229, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 45, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 74, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 59, Foundation R23-11)
      - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (Page 31, Foundation R23-11)
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 60, Foundation R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 191, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is Identifiable:
            raise TypeError("Identifiable is an abstract class.")
        super().__init__()

        # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the administrative data for the identifiable 381 Document ID
        # 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module Description Template
        # R23-11.
        self._adminData: Optional[AdminData] = None
        # Possibility to provide additional notes while defining a (e.
        # g.
        # the ECU Configuration Parameter are not intended as documentation but design
        # notes.
        self._annotation: List[Annotation] = []
        # The category is a keyword that specializes the semantics Identifiable.
        # It affects the expected existence of the applicability of constraints.
        self._category: Optional[CategoryString] = None
        # This represents a general but brief (one paragraph) what the object in
        # question is about.
        # It is only Desc is intended to be collected into This property helps a human
        # reader to object in question.
        # documentation, (in particular how the built or used) should go to
        # "introduction".
        self._desc: Optional["MultiLanguageOverview"] = None
        # This represents more information about how the object in built or is used.
        # Therefore it is a.
        self._introduction: Optional["DocumentationBlock"] = None
        # The purpose of this attribute is to provide a globally for an instance of a
        # meta-class.
        # The this attribute should be globally unique strings the type of identifier.
        # For example, to include a as defined by The Open Group, the UUID preceded by
        # "DCE:".
        # The values of this attribute used to support merging of different AUTOSAR
        # form of the UUID (Universally Unique taken from a standard defined by the
        # Open Open Software Foundation).
        # This standard is including by Microsoft for COM (GUIDs) and companies for
        # DCE, which is based on CORBA.
        # for generating these 128-bit IDs is published standard and the effectiveness
        # and uniqueness of is not in practice disputed.
        # If the id namespace is is assumed.
        # An example is has no semantic meaning for an AUTOSAR there is no requirement
        # for AUTOSAR tools to timestamp.
        self._uuid: Optional[String] = None

    @property
    def admin_data(self) -> Optional["AdminData"]:
        """Get adminData (Pythonic accessor)."""
        return self._adminData

    @admin_data.setter
    def admin_data(self, value: Optional["AdminData"]) -> None:
        """
        Set adminData with validation.

        Args:
            value: The adminData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._adminData = None
            return

        AdminData = _get_admin_data_class()
        if not isinstance(value, AdminData):
            raise TypeError(
                f"adminData must be AdminData or None, got {type(value).__name__}"
            )
        self._adminData = value

    @property
    def annotation(self) -> List["Annotation"]:
        """Get annotation (Pythonic accessor)."""
        return self._annotation

    @annotation.setter
    def annotation(self, value: List["Annotation"]) -> None:
        """
        Set annotation with validation.

        Args:
            value: The annotation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, list):
            raise TypeError(
                f"annotation must be a list or None, got {type(value).__name__}"
            )
        self._annotation = value

    @property
    def category(self) -> Optional[CategoryString]:
        """Get category (Pythonic accessor)."""
        return self._category

    @category.setter
    def category(self, value: Optional[CategoryString]) -> None:
        """
        Set category with validation.

        Args:
            value: The category to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._category = None
            return

        if not isinstance(value, CategoryString):
            raise TypeError(
                f"category must be CategoryString or None, got {type(value).__name__}"
            )
        self._category = value

    @property
    def desc(self) -> Optional["MultiLanguageOverview"]:
        """Get desc (Pythonic accessor)."""
        return self._desc

    @desc.setter
    def desc(self, value: Optional["MultiLanguageOverview"]) -> None:
        """
        Set desc with validation.

        Args:
            value: The desc to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._desc = None
            return

        # Skip type check for MultiLanguageOverview (missing from class-package.json)
        self._desc = value

    @property
    def introduction(self) -> Optional["DocumentationBlock"]:
        """Get introduction (Pythonic accessor)."""
        return self._introduction

    @introduction.setter
    def introduction(self, value: Optional["DocumentationBlock"]) -> None:
        """
        Set introduction with validation.

        Args:
            value: The introduction to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._introduction = None
            return

        from armodel.v2.models.M2.MSR.Documentation.BlockElements import (
            DocumentationBlock,
        )
        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"introduction must be DocumentationBlock or None, got {type(value).__name__}"
            )
        self._introduction = value
                # meta-class.
        # The this attribute should be globally unique strings the type of identifier.
        # For example, to include a as defined by The Open Group, the UUID preceded by
                # "DCE:".
        # The values of this attribute used to support merging of different AUTOSAR
                # form of the UUID (Universally Unique taken from a standard defined by the
                # Open Open Software Foundation).
        # This standard is including by Microsoft for COM (GUIDs) and companies for
                # DCE, which is based on CORBA.
        # for generating these 128-bit IDs is published standard and the effectiveness
                # and uniqueness of is not in practice disputed.
        # If the id namespace is is assumed.
        # An example is has no semantic meaning for an AUTOSAR there is no requirement
                # for AUTOSAR tools to timestamp.
        self._uuid: Optional[String] = None

    @property
    def uuid(self) -> Optional[String]:
        """Get uuid (Pythonic accessor)."""
        return self._uuid

    @uuid.setter
    def uuid(self, value: Optional[String]) -> None:
        """
        Set uuid with validation.

        Args:
            value: The uuid to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._uuid = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"uuid must be String or str or None, got {type(value).__name__}"
            )
        self._uuid = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAdminData(self) -> AdminData:
        """
        AUTOSAR-compliant getter for adminData.

        Returns:
            The adminData value

        Note:
            Delegates to admin_data property (CODING_RULE_V2_00017)
        """
        return self.admin_data  # Delegates to property

    def setAdminData(self, value: AdminData) -> Identifiable:
        """
        AUTOSAR-compliant setter for adminData with method chaining.

        Args:
            value: The adminData to set

        Returns:
            self for method chaining

        Note:
            Delegates to admin_data property setter (gets validation automatically)
        """
        self.admin_data = value  # Delegates to property setter
        return self

    def getAnnotation(self) -> List[Annotation]:
        """
        AUTOSAR-compliant getter for annotation.

        Returns:
            The annotation value

        Note:
            Delegates to annotation property (CODING_RULE_V2_00017)
        """
        return self.annotation  # Delegates to property

    def getCategory(self) -> CategoryString:
        """
        AUTOSAR-compliant getter for category.

        Returns:
            The category value

        Note:
            Delegates to category property (CODING_RULE_V2_00017)
        """
        return self.category  # Delegates to property

    def setCategory(self, value: CategoryString) -> Identifiable:
        """
        AUTOSAR-compliant setter for category with method chaining.

        Args:
            value: The category to set

        Returns:
            self for method chaining

        Note:
            Delegates to category property setter (gets validation automatically)
        """
        self.category = value  # Delegates to property setter
        return self

    def getDesc(self) -> "MultiLanguageOverview":
        """
        AUTOSAR-compliant getter for desc.

        Returns:
            The desc value

        Note:
            Delegates to desc property (CODING_RULE_V2_00017)
        """
        return self.desc  # Delegates to property

    def setDesc(self, value: "MultiLanguageOverview") -> Identifiable:
        """
        AUTOSAR-compliant setter for desc with method chaining.

        Args:
            value: The desc to set

        Returns:
            self for method chaining

        Note:
            Delegates to desc property setter (gets validation automatically)
        """
        self.desc = value  # Delegates to property setter
        return self

    def getIntroduction(self) -> DocumentationBlock:
        """
        AUTOSAR-compliant getter for introduction.

        Returns:
            The introduction value

        Note:
            Delegates to introduction property (CODING_RULE_V2_00017)
        """
        return self.introduction  # Delegates to property

    def setIntroduction(self, value: DocumentationBlock) -> Identifiable:
        """
        AUTOSAR-compliant setter for introduction with method chaining.

        Args:
            value: The introduction to set

        Returns:
            self for method chaining

        Note:
            Delegates to introduction property setter (gets validation automatically)
        """
        self.introduction = value  # Delegates to property setter
        return self

    def getUuid(self) -> String:
        """
        AUTOSAR-compliant getter for uuid.

        Returns:
            The uuid value

        Note:
            Delegates to uuid property (CODING_RULE_V2_00017)
        """
        return self.uuid  # Delegates to property

    def setUuid(self, value: String) -> Identifiable:
        """
        AUTOSAR-compliant setter for uuid with method chaining.

        Args:
            value: The uuid to set

        Returns:
            self for method chaining

        Note:
            Delegates to uuid property setter (gets validation automatically)
        """
        self.uuid = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_admin_data(self, value: Optional[AdminData]) -> Identifiable:
        """
        Set adminData and return self for chaining.

        Args:
            value: The adminData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_admin_data("value")
        """
        self.admin_data = value  # Use property setter (gets validation)
        return self

    def with_category(self, value: Optional[CategoryString]) -> Identifiable:
        """
        Set category and return self for chaining.

        Args:
            value: The category to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_category("value")
        """
        self.category = value  # Use property setter (gets validation)
        return self

    def with_desc(self, value: Optional["MultiLanguageOverview"]) -> Identifiable:
        """
        Set desc and return self for chaining.

        Args:
            value: The desc to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_desc("value")
        """
        self.desc = value  # Use property setter (gets validation)
        return self

    def with_introduction(self, value: Optional[DocumentationBlock]) -> Identifiable:
        """
        Set introduction and return self for chaining.

        Args:
            value: The introduction to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_introduction("value")
        """
        self.introduction = value  # Use property setter (gets validation)
        return self

    def with_uuid(self, value: Optional[String]) -> Identifiable:
        """
        Set uuid and return self for chaining.

        Args:
            value: The uuid to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_uuid("value")
        """
        self.uuid = value  # Use property setter (gets validation)
        return self


# Export all classes
__all__ = [
    "Referrable",
    "MultilanguageReferrable",
    "SingleLanguageReferrable",
    "ShortNameFragment",
    "Describable",
    "Identifiable",
]
