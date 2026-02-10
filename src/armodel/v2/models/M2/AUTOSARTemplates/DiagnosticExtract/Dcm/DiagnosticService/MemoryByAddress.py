"""
AUTOSAR Package - MemoryByAddress

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::MemoryByAddress
"""

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import (
    DiagnosticCommonElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService import (
    DiagnosticServiceClass,
    DiagnosticServiceInstance,
)


class DiagnosticMemoryByAddress(DiagnosticServiceInstance, ABC):
    """
    This represents an abstract base class for diagnostic services that deal
    with accessing memory by address.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::MemoryByAddress::DiagnosticMemoryByAddress

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 139, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticMemoryByAddress:
            raise TypeError("DiagnosticMemoryByAddress is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    def with_memory_range(self, value):
        """
        Set memory_range and return self for chaining.

        Args:
            value: The memory_range to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_memory_range("value")
        """
        self.memory_range = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticMemoryIdentifier(DiagnosticCommonElement):
    """
    This meta-class represents the ability to define memory properties from the
    diagnostics point of view.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::MemoryByAddress::DiagnosticMemoryIdentifier

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 140, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents that access permission defined for the specific
        # DiagnosticMemoryIdentifier.
        self._access: Optional["DiagnosticAccess"] = None

    @property
    def access(self) -> Optional["DiagnosticAccess"]:
        """Get access (Pythonic accessor)."""
        return self._access

    @access.setter
    def access(self, value: Optional["DiagnosticAccess"]) -> None:
        """
        Set access with validation.

        Args:
            value: The access to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._access = None
            return

        if not isinstance(value, DiagnosticAccess):
            raise TypeError(
                f"access must be DiagnosticAccess or None, got {type(value).__name__}"
            )
        self._access = value
        self._id: Optional["PositiveInteger"] = None

    @property
    def id(self) -> Optional["PositiveInteger"]:
        """Get id (Pythonic accessor)."""
        return self._id

    @id.setter
    def id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set id with validation.

        Args:
            value: The id to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._id = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"id must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._id = value
        # segment.
        self._memoryHigh: Optional["String"] = None

    @property
    def memory_high(self) -> Optional["String"]:
        """Get memoryHigh (Pythonic accessor)."""
        return self._memoryHigh

    @memory_high.setter
    def memory_high(self, value: Optional["String"]) -> None:
        """
        Set memoryHigh with validation.

        Args:
            value: The memoryHigh to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._memoryHigh = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"memoryHigh must be String or str or None, got {type(value).__name__}"
            )
        self._memoryHigh = value
        # segment.
        self._memoryLow: Optional["String"] = None

    @property
    def memory_low(self) -> Optional["String"]:
        """Get memoryLow (Pythonic accessor)."""
        return self._memoryLow

    @memory_low.setter
    def memory_low(self, value: Optional["String"]) -> None:
        """
        Set memoryLow with validation.

        Args:
            value: The memoryLow to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._memoryLow = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"memoryLow must be String or str or None, got {type(value).__name__}"
            )
        self._memoryLow = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAccess(self) -> "DiagnosticAccess":
        """
        AUTOSAR-compliant getter for access.

        Returns:
            The access value

        Note:
            Delegates to access property (CODING_RULE_V2_00017)
        """
        return self.access  # Delegates to property

    def setAccess(self, value: "DiagnosticAccess") -> "DiagnosticMemoryIdentifier":
        """
        AUTOSAR-compliant setter for access with method chaining.

        Args:
            value: The access to set

        Returns:
            self for method chaining

        Note:
            Delegates to access property setter (gets validation automatically)
        """
        self.access = value  # Delegates to property setter
        return self

    def getId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for id.

        Returns:
            The id value

        Note:
            Delegates to id property (CODING_RULE_V2_00017)
        """
        return self.id  # Delegates to property

    def setId(self, value: "PositiveInteger") -> "DiagnosticMemoryIdentifier":
        """
        AUTOSAR-compliant setter for id with method chaining.

        Args:
            value: The id to set

        Returns:
            self for method chaining

        Note:
            Delegates to id property setter (gets validation automatically)
        """
        self.id = value  # Delegates to property setter
        return self

    def getMemoryHigh(self) -> "String":
        """
        AUTOSAR-compliant getter for memoryHigh.

        Returns:
            The memoryHigh value

        Note:
            Delegates to memory_high property (CODING_RULE_V2_00017)
        """
        return self.memory_high  # Delegates to property

    def setMemoryHigh(self, value: "String") -> "DiagnosticMemoryIdentifier":
        """
        AUTOSAR-compliant setter for memoryHigh with method chaining.

        Args:
            value: The memoryHigh to set

        Returns:
            self for method chaining

        Note:
            Delegates to memory_high property setter (gets validation automatically)
        """
        self.memory_high = value  # Delegates to property setter
        return self

    def getMemoryLow(self) -> "String":
        """
        AUTOSAR-compliant getter for memoryLow.

        Returns:
            The memoryLow value

        Note:
            Delegates to memory_low property (CODING_RULE_V2_00017)
        """
        return self.memory_low  # Delegates to property

    def setMemoryLow(self, value: "String") -> "DiagnosticMemoryIdentifier":
        """
        AUTOSAR-compliant setter for memoryLow with method chaining.

        Args:
            value: The memoryLow to set

        Returns:
            self for method chaining

        Note:
            Delegates to memory_low property setter (gets validation automatically)
        """
        self.memory_low = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_access(self, value: Optional["DiagnosticAccess"]) -> "DiagnosticMemoryIdentifier":
        """
        Set access and return self for chaining.

        Args:
            value: The access to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_access("value")
        """
        self.access = value  # Use property setter (gets validation)
        return self

    def with_id(self, value: Optional["PositiveInteger"]) -> "DiagnosticMemoryIdentifier":
        """
        Set id and return self for chaining.

        Args:
            value: The id to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_id("value")
        """
        self.id = value  # Use property setter (gets validation)
        return self

    def with_memory_high(self, value: Optional["String"]) -> "DiagnosticMemoryIdentifier":
        """
        Set memoryHigh and return self for chaining.

        Args:
            value: The memoryHigh to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_memory_high("value")
        """
        self.memory_high = value  # Use property setter (gets validation)
        return self

    def with_memory_low(self, value: Optional["String"]) -> "DiagnosticMemoryIdentifier":
        """
        Set memoryLow and return self for chaining.

        Args:
            value: The memoryLow to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_memory_low("value")
        """
        self.memory_low = value  # Use property setter (gets validation)
        return self



