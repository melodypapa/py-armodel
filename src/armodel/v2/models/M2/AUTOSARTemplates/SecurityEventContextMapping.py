from abc import ABC
from typing import List, Optional


class SecurityEventContextMapping(IdsMapping, ABC):
    """
    This meta-class represents the ability to create an association between a
    collection of security events, an IdsM instance which handles the security
    events and the filter chains applicable to the security events.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::SecurityEventContextMapping

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 32, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is SecurityEventContextMapping:
            raise TypeError("SecurityEventContextMapping is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference defines the filter chain to be applied to of the referenced
        # security events (depending on the atpVariation.
        self._filterChain: Optional["SecurityEventFilter"] = None

    @property
    def filter_chain(self) -> Optional["SecurityEventFilter"]:
        """Get filterChain (Pythonic accessor)."""
        return self._filterChain

    @filter_chain.setter
    def filter_chain(self, value: Optional["SecurityEventFilter"]) -> None:
        """
        Set filterChain with validation.

        Args:
            value: The filterChain to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._filterChain = None
            return

        if not isinstance(value, SecurityEventFilter):
            raise TypeError(
                f"filterChain must be SecurityEventFilter or None, got {type(value).__name__}"
            )
        self._filterChain = value
        # This reference defines the IdsmInstance onto which the are mapped.
        # atpVariation 97 Document ID 980: AUTOSAR_FO_TPS_SecurityExtractTemplate
                # Template R23-11.
        self._idsmInstance: Optional["IdsmInstance"] = None

    @property
    def idsm_instance(self) -> Optional["IdsmInstance"]:
        """Get idsmInstance (Pythonic accessor)."""
        return self._idsmInstance

    @idsm_instance.setter
    def idsm_instance(self, value: Optional["IdsmInstance"]) -> None:
        """
        Set idsmInstance with validation.

        Args:
            value: The idsmInstance to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._idsmInstance = None
            return

        if not isinstance(value, IdsmInstance):
            raise TypeError(
                f"idsmInstance must be IdsmInstance or None, got {type(value).__name__}"
            )
        self._idsmInstance = value
        # This aggregation represents (through further references) the
                # SecurityEventDefinitions to be mapped to an Idsm additional mapping-dependent
                # properties.
        # atpVariation.
        self._mappedSecurity: List["SecurityEventContext"] = []

    @property
    def mapped_security(self) -> List["SecurityEventContext"]:
        """Get mappedSecurity (Pythonic accessor)."""
        return self._mappedSecurity

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFilterChain(self) -> "SecurityEventFilter":
        """
        AUTOSAR-compliant getter for filterChain.

        Returns:
            The filterChain value

        Note:
            Delegates to filter_chain property (CODING_RULE_V2_00017)
        """
        return self.filter_chain  # Delegates to property

    def setFilterChain(self, value: "SecurityEventFilter") -> "SecurityEventContextMapping":
        """
        AUTOSAR-compliant setter for filterChain with method chaining.

        Args:
            value: The filterChain to set

        Returns:
            self for method chaining

        Note:
            Delegates to filter_chain property setter (gets validation automatically)
        """
        self.filter_chain = value  # Delegates to property setter
        return self

    def getIdsmInstance(self) -> "IdsmInstance":
        """
        AUTOSAR-compliant getter for idsmInstance.

        Returns:
            The idsmInstance value

        Note:
            Delegates to idsm_instance property (CODING_RULE_V2_00017)
        """
        return self.idsm_instance  # Delegates to property

    def setIdsmInstance(self, value: "IdsmInstance") -> "SecurityEventContextMapping":
        """
        AUTOSAR-compliant setter for idsmInstance with method chaining.

        Args:
            value: The idsmInstance to set

        Returns:
            self for method chaining

        Note:
            Delegates to idsm_instance property setter (gets validation automatically)
        """
        self.idsm_instance = value  # Delegates to property setter
        return self

    def getMappedSecurity(self) -> List["SecurityEventContext"]:
        """
        AUTOSAR-compliant getter for mappedSecurity.

        Returns:
            The mappedSecurity value

        Note:
            Delegates to mapped_security property (CODING_RULE_V2_00017)
        """
        return self.mapped_security  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_filter_chain(self, value: Optional["SecurityEventFilter"]) -> "SecurityEventContextMapping":
        """
        Set filterChain and return self for chaining.

        Args:
            value: The filterChain to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_filter_chain("value")
        """
        self.filter_chain = value  # Use property setter (gets validation)
        return self

    def with_idsm_instance(self, value: Optional["IdsmInstance"]) -> "SecurityEventContextMapping":
        """
        Set idsmInstance and return self for chaining.

        Args:
            value: The idsmInstance to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_idsm_instance("value")
        """
        self.idsm_instance = value  # Use property setter (gets validation)
        return self
