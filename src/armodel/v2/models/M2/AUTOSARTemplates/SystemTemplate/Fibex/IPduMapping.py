from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


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
        # Define the maximum length in bytes which limits the the Pdu during gateway
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"pduMaxLength must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._pduMaxLength = value
        # Optionally defines the to be configured Pdu Router Tp for this routing
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"pdurTpChunk must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._pdurTpChunk = value
        # Source destination of the referencing mapping.
        self._sourceIPdu: RefType = None

    @property
    def source_i_pdu(self) -> RefType:
        """Get sourceIPdu (Pythonic accessor)."""
        return self._sourceIPdu

    @source_i_pdu.setter
    def source_i_pdu(self, value: RefType) -> None:
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
        # Target destination of the referencing mapping.
        self._targetIPdu: RefType = None

    @property
    def target_i_pdu(self) -> RefType:
        """Get targetIPdu (Pythonic accessor)."""
        return self._targetIPdu

    @target_i_pdu.setter
    def target_i_pdu(self, value: RefType) -> None:
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

    def getSourceIPdu(self) -> RefType:
        """
        AUTOSAR-compliant getter for sourceIPdu.

        Returns:
            The sourceIPdu value

        Note:
            Delegates to source_i_pdu property (CODING_RULE_V2_00017)
        """
        return self.source_i_pdu  # Delegates to property

    def setSourceIPdu(self, value: RefType) -> "IPduMapping":
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

    def getTargetIPdu(self) -> RefType:
        """
        AUTOSAR-compliant getter for targetIPdu.

        Returns:
            The targetIPdu value

        Note:
            Delegates to target_i_pdu property (CODING_RULE_V2_00017)
        """
        return self.target_i_pdu  # Delegates to property

    def setTargetIPdu(self, value: RefType) -> "IPduMapping":
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