class DiagnosticWriteMemoryByAddressClass(DiagnosticServiceClass):
    """
    This meta-class contains attributes shared by all instances of the "Write
    Memory by Address" diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::MemoryByAddress::DiagnosticWriteMemoryByAddressClass

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 141, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticReadMemoryByAddressClass(DiagnosticServiceClass):
    """
    This meta-class contains attributes shared by all instances of the "Read
    Memory by Address" diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::MemoryByAddress::DiagnosticReadMemoryByAddressClass

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 142, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticTransferExitClass(DiagnosticServiceClass):
    """
    This meta-class contains attributes shared by all instances of the "Transfer
    Exit" diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::MemoryByAddress::DiagnosticTransferExitClass

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 143, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticDataTransferClass(DiagnosticServiceClass):
    """
    This meta-class contains attributes shared by all instances of the "Data
    Transfer" diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::MemoryByAddress::DiagnosticDataTransferClass

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 144, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticRequestDownloadClass(DiagnosticServiceClass):
    """
    This meta-class contains attributes shared by all instances of the "Request
    Download" diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::MemoryByAddress::DiagnosticRequestDownloadClass

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 144, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticRequestUploadClass(DiagnosticServiceClass):
    """
    This meta-class contains attributes shared by all instances of the "Request
    Upload" diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::MemoryByAddress::DiagnosticRequestUploadClass

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 146, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticMemoryAddressableRangeAccess(DiagnosticMemoryByAddress, ABC):
    """
    This abstract base class

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::MemoryByAddress::DiagnosticMemoryAddressableRangeAccess

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 140, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticMemoryAddressableRangeAccess:
            raise TypeError("DiagnosticMemoryAddressableRangeAccess is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the formal description of the memory to which the
        # DiagnosticMemoryByAddress.
        self._memoryRange: List["DiagnosticMemory"] = []

    @property
    def memory_range(self) -> List["DiagnosticMemory"]:
        """Get memoryRange (Pythonic accessor)."""
        return self._memoryRange

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMemoryRange(self) -> List["DiagnosticMemory"]:
        """
        AUTOSAR-compliant getter for memoryRange.

        Returns:
            The memoryRange value

        Note:
            Delegates to memory_range property (CODING_RULE_V2_00017)
        """
        return self.memory_range  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticTransferExit(DiagnosticMemoryByAddress):
    """
    This represents an instance of the "Transfer Exit" diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::MemoryByAddress::DiagnosticTransferExit

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 142, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference substantiates that abstract reference in the reference
        # represents the ability to access among all DiagnosticTransferExit in the.
        self._transferExit: Optional["DiagnosticTransferExit"] = None

    @property
    def transfer_exit(self) -> Optional["DiagnosticTransferExit"]:
        """Get transferExit (Pythonic accessor)."""
        return self._transferExit

    @transfer_exit.setter
    def transfer_exit(self, value: Optional["DiagnosticTransferExit"]) -> None:
        """
        Set transferExit with validation.

        Args:
            value: The transferExit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transferExit = None
            return

        if not isinstance(value, DiagnosticTransferExit):
            raise TypeError(
                f"transferExit must be DiagnosticTransferExit or None, got {type(value).__name__}"
            )
        self._transferExit = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTransferExit(self) -> "DiagnosticTransferExit":
        """
        AUTOSAR-compliant getter for transferExit.

        Returns:
            The transferExit value

        Note:
            Delegates to transfer_exit property (CODING_RULE_V2_00017)
        """
        return self.transfer_exit  # Delegates to property

    def setTransferExit(self, value: "DiagnosticTransferExit") -> "DiagnosticTransferExit":
        """
        AUTOSAR-compliant setter for transferExit with method chaining.

        Args:
            value: The transferExit to set

        Returns:
            self for method chaining

        Note:
            Delegates to transfer_exit property setter (gets validation automatically)
        """
        self.transfer_exit = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_transfer_exit(self, value: Optional["DiagnosticTransferExit"]) -> "DiagnosticTransferExit":
        """
        Set transferExit and return self for chaining.

        Args:
            value: The transferExit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_transfer_exit("value")
        """
        self.transfer_exit = value  # Use property setter (gets validation)
        return self



class DiagnosticDataTransfer(DiagnosticMemoryByAddress):
    """
    This represents an instance of the "Data Transfer" diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::MemoryByAddress::DiagnosticDataTransfer

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 143, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference substantiates that abstract reference in the reference
        # represents the ability to access among all DiagnosticDataTransfer in the.
        self._dataTransfer: Optional["DiagnosticDataTransfer"] = None

    @property
    def data_transfer(self) -> Optional["DiagnosticDataTransfer"]:
        """Get dataTransfer (Pythonic accessor)."""
        return self._dataTransfer

    @data_transfer.setter
    def data_transfer(self, value: Optional["DiagnosticDataTransfer"]) -> None:
        """
        Set dataTransfer with validation.

        Args:
            value: The dataTransfer to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataTransfer = None
            return

        if not isinstance(value, DiagnosticDataTransfer):
            raise TypeError(
                f"dataTransfer must be DiagnosticDataTransfer or None, got {type(value).__name__}"
            )
        self._dataTransfer = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataTransfer(self) -> "DiagnosticDataTransfer":
        """
        AUTOSAR-compliant getter for dataTransfer.

        Returns:
            The dataTransfer value

        Note:
            Delegates to data_transfer property (CODING_RULE_V2_00017)
        """
        return self.data_transfer  # Delegates to property

    def setDataTransfer(self, value: "DiagnosticDataTransfer") -> "DiagnosticDataTransfer":
        """
        AUTOSAR-compliant setter for dataTransfer with method chaining.

        Args:
            value: The dataTransfer to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_transfer property setter (gets validation automatically)
        """
        self.data_transfer = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_transfer(self, value: Optional["DiagnosticDataTransfer"]) -> "DiagnosticDataTransfer":
        """
        Set dataTransfer and return self for chaining.

        Args:
            value: The dataTransfer to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_transfer("value")
        """
        self.data_transfer = value  # Use property setter (gets validation)
        return self



class DiagnosticWriteMemoryByAddress(DiagnosticMemoryAddressableRangeAccess):
    """
    This represents an instance of the "Write Memory by Address" diagnostic
    service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::MemoryByAddress::DiagnosticWriteMemoryByAddress

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 140, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference substantiates that abstract reference in the serviceClass for
                # this specific concrete class.
        # reference represents the ability to access among all DiagnosticWritememoryBy
                # the given context.
        self._writeClass: Optional["DiagnosticWriteMemory"] = None

    @property
    def write_class(self) -> Optional["DiagnosticWriteMemory"]:
        """Get writeClass (Pythonic accessor)."""
        return self._writeClass

    @write_class.setter
    def write_class(self, value: Optional["DiagnosticWriteMemory"]) -> None:
        """
        Set writeClass with validation.

        Args:
            value: The writeClass to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._writeClass = None
            return

        if not isinstance(value, DiagnosticWriteMemory):
            raise TypeError(
                f"writeClass must be DiagnosticWriteMemory or None, got {type(value).__name__}"
            )
        self._writeClass = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getWriteClass(self) -> "DiagnosticWriteMemory":
        """
        AUTOSAR-compliant getter for writeClass.

        Returns:
            The writeClass value

        Note:
            Delegates to write_class property (CODING_RULE_V2_00017)
        """
        return self.write_class  # Delegates to property

    def setWriteClass(self, value: "DiagnosticWriteMemory") -> "DiagnosticWriteMemoryByAddress":
        """
        AUTOSAR-compliant setter for writeClass with method chaining.

        Args:
            value: The writeClass to set

        Returns:
            self for method chaining

        Note:
            Delegates to write_class property setter (gets validation automatically)
        """
        self.write_class = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_write_class(self, value: Optional["DiagnosticWriteMemory"]) -> "DiagnosticWriteMemoryByAddress":
        """
        Set writeClass and return self for chaining.

        Args:
            value: The writeClass to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_write_class("value")
        """
        self.write_class = value  # Use property setter (gets validation)
        return self



class DiagnosticReadMemoryByAddress(DiagnosticMemoryAddressableRangeAccess):
    """
    This represents an instance of the "Read Memory by Address" diagnostic
    service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::MemoryByAddress::DiagnosticReadMemoryByAddress

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 141, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference substantiates that abstract reference in the serviceClass for
                # this specific concrete class.
        # reference represents the ability to access among all DiagnosticReadMemoryBy
                # the given context.
        self._readClass: Optional["DiagnosticReadMemory"] = None

    @property
    def read_class(self) -> Optional["DiagnosticReadMemory"]:
        """Get readClass (Pythonic accessor)."""
        return self._readClass

    @read_class.setter
    def read_class(self, value: Optional["DiagnosticReadMemory"]) -> None:
        """
        Set readClass with validation.

        Args:
            value: The readClass to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._readClass = None
            return

        if not isinstance(value, DiagnosticReadMemory):
            raise TypeError(
                f"readClass must be DiagnosticReadMemory or None, got {type(value).__name__}"
            )
        self._readClass = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getReadClass(self) -> "DiagnosticReadMemory":
        """
        AUTOSAR-compliant getter for readClass.

        Returns:
            The readClass value

        Note:
            Delegates to read_class property (CODING_RULE_V2_00017)
        """
        return self.read_class  # Delegates to property

    def setReadClass(self, value: "DiagnosticReadMemory") -> "DiagnosticReadMemoryByAddress":
        """
        AUTOSAR-compliant setter for readClass with method chaining.

        Args:
            value: The readClass to set

        Returns:
            self for method chaining

        Note:
            Delegates to read_class property setter (gets validation automatically)
        """
        self.read_class = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_read_class(self, value: Optional["DiagnosticReadMemory"]) -> "DiagnosticReadMemoryByAddress":
        """
        Set readClass and return self for chaining.

        Args:
            value: The readClass to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_read_class("value")
        """
        self.read_class = value  # Use property setter (gets validation)
        return self



class DiagnosticRequestDownload(DiagnosticMemoryAddressableRangeAccess):
    """
    This represents an instance of the "Request Download" diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::MemoryByAddress::DiagnosticRequestDownload

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 144, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference substantiates that abstract reference in the role serviceClass
                # for this specific concrete class.
        # reference represents the ability to access among all
                # DiagnosticRequestDownload given context.
        self._request: Optional["DiagnosticRequest"] = None

    @property
    def request(self) -> Optional["DiagnosticRequest"]:
        """Get request (Pythonic accessor)."""
        return self._request

    @request.setter
    def request(self, value: Optional["DiagnosticRequest"]) -> None:
        """
        Set request with validation.

        Args:
            value: The request to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._request = None
            return

        if not isinstance(value, DiagnosticRequest):
            raise TypeError(
                f"request must be DiagnosticRequest or None, got {type(value).__name__}"
            )
        self._request = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRequest(self) -> "DiagnosticRequest":
        """
        AUTOSAR-compliant getter for request.

        Returns:
            The request value

        Note:
            Delegates to request property (CODING_RULE_V2_00017)
        """
        return self.request  # Delegates to property

    def setRequest(self, value: "DiagnosticRequest") -> "DiagnosticRequestDownload":
        """
        AUTOSAR-compliant setter for request with method chaining.

        Args:
            value: The request to set

        Returns:
            self for method chaining

        Note:
            Delegates to request property setter (gets validation automatically)
        """
        self.request = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_request(self, value: Optional["DiagnosticRequest"]) -> "DiagnosticRequestDownload":
        """
        Set request and return self for chaining.

        Args:
            value: The request to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_request("value")
        """
        self.request = value  # Use property setter (gets validation)
        return self



class DiagnosticRequestUpload(DiagnosticMemoryAddressableRangeAccess):
    """
    This represents an instance of the "Request Upload" diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::MemoryByAddress::DiagnosticRequestUpload

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 145, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference substantiates that abstract reference in the reference
        # represents the ability to access among all DiagnosticRequestUpload in
        # context.
        self._requestUpload: Optional["DiagnosticRequest"] = None

    @property
    def request_upload(self) -> Optional["DiagnosticRequest"]:
        """Get requestUpload (Pythonic accessor)."""
        return self._requestUpload

    @request_upload.setter
    def request_upload(self, value: Optional["DiagnosticRequest"]) -> None:
        """
        Set requestUpload with validation.

        Args:
            value: The requestUpload to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._requestUpload = None
            return

        if not isinstance(value, DiagnosticRequest):
            raise TypeError(
                f"requestUpload must be DiagnosticRequest or None, got {type(value).__name__}"
            )
        self._requestUpload = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRequestUpload(self) -> "DiagnosticRequest":
        """
        AUTOSAR-compliant getter for requestUpload.

        Returns:
            The requestUpload value

        Note:
            Delegates to request_upload property (CODING_RULE_V2_00017)
        """
        return self.request_upload  # Delegates to property

    def setRequestUpload(self, value: "DiagnosticRequest") -> "DiagnosticRequestUpload":
        """
        AUTOSAR-compliant setter for requestUpload with method chaining.

        Args:
            value: The requestUpload to set

        Returns:
            self for method chaining

        Note:
            Delegates to request_upload property setter (gets validation automatically)
        """
        self.request_upload = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_request_upload(self, value: Optional["DiagnosticRequest"]) -> "DiagnosticRequestUpload":
        """
        Set requestUpload and return self for chaining.

        Args:
            value: The requestUpload to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_request_upload("value")
        """
        self.request_upload = value  # Use property setter (gets validation)
        return self
