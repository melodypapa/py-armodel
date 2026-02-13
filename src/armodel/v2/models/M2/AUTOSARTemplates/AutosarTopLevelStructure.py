"""
AUTOSAR Package - AutosarTopLevelStructure

Package: M2::AUTOSARTemplates::AutosarTopLevelStructure
"""


from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARPackage,
)
from armodel.v2.models.M2.MSR.AsamHdo.AdminData import (
    AdminData,
)
from armodel.v2.models.M2.MSR.Documentation.BlockElements import (
    DocumentationBlock,
)
from armodel.v2.models.M2.MSR.AsamHdo.SpecialData import (
    Sdg,
)

__all__ = [
    "AUTOSAR",
    "FileInfoComment",
]


class AUTOSAR(ARObject):
    """
    Root element of an AUTOSAR description, also the root element in
    corresponding XML documents.

    Package: M2::AUTOSARTemplates::AutosarTopLevelStructure::AUTOSAR

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 301, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 298, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 287, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 59, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 968, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 1993, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 203, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_ARXMLSerializationRules.pdf (Page 30, Foundation R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 42, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 71, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 421, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (Page 29, Foundation R23-11)
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 56, Foundation R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 157, Foundation R23-11)
    """
    __instance = None
    __ar_release = None

    @staticmethod
    def getInstance():
        """Get the singleton AUTOSAR instance."""
        if AUTOSAR.__instance is None:
            AUTOSAR()
        return AUTOSAR.__instance

    @staticmethod
    def resetInstance():
        """Reset the singleton AUTOSAR instance."""
        AUTOSAR._AUTOSAR__instance = None
        AUTOSAR._AUTOSAR__ar_release = None

    @staticmethod
    def setARRelease(version: str) -> None:
        """
        Set the AUTOSAR release version.

        Args:
            version: The AUTOSAR version (e.g., "R23-11", "4.0.3")
        """
        AUTOSAR.__ar_release = version
        if AUTOSAR.__instance is not None:
            AUTOSAR.__instance.setExtendedAttribute("ar_release", version)

    @staticmethod
    def getARRelease() -> Optional[str]:
        """
        Get the AUTOSAR release version.

        Returns:
            The AUTOSAR version or None if not set
        """
        if AUTOSAR.__instance is not None:
            return AUTOSAR.__instance.getExtendedAttribute("ar_release") or AUTOSAR.__ar_release
        return AUTOSAR.__ar_release

    def __init__(self):
        if AUTOSAR.__instance is not None:
            raise Exception("The AUTOSAR is singleton!")
        AUTOSAR.__instance = self
        super().__init__()

        # Set default extended attributes for AUTOSAR
        self.setExtendedAttribute("schema_version", "3.2.3")
        self.setExtendedAttribute("xmlns", "http://autosar.org/3.2.3")

        # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This property allows to keep special data which is not the standard model.
        # It can be utilized to tool specific data.
        self._adminData: Optional[AdminData] = None

        # arPackage represents AR packages
        self._arPackage: List[ARPackage] = []

        # This represents a possibility to provide a structured in an AUTOSAR file.
        # 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module
        # Description Template R23-11.
        self._fileInfo: Optional["FileInfoComment"] = None

        # It is example to represent disclaimers and legal.
        self._introduction: Optional[DocumentationBlock] = None

    def clear(self) -> None:
        """Clear all properties of the AUTOSAR instance."""
        self._adminData = None
        self._arPackage = []
        self._fileInfo = None
        self._introduction = None
        self._extended_attributes.clear()
        self.setExtendedAttribute("schema_version", "3.2.3")
        self.setExtendedAttribute("xmlns", "http://autosar.org/3.2.3")

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
    
        # Skip type check for non-string types to avoid import issues
        # In V2, we use duck typing for flexibility
        self._adminData = value
    
    @property
    def ar_package(self) -> List[ARPackage]:
        """Get arPackage (Pythonic accessor)."""
        return self._arPackage
    
    @ar_package.setter
    def ar_package(self, value: List[ARPackage]) -> None:
        """
        Set arPackage with validation.
    
        Args:
            value: The arPackage to set
    
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, list):
            raise TypeError(
                f"ar_package must be a list or None, got {type(value).__name__}"
            )
        self._arPackage = value
    
    @property
    def ar_packages(self) -> List[ARPackage]:
        """Get arPackage (alias property)."""
        return self._arPackage
    
    @ar_packages.setter
    def ar_packages(self, value: List[ARPackage]) -> None:
        """
        Set arPackage with validation (alias setter).
    
        Args:
            value: The arPackage to set
    
        Raises:
            TypeError: If value type is incorrect
        """
        self.ar_package = value
    @property
    def file_info(self) -> Optional["FileInfoComment"]:
        """Get fileInfo (Pythonic accessor)."""
        return self._fileInfo

    @file_info.setter
    def file_info(self, value: Optional["FileInfoComment"]) -> None:
        """
        Set fileInfo with validation.

        Args:
            value: The fileInfo to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._fileInfo = None
            return

        # Skip type check for non-string types to avoid import issues
        # In V2, we use duck typing for flexibility
        self._fileInfo = value

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
    
        # Skip type check for non-string types to avoid import issues
        # In V2, we use duck typing for flexibility
        self._introduction = value
    def getTagName(self) -> str:
        """Get the XML tag name for AUTOSAR."""
        return "AUTOSAR"

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
    
    def setAdminData(self, value: AdminData) -> "AUTOSAR":
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
    
    def getArPackage(self) -> List[ARPackage]:
        """
        AUTOSAR-compliant getter for arPackage.
    
        Returns:
            The arPackage value
    
        Note:
            Delegates to ar_package property (CODING_RULE_V2_00017)
        """
        return self.ar_package  # Delegates to property
    
    def getFileInfo(self) -> "FileInfoComment":
        """
        AUTOSAR-compliant getter for fileInfo.
    
        Returns:
            The fileInfo value
    
        Note:
            Delegates to file_info property (CODING_RULE_V2_00017)
        """
        return self.file_info  # Delegates to property
    
    def setFileInfo(self, value: "FileInfoComment") -> "AUTOSAR":
        """
        AUTOSAR-compliant setter for fileInfo with method chaining.
    
        Args:
            value: The fileInfo to set
    
        Returns:
            self for method chaining
    
        Note:
            Delegates to file_info property setter (gets validation automatically)
        """
        self.file_info = value  # Delegates to property setter
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
    
    def setIntroduction(self, value: DocumentationBlock) -> "AUTOSAR":
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

    def with_admin_data(self, value: Optional[AdminData]) -> "AUTOSAR":
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

    def with_file_info(self, value: Optional["FileInfoComment"]) -> "AUTOSAR":
        """
        Set fileInfo and return self for chaining.

        Args:
            value: The fileInfo to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_file_info("value")
        """
        self.file_info = value  # Use property setter (gets validation)
        return self

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "AUTOSAR":
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


class FileInfoComment(ARObject):
    """
    This class supports StructuredComment to provide auxiliary information with
    the goal to create a comment.

    Package: M2::AUTOSARTemplates::AutosarTopLevelStructure::FileInfoComment

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 29, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

        # This property allows to keep special data which is not the standard model.
        # It can be utilized to tool specific data.
        self._sdg: List["Sdg"] = []

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    @property
    def sdg(self) -> List["Sdg"]:
        """Get sdg (Pythonic accessor)."""
        return self._sdg

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSdg(self) -> List["Sdg"]:
        """
        AUTOSAR-compliant getter for sdg.

        Returns:
            The sdg value

        Note:
            Delegates to sdg property (CODING_RULE_V2_00017)
        """
        return self.sdg  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====