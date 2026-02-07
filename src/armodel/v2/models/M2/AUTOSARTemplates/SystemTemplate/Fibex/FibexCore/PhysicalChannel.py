from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class PhysicalChannel(Identifiable, ABC):
    """
    A physical channel is the transmission medium that is used to send and
    receive information between communicating ECUs. Each CommunicationCluster
    has at least one physical channel. Bus systems like CAN and LIN only have
    exactly one PhysicalChannel. A FlexRay cluster may have more than one
    PhysicalChannels that may be used in parallel for redundant communication.
    An ECU is part of a cluster if it contains at least one controller that is
    connected to at least one channel of the cluster.#
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology::PhysicalChannel
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 325, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 58, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 235, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is PhysicalChannel:
            raise TypeError("PhysicalChannel is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the ECUInstance via a Communication Connector to which the
                # channel is connected.
        # assignment of Physical Channels to is expressed with atpVariation.
        self._comm: List["Communication"] = []

    @property
    def comm(self) -> List["Communication"]:
        """Get comm (Pythonic accessor)."""
        return self._comm
        # One frame triggering is defined for exactly one channel.
        # have assigned an arbitrary number of signals/PDUs/frames are variable, the
                # shall be variable, too.
        # atpVariation.
        self._frameTriggering: List[RefType] = []

    @property
    def frame_triggering(self) -> List[RefType]:
        """Get frameTriggering (Pythonic accessor)."""
        return self._frameTriggering
        # One ISignalTriggering is defined for exactly one channel.
        # may have assigned an arbitrary number of signals/PDUs/frames are variable,
                # the shall be variable, too.
        # atpVariation 719 Document ID 673: AUTOSAR_CP_TPS_DiagnosticExtractTemplate
                # Template R23-11.
        self._iSignal: List[RefType] = []

    @property
    def i_signal(self) -> List[RefType]:
        """Get iSignal (Pythonic accessor)."""
        return self._iSignal
        # Reference between a channel with role managing and a channel with role
        # managed channel.
        self._managed: List["PhysicalChannel"] = []

    @property
    def managed(self) -> List["PhysicalChannel"]:
        """Get managed (Pythonic accessor)."""
        return self._managed
        # One PduTriggering is defined for exactly one channel.
        # have assigned an arbitrary number of signals/PDUs/frames are variable, the
                # shall be variable, too.
        # atpVariation.
        self._pduTriggering: List[RefType] = []

    @property
    def pdu_triggering(self) -> List[RefType]:
        """Get pduTriggering (Pythonic accessor)."""
        return self._pduTriggering

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getComm(self) -> List["Communication"]:
        """
        AUTOSAR-compliant getter for comm.
        
        Returns:
            The comm value
        
        Note:
            Delegates to comm property (CODING_RULE_V2_00017)
        """
        return self.comm  # Delegates to property

    def getFrameTriggering(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for frameTriggering.
        
        Returns:
            The frameTriggering value
        
        Note:
            Delegates to frame_triggering property (CODING_RULE_V2_00017)
        """
        return self.frame_triggering  # Delegates to property

    def getISignal(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for iSignal.
        
        Returns:
            The iSignal value
        
        Note:
            Delegates to i_signal property (CODING_RULE_V2_00017)
        """
        return self.i_signal  # Delegates to property

    def getManaged(self) -> List["PhysicalChannel"]:
        """
        AUTOSAR-compliant getter for managed.
        
        Returns:
            The managed value
        
        Note:
            Delegates to managed property (CODING_RULE_V2_00017)
        """
        return self.managed  # Delegates to property

    def getPduTriggering(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for pduTriggering.
        
        Returns:
            The pduTriggering value
        
        Note:
            Delegates to pdu_triggering property (CODING_RULE_V2_00017)
        """
        return self.pdu_triggering  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====