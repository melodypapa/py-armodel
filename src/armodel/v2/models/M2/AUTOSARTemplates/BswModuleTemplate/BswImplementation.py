"""
AUTOSAR Package - BswImplementation

Package: M2::AUTOSARTemplates::BswModuleTemplate::BswImplementation
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Implementation import (
    Implementation,
)


class BswImplementation(Implementation):
    """
    Contains the implementation specific information in addition to the generic
    specification (BswModule Description and BswBehavior). It is possible to
    have several different BswImplementations referring to the same BswBehavior.
    
    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswImplementation::BswImplementation
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 120, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 290, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 972, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 207, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 425, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Version of the AUTOSAR Release on which this is based.
        # The numbering contains three minor, revision) which are defined by.
        self._arRelease: Optional["RevisionLabelString"] = None

    @property
    def ar_release(self) -> Optional["RevisionLabelString"]:
        """Get arRelease (Pythonic accessor)."""
        return self._arRelease

    @ar_release.setter
    def ar_release(self, value: Optional["RevisionLabelString"]) -> None:
        """
        Set arRelease with validation.
        
        Args:
            value: The arRelease to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._arRelease = None
            return

        if not isinstance(value, RevisionLabelString):
            raise TypeError(
                f"arRelease must be RevisionLabelString or None, got {type(value).__name__}"
            )
        self._arRelease = value
        # is made as an association because follows the pattern of the SWCT ARElement
                # cannot be splitted, but we want implementation later, the Bsw not aggregated
                # in BswBehavior.
        self._behavior: Optional["BswInternalBehavior"] = None

    @property
    def behavior(self) -> Optional["BswInternalBehavior"]:
        """Get behavior (Pythonic accessor)."""
        return self._behavior

    @behavior.setter
    def behavior(self, value: Optional["BswInternalBehavior"]) -> None:
        """
        Set behavior with validation.
        
        Args:
            value: The behavior to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._behavior = None
            return

        if not isinstance(value, BswInternalBehavior):
            raise TypeError(
                f"behavior must be BswInternalBehavior or None, got {type(value).__name__}"
            )
        self._behavior = value
        # e.
        # fixed) configuration values for this BswImplementation.
        # BswImplementation represents a cluster of several than one
                # EcucModuleConfigurationValues be referred (at most one per module), most one
                # such element can be referred.
        self._preconfigured: List["EcucModule"] = []

    @property
    def preconfigured(self) -> List["EcucModule"]:
        """Get preconfigured (Pythonic accessor)."""
        return self._preconfigured
        # Reference to one or more sets of recommended configuration values for this
        # module or module cluster.
        self._recommended: List["EcucModule"] = []

    @property
    def recommended(self) -> List["EcucModule"]:
        """Get recommended (Pythonic accessor)."""
        return self._recommended
        # In driver modules which can be instantiated several times single ECU,
                # SRS_BSW_00347 requires that the files, APIs, published parameters and memory
                # are extended by the vendorId and a name.
        # This parameter is used to specify specific name.
        # In total, the implementation name is generated as follows: <Module name from
                # that the vendorId of the implementer is the implementer chose a
                # vendorApiInfix of API name Can_Write defined in the SWS to
                # Can_123_v11r456_Write.
        # is mandatory for all modules with upper 1.
        # It shall not be used for modules with =1.
        # SWS_BSW_00102.
        self._vendorApiInfix: Optional["Identifier"] = None

    @property
    def vendor_api_infix(self) -> Optional["Identifier"]:
        """Get vendorApiInfix (Pythonic accessor)."""
        return self._vendorApiInfix

    @vendor_api_infix.setter
    def vendor_api_infix(self, value: Optional["Identifier"]) -> None:
        """
        Set vendorApiInfix with validation.
        
        Args:
            value: The vendorApiInfix to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vendorApiInfix = None
            return

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"vendorApiInfix must be Identifier or str or None, got {type(value).__name__}"
            )
        self._vendorApiInfix = value
        # a single module EcucModuleDefs used in this Bsw it represents a cluster of
        # modules or no EcucModuleDefs used in this Bsw it represents a library.
        self._vendorSpecific: List["EcucModuleDef"] = []

    @property
    def vendor_specific(self) -> List["EcucModuleDef"]:
        """Get vendorSpecific (Pythonic accessor)."""
        return self._vendorSpecific

    def with_preconfigured(self, value):
        """
        Set preconfigured and return self for chaining.

        Args:
            value: The preconfigured to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_preconfigured("value")
        """
        self.preconfigured = value  # Use property setter (gets validation)
        return self

    def with_recommended(self, value):
        """
        Set recommended and return self for chaining.

        Args:
            value: The recommended to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_recommended("value")
        """
        self.recommended = value  # Use property setter (gets validation)
        return self

    def with_vendor_specific(self, value):
        """
        Set vendor_specific and return self for chaining.

        Args:
            value: The vendor_specific to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vendor_specific("value")
        """
        self.vendor_specific = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArRelease(self) -> "RevisionLabelString":
        """
        AUTOSAR-compliant getter for arRelease.
        
        Returns:
            The arRelease value
        
        Note:
            Delegates to ar_release property (CODING_RULE_V2_00017)
        """
        return self.ar_release  # Delegates to property

    def setArRelease(self, value: "RevisionLabelString") -> "BswImplementation":
        """
        AUTOSAR-compliant setter for arRelease with method chaining.
        
        Args:
            value: The arRelease to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ar_release property setter (gets validation automatically)
        """
        self.ar_release = value  # Delegates to property setter
        return self

    def getBehavior(self) -> "BswInternalBehavior":
        """
        AUTOSAR-compliant getter for behavior.
        
        Returns:
            The behavior value
        
        Note:
            Delegates to behavior property (CODING_RULE_V2_00017)
        """
        return self.behavior  # Delegates to property

    def setBehavior(self, value: "BswInternalBehavior") -> "BswImplementation":
        """
        AUTOSAR-compliant setter for behavior with method chaining.
        
        Args:
            value: The behavior to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to behavior property setter (gets validation automatically)
        """
        self.behavior = value  # Delegates to property setter
        return self

    def getPreconfigured(self) -> List["EcucModule"]:
        """
        AUTOSAR-compliant getter for preconfigured.
        
        Returns:
            The preconfigured value
        
        Note:
            Delegates to preconfigured property (CODING_RULE_V2_00017)
        """
        return self.preconfigured  # Delegates to property

    def getRecommended(self) -> List["EcucModule"]:
        """
        AUTOSAR-compliant getter for recommended.
        
        Returns:
            The recommended value
        
        Note:
            Delegates to recommended property (CODING_RULE_V2_00017)
        """
        return self.recommended  # Delegates to property

    def getVendorApiInfix(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for vendorApiInfix.
        
        Returns:
            The vendorApiInfix value
        
        Note:
            Delegates to vendor_api_infix property (CODING_RULE_V2_00017)
        """
        return self.vendor_api_infix  # Delegates to property

    def setVendorApiInfix(self, value: "Identifier") -> "BswImplementation":
        """
        AUTOSAR-compliant setter for vendorApiInfix with method chaining.
        
        Args:
            value: The vendorApiInfix to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to vendor_api_infix property setter (gets validation automatically)
        """
        self.vendor_api_infix = value  # Delegates to property setter
        return self

    def getVendorSpecific(self) -> List["EcucModuleDef"]:
        """
        AUTOSAR-compliant getter for vendorSpecific.
        
        Returns:
            The vendorSpecific value
        
        Note:
            Delegates to vendor_specific property (CODING_RULE_V2_00017)
        """
        return self.vendor_specific  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ar_release(self, value: Optional["RevisionLabelString"]) -> "BswImplementation":
        """
        Set arRelease and return self for chaining.
        
        Args:
            value: The arRelease to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ar_release("value")
        """
        self.ar_release = value  # Use property setter (gets validation)
        return self

    def with_behavior(self, value: Optional["BswInternalBehavior"]) -> "BswImplementation":
        """
        Set behavior and return self for chaining.
        
        Args:
            value: The behavior to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_behavior("value")
        """
        self.behavior = value  # Use property setter (gets validation)
        return self

    def with_vendor_api_infix(self, value: Optional["Identifier"]) -> "BswImplementation":
        """
        Set vendorApiInfix and return self for chaining.
        
        Args:
            value: The vendorApiInfix to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_vendor_api_infix("value")
        """
        self.vendor_api_infix = value  # Use property setter (gets validation)
        return self
