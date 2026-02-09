"""
AUTOSAR Package - DataByIdentifier

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::DataByIdentifier
"""

from abc import ABC
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService import (
    DiagnosticServiceClass,
    DiagnosticServiceInstance,
)


class DiagnosticWriteDataByIdentifierClass(DiagnosticServiceClass):
    """
    This meta-class contains attributes shared by all instances of the "Write
    Data by Identifier" diagnostic service.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::DataByIdentifier::DiagnosticWriteDataByIdentifierClass
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 113, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticDataByIdentifier(DiagnosticServiceInstance, ABC):
    """
    This represents an abstract base class for all diagnostic services that
    access data by identifier.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::DataByIdentifier::DiagnosticDataByIdentifier
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 113, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticDataByIdentifier:
            raise TypeError("DiagnosticDataByIdentifier is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the linked DiagnosticDataIdentifier.
        self._dataIdentifier: Optional["DiagnosticAbstractData"] = None

    @property
    def data_identifier(self) -> Optional["DiagnosticAbstractData"]:
        """Get dataIdentifier (Pythonic accessor)."""
        return self._dataIdentifier

    @data_identifier.setter
    def data_identifier(self, value: Optional["DiagnosticAbstractData"]) -> None:
        """
        Set dataIdentifier with validation.
        
        Args:
            value: The dataIdentifier to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataIdentifier = None
            return

        if not isinstance(value, DiagnosticAbstractData):
            raise TypeError(
                f"dataIdentifier must be DiagnosticAbstractData or None, got {type(value).__name__}"
            )
        self._dataIdentifier = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataIdentifier(self) -> "DiagnosticAbstractData":
        """
        AUTOSAR-compliant getter for dataIdentifier.
        
        Returns:
            The dataIdentifier value
        
        Note:
            Delegates to data_identifier property (CODING_RULE_V2_00017)
        """
        return self.data_identifier  # Delegates to property

    def setDataIdentifier(self, value: "DiagnosticAbstractData") -> "DiagnosticDataByIdentifier":
        """
        AUTOSAR-compliant setter for dataIdentifier with method chaining.
        
        Args:
            value: The dataIdentifier to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to data_identifier property setter (gets validation automatically)
        """
        self.data_identifier = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_identifier(self, value: Optional["DiagnosticAbstractData"]) -> "DiagnosticDataByIdentifier":
        """
        Set dataIdentifier and return self for chaining.
        
        Args:
            value: The dataIdentifier to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_data_identifier("value")
        """
        self.data_identifier = value  # Use property setter (gets validation)
        return self



class DiagnosticReadDataByIdentifierClass(DiagnosticServiceClass):
    """
    This meta-class contains attributes shared by all instances of the "Read
    Data by Identifier" diagnostic service. (cid:53) 113 of 719 Document ID 673:
    AUTOSAR_CP_TPS_DiagnosticExtractTemplate Diagnostic Extract Template AUTOSAR
    CP R23-11 (cid:52)
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::DataByIdentifier::DiagnosticReadDataByIdentifierClass
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 113, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents the maximum number of allowed a single instance of
        # DiagnosticReadDataBy.
        self._maxDidToRead: Optional["PositiveInteger"] = None

    @property
    def max_did_to_read(self) -> Optional["PositiveInteger"]:
        """Get maxDidToRead (Pythonic accessor)."""
        return self._maxDidToRead

    @max_did_to_read.setter
    def max_did_to_read(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxDidToRead with validation.
        
        Args:
            value: The maxDidToRead to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxDidToRead = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxDidToRead must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maxDidToRead = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaxDidToRead(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxDidToRead.
        
        Returns:
            The maxDidToRead value
        
        Note:
            Delegates to max_did_to_read property (CODING_RULE_V2_00017)
        """
        return self.max_did_to_read  # Delegates to property

    def setMaxDidToRead(self, value: "PositiveInteger") -> "DiagnosticReadDataByIdentifierClass":
        """
        AUTOSAR-compliant setter for maxDidToRead with method chaining.
        
        Args:
            value: The maxDidToRead to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to max_did_to_read property setter (gets validation automatically)
        """
        self.max_did_to_read = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max_did_to_read(self, value: Optional["PositiveInteger"]) -> "DiagnosticReadDataByIdentifierClass":
        """
        Set maxDidToRead and return self for chaining.
        
        Args:
            value: The maxDidToRead to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_max_did_to_read("value")
        """
        self.max_did_to_read = value  # Use property setter (gets validation)
        return self



class DiagnosticReadScalingDataByIdentifierClass(DiagnosticServiceClass):
    """
    This meta-class contains attributes shared by all instances of the "Read
    Scaling Data by Identifier" diagnostic service.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::DataByIdentifier::DiagnosticReadScalingDataByIdentifierClass
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 116, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticReadDataByIdentifier(DiagnosticDataByIdentifier):
    """
    This represents an instance of the "Read Data by Identifier" diagnostic
    service.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::DataByIdentifier::DiagnosticReadDataByIdentifier
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 112, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference substantiates that abstract reference in the serviceClass for
                # this specific concrete class.
        # reference represents the ability to access among all DiagnosticReadDataBy the
                # given context.
        self._readClass: Optional["DiagnosticReadDataBy"] = None

    @property
    def read_class(self) -> Optional["DiagnosticReadDataBy"]:
        """Get readClass (Pythonic accessor)."""
        return self._readClass

    @read_class.setter
    def read_class(self, value: Optional["DiagnosticReadDataBy"]) -> None:
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

        if not isinstance(value, DiagnosticReadDataBy):
            raise TypeError(
                f"readClass must be DiagnosticReadDataBy or None, got {type(value).__name__}"
            )
        self._readClass = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getReadClass(self) -> "DiagnosticReadDataBy":
        """
        AUTOSAR-compliant getter for readClass.
        
        Returns:
            The readClass value
        
        Note:
            Delegates to read_class property (CODING_RULE_V2_00017)
        """
        return self.read_class  # Delegates to property

    def setReadClass(self, value: "DiagnosticReadDataBy") -> "DiagnosticReadDataByIdentifier":
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

    def with_read_class(self, value: Optional["DiagnosticReadDataBy"]) -> "DiagnosticReadDataByIdentifier":
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



class DiagnosticWriteDataByIdentifier(DiagnosticDataByIdentifier):
    """
    This represents an instance of the "Write Data by Identifier" diagnostic
    service.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::DataByIdentifier::DiagnosticWriteDataByIdentifier
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 113, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference substantiates that abstract reference in the serviceClass for
                # this specific concrete class.
        # reference represents the ability to access among all DiagnosticWriteDataBy
                # the given context.
        self._writeClass: Optional["DiagnosticWriteDataBy"] = None

    @property
    def write_class(self) -> Optional["DiagnosticWriteDataBy"]:
        """Get writeClass (Pythonic accessor)."""
        return self._writeClass

    @write_class.setter
    def write_class(self, value: Optional["DiagnosticWriteDataBy"]) -> None:
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

        if not isinstance(value, DiagnosticWriteDataBy):
            raise TypeError(
                f"writeClass must be DiagnosticWriteDataBy or None, got {type(value).__name__}"
            )
        self._writeClass = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getWriteClass(self) -> "DiagnosticWriteDataBy":
        """
        AUTOSAR-compliant getter for writeClass.
        
        Returns:
            The writeClass value
        
        Note:
            Delegates to write_class property (CODING_RULE_V2_00017)
        """
        return self.write_class  # Delegates to property

    def setWriteClass(self, value: "DiagnosticWriteDataBy") -> "DiagnosticWriteDataByIdentifier":
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

    def with_write_class(self, value: Optional["DiagnosticWriteDataBy"]) -> "DiagnosticWriteDataByIdentifier":
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



class DiagnosticReadScalingDataByIdentifier(DiagnosticDataByIdentifier):
    """
    This represents an instance of the "Read Scaling Data by Identifier"
    diagnostic service.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::DataByIdentifier::DiagnosticReadScalingDataByIdentifier
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 116, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference substantiates that abstract reference in the role serviceClass
                # for this specific concrete class.
        # reference represents the ability to access among all
                # DiagnosticReadScalingData the given context.
        self._readScaling: Optional["DiagnosticReadScaling"] = None

    @property
    def read_scaling(self) -> Optional["DiagnosticReadScaling"]:
        """Get readScaling (Pythonic accessor)."""
        return self._readScaling

    @read_scaling.setter
    def read_scaling(self, value: Optional["DiagnosticReadScaling"]) -> None:
        """
        Set readScaling with validation.
        
        Args:
            value: The readScaling to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._readScaling = None
            return

        if not isinstance(value, DiagnosticReadScaling):
            raise TypeError(
                f"readScaling must be DiagnosticReadScaling or None, got {type(value).__name__}"
            )
        self._readScaling = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getReadScaling(self) -> "DiagnosticReadScaling":
        """
        AUTOSAR-compliant getter for readScaling.
        
        Returns:
            The readScaling value
        
        Note:
            Delegates to read_scaling property (CODING_RULE_V2_00017)
        """
        return self.read_scaling  # Delegates to property

    def setReadScaling(self, value: "DiagnosticReadScaling") -> "DiagnosticReadScalingDataByIdentifier":
        """
        AUTOSAR-compliant setter for readScaling with method chaining.
        
        Args:
            value: The readScaling to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to read_scaling property setter (gets validation automatically)
        """
        self.read_scaling = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_read_scaling(self, value: Optional["DiagnosticReadScaling"]) -> "DiagnosticReadScalingDataByIdentifier":
        """
        Set readScaling and return self for chaining.
        
        Args:
            value: The readScaling to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_read_scaling("value")
        """
        self.read_scaling = value  # Use property setter (gets validation)
        return self
