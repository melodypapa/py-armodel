"""
AUTOSAR Package - PncMapping

Package: M2::AUTOSARTemplates::SystemTemplate::PncMapping
"""


from __future__ import annotations

from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Describable,
    Referrable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Identifier,
    PositiveInteger,
    RefType,
)


class PncMapping(Describable):
    """
    Describes a mapping between one or several Virtual Function Clusters onto
    Partial Network Clusters. A Virtual Function Cluster is realized by a
    PortGroup. A Partial Network Cluster is realized by one or more IPduGroups.

    Package: M2::AUTOSARTemplates::SystemTemplate::PncMapping::PncMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 264, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to an ISignalIPduGroup that allows mapping of PNC without
        # statically mapping this PNC directly to a This is needed to describe dynamic
        # PNCs that learned only at run-time and which have also a an ISignalIPduGroup.
        self._dynamicPnc: List[RefType] = []

    @property
    def dynamic_pnc(self) -> List[RefType]:
        """Get dynamicPnc (Pythonic accessor)."""
        return self._dynamicPnc
        # This adds the ability to become referrable to PncMapping.
        self._ident: Optional[RefType] = None

    @property
    def ident(self) -> Optional[RefType]:
        """Get ident (Pythonic accessor)."""
        return self._ident

    @ident.setter
    def ident(self, value: Optional[RefType]) -> None:
        """
        Set ident with validation.

        Args:
            value: The ident to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ident = None
            return

        self._ident = value
        self._physical: List[PhysicalChannel] = []

    @property
    def physical(self) -> List[PhysicalChannel]:
        """Get physical (Pythonic accessor)."""
        return self._physical
        # ConsumedProvidedServiceInstanceGroup used in a Partial Network Cluster.
        # This reference is optional, since could be used for starting and stopping
                # Consumed according the requested but is not necessarily needed.
        # atpVariation.
        self._pncConsumed: List["ConsumedProvided"] = []

    @property
    def pnc_consumed(self) -> List["ConsumedProvided"]:
        """Get pncConsumed (Pythonic accessor)."""
        return self._pncConsumed
        # IPduGroup participating in a Partial Network Cluster.
        # This optional in case an ecu extract has only access, i.
        # e.
        # ecu is not directly connected to a supports partial network.
        self._pncGroup: List[RefType] = []

    @property
    def pnc_group(self) -> List[RefType]:
        """Get pncGroup (Pythonic accessor)."""
        return self._pncGroup
        # Identifer of the Partial Network Cluster.
        # This number absolute bit position of this Partial Network the NM Pdu.
        self._pncIdentifier: Optional[PositiveInteger] = None

    @property
    def pnc_identifier(self) -> Optional[PositiveInteger]:
        """Get pncIdentifier (Pythonic accessor)."""
        return self._pncIdentifier

    @pnc_identifier.setter
    def pnc_identifier(self, value: Optional[PositiveInteger]) -> None:
        """
        Set pncIdentifier with validation.

        Args:
            value: The pncIdentifier to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pncIdentifier = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"pncIdentifier must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._pncIdentifier = value
        self._pncPdurGroup: List[RefType] = []

    @property
    def pnc_pdur_group(self) -> List[RefType]:
        """Get pncPdurGroup (Pythonic accessor)."""
        return self._pncPdurGroup
        # If this parameter is available and set to true then this PNC be woken up as
                # soon as a channel wakeup occurs on where this PNC is assigned to.
        # This is ensured this PNC to the corresponding channel wakeup upstream
                # mapping.
        self._pncWakeup: Optional[Boolean] = None

    @property
    def pnc_wakeup(self) -> Optional[Boolean]:
        """Get pncWakeup (Pythonic accessor)."""
        return self._pncWakeup

    @pnc_wakeup.setter
    def pnc_wakeup(self, value: Optional[Boolean]) -> None:
        """
        Set pncWakeup with validation.

        Args:
            value: The pncWakeup to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pncWakeup = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"pncWakeup must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._pncWakeup = value
                # mapping.
        # This is needed to dynamic PNCs that can be learned only at which have no
                # relation to an ISignalIPdu.
        self._relevantFor: List[EcuInstance] = []

    @property
    def relevant_for(self) -> List[EcuInstance]:
        """Get relevantFor (Pythonic accessor)."""
        return self._relevantFor
        # This attribute specifies an identifying shortName for the shall be unique in
                # the System scope.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._shortLabel: Optional["Identifier"] = None

    @property
    def short_label(self) -> Optional["Identifier"]:
        """Get shortLabel (Pythonic accessor)."""
        return self._shortLabel

    @short_label.setter
    def short_label(self, value: Optional["Identifier"]) -> None:
        """
        Set shortLabel with validation.

        Args:
            value: The shortLabel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._shortLabel = None
            return

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"shortLabel must be Identifier or str or None, got {type(value).__name__}"
            )
        self._shortLabel = value
                # Software (VFB View).
        # This supports the legacy systems.
        # by: PortGroupInSystem.
        self._vfc: List[RefType] = []

    @property
    def vfc(self) -> List[RefType]:
        """Get vfc (Pythonic accessor)."""
        return self._vfc
        # Reference to collection of FrameTriggerings that are used wakeup of this PNC
                # (Application Frames or Nm be used).
        # This reference is only valid if this an ECU which has direct PNC ECU is
                # directly connected to a network which network.
        self._wakeupFrame: List[RefType] = []

    @property
    def wakeup_frame(self) -> List[RefType]:
        """Get wakeupFrame (Pythonic accessor)."""
        return self._wakeupFrame

    def with_dynamic_pnc(self, value):
        """
        Set dynamic_pnc and return self for chaining.

        Args:
            value: The dynamic_pnc to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dynamic_pnc("value")
        """
        self.dynamic_pnc = value  # Use property setter (gets validation)
        return self

    def with_physical(self, value):
        """
        Set physical and return self for chaining.

        Args:
            value: The physical to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_physical("value")
        """
        self.physical = value  # Use property setter (gets validation)
        return self

    def with_pnc_consumed(self, value):
        """
        Set pnc_consumed and return self for chaining.

        Args:
            value: The pnc_consumed to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pnc_consumed("value")
        """
        self.pnc_consumed = value  # Use property setter (gets validation)
        return self

    def with_pnc_group(self, value):
        """
        Set pnc_group and return self for chaining.

        Args:
            value: The pnc_group to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pnc_group("value")
        """
        self.pnc_group = value  # Use property setter (gets validation)
        return self

    def with_pnc_pdur_group(self, value):
        """
        Set pnc_pdur_group and return self for chaining.

        Args:
            value: The pnc_pdur_group to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pnc_pdur_group("value")
        """
        self.pnc_pdur_group = value  # Use property setter (gets validation)
        return self

    def with_relevant_for(self, value):
        """
        Set relevant_for and return self for chaining.

        Args:
            value: The relevant_for to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_relevant_for("value")
        """
        self.relevant_for = value  # Use property setter (gets validation)
        return self

    def with_vfc(self, value):
        """
        Set vfc and return self for chaining.

        Args:
            value: The vfc to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vfc("value")
        """
        self.vfc = value  # Use property setter (gets validation)
        return self

    def with_wakeup_frame(self, value):
        """
        Set wakeup_frame and return self for chaining.

        Args:
            value: The wakeup_frame to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_wakeup_frame("value")
        """
        self.wakeup_frame = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDynamicPnc(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for dynamicPnc.

        Returns:
            The dynamicPnc value

        Note:
            Delegates to dynamic_pnc property (CODING_RULE_V2_00017)
        """
        return self.dynamic_pnc  # Delegates to property

    def getIdent(self) -> RefType:
        """
        AUTOSAR-compliant getter for ident.

        Returns:
            The ident value

        Note:
            Delegates to ident property (CODING_RULE_V2_00017)
        """
        return self.ident  # Delegates to property

    def setIdent(self, value: RefType) -> PncMapping:
        """
        AUTOSAR-compliant setter for ident with method chaining.

        Args:
            value: The ident to set

        Returns:
            self for method chaining

        Note:
            Delegates to ident property setter (gets validation automatically)
        """
        self.ident = value  # Delegates to property setter
        return self

    def getPhysical(self) -> List[PhysicalChannel]:
        """
        AUTOSAR-compliant getter for physical.

        Returns:
            The physical value

        Note:
            Delegates to physical property (CODING_RULE_V2_00017)
        """
        return self.physical  # Delegates to property

    def getPncConsumed(self) -> List["ConsumedProvided"]:
        """
        AUTOSAR-compliant getter for pncConsumed.

        Returns:
            The pncConsumed value

        Note:
            Delegates to pnc_consumed property (CODING_RULE_V2_00017)
        """
        return self.pnc_consumed  # Delegates to property

    def getPncGroup(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for pncGroup.

        Returns:
            The pncGroup value

        Note:
            Delegates to pnc_group property (CODING_RULE_V2_00017)
        """
        return self.pnc_group  # Delegates to property

    def getPncIdentifier(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for pncIdentifier.

        Returns:
            The pncIdentifier value

        Note:
            Delegates to pnc_identifier property (CODING_RULE_V2_00017)
        """
        return self.pnc_identifier  # Delegates to property

    def setPncIdentifier(self, value: PositiveInteger) -> PncMapping:
        """
        AUTOSAR-compliant setter for pncIdentifier with method chaining.

        Args:
            value: The pncIdentifier to set

        Returns:
            self for method chaining

        Note:
            Delegates to pnc_identifier property setter (gets validation automatically)
        """
        self.pnc_identifier = value  # Delegates to property setter
        return self

    def getPncPdurGroup(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for pncPdurGroup.

        Returns:
            The pncPdurGroup value

        Note:
            Delegates to pnc_pdur_group property (CODING_RULE_V2_00017)
        """
        return self.pnc_pdur_group  # Delegates to property

    def getPncWakeup(self) -> Boolean:
        """
        AUTOSAR-compliant getter for pncWakeup.

        Returns:
            The pncWakeup value

        Note:
            Delegates to pnc_wakeup property (CODING_RULE_V2_00017)
        """
        return self.pnc_wakeup  # Delegates to property

    def setPncWakeup(self, value: Boolean) -> PncMapping:
        """
        AUTOSAR-compliant setter for pncWakeup with method chaining.

        Args:
            value: The pncWakeup to set

        Returns:
            self for method chaining

        Note:
            Delegates to pnc_wakeup property setter (gets validation automatically)
        """
        self.pnc_wakeup = value  # Delegates to property setter
        return self

    def getRelevantFor(self) -> List[EcuInstance]:
        """
        AUTOSAR-compliant getter for relevantFor.

        Returns:
            The relevantFor value

        Note:
            Delegates to relevant_for property (CODING_RULE_V2_00017)
        """
        return self.relevant_for  # Delegates to property

    def getShortLabel(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for shortLabel.

        Returns:
            The shortLabel value

        Note:
            Delegates to short_label property (CODING_RULE_V2_00017)
        """
        return self.short_label  # Delegates to property

    def setShortLabel(self, value: "Identifier") -> PncMapping:
        """
        AUTOSAR-compliant setter for shortLabel with method chaining.

        Args:
            value: The shortLabel to set

        Returns:
            self for method chaining

        Note:
            Delegates to short_label property setter (gets validation automatically)
        """
        self.short_label = value  # Delegates to property setter
        return self

    def getVfc(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for vfc.

        Returns:
            The vfc value

        Note:
            Delegates to vfc property (CODING_RULE_V2_00017)
        """
        return self.vfc  # Delegates to property

    def getWakeupFrame(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for wakeupFrame.

        Returns:
            The wakeupFrame value

        Note:
            Delegates to wakeup_frame property (CODING_RULE_V2_00017)
        """
        return self.wakeup_frame  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ident(self, value: Optional[RefType]) -> PncMapping:
        """
        Set ident and return self for chaining.

        Args:
            value: The ident to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ident("value")
        """
        self.ident = value  # Use property setter (gets validation)
        return self

    def with_pnc_identifier(self, value: Optional[PositiveInteger]) -> PncMapping:
        """
        Set pncIdentifier and return self for chaining.

        Args:
            value: The pncIdentifier to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pnc_identifier("value")
        """
        self.pnc_identifier = value  # Use property setter (gets validation)
        return self

    def with_pnc_wakeup(self, value: Optional[Boolean]) -> PncMapping:
        """
        Set pncWakeup and return self for chaining.

        Args:
            value: The pncWakeup to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pnc_wakeup("value")
        """
        self.pnc_wakeup = value  # Use property setter (gets validation)
        return self

    def with_short_label(self, value: Optional["Identifier"]) -> PncMapping:
        """
        Set shortLabel and return self for chaining.

        Args:
            value: The shortLabel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_short_label("value")
        """
        self.short_label = value  # Use property setter (gets validation)
        return self



class PncMappingIdent(Referrable):
    """
    This meta-class is created to add the ability to become the target of a
    reference to the non-Referrable PncMapping.

    Package: M2::AUTOSARTemplates::SystemTemplate::PncMapping::PncMappingIdent

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2044, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
