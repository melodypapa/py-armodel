"""
AUTOSAR root element - singleton pattern with extensible design.

Package: M2::AUTOSARTemplates::AutosarTopLevelStructure::AUTOSAR

Sources:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 301, Classic Platform R23-11)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 298, Classic Platform R23-11)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 287, Classic Platform R23-11)
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 59, Classic Platform R23-11)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 968, Classic Platform R23-11)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 1993, Classic Platform R23-11)
"""
from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.FileInfoComment import (
    FileInfoComment,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARPackage,
)
from armodel.v2.models.M2.MSR.AsamHdo.AdminData import (
    AdminData,
)
from armodel.v2.models.M2.MSR.Documentation.DocumentationBlock import (
    DocumentationBlock,
)


class AUTOSAR(ARObject):
    """
    Package: M2::AUTOSARTemplates::AutosarTopLevelStructure
    AUTOSAR root element - singleton pattern with extensible design.

    This class follows the singleton pattern and provides extension points
    for V2 modules to add custom functionality.

    Singleton Pattern:
    - Use getInstance() to get the singleton instance
    - Instance is created on first call
    - Can be reset by setting _instance = None (for testing)

    Extension Points:
    - _extended_attributes: Custom properties for V2 modules
    - getTagName(): Override for custom XML tags
    - AUTOSAR M2 properties (adminData, fileInfo, introduction, arPackages)

    AUTOSAR M2 Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 301, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 298, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 287, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 59, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 968, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 1993, Classic Platform R23-11)
    """

    # Class variable for singleton instance
    _instance: Optional["AUTOSAR"] = None

    def __init__(self) -> None:
        """
        Initialize AUTOSAR singleton.

        Raises:
            TypeError: If instance already exists (singleton enforcement).
        """
        super().__init__()
        # Core AUTOSAR attribute
        self.ar_packages: List[ARPackage] = []

        # AUTOSAR M2 attributes
        # Administrative data of an AUTOSAR file
        self._adminData: Optional[AdminData] = None

        # File information
        self._fileInfo: Optional[FileInfoComment] = None

        # Introduction (disclaimers, legal information)
        self._introduction: Optional[DocumentationBlock] = None

        # V2 extended attributes for custom properties
        self.setExtendedAttribute("schema_version", "3.2.3")
        self.setExtendedAttribute("xmlns", "http://autosar.org/3.2.3")

    @classmethod
    def getInstance(cls) -> "AUTOSAR":
        """
        Get the singleton AUTOSAR instance.

        Creates instance on first call, returns existing instance on
        subsequent calls.

        Returns:
            The singleton AUTOSAR instance.
        """
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @classmethod
    def resetInstance(cls) -> None:
        """
        Reset the singleton instance.

        This is primarily intended for testing purposes where a fresh
        AUTOSAR instance is needed.
        """
        cls._instance = None

    @classmethod
    def setARRelease(cls, version: str) -> None:
        """
        Set the AUTOSAR release version.

        Args:
            version: The AUTOSAR version (e.g., "R23-11", "4.0.3", "R24-11")
        """
        if cls._instance is not None:
            cls._instance.setExtendedAttribute("ar_release", version)

    @classmethod
    def getARRelease(cls) -> Optional[str]:
        """
        Get the AUTOSAR release version.

        Returns:
            The AUTOSAR version or None if not set.
        """
        if cls._instance is not None:
            return cls._instance.getExtendedAttribute("ar_release")
        return None

    # ===== AUTOSAR M2 Properties (CODING_RULE_V2_00016) =====

    @property
    def admin_data(self) -> Optional[AdminData]:
        """
        Get adminData (Pythonic accessor).

        Administrative data of an AUTOSAR file.
        """
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
    def ar_package(self) -> List[ARPackage]:
        """
        Get arPackage (Pythonic accessor).

        Top level packages in an AUTOSAR model.
        """
        return self.ar_packages

    @property
    def file_info(self) -> Optional[FileInfoComment]:
        """
        Get fileInfo (Pythonic accessor).

        Structured information about an AUTOSAR file.
        """
        return self._fileInfo

    @file_info.setter
    def file_info(self, value: Optional[FileInfoComment]) -> None:
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

        if not isinstance(value, FileInfoComment):
            raise TypeError(
                f"fileInfo must be FileInfoComment or None, got {type(value).__name__}"
            )
        self._fileInfo = value

    @property
    def introduction(self) -> Optional[DocumentationBlock]:
        """
        Get introduction (Pythonic accessor).

        Introduction on an AUTOSAR file (disclaimers, legal information).
        """
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

    def with_ar_package(self, value):
        """
        Set ar_package and return self for chaining.

        Args:
            value: The ar_package to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ar_package("value")
        """
        self.ar_package = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (CODING_RULE_V2_00017) =====

    def getAdminData(self) -> AdminData:
        """
        AUTOSAR-compliant getter for adminData.

        Returns:
            The adminData value

        Note:
            Delegates to admin_data property (CODING_RULE_V2_00017)
        """
        return self.admin_data

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
        self.admin_data = value
        return self

    def getArPackage(self) -> List[ARPackage]:
        """
        AUTOSAR-compliant getter for arPackage.

        Returns:
            The arPackage value

        Note:
            Delegates to ar_package property (CODING_RULE_V2_00017)
        """
        return self.ar_package

    def getFileInfo(self) -> FileInfoComment:
        """
        AUTOSAR-compliant getter for fileInfo.

        Returns:
            The fileInfo value

        Note:
            Delegates to file_info property (CODING_RULE_V2_00017)
        """
        return self.file_info

    def setFileInfo(self, value: FileInfoComment) -> "AUTOSAR":
        """
        AUTOSAR-compliant setter for fileInfo with method chaining.

        Args:
            value: The fileInfo to set

        Returns:
            self for method chaining

        Note:
            Delegates to file_info property setter (gets validation automatically)
        """
        self.file_info = value
        return self

    def getIntroduction(self) -> DocumentationBlock:
        """
        AUTOSAR-compliant getter for introduction.

        Returns:
            The introduction value

        Note:
            Delegates to introduction property (CODING_RULE_V2_00017)
        """
        return self.introduction

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
        self.introduction = value
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
            >>> AUTOSAR.getInstance().with_admin_data(admin_data)
        """
        self.admin_data = value
        return self

    def with_file_info(self, value: Optional[FileInfoComment]) -> "AUTOSAR":
        """
        Set fileInfo and return self for chaining.

        Args:
            value: The fileInfo to set

        Returns:
            self for method chaining

        Example:
            >>> AUTOSAR.getInstance().with_file_info(file_info)
        """
        self.file_info = value
        return self

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "AUTOSAR":
        """
        Set introduction and return self for chaining.

        Args:
            value: The introduction to set

        Returns:
            self for method chaining

        Example:
            >>> AUTOSAR.getInstance().with_introduction(intro)
        """
        self.introduction = value
        return self


