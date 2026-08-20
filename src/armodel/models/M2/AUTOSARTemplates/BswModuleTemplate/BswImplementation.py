"""
This module contains classes for representing AUTOSAR Basic Software (BSW) implementation.
BSW implementation describes how BSW modules are implemented, including their behavior references,
configuration options, and version information.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType, RevisionLabelString
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation import Implementation
from typing import List, Optional


class BswImplementation(Implementation):
    """Contains the implementation specific information in addition to the generic specification (BswModule Description and BswBehavior). It is possible to have several different BswImplementations referring to the same BswBehavior."""

    # BswImplementation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 6.1, p.120
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getArReleaseVersion             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setArReleaseVersion             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getBehaviorRef                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setBehaviorRef                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPreconfiguredConfigurationRefs [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addPreconfiguredConfigurationRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRecommendedConfigurationRefs [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addRecommendedConfigurationRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getVendorApiInfix               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setVendorApiInfix               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getVendorSpecificModuleDefRefs  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addVendorSpecificModuleDefRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        # Version of the AUTOSAR Release on which this implementation is based. The numbering contains three levels (major, minor, revision) which are defined by AUTOSAR.
        self.arReleaseVersion: Optional[RevisionLabelString] = None

        # The behavior of this implementation. This relation is made as an association because • it follows the pattern of the SWCT • since ARElement cannot be splitted, but we want supply the implementation later, the Bsw Implementation is not aggregated in BswBehavior
        self.behaviorRef: Optional[RefType] = None

        # Reference to the set of preconfigured (i.e. fixed) configuration values for this BswImplementation. If the BswImplementation represents a cluster of several modules, more than one EcucModuleConfigurationValues element can be referred (at most one per module), otherwise at most one such element can be referred.
        self.preconfiguredConfigurationRefs: List[RefType] = []

        # Reference to one or more sets of recommended configuration values for this module or module cluster.
        self.recommendedConfigurationRefs: List[RefType] = []

        # In driver modules which can be instantiated several times on a single ECU, SRS_BSW_00347 requires that the names of files, APIs, published parameters and memory allocation keywords are extended by the vendorId and a vendor specific name. This parameter is used to specify the vendor specific name. In total, the implementation specific API name is generated as follows: <Module Name>_<vendorId>_ <vendorApiInfix>_<API name from SWS>. E.g. assuming that the vendorId of the implementer is 123 and the implementer chose a vendorApiInfix of "v11r456" an API name Can_Write defined in the SWS will translate to Can_123_v11r456_Write. This attribute is mandatory for all modules with upper multiplicity > 1. It shall not be used for modules with upper multiplicity =1. See also SWS_BSW_00102.
        self.vendorApiInfix: Optional[Identifier] = None

        # Reference to • the vendor specific EcucModuleDef used in this Bsw Implementation if it represents a single module • several EcucModuleDefs used in this Bsw Implementation if it represents a cluster of modules • one or no EcucModuleDefs used in this Bsw Implementation if it represents a library
        self.vendorSpecificModuleDefRefs: List[RefType] = []

    def getArReleaseVersion(self) -> Optional[RevisionLabelString]:
        """Version of the AUTOSAR Release on which this implementation is based. The numbering contains three levels (major, minor, revision) which are defined by AUTOSAR."""
        return self.arReleaseVersion

    def setArReleaseVersion(self, value: Optional[RevisionLabelString]) -> "BswImplementation":
        """Version of the AUTOSAR Release on which this implementation is based. The numbering contains three levels (major, minor, revision) which are defined by AUTOSAR. A None value is a no-op and does not overwrite an existing version."""
        if value is not None:
            self.arReleaseVersion = value
        return self

    def getBehaviorRef(self) -> Optional[RefType]:
        """The behavior of this implementation. This relation is made as an association because • it follows the pattern of the SWCT • since ARElement cannot be splitted, but we want supply the implementation later, the Bsw Implementation is not aggregated in BswBehavior"""
        return self.behaviorRef

    def setBehaviorRef(self, value: Optional[RefType]) -> "BswImplementation":
        """The behavior of this implementation. This relation is made as an association because • it follows the pattern of the SWCT • since ARElement cannot be splitted, but we want supply the implementation later, the Bsw Implementation is not aggregated in BswBehavior A None value is a no-op and does not overwrite an existing reference."""
        if value is not None:
            self.behaviorRef = value
        return self

    def getPreconfiguredConfigurationRefs(self) -> List[RefType]:
        """Reference to the set of preconfigured (i.e. fixed) configuration values for this BswImplementation. If the BswImplementation represents a cluster of several modules, more than one EcucModuleConfigurationValues element can be referred (at most one per module), otherwise at most one such element can be referred."""
        return self.preconfiguredConfigurationRefs

    def addPreconfiguredConfigurationRef(self, value: RefType) -> "BswImplementation":
        """Reference to the set of preconfigured (i.e. fixed) configuration values for this BswImplementation. If the BswImplementation represents a cluster of several modules, more than one EcucModuleConfigurationValues element can be referred (at most one per module), otherwise at most one such element can be referred. A None value is a no-op and is not appended."""
        if value is not None:
            self.preconfiguredConfigurationRefs.append(value)
        return self

    def getRecommendedConfigurationRefs(self) -> List[RefType]:
        """Reference to one or more sets of recommended configuration values for this module or module cluster."""
        return self.recommendedConfigurationRefs

    def addRecommendedConfigurationRef(self, value: RefType) -> "BswImplementation":
        """Reference to one or more sets of recommended configuration values for this module or module cluster. A None value is a no-op and is not appended."""
        if value is not None:
            self.recommendedConfigurationRefs.append(value)
        return self

    def getVendorApiInfix(self) -> Optional[Identifier]:
        """In driver modules which can be instantiated several times on a single ECU, SRS_BSW_00347 requires that the names of files, APIs, published parameters and memory allocation keywords are extended by the vendorId and a vendor specific name. This parameter is used to specify the vendor specific name. In total, the implementation specific API name is generated as follows: <Module Name>_<vendorId>_ <vendorApiInfix>_<API name from SWS>. E.g. assuming that the vendorId of the implementer is 123 and the implementer chose a vendorApiInfix of "v11r456" an API name Can_Write defined in the SWS will translate to Can_123_v11r456_Write. This attribute is mandatory for all modules with upper multiplicity > 1. It shall not be used for modules with upper multiplicity =1. See also SWS_BSW_00102."""
        return self.vendorApiInfix

    def setVendorApiInfix(self, value: Optional[Identifier]) -> "BswImplementation":
        """In driver modules which can be instantiated several times on a single ECU, SRS_BSW_00347 requires that the names of files, APIs, published parameters and memory allocation keywords are extended by the vendorId and a vendor specific name. This parameter is used to specify the vendor specific name. In total, the implementation specific API name is generated as follows: <Module Name>_<vendorId>_ <vendorApiInfix>_<API name from SWS>. E.g. assuming that the vendorId of the implementer is 123 and the implementer chose a vendorApiInfix of "v11r456" an API name Can_Write defined in the SWS will translate to Can_123_v11r456_Write. This attribute is mandatory for all modules with upper multiplicity > 1. It shall not be used for modules with upper multiplicity =1. See also SWS_BSW_00102. A None value is a no-op and does not overwrite an existing infix."""
        if value is not None:
            self.vendorApiInfix = value
        return self

    def getVendorSpecificModuleDefRefs(self) -> List[RefType]:
        """Reference to • the vendor specific EcucModuleDef used in this Bsw Implementation if it represents a single module • several EcucModuleDefs used in this Bsw Implementation if it represents a cluster of modules • one or no EcucModuleDefs used in this Bsw Implementation if it represents a library"""
        return self.vendorSpecificModuleDefRefs

    def addVendorSpecificModuleDefRef(self, value: RefType) -> "BswImplementation":
        """Reference to • the vendor specific EcucModuleDef used in this Bsw Implementation if it represents a single module • several EcucModuleDefs used in this Bsw Implementation if it represents a cluster of modules • one or no EcucModuleDefs used in this Bsw Implementation if it represents a library A None value is a no-op and is not appended."""
        if value is not None:
            self.vendorSpecificModuleDefRefs.append(value)
        return self
