"""
This module contains classes for representing AUTOSAR Basic Software (BSW) implementation.
BSW implementation describes how BSW modules are implemented, including their behavior references,
configuration options, and version information.
"""

from typing import List

from armodel.models_v2.M2.AUTOSARTemplates.CommonStructure.Implementation import (
    Implementation,
)
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    RefType,
    RevisionLabelString,
)


class BswImplementation(Implementation):
    """
    Represents a Basic Software (BSW) implementation in AUTOSAR.
    This class defines the implementation details of a BSW module, including version information,
    behavior references, configuration options, and vendor-specific definitions.
    """

    def __init__(self, parent: ARObject, short_name: str) -> None:
        """
        Initializes the BSW implementation with a parent and short name.
        
        Args:
            parent: The parent ARObject that contains this implementation
            short_name: The unique short name of this implementation
        """
        super().__init__(parent, short_name)

        # AUTOSAR release version for this implementation
        self.arReleaseVersion: RevisionLabelString = None
        # Reference to the behavior associated with this implementation
        self.behaviorRef: RefType = None
        # List of references to preconfigured configurations for this implementation
        self.preconfiguredConfigurationRefs: List[RefType] = []
        # List of references to recommended configurations for this implementation
        self.recommendedConfigurationRefs: List[RefType] = []
        # Vendor-specific API infix used in naming conventions
        self.vendorApiInfix: Identifier = None
        # List of references to vendor-specific module definitions
        self.vendorSpecificModuleDefRefs: List[RefType] = []

    def getArReleaseVersion(self):
        """
        Gets the AUTOSAR release version for this implementation.
        
        Returns:
            RevisionLabelString representing the AUTOSAR release version
        """
        return self.arReleaseVersion

    def setArReleaseVersion(self, value):
        """
        Sets the AUTOSAR release version for this implementation.
        
        Args:
            value: The AUTOSAR release version to set
            
        Returns:
            self for method chaining
        """
        self.arReleaseVersion = value
        return self

    def getBehaviorRef(self):
        """
        Gets the reference to the behavior associated with this implementation.
        
        Returns:
            RefType to the behavior element
        """
        return self.behaviorRef

    def setBehaviorRef(self, value):
        """
        Sets the reference to the behavior associated with this implementation.
        
        Args:
            value: The behavior reference to set
            
        Returns:
            self for method chaining
        """
        self.behaviorRef = value
        return self

    def getPreconfiguredConfigurationRefs(self):
        """
        Gets the list of references to preconfigured configurations for this implementation.
        These are configurations that are already set up and ready to use.
        
        Returns:
            List of RefType to preconfigured configurations
        """
        return self.preconfiguredConfigurationRefs

    def addPreconfiguredConfigurationRef(self, value):
        """
        Adds a reference to a preconfigured configuration for this implementation.
        These are configurations that are already set up and ready to use.
        
        Args:
            value: The configuration reference to add
            
        Returns:
            self for method chaining
        """
        self.preconfiguredConfigurationRefs.append(value)
        return self

    def getRecommendedConfigurationRefs(self):
        """
        Gets the list of references to recommended configurations for this implementation.
        These are configurations that are suggested for use with this implementation.
        
        Returns:
            List of RefType to recommended configurations
        """
        return self.recommendedConfigurationRefs

    def addRecommendedConfigurationRef(self, value):
        """
        Adds a reference to a recommended configuration for this implementation.
        These are configurations that are suggested for use with this implementation.
        
        Args:
            value: The configuration reference to add
            
        Returns:
            self for method chaining
        """
        self.recommendedConfigurationRefs.append(value)
        return self

    def getVendorApiInfix(self):
        """
        Gets the vendor-specific API infix used in naming conventions for this implementation.
        This infix is typically used to distinguish vendor-specific APIs in the code generation process.
        
        Returns:
            Identifier for the vendor API infix
        """
        return self.vendorApiInfix

    def setVendorApiInfix(self, value):
        """
        Sets the vendor-specific API infix used in naming conventions for this implementation.
        This infix is typically used to distinguish vendor-specific APIs in the code generation process.
        
        Args:
            value: The vendor API infix to set
            
        Returns:
            self for method chaining
        """
        self.vendorApiInfix = value
        return self

    def getVendorSpecificModuleDefRefs(self):
        """
        Gets the list of references to vendor-specific module definitions for this implementation.
        These references point to vendor-specific module definitions that are used in this implementation.
        
        Returns:
            List of RefType to vendor-specific module definitions
        """
        return self.vendorSpecificModuleDefRefs

    def addVendorSpecificModuleDefRef(self, value):
        """
        Adds a reference to a vendor-specific module definition for this implementation.
        These references point to vendor-specific module definitions that are used in this implementation.
        
        Args:
            value: The vendor-specific module definition reference to add
            
        Returns:
            self for method chaining
        """
        self.vendorSpecificModuleDefRefs.append(value)
        return self
