from typing import List


class EthernetWakeupSleepOnDatalineConfigSet(FibexElement):
    """
    This meta-class is the main element that aggregates different config set
    regarding the ethernet wakeup and sleep on data line.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::EthernetWakeupSleepOnDatalineConfigSet

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 159, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The relationship defines a collection of EthernetWakeup SleepOnDatalineConfig
        # configurations which are.
        self._ethernet: List["EthernetWakeupSleep"] = []

    @property
    def ethernet(self) -> List["EthernetWakeupSleep"]:
        """Get ethernet (Pythonic accessor)."""
        return self._ethernet

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEthernet(self) -> List["EthernetWakeupSleep"]:
        """
        AUTOSAR-compliant getter for ethernet.

        Returns:
            The ethernet value

        Note:
            Delegates to ethernet property (CODING_RULE_V2_00017)
        """
        return self.ethernet  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
