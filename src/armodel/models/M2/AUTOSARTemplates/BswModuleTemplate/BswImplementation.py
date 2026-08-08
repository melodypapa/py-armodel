"""
This module contains classes for representing AUTOSAR Basic Software (BSW) implementation.
BSW implementation describes how BSW modules are implemented, including their behavior references,
configuration options, and version information.
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation import Implementation
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType, RevisionLabelString


class BswImplementation(Implementation):
    """
    Represents a Basic Software (BSW) implementation in AUTOSAR.
    This class defines the implementation details of a BSW module, including version information,
    behavior references, configuration options, and vendor-specific definitions.
    """

    # BswImplementation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 6.1, p.120
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getArReleaseVersion          [x] impl  [x] docstring  [x] test
    # [x] setArReleaseVersion          [x] impl  [x] docstring  [x] test
    # [x] getBehaviorRef               [x] impl  [x] docstring  [x] test
    # [x] setBehaviorRef               [x] impl  [x] docstring  [x] test
    # [x] getPreconfiguredConfigurationRefs [x] impl  [x] docstring  [x] test
    # [x] addPreconfiguredConfigurationRef [x] impl  [x] docstring  [x] test
    # [x] getRecommendedConfigurationRefs [x] impl  [x] docstring  [x] test
    # [x] addRecommendedConfigurationRef [x] impl  [x] docstring  [x] test
    # [x] getVendorApiInfix            [x] impl  [x] docstring  [x] test
    # [x] setVendorApiInfix            [x] impl  [x] docstring  [x] test
    # [x] getVendorSpecificModuleDefRefs [x] impl  [x] docstring  [x] test
    # [x] addVendorSpecificModuleDefRef [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str) -> None:
        """
        Initializes the BSW implementation with a parent and short name.

        Args:
            parent: The parent ARObject that contains this implementation
            short_name: The unique short name of this implementation
        """
        super().__init__(parent, short_name)

        # Version of the AUTOSAR Release on which this implementation is based.
        # The numbering contains three levels (major, minor, revision) defined by AUTOSAR.
        # [constr_10302] The attribute shall exist when the configuration of the BSW module is finished.
        self.arReleaseVersion: Optional[RevisionLabelString] = None

        # The behavior of this implementation, made an association because it follows the SWCT pattern
        # and since ARElement cannot be split, the BswImplementation is not aggregated in BswBehavior.
        # [constr_10303] The reference shall exist when the configuration of the BSW module is finished.
        self.behaviorRef: Optional[RefType] = None

        # Reference to the set of preconfigured (i.e. fixed) configuration values for this BswImplementation.
        # For a cluster of modules more than one EcucModuleConfigurationValues can be referred (at most one per
        # module), otherwise at most one. [constr_4048] [constr_4045]
        self.preconfiguredConfigurationRefs: List[RefType] = []

        # Reference to one or more sets of recommended configuration values for this module or module cluster.
        # [constr_4046]
        self.recommendedConfigurationRefs: List[RefType] = []

        # Vendor-specific API infix used to extend API names for modules instantiated several times on a single ECU:
        # <Module Name>_<vendorId>_<vendorApiInfix>_<API name from SWS>. Mandatory for modules with upper
        # multiplicity > 1 and shall not be used for modules with upper multiplicity = 1. [constr_4099] SWS_BSW_00102.
        self.vendorApiInfix: Optional[Identifier] = None

        # Reference to the vendor specific EcucModuleDef used in this BswImplementation: one if it represents a
        # single module, several if it represents a cluster, and one or none if it represents a library. [constr_4047]
        self.vendorSpecificModuleDefRefs: List[RefType] = []

    def getArReleaseVersion(self) -> Optional[RevisionLabelString]:
        """
        Gets the AUTOSAR Release version on which this implementation is based.
        The numbering contains three levels (major, minor, revision). [constr_10302]

        Returns:
            RevisionLabelString representing the AUTOSAR release version
        """
        return self.arReleaseVersion

    def setArReleaseVersion(self, value: Optional[RevisionLabelString]) -> "BswImplementation":
        """
        Sets the AUTOSAR Release version on which this implementation is based.
        A None value is a no-op and does not overwrite an existing version. [constr_10302]

        Args:
            value: The AUTOSAR release version to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.arReleaseVersion = value
        return self

    def getBehaviorRef(self) -> Optional[RefType]:
        """
        Gets the reference to the behavior of this implementation.
        The relation is an association following the SWCT pattern; the BswImplementation is not
        aggregated in BswBehavior. [constr_10303]

        Returns:
            RefType to the behavior element
        """
        return self.behaviorRef

    def setBehaviorRef(self, value: Optional[RefType]) -> "BswImplementation":
        """
        Sets the reference to the behavior of this implementation.
        A None value is a no-op and does not overwrite an existing reference. [constr_10303]

        Args:
            value: The behavior reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.behaviorRef = value
        return self

    def getPreconfiguredConfigurationRefs(self) -> List[RefType]:
        """
        Gets the list of references to the set of preconfigured (i.e. fixed) configuration values.
        For a cluster of modules more than one EcucModuleConfigurationValues can be referred (at most one
        per module), otherwise at most one. [constr_4048] [constr_4045]

        Returns:
            List of RefType to preconfigured configurations
        """
        return self.preconfiguredConfigurationRefs

    def addPreconfiguredConfigurationRef(self, value: RefType) -> "BswImplementation":
        """
        Adds a reference to a set of preconfigured (i.e. fixed) configuration values.
        A None value is a no-op and is not appended. [constr_4048] [constr_4045]

        Args:
            value: The configuration reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.preconfiguredConfigurationRefs.append(value)
        return self

    def getRecommendedConfigurationRefs(self) -> List[RefType]:
        """
        Gets the list of references to one or more sets of recommended configuration values
        for this module or module cluster. [constr_4046]

        Returns:
            List of RefType to recommended configurations
        """
        return self.recommendedConfigurationRefs

    def addRecommendedConfigurationRef(self, value: RefType) -> "BswImplementation":
        """
        Adds a reference to a set of recommended configuration values for this module or module cluster.
        A None value is a no-op and is not appended. [constr_4046]

        Args:
            value: The configuration reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.recommendedConfigurationRefs.append(value)
        return self

    def getVendorApiInfix(self) -> Optional[Identifier]:
        """
        Gets the vendor-specific API infix used in naming conventions for this implementation.
        The implementation specific API name is generated as <Module Name>_<vendorId>_<vendorApiInfix>_<API name
        from SWS>. Mandatory for modules with upper multiplicity > 1. [constr_4099]

        Returns:
            Identifier for the vendor API infix
        """
        return self.vendorApiInfix

    def setVendorApiInfix(self, value: Optional[Identifier]) -> "BswImplementation":
        """
        Sets the vendor-specific API infix used in naming conventions for this implementation.
        A None value is a no-op and does not overwrite an existing infix. [constr_4099]

        Args:
            value: The vendor API infix to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.vendorApiInfix = value
        return self

    def getVendorSpecificModuleDefRefs(self) -> List[RefType]:
        """
        Gets the list of references to the vendor-specific EcucModuleDef(s) used in this BswImplementation:
        one if it represents a single module, several if a cluster, one or none if a library. [constr_4047]

        Returns:
            List of RefType to vendor-specific module definitions
        """
        return self.vendorSpecificModuleDefRefs

    def addVendorSpecificModuleDefRef(self, value: RefType) -> "BswImplementation":
        """
        Adds a reference to a vendor-specific EcucModuleDef used in this BswImplementation.
        A None value is a no-op and is not appended. [constr_4047]

        Args:
            value: The vendor-specific module definition reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.vendorSpecificModuleDefRefs.append(value)
        return self
