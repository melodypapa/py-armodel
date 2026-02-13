"""
AUTOSAR Package - CommonService

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::CommonService
"""


from __future__ import annotations

from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import (
    DiagnosticCommonElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticServiceClass(DiagnosticCommonElement, ABC):
    """
    This meta-class provides the ability to define common properties that are
    shared among all instances of sub-classes of DiagnosticServiceInstance.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::CommonService::DiagnosticServiceClass

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 69, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticServiceClass:
            raise TypeError("DiagnosticServiceClass is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticServiceInstance(DiagnosticCommonElement, ABC):
    """
    This represents a concrete instance of a diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::CommonService::DiagnosticServiceInstance

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 69, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticServiceInstance:
            raise TypeError("DiagnosticServiceInstance is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the collection of DiagnosticAccess Permissions that allow for
        # the execution of the referencing 719 Document ID 673:
        # AUTOSAR_CP_TPS_DiagnosticExtractTemplate Template R23-11.
        self._access: Optional[DiagnosticAccess] = None

    @property
    def access(self) -> Optional[DiagnosticAccess]:
        """Get access (Pythonic accessor)."""
        return self._access

    @access.setter
    def access(self, value: Optional[DiagnosticAccess]) -> None:
        """
        Set access with validation.

        Args:
            value: The access to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._access = None
            return

        if not isinstance(value, DiagnosticAccess):
            raise TypeError(
                f"access must be DiagnosticAccess or None, got {type(value).__name__}"
            )
        self._access = value
        # e.
        # this properties that are shared among all applicable sub-classes of
                # DiagnosticService that affected by this pattern implement the applicable
                # "class"-role that substantiate reference.
        self._serviceClass: Optional[DiagnosticServiceClass] = None

    @property
    def service_class(self) -> Optional[DiagnosticServiceClass]:
        """Get serviceClass (Pythonic accessor)."""
        return self._serviceClass

    @service_class.setter
    def service_class(self, value: Optional[DiagnosticServiceClass]) -> None:
        """
        Set serviceClass with validation.

        Args:
            value: The serviceClass to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._serviceClass = None
            return

        if not isinstance(value, DiagnosticServiceClass):
            raise TypeError(
                f"serviceClass must be DiagnosticServiceClass or None, got {type(value).__name__}"
            )
        self._serviceClass = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAccess(self) -> DiagnosticAccess:
        """
        AUTOSAR-compliant getter for access.

        Returns:
            The access value

        Note:
            Delegates to access property (CODING_RULE_V2_00017)
        """
        return self.access  # Delegates to property

    def setAccess(self, value: DiagnosticAccess) -> DiagnosticServiceInstance:
        """
        AUTOSAR-compliant setter for access with method chaining.

        Args:
            value: The access to set

        Returns:
            self for method chaining

        Note:
            Delegates to access property setter (gets validation automatically)
        """
        self.access = value  # Delegates to property setter
        return self

    def getServiceClass(self) -> DiagnosticServiceClass:
        """
        AUTOSAR-compliant getter for serviceClass.

        Returns:
            The serviceClass value

        Note:
            Delegates to service_class property (CODING_RULE_V2_00017)
        """
        return self.service_class  # Delegates to property

    def setServiceClass(self, value: DiagnosticServiceClass) -> DiagnosticServiceInstance:
        """
        AUTOSAR-compliant setter for serviceClass with method chaining.

        Args:
            value: The serviceClass to set

        Returns:
            self for method chaining

        Note:
            Delegates to service_class property setter (gets validation automatically)
        """
        self.service_class = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_access(self, value: Optional[DiagnosticAccess]) -> DiagnosticServiceInstance:
        """
        Set access and return self for chaining.

        Args:
            value: The access to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_access("value")
        """
        self.access = value  # Use property setter (gets validation)
        return self

    def with_service_class(self, value: Optional[DiagnosticServiceClass]) -> DiagnosticServiceInstance:
        """
        Set serviceClass and return self for chaining.

        Args:
            value: The serviceClass to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_service_class("value")
        """
        self.service_class = value  # Use property setter (gets validation)
        return self



class DiagnosticCustomServiceClass(DiagnosticServiceClass):
    """
    This represents the ability to define a custom diagnostic service class and
    assign an ID to it. Further configuration is not foreseen from the point of
    view of the diagnostic extract and consequently needs to be done on the
    level of ECUC.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::CommonService::DiagnosticCustomServiceClass

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 71, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute may only be used for the definition of services.
        # The values shall not overlap with service IDs.
        self._customService: Optional[PositiveInteger] = None

    @property
    def custom_service(self) -> Optional[PositiveInteger]:
        """Get customService (Pythonic accessor)."""
        return self._customService

    @custom_service.setter
    def custom_service(self, value: Optional[PositiveInteger]) -> None:
        """
        Set customService with validation.

        Args:
            value: The customService to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._customService = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"customService must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._customService = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCustomService(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for customService.

        Returns:
            The customService value

        Note:
            Delegates to custom_service property (CODING_RULE_V2_00017)
        """
        return self.custom_service  # Delegates to property

    def setCustomService(self, value: PositiveInteger) -> DiagnosticCustomServiceClass:
        """
        AUTOSAR-compliant setter for customService with method chaining.

        Args:
            value: The customService to set

        Returns:
            self for method chaining

        Note:
            Delegates to custom_service property setter (gets validation automatically)
        """
        self.custom_service = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_custom_service(self, value: Optional[PositiveInteger]) -> DiagnosticCustomServiceClass:
        """
        Set customService and return self for chaining.

        Args:
            value: The customService to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_custom_service("value")
        """
        self.custom_service = value  # Use property setter (gets validation)
        return self
