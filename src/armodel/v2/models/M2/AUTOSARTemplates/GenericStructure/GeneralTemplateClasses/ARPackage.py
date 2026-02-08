from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import (
    CollectableElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class ARPackage(CollectableElement):
    """
    AUTOSAR package, allowing to create top level packages to structure the
    contained ARElements. ARPackages are open sets. This means that in a file
    based description system multiple files can be used to partially describe
    the contents of a package. This is an extended version of MSR’s SW-SYSTEM.

    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ARPackage::ARPackage

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 300, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 297, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 286, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 58, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 967, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 1992, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 203, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 53, Foundation R23-11)
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 55, Foundation R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 156, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents a sub package within an ARPackage, for an unlimited package
                # hierarchy.
        # atpVariation.
        self._arPackage: List["ARPackage"] = []

    @property
    def ar_package(self) -> List["ARPackage"]:
        """Get arPackage (Pythonic accessor)."""
        return self._arPackage
        # Elements that are part of this package atpVariation.
        self._element: List["PackageableElement"] = []

    @property
    def element(self) -> List["PackageableElement"]:
        """Get element (Pythonic accessor)."""
        return self._element
        # This denotes the reference bases for the package.
        # This is for all relative references within the package.
        # needs to be selected according to the base the references.
        self._referenceBase: List[RefType] = []

    @property
    def reference_base(self) -> List[RefType]:
        """Get referenceBase (Pythonic accessor)."""
        return self._referenceBase

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArPackage(self) -> List["ARPackage"]:
        """
        AUTOSAR-compliant getter for arPackage.

        Returns:
            The arPackage value

        Note:
            Delegates to ar_package property (CODING_RULE_V2_00017)
        """
        return self.ar_package  # Delegates to property

    def getElement(self) -> List["PackageableElement"]:
        """
        AUTOSAR-compliant getter for element.

        Returns:
            The element value

        Note:
            Delegates to element property (CODING_RULE_V2_00017)
        """
        return self.element  # Delegates to property

    def getReferenceBase(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for referenceBase.

        Returns:
            The referenceBase value

        Note:
            Delegates to reference_base property (CODING_RULE_V2_00017)
        """
        return self.reference_base  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
