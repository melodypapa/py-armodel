"""
AUTOSAR Package - AutosarTopLevelStructure

Package: M2::AUTOSARTemplates::AutosarTopLevelStructure
"""


from __future__ import annotations
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


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

    @staticmethod
    def getInstance():
        """Get the singleton AUTOSAR instance."""
        if AUTOSAR.__instance is None:
            AUTOSAR()
        return AUTOSAR.__instance

    @staticmethod
    def resetInstance():
        """Reset the singleton AUTOSAR instance."""
        AUTOSAR.__instance = None

    def __init__(self):
        if AUTOSAR.__instance is not None:
            raise Exception("The AUTOSAR is singleton!")
        AUTOSAR.__instance = self
        super().__init__()

        # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This property allows to keep special data which is not the standard model.
        # It can be utilized to tool specific data.
        self._adminData: Optional["AdminData"] = None

        # arPackage represents AR packages
        self._arPackage: List["ARPackage"] = []


    @property
    def admin_data(self) -> Optional["AdminData"]:
        """Get adminData (Pythonic accessor)."""
        return self._adminData

    @admin_data.setter
    def admin_data(self, value: Optional["AdminData"]) -> None:
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
    def ar_package(self) -> List["ARPackage"]:
        """Get arPackage (Pythonic accessor)."""
        return self._arPackage
        # This represents a possibility to provide a structured in an AUTOSAR file.
        # 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module
                # Description Template R23-11.
        self._fileInfo: Optional[FileInfoComment] = None

    @property
    def file_info(self) -> Optional[FileInfoComment]:
        """Get fileInfo (Pythonic accessor)."""
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
        # It is example to represent disclaimers and legal.
        self._introduction: Optional["DocumentationBlock"] = None

    @property
    def introduction(self) -> Optional["DocumentationBlock"]:
        """Get introduction (Pythonic accessor)."""
        return self._introduction

    @introduction.setter
    def introduction(self, value: Optional["DocumentationBlock"]) -> None:
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

    def with_sdg(self, value):
        """
        Set sdg and return self for chaining.

        Args:
            value: The sdg to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sdg("value")
        """
        self.sdg = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAdminData(self) -> "AdminData":
        """
        AUTOSAR-compliant getter for adminData.

        Returns:
            The adminData value

        Note:
            Delegates to admin_data property (CODING_RULE_V2_00017)
        """
        return self.admin_data  # Delegates to property

    def setAdminData(self, value: "AdminData") -> AUTOSAR:
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

    def getArPackage(self) -> List["ARPackage"]:
        """
        AUTOSAR-compliant getter for arPackage.

        Returns:
            The arPackage value

        Note:
            Delegates to ar_package property (CODING_RULE_V2_00017)
        """
        return self.ar_package  # Delegates to property

    def getFileInfo(self) -> FileInfoComment:
        """
        AUTOSAR-compliant getter for fileInfo.

        Returns:
            The fileInfo value

        Note:
            Delegates to file_info property (CODING_RULE_V2_00017)
        """
        return self.file_info  # Delegates to property

    def setFileInfo(self, value: FileInfoComment) -> AUTOSAR:
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

    def getIntroduction(self) -> "DocumentationBlock":
        """
        AUTOSAR-compliant getter for introduction.

        Returns:
            The introduction value

        Note:
            Delegates to introduction property (CODING_RULE_V2_00017)
        """
        return self.introduction  # Delegates to property

    def setIntroduction(self, value: "DocumentationBlock") -> AUTOSAR:
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

    def with_admin_data(self, value: Optional["AdminData"]) -> AUTOSAR:
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

    def with_file_info(self, value: Optional[FileInfoComment]) -> AUTOSAR:
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

    def with_introduction(self, value: Optional["DocumentationBlock"]) -> AUTOSAR:
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

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This property allows to keep special data which is not the standard model.
        # It can be utilized to tool specific data.
        self._sdg: List["Sdg"] = []

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
