from typing import List


class SecurityEventStateFilter(AbstractSecurityEventFilter):
    """
    This meta-class represents the configuration of a state filter for security
    events. The referenced states represent a block list, i.e. the security
    events are dropped if the referenced state is the active state in the
    relevant state machine (which depends on whether the IdsM instance runs on
    the Classic or the Adaptive Platform).

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::SecurityEventStateFilter

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 22, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # For the CP, this reference defines the states of the block That means, if a
        # security event (mapped to the filter which the SecurityEventStateFilter
        # belongs to) is the currently active block state in the IdsM of the referenced
        # block listed states, the IdsM shall reported security event.
        self._blockIfState: List["BlockState"] = []

    @property
    def block_if_state(self) -> List["BlockState"]:
        """Get blockIfState (Pythonic accessor)."""
        return self._blockIfState

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBlockIfState(self) -> List["BlockState"]:
        """
        AUTOSAR-compliant getter for blockIfState.

        Returns:
            The blockIfState value

        Note:
            Delegates to block_if_state property (CODING_RULE_V2_00017)
        """
        return self.block_if_state  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
