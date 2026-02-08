"""
V2 M2::AUTOSARTemplates::SWComponentTemplate::PortInterface package.
"""

from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARElement import (
    ARElement,
)
from .InstanceRefs import *


class PortInterface(ARElement, ABC):
    """
    Abstract base class for an interface that is either provided or required by
    a port of a software component.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::PortInterface

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 326, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 87, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2046, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 27, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 457, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 200, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is PortInterface:
            raise TypeError("PortInterface is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This flag is set if the PortInterface is to be used for an or or or
                # ServiceSwComponentType (namely an AUTOSAR on the same ECU.
        # Otherwise the flag is.
        self._isService: Optional["Boolean"] = None

    @property
    def is_service(self) -> Optional["Boolean"]:
        """Get isService (Pythonic accessor)."""
        return self._isService

    @is_service.setter
    def is_service(self, value: Optional["Boolean"]) -> None:
        """
        Set isService with validation.

        Args:
            value: The isService to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._isService = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"isService must be Boolean or None, got {type(value).__name__}"
            )
        self._isService = value
        # This attribute provides further details about the nature of service.
        self._serviceKind: Optional["ServiceProviderEnum"] = None

    @property
    def service_kind(self) -> Optional["ServiceProviderEnum"]:
        """Get serviceKind (Pythonic accessor)."""
        return self._serviceKind

    @service_kind.setter
    def service_kind(self, value: Optional["ServiceProviderEnum"]) -> None:
        """
        Set serviceKind with validation.

        Args:
            value: The serviceKind to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._serviceKind = None
            return

        if not isinstance(value, ServiceProviderEnum):
            raise TypeError(
                f"serviceKind must be ServiceProviderEnum or None, got {type(value).__name__}"
            )
        self._serviceKind = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIsService(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for isService.

        Returns:
            The isService value

        Note:
            Delegates to is_service property (CODING_RULE_V2_00017)
        """
        return self.is_service  # Delegates to property

    def setIsService(self, value: "Boolean") -> "PortInterface":
        """
        AUTOSAR-compliant setter for isService with method chaining.

        Args:
            value: The isService to set

        Returns:
            self for method chaining

        Note:
            Delegates to is_service property setter (gets validation automatically)
        """
        self.is_service = value  # Delegates to property setter
        return self

    def getServiceKind(self) -> "ServiceProviderEnum":
        """
        AUTOSAR-compliant getter for serviceKind.

        Returns:
            The serviceKind value

        Note:
            Delegates to service_kind property (CODING_RULE_V2_00017)
        """
        return self.service_kind  # Delegates to property

    def setServiceKind(self, value: "ServiceProviderEnum") -> "PortInterface":
        """
        AUTOSAR-compliant setter for serviceKind with method chaining.

        Args:
            value: The serviceKind to set

        Returns:
            self for method chaining

        Note:
            Delegates to service_kind property setter (gets validation automatically)
        """
        self.service_kind = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_is_service(self, value: Optional["Boolean"]) -> "PortInterface":
        """
        Set isService and return self for chaining.

        Args:
            value: The isService to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_is_service("value")
        """
        self.is_service = value  # Use property setter (gets validation)
        return self

    def with_service_kind(self, value: Optional["ServiceProviderEnum"]) -> "PortInterface":
        """
        Set serviceKind and return self for chaining.

        Args:
            value: The serviceKind to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_service_kind("value")
        """
        self.service_kind = value  # Use property setter (gets validation)
        return self


# Classes defined in this package:
from .ApplicationCompositeElementInPortInterfaceInstanceRef import (
    ApplicationCompositeElementInPortInterfaceInstanceRef,
)

__all__ = [
    # .InstanceRefs.*,
    "PortInterface",
    "ApplicationCompositeElementInPortInterfaceInstanceRef",
]