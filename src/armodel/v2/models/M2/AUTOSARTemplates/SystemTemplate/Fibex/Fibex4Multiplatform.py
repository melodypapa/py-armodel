"""
AUTOSAR Package - Fibex4Multiplatform

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Multiplatform
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    PositiveInteger,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.__init__ import (
    FibexElement,
)


class Gateway(FibexElement):
    """
    A gateway is an ECU that is connected to two or more clusters (channels, but
    not redundant), and performs a frame, Pdu or signal mapping between them.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Multiplatform::Gateway
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 837, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to one ECU instance that implements the.
        self._ecu: Optional["EcuInstance"] = None

    @property
    def ecu(self) -> Optional["EcuInstance"]:
        """Get ecu (Pythonic accessor)."""
        return self._ecu

    @ecu.setter
    def ecu(self, value: Optional["EcuInstance"]) -> None:
        """
        Set ecu with validation.
        
        Args:
            value: The ecu to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecu = None
            return

        if not isinstance(value, EcuInstance):
            raise TypeError(
                f"ecu must be EcuInstance or None, got {type(value).__name__}"
            )
        self._ecu = value
                # in general is only possible a common platform).
        # In this case source and should be the identical object.
        # frames are variable in clusters, the mapping needs to be variable, too.
        # atpVariation.
        self._frameMapping: List["RefType"] = []

    @property
    def frame_mapping(self) -> List["RefType"]:
        """Get frameMapping (Pythonic accessor)."""
        return self._frameMapping
        # IPdu Gateway: Arranges those IPdus that are transferred gateway from one
                # channel to the other in pairs and mapping between them.
        # PDUs are variable in clusters, the gateway needs to be variable, too.
        # atpVariation.
        self._iPduMapping: List["RefType"] = []

    @property
    def i_pdu_mapping(self) -> List["RefType"]:
        """Get iPduMapping (Pythonic accessor)."""
        return self._iPduMapping
        # Signal Gateway: Arranges those signals that are the gateway from one channel
                # to the other and defines the mapping between them.
        # signals are variable in clusters, the mapping needs to be variable, too.
        # atpVariation.
        self._signalMapping: List["RefType"] = []

    @property
    def signal_mapping(self) -> List["RefType"]:
        """Get signalMapping (Pythonic accessor)."""
        return self._signalMapping

    def with_frame_mapping(self, value):
        """
        Set frame_mapping and return self for chaining.

        Args:
            value: The frame_mapping to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_frame_mapping("value")
        """
        self.frame_mapping = value  # Use property setter (gets validation)
        return self

    def with_i_pdu_mapping(self, value):
        """
        Set i_pdu_mapping and return self for chaining.

        Args:
            value: The i_pdu_mapping to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_i_pdu_mapping("value")
        """
        self.i_pdu_mapping = value  # Use property setter (gets validation)
        return self

    def with_signal_mapping(self, value):
        """
        Set signal_mapping and return self for chaining.

        Args:
            value: The signal_mapping to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_signal_mapping("value")
        """
        self.signal_mapping = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEcu(self) -> "EcuInstance":
        """
        AUTOSAR-compliant getter for ecu.
        
        Returns:
            The ecu value
        
        Note:
            Delegates to ecu property (CODING_RULE_V2_00017)
        """
        return self.ecu  # Delegates to property

    def setEcu(self, value: "EcuInstance") -> "Gateway":
        """
        AUTOSAR-compliant setter for ecu with method chaining.
        
        Args:
            value: The ecu to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ecu property setter (gets validation automatically)
        """
        self.ecu = value  # Delegates to property setter
        return self

    def getFrameMapping(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for frameMapping.
        
        Returns:
            The frameMapping value
        
        Note:
            Delegates to frame_mapping property (CODING_RULE_V2_00017)
        """
        return self.frame_mapping  # Delegates to property

    def getIPduMapping(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for iPduMapping.
        
        Returns:
            The iPduMapping value
        
        Note:
            Delegates to i_pdu_mapping property (CODING_RULE_V2_00017)
        """
        return self.i_pdu_mapping  # Delegates to property

    def getSignalMapping(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for signalMapping.
        
        Returns:
            The signalMapping value
        
        Note:
            Delegates to signal_mapping property (CODING_RULE_V2_00017)
        """
        return self.signal_mapping  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ecu(self, value: Optional["EcuInstance"]) -> "Gateway":
        """
        Set ecu and return self for chaining.
        
        Args:
            value: The ecu to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ecu("value")
        """
        self.ecu = value  # Use property setter (gets validation)
        return self



class FrameMapping(ARObject):
    """
    The entire source frame is mapped as it is onto the target frame (what in
    general is only possible inside of a common platform). In this case source
    and target frame should be the identical object. Each pair consists in a
    SOURCE and a TARGET referencing to a FrameTriggering. The Frame Mapping is
    not supported by the Autosar BSW. The existence is optional and has been
    incorporated into the System Template mainly for compatibility in order to
    allow interchange between FIBEX and AUTOSAR descriptions.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Multiplatform::FrameMapping
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 838, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents introductory documentation about the.
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
        self._sourceFrame: Optional["RefType"] = None

    @property
    def source_frame(self) -> Optional["RefType"]:
        """Get sourceFrame (Pythonic accessor)."""
        return self._sourceFrame

    @source_frame.setter
    def source_frame(self, value: Optional["RefType"]) -> None:
        """
        Set sourceFrame with validation.
        
        Args:
            value: The sourceFrame to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sourceFrame = None
            return

        self._sourceFrame = value
        self._targetFrame: Optional["RefType"] = None

    @property
    def target_frame(self) -> Optional["RefType"]:
        """Get targetFrame (Pythonic accessor)."""
        return self._targetFrame

    @target_frame.setter
    def target_frame(self, value: Optional["RefType"]) -> None:
        """
        Set targetFrame with validation.
        
        Args:
            value: The targetFrame to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetFrame = None
            return

        self._targetFrame = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIntroduction(self) -> "DocumentationBlock":
        """
        AUTOSAR-compliant getter for introduction.
        
        Returns:
            The introduction value
        
        Note:
            Delegates to introduction property (CODING_RULE_V2_00017)
        """
        return self.introduction  # Delegates to property

    def setIntroduction(self, value: "DocumentationBlock") -> "FrameMapping":
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

    def getSourceFrame(self) -> "RefType":
        """
        AUTOSAR-compliant getter for sourceFrame.
        
        Returns:
            The sourceFrame value
        
        Note:
            Delegates to source_frame property (CODING_RULE_V2_00017)
        """
        return self.source_frame  # Delegates to property

    def setSourceFrame(self, value: "RefType") -> "FrameMapping":
        """
        AUTOSAR-compliant setter for sourceFrame with method chaining.
        
        Args:
            value: The sourceFrame to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to source_frame property setter (gets validation automatically)
        """
        self.source_frame = value  # Delegates to property setter
        return self

    def getTargetFrame(self) -> "RefType":
        """
        AUTOSAR-compliant getter for targetFrame.
        
        Returns:
            The targetFrame value
        
        Note:
            Delegates to target_frame property (CODING_RULE_V2_00017)
        """
        return self.target_frame  # Delegates to property

    def setTargetFrame(self, value: "RefType") -> "FrameMapping":
        """
        AUTOSAR-compliant setter for targetFrame with method chaining.
        
        Args:
            value: The targetFrame to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to target_frame property setter (gets validation automatically)
        """
        self.target_frame = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_introduction(self, value: Optional["DocumentationBlock"]) -> "FrameMapping":
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

    def with_source_frame(self, value: Optional[RefType]) -> "FrameMapping":
        """
        Set sourceFrame and return self for chaining.
        
        Args:
            value: The sourceFrame to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_source_frame("value")
        """
        self.source_frame = value  # Use property setter (gets validation)
        return self

    def with_target_frame(self, value: Optional[RefType]) -> "FrameMapping":
        """
        Set targetFrame and return self for chaining.
        
        Args:
            value: The targetFrame to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_target_frame("value")
        """
        self.target_frame = value  # Use property setter (gets validation)
        return self



class IPduMapping(ARObject):
    """
    Arranges those IPdus that are transferred by the gateway from one channel to
    the other in pairs and defines the mapping between them.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Multiplatform::IPduMapping
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 840, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents introductory documentation about the.
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
        # operation if the runtime the received Pdu exceeds this limit.
        self._pduMaxLength: Optional["PositiveInteger"] = None

    @property
    def pdu_max_length(self) -> Optional["PositiveInteger"]:
        """Get pduMaxLength (Pythonic accessor)."""
        return self._pduMaxLength

    @pdu_max_length.setter
    def pdu_max_length(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set pduMaxLength with validation.
        
        Args:
            value: The pduMaxLength to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pduMaxLength = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"pduMaxLength must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._pduMaxLength = value
        # relation.
        self._pdurTpChunk: Optional["PositiveInteger"] = None

    @property
    def pdur_tp_chunk(self) -> Optional["PositiveInteger"]:
        """Get pdurTpChunk (Pythonic accessor)."""
        return self._pdurTpChunk

    @pdur_tp_chunk.setter
    def pdur_tp_chunk(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set pdurTpChunk with validation.
        
        Args:
            value: The pdurTpChunk to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pdurTpChunk = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"pdurTpChunk must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._pdurTpChunk = value
        self._sourceIPdu: Optional["RefType"] = None

    @property
    def source_i_pdu(self) -> Optional["RefType"]:
        """Get sourceIPdu (Pythonic accessor)."""
        return self._sourceIPdu

    @source_i_pdu.setter
    def source_i_pdu(self, value: Optional["RefType"]) -> None:
        """
        Set sourceIPdu with validation.
        
        Args:
            value: The sourceIPdu to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sourceIPdu = None
            return

        self._sourceIPdu = value
        self._targetIPdu: Optional["RefType"] = None

    @property
    def target_i_pdu(self) -> Optional["RefType"]:
        """Get targetIPdu (Pythonic accessor)."""
        return self._targetIPdu

    @target_i_pdu.setter
    def target_i_pdu(self, value: Optional["RefType"]) -> None:
        """
        Set targetIPdu with validation.
        
        Args:
            value: The targetIPdu to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetIPdu = None
            return

        self._targetIPdu = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIntroduction(self) -> "DocumentationBlock":
        """
        AUTOSAR-compliant getter for introduction.
        
        Returns:
            The introduction value
        
        Note:
            Delegates to introduction property (CODING_RULE_V2_00017)
        """
        return self.introduction  # Delegates to property

    def setIntroduction(self, value: "DocumentationBlock") -> "IPduMapping":
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

    def getPduMaxLength(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for pduMaxLength.
        
        Returns:
            The pduMaxLength value
        
        Note:
            Delegates to pdu_max_length property (CODING_RULE_V2_00017)
        """
        return self.pdu_max_length  # Delegates to property

    def setPduMaxLength(self, value: "PositiveInteger") -> "IPduMapping":
        """
        AUTOSAR-compliant setter for pduMaxLength with method chaining.
        
        Args:
            value: The pduMaxLength to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to pdu_max_length property setter (gets validation automatically)
        """
        self.pdu_max_length = value  # Delegates to property setter
        return self

    def getPdurTpChunk(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for pdurTpChunk.
        
        Returns:
            The pdurTpChunk value
        
        Note:
            Delegates to pdur_tp_chunk property (CODING_RULE_V2_00017)
        """
        return self.pdur_tp_chunk  # Delegates to property

    def setPdurTpChunk(self, value: "PositiveInteger") -> "IPduMapping":
        """
        AUTOSAR-compliant setter for pdurTpChunk with method chaining.
        
        Args:
            value: The pdurTpChunk to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to pdur_tp_chunk property setter (gets validation automatically)
        """
        self.pdur_tp_chunk = value  # Delegates to property setter
        return self

    def getSourceIPdu(self) -> "RefType":
        """
        AUTOSAR-compliant getter for sourceIPdu.
        
        Returns:
            The sourceIPdu value
        
        Note:
            Delegates to source_i_pdu property (CODING_RULE_V2_00017)
        """
        return self.source_i_pdu  # Delegates to property

    def setSourceIPdu(self, value: "RefType") -> "IPduMapping":
        """
        AUTOSAR-compliant setter for sourceIPdu with method chaining.
        
        Args:
            value: The sourceIPdu to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to source_i_pdu property setter (gets validation automatically)
        """
        self.source_i_pdu = value  # Delegates to property setter
        return self

    def getTargetIPdu(self) -> "RefType":
        """
        AUTOSAR-compliant getter for targetIPdu.
        
        Returns:
            The targetIPdu value
        
        Note:
            Delegates to target_i_pdu property (CODING_RULE_V2_00017)
        """
        return self.target_i_pdu  # Delegates to property

    def setTargetIPdu(self, value: "RefType") -> "IPduMapping":
        """
        AUTOSAR-compliant setter for targetIPdu with method chaining.
        
        Args:
            value: The targetIPdu to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to target_i_pdu property setter (gets validation automatically)
        """
        self.target_i_pdu = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_introduction(self, value: Optional["DocumentationBlock"]) -> "IPduMapping":
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

    def with_pdu_max_length(self, value: Optional["PositiveInteger"]) -> "IPduMapping":
        """
        Set pduMaxLength and return self for chaining.
        
        Args:
            value: The pduMaxLength to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_pdu_max_length("value")
        """
        self.pdu_max_length = value  # Use property setter (gets validation)
        return self

    def with_pdur_tp_chunk(self, value: Optional["PositiveInteger"]) -> "IPduMapping":
        """
        Set pdurTpChunk and return self for chaining.
        
        Args:
            value: The pdurTpChunk to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_pdur_tp_chunk("value")
        """
        self.pdur_tp_chunk = value  # Use property setter (gets validation)
        return self

    def with_source_i_pdu(self, value: Optional[RefType]) -> "IPduMapping":
        """
        Set sourceIPdu and return self for chaining.
        
        Args:
            value: The sourceIPdu to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_source_i_pdu("value")
        """
        self.source_i_pdu = value  # Use property setter (gets validation)
        return self

    def with_target_i_pdu(self, value: Optional[RefType]) -> "IPduMapping":
        """
        Set targetIPdu and return self for chaining.
        
        Args:
            value: The targetIPdu to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_target_i_pdu("value")
        """
        self.target_i_pdu = value  # Use property setter (gets validation)
        return self



class TargetIPduRef(ARObject):
    """
    Target destination of the referencing mapping.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Multiplatform::TargetIPduRef
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 841, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # If no I-Pdu has been received a default value will be.
        self._defaultValue: Optional["RefType"] = None

    @property
    def default_value(self) -> Optional["RefType"]:
        """Get defaultValue (Pythonic accessor)."""
        return self._defaultValue

    @default_value.setter
    def default_value(self, value: Optional["RefType"]) -> None:
        """
        Set defaultValue with validation.
        
        Args:
            value: The defaultValue to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._defaultValue = None
            return

        self._defaultValue = value
        self._targetIPdu: Optional["RefType"] = None

    @property
    def target_i_pdu(self) -> Optional["RefType"]:
        """Get targetIPdu (Pythonic accessor)."""
        return self._targetIPdu

    @target_i_pdu.setter
    def target_i_pdu(self, value: Optional["RefType"]) -> None:
        """
        Set targetIPdu with validation.
        
        Args:
            value: The targetIPdu to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetIPdu = None
            return

        self._targetIPdu = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDefaultValue(self) -> "RefType":
        """
        AUTOSAR-compliant getter for defaultValue.
        
        Returns:
            The defaultValue value
        
        Note:
            Delegates to default_value property (CODING_RULE_V2_00017)
        """
        return self.default_value  # Delegates to property

    def setDefaultValue(self, value: "RefType") -> "TargetIPduRef":
        """
        AUTOSAR-compliant setter for defaultValue with method chaining.
        
        Args:
            value: The defaultValue to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to default_value property setter (gets validation automatically)
        """
        self.default_value = value  # Delegates to property setter
        return self

    def getTargetIPdu(self) -> "RefType":
        """
        AUTOSAR-compliant getter for targetIPdu.
        
        Returns:
            The targetIPdu value
        
        Note:
            Delegates to target_i_pdu property (CODING_RULE_V2_00017)
        """
        return self.target_i_pdu  # Delegates to property

    def setTargetIPdu(self, value: "RefType") -> "TargetIPduRef":
        """
        AUTOSAR-compliant setter for targetIPdu with method chaining.
        
        Args:
            value: The targetIPdu to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to target_i_pdu property setter (gets validation automatically)
        """
        self.target_i_pdu = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_default_value(self, value: Optional[RefType]) -> "TargetIPduRef":
        """
        Set defaultValue and return self for chaining.
        
        Args:
            value: The defaultValue to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_default_value("value")
        """
        self.default_value = value  # Use property setter (gets validation)
        return self

    def with_target_i_pdu(self, value: Optional[RefType]) -> "TargetIPduRef":
        """
        Set targetIPdu and return self for chaining.
        
        Args:
            value: The targetIPdu to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_target_i_pdu("value")
        """
        self.target_i_pdu = value  # Use property setter (gets validation)
        return self



class PduMappingDefaultValue(ARObject):
    """
    Default Value which will be distributed if no I-Pdu has been received since
    last sending.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Multiplatform::PduMappingDefaultValue
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 841, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The default value consists of a number of elements.
        # Each value element is represented by the element and in an array.
        self._defaultValue: List["DefaultValueElement"] = []

    @property
    def default_value(self) -> List["DefaultValueElement"]:
        """Get defaultValue (Pythonic accessor)."""
        return self._defaultValue

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDefaultValue(self) -> List["DefaultValueElement"]:
        """
        AUTOSAR-compliant getter for defaultValue.
        
        Returns:
            The defaultValue value
        
        Note:
            Delegates to default_value property (CODING_RULE_V2_00017)
        """
        return self.default_value  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DefaultValueElement(ARObject):
    """
    The default value consists of a number of elements. Each element is one byte
    long and the number of elements is specified by SduLength.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Multiplatform::DefaultValueElement
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 841, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The integer value of a freely defined data byte.
        self._elementByteValue: Optional["Integer"] = None

    @property
    def element_byte_value(self) -> Optional["Integer"]:
        """Get elementByteValue (Pythonic accessor)."""
        return self._elementByteValue

    @element_byte_value.setter
    def element_byte_value(self, value: Optional["Integer"]) -> None:
        """
        Set elementByteValue with validation.
        
        Args:
            value: The elementByteValue to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._elementByteValue = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"elementByteValue must be Integer or int or None, got {type(value).__name__}"
            )
        self._elementByteValue = value
        self._elementPosition: Optional["Integer"] = None

    @property
    def element_position(self) -> Optional["Integer"]:
        """Get elementPosition (Pythonic accessor)."""
        return self._elementPosition

    @element_position.setter
    def element_position(self, value: Optional["Integer"]) -> None:
        """
        Set elementPosition with validation.
        
        Args:
            value: The elementPosition to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._elementPosition = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"elementPosition must be Integer or int or None, got {type(value).__name__}"
            )
        self._elementPosition = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getElementByteValue(self) -> "Integer":
        """
        AUTOSAR-compliant getter for elementByteValue.
        
        Returns:
            The elementByteValue value
        
        Note:
            Delegates to element_byte_value property (CODING_RULE_V2_00017)
        """
        return self.element_byte_value  # Delegates to property

    def setElementByteValue(self, value: "Integer") -> "DefaultValueElement":
        """
        AUTOSAR-compliant setter for elementByteValue with method chaining.
        
        Args:
            value: The elementByteValue to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to element_byte_value property setter (gets validation automatically)
        """
        self.element_byte_value = value  # Delegates to property setter
        return self

    def getElementPosition(self) -> "Integer":
        """
        AUTOSAR-compliant getter for elementPosition.
        
        Returns:
            The elementPosition value
        
        Note:
            Delegates to element_position property (CODING_RULE_V2_00017)
        """
        return self.element_position  # Delegates to property

    def setElementPosition(self, value: "Integer") -> "DefaultValueElement":
        """
        AUTOSAR-compliant setter for elementPosition with method chaining.
        
        Args:
            value: The elementPosition to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to element_position property setter (gets validation automatically)
        """
        self.element_position = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_element_byte_value(self, value: Optional["Integer"]) -> "DefaultValueElement":
        """
        Set elementByteValue and return self for chaining.
        
        Args:
            value: The elementByteValue to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_element_byte_value("value")
        """
        self.element_byte_value = value  # Use property setter (gets validation)
        return self

    def with_element_position(self, value: Optional["Integer"]) -> "DefaultValueElement":
        """
        Set elementPosition and return self for chaining.
        
        Args:
            value: The elementPosition to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_element_position("value")
        """
        self.element_position = value  # Use property setter (gets validation)
        return self



class ISignalMapping(ARObject):
    """
    Arranges those signals (or SignalGroups) that are transferred by the gateway
    from one channel to the other in pairs and defines the mapping between them.
    Each pair consists in a source and a target referencing to a
    ISignalTriggering.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Multiplatform::ISignalMapping
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 846, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents introductory documentation about the.
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
        self._sourceSignal: Optional["RefType"] = None

    @property
    def source_signal(self) -> Optional["RefType"]:
        """Get sourceSignal (Pythonic accessor)."""
        return self._sourceSignal

    @source_signal.setter
    def source_signal(self, value: Optional["RefType"]) -> None:
        """
        Set sourceSignal with validation.
        
        Args:
            value: The sourceSignal to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sourceSignal = None
            return

        self._sourceSignal = value
        self._targetSignal: Optional["RefType"] = None

    @property
    def target_signal(self) -> Optional["RefType"]:
        """Get targetSignal (Pythonic accessor)."""
        return self._targetSignal

    @target_signal.setter
    def target_signal(self, value: Optional["RefType"]) -> None:
        """
        Set targetSignal with validation.
        
        Args:
            value: The targetSignal to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetSignal = None
            return

        self._targetSignal = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIntroduction(self) -> "DocumentationBlock":
        """
        AUTOSAR-compliant getter for introduction.
        
        Returns:
            The introduction value
        
        Note:
            Delegates to introduction property (CODING_RULE_V2_00017)
        """
        return self.introduction  # Delegates to property

    def setIntroduction(self, value: "DocumentationBlock") -> "ISignalMapping":
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

    def getSourceSignal(self) -> "RefType":
        """
        AUTOSAR-compliant getter for sourceSignal.
        
        Returns:
            The sourceSignal value
        
        Note:
            Delegates to source_signal property (CODING_RULE_V2_00017)
        """
        return self.source_signal  # Delegates to property

    def setSourceSignal(self, value: "RefType") -> "ISignalMapping":
        """
        AUTOSAR-compliant setter for sourceSignal with method chaining.
        
        Args:
            value: The sourceSignal to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to source_signal property setter (gets validation automatically)
        """
        self.source_signal = value  # Delegates to property setter
        return self

    def getTargetSignal(self) -> "RefType":
        """
        AUTOSAR-compliant getter for targetSignal.
        
        Returns:
            The targetSignal value
        
        Note:
            Delegates to target_signal property (CODING_RULE_V2_00017)
        """
        return self.target_signal  # Delegates to property

    def setTargetSignal(self, value: "RefType") -> "ISignalMapping":
        """
        AUTOSAR-compliant setter for targetSignal with method chaining.
        
        Args:
            value: The targetSignal to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to target_signal property setter (gets validation automatically)
        """
        self.target_signal = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_introduction(self, value: Optional["DocumentationBlock"]) -> "ISignalMapping":
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

    def with_source_signal(self, value: Optional[RefType]) -> "ISignalMapping":
        """
        Set sourceSignal and return self for chaining.
        
        Args:
            value: The sourceSignal to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_source_signal("value")
        """
        self.source_signal = value  # Use property setter (gets validation)
        return self

    def with_target_signal(self, value: Optional[RefType]) -> "ISignalMapping":
        """
        Set targetSignal and return self for chaining.
        
        Args:
            value: The targetSignal to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_target_signal("value")
        """
        self.target_signal = value  # Use property setter (gets validation)
        return self
