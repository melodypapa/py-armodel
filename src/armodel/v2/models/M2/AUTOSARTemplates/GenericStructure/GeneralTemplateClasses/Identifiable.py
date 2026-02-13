"""
AUTOSAR Package - Identifiable

Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable
"""


from __future__ import annotations

from abc import (
    ABC,
)
from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CategoryString,
    String,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Referrable import (
    MultilanguageReferrable,
    Referrable,
    ShortNameFragment,
    SingleLanguageReferrable,
)
from armodel.v2.models.M2.MSR.AsamHdo.AdminData import (
    AdminData,
)
from armodel.v2.models.M2.MSR.Documentation.Annotation import (
    Annotation,
)
from armodel.v2.models.M2.MSR.Documentation.BlockElements import (
    DocumentationBlock,
)


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
    def admin_data(self) -> Optional[AdminData]:
        """Get adminData (Pythonic accessor)."""
        return self._adminData

    @admin_data.setter
    def admin_data(self, value: Optional[AdminData]) -> None:
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
        self._introduction: Optional[DocumentationBlock] = None
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
    def admin_data(self) -> Optional[AdminData]:
        """Get adminData (Pythonic accessor)."""
        return self._adminData

    @admin_data.setter
    def admin_data(self, value: Optional[AdminData]) -> None:
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

        if not isinstance(value, AdminData):
            raise TypeError(
                f"adminData must be AdminData or None, got {type(value).__name__}"
            )
        self._adminData = value

    @property
    def annotation(self) -> List[Annotation]:
        """Get annotation (Pythonic accessor)."""
        return self._annotation

    @annotation.setter
    def annotation(self, value: List[Annotation]) -> None:
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
