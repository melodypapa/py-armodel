from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class LinErrorResponse(ARObject):
    """
    Each slave node shall publish a one bit signal, named response_error, to the
    master node in one of its transmitted unconditional frames. The
    response_error signal shall be set whenever a frame (except for event
    triggered frame responses) that is transmitted or received by the slave node
    contains an error in the frame response. The response_error signal shall be
    cleared when the unconditional frame containing the response_error signal is
    successfully transmitted.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 97, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This ISignal shall be taken to transport the responseError.
        self._responseError: RefType = None

    @property
    def response_error(self) -> RefType:
        """Get responseError (Pythonic accessor)."""
        return self._responseError

    @response_error.setter
    def response_error(self, value: RefType) -> None:
        """
        Set responseError with validation.

        Args:
            value: The responseError to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._responseError = None
            return

        self._responseError = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getResponseError(self) -> RefType:
        """
        AUTOSAR-compliant getter for responseError.

        Returns:
            The responseError value

        Note:
            Delegates to response_error property (CODING_RULE_V2_00017)
        """
        return self.response_error  # Delegates to property

    def setResponseError(self, value: RefType) -> "LinErrorResponse":
        """
        AUTOSAR-compliant setter for responseError with method chaining.

        Args:
            value: The responseError to set

        Returns:
            self for method chaining

        Note:
            Delegates to response_error property setter (gets validation automatically)
        """
        self.response_error = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_response_error(self, value: Optional[RefType]) -> "LinErrorResponse":
        """
        Set responseError and return self for chaining.

        Args:
            value: The responseError to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_response_error("value")
        """
        self.response_error = value  # Use property setter (gets validation)
        return self

from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    Frame,
)


class LinFrame(Frame, ABC):
    """
    Lin specific Frame element.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 428, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is LinFrame:
            raise TypeError("LinFrame is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    FrameTriggering,
)


class LinFrameTriggering(FrameTriggering):
    """
    LIN specific attributes to the FrameTriggering

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 428, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # To describe a frames identifier on the communication with a fixed
                # identifierValue.
        # For Lin attribute shall be ignored.
        self._identifier: Optional["Integer"] = None

    @property
    def identifier(self) -> Optional["Integer"]:
        """Get identifier (Pythonic accessor)."""
        return self._identifier

    @identifier.setter
    def identifier(self, value: Optional["Integer"]) -> None:
        """
        Set identifier with validation.

        Args:
            value: The identifier to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._identifier = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"identifier must be Integer or None, got {type(value).__name__}"
            )
        self._identifier = value
        # Type of checksum that the frame is using.
        # This attribute is in case of sporadic frames it should not.
        self._linChecksum: Optional["LinChecksumType"] = None

    @property
    def lin_checksum(self) -> Optional["LinChecksumType"]:
        """Get linChecksum (Pythonic accessor)."""
        return self._linChecksum

    @lin_checksum.setter
    def lin_checksum(self, value: Optional["LinChecksumType"]) -> None:
        """
        Set linChecksum with validation.

        Args:
            value: The linChecksum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._linChecksum = None
            return

        if not isinstance(value, LinChecksumType):
            raise TypeError(
                f"linChecksum must be LinChecksumType or None, got {type(value).__name__}"
            )
        self._linChecksum = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIdentifier(self) -> "Integer":
        """
        AUTOSAR-compliant getter for identifier.

        Returns:
            The identifier value

        Note:
            Delegates to identifier property (CODING_RULE_V2_00017)
        """
        return self.identifier  # Delegates to property

    def setIdentifier(self, value: "Integer") -> "LinFrameTriggering":
        """
        AUTOSAR-compliant setter for identifier with method chaining.

        Args:
            value: The identifier to set

        Returns:
            self for method chaining

        Note:
            Delegates to identifier property setter (gets validation automatically)
        """
        self.identifier = value  # Delegates to property setter
        return self

    def getLinChecksum(self) -> "LinChecksumType":
        """
        AUTOSAR-compliant getter for linChecksum.

        Returns:
            The linChecksum value

        Note:
            Delegates to lin_checksum property (CODING_RULE_V2_00017)
        """
        return self.lin_checksum  # Delegates to property

    def setLinChecksum(self, value: "LinChecksumType") -> "LinFrameTriggering":
        """
        AUTOSAR-compliant setter for linChecksum with method chaining.

        Args:
            value: The linChecksum to set

        Returns:
            self for method chaining

        Note:
            Delegates to lin_checksum property setter (gets validation automatically)
        """
        self.lin_checksum = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_identifier(self, value: Optional["Integer"]) -> "LinFrameTriggering":
        """
        Set identifier and return self for chaining.

        Args:
            value: The identifier to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_identifier("value")
        """
        self.identifier = value  # Use property setter (gets validation)
        return self

    def with_lin_checksum(self, value: Optional["LinChecksumType"]) -> "LinFrameTriggering":
        """
        Set linChecksum and return self for chaining.

        Args:
            value: The linChecksum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_lin_checksum("value")
        """
        self.lin_checksum = value  # Use property setter (gets validation)
        return self

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import (
    LinFrame,
)


class LinUnconditionalFrame(LinFrame):
    """
    Unconditional frames carry signals. The master sends a frame header in a
    scheduled frame slot and the designated slave node fills the frame with
    data.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 429, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import (
    LinFrame,
)


class LinSporadicFrame(LinFrame):
    """
    A sporadic frame is a group of unconditional frames that share the same
    frame slot. The sporadic frame shall not contain any Pdus.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 429, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a group of unconditional frames that share the same frame slot.
        # In case that more than one of the needs to be transferred, the one first be
                # chosen.
        # channel a LIN Frame shall be referenced by only This allows a derivation of
                # the a substituted Frame.
        # The identifier is specified element.
        # associated with a LinSporadic not be allocated in the same LinSchedule.
        self._substituted: List["LinUnconditionalFrame"] = []

    @property
    def substituted(self) -> List["LinUnconditionalFrame"]:
        """Get substituted (Pythonic accessor)."""
        return self._substituted

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSubstituted(self) -> List["LinUnconditionalFrame"]:
        """
        AUTOSAR-compliant getter for substituted.

        Returns:
            The substituted value

        Note:
            Delegates to substituted property (CODING_RULE_V2_00017)
        """
        return self.substituted  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import (
    LinFrame,
)


class LinEventTriggeredFrame(LinFrame):
    """
    An event triggered frame is used as a placeholder to allow multiple slave
    nodes to provide its response. The header of an event triggered frame is
    transmitted when a frame slot allocated to the event triggered frame is
    processed. The publisher of an associated unconditional frame shall only
    transmit the response if at least one of the signals carried in its
    unconditional frame is updated. The LIN Master discovers and purges
    collisions with the collisionResolvingScheduleTable. The event controlled
    frame shall not contain any Pdus.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 430, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the schedule table, which resolves a.
        self._collisionSchedule: Optional["LinScheduleTable"] = None

    @property
    def collision_schedule(self) -> Optional["LinScheduleTable"]:
        """Get collisionSchedule (Pythonic accessor)."""
        return self._collisionSchedule

    @collision_schedule.setter
    def collision_schedule(self, value: Optional["LinScheduleTable"]) -> None:
        """
        Set collisionSchedule with validation.

        Args:
            value: The collisionSchedule to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._collisionSchedule = None
            return

        if not isinstance(value, LinScheduleTable):
            raise TypeError(
                f"collisionSchedule must be LinScheduleTable or None, got {type(value).__name__}"
            )
        self._collisionSchedule = value
        # A list of slaves can respond to the master request if at one of the signals
                # carried in its unconditional frame For each response a LinFrameTriggering and
                # shall be defined.
        # Within a LIN Frame shall be referenced by only one allows a derivation of the
                # identifier substituted Frame.
        # The identifier is specified in The Unconditional frames an event triggered
                # frame shall: equal length.
        # the same checksum model (i.
        # e.
        # mixing LIN 1.
        # x and frames is not allowed).
        # the first data field to its protected identifier the associated unconditional
                # frame is a unconditional frame in the same or table).
        # published by different slave nodes.
        # not be included directly in the same schedule the event triggered frame is
                # scheduled.
        self._linUnconditional: List["LinUnconditionalFrame"] = []

    @property
    def lin_unconditional(self) -> List["LinUnconditionalFrame"]:
        """Get linUnconditional (Pythonic accessor)."""
        return self._linUnconditional

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCollisionSchedule(self) -> "LinScheduleTable":
        """
        AUTOSAR-compliant getter for collisionSchedule.

        Returns:
            The collisionSchedule value

        Note:
            Delegates to collision_schedule property (CODING_RULE_V2_00017)
        """
        return self.collision_schedule  # Delegates to property

    def setCollisionSchedule(self, value: "LinScheduleTable") -> "LinEventTriggeredFrame":
        """
        AUTOSAR-compliant setter for collisionSchedule with method chaining.

        Args:
            value: The collisionSchedule to set

        Returns:
            self for method chaining

        Note:
            Delegates to collision_schedule property setter (gets validation automatically)
        """
        self.collision_schedule = value  # Delegates to property setter
        return self

    def getLinUnconditional(self) -> List["LinUnconditionalFrame"]:
        """
        AUTOSAR-compliant getter for linUnconditional.

        Returns:
            The linUnconditional value

        Note:
            Delegates to lin_unconditional property (CODING_RULE_V2_00017)
        """
        return self.lin_unconditional  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_collision_schedule(self, value: Optional["LinScheduleTable"]) -> "LinEventTriggeredFrame":
        """
        Set collisionSchedule and return self for chaining.

        Args:
            value: The collisionSchedule to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_collision_schedule("value")
        """
        self.collision_schedule = value  # Use property setter (gets validation)
        return self

from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class LinScheduleTable(Identifiable):
    """
    The master task (in the master node) transmits frame headers based on a
    schedule table. The schedule table specifies the identifiers for each header
    and the interval between the start of a frame and the start of the following
    frame.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 432, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines, where a schedule table shall be proceeded in it has been interrupted
        # by a run-once table or.
        self._resumePosition: Optional["ResumePosition"] = None

    @property
    def resume_position(self) -> Optional["ResumePosition"]:
        """Get resumePosition (Pythonic accessor)."""
        return self._resumePosition

    @resume_position.setter
    def resume_position(self, value: Optional["ResumePosition"]) -> None:
        """
        Set resumePosition with validation.

        Args:
            value: The resumePosition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._resumePosition = None
            return

        if not isinstance(value, ResumePosition):
            raise TypeError(
                f"resumePosition must be ResumePosition or None, got {type(value).__name__}"
            )
        self._resumePosition = value
        # The schedule table can be executed in two different.
        self._runMode: Optional["RunMode"] = None

    @property
    def run_mode(self) -> Optional["RunMode"]:
        """Get runMode (Pythonic accessor)."""
        return self._runMode

    @run_mode.setter
    def run_mode(self, value: Optional["RunMode"]) -> None:
        """
        Set runMode with validation.

        Args:
            value: The runMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._runMode = None
            return

        if not isinstance(value, RunMode):
            raise TypeError(
                f"runMode must be RunMode or None, got {type(value).__name__}"
            )
        self._runMode = value
        # The scheduling table consists of table entries, which slots.
        self._tableEntry: List["ScheduleTableEntry"] = []

    @property
    def table_entry(self) -> List["ScheduleTableEntry"]:
        """Get tableEntry (Pythonic accessor)."""
        return self._tableEntry

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getResumePosition(self) -> "ResumePosition":
        """
        AUTOSAR-compliant getter for resumePosition.

        Returns:
            The resumePosition value

        Note:
            Delegates to resume_position property (CODING_RULE_V2_00017)
        """
        return self.resume_position  # Delegates to property

    def setResumePosition(self, value: "ResumePosition") -> "LinScheduleTable":
        """
        AUTOSAR-compliant setter for resumePosition with method chaining.

        Args:
            value: The resumePosition to set

        Returns:
            self for method chaining

        Note:
            Delegates to resume_position property setter (gets validation automatically)
        """
        self.resume_position = value  # Delegates to property setter
        return self

    def getRunMode(self) -> "RunMode":
        """
        AUTOSAR-compliant getter for runMode.

        Returns:
            The runMode value

        Note:
            Delegates to run_mode property (CODING_RULE_V2_00017)
        """
        return self.run_mode  # Delegates to property

    def setRunMode(self, value: "RunMode") -> "LinScheduleTable":
        """
        AUTOSAR-compliant setter for runMode with method chaining.

        Args:
            value: The runMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to run_mode property setter (gets validation automatically)
        """
        self.run_mode = value  # Delegates to property setter
        return self

    def getTableEntry(self) -> List["ScheduleTableEntry"]:
        """
        AUTOSAR-compliant getter for tableEntry.

        Returns:
            The tableEntry value

        Note:
            Delegates to table_entry property (CODING_RULE_V2_00017)
        """
        return self.table_entry  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_resume_position(self, value: Optional["ResumePosition"]) -> "LinScheduleTable":
        """
        Set resumePosition and return self for chaining.

        Args:
            value: The resumePosition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_resume_position("value")
        """
        self.resume_position = value  # Use property setter (gets validation)
        return self

    def with_run_mode(self, value: Optional["RunMode"]) -> "LinScheduleTable":
        """
        Set runMode and return self for chaining.

        Args:
            value: The runMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_run_mode("value")
        """
        self.run_mode = value  # Use property setter (gets validation)
        return self

from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class ScheduleTableEntry(ARObject, ABC):
    """
    Table entry in a LinScheduleTable. Specifies what will be done in the frame
    slot.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 433, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is ScheduleTableEntry:
            raise TypeError("ScheduleTableEntry is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Relative delay between this tableEntry and the start of the the schedule
        # table in seconds.
        self._delay: Optional["TimeValue"] = None

    @property
    def delay(self) -> Optional["TimeValue"]:
        """Get delay (Pythonic accessor)."""
        return self._delay

    @delay.setter
    def delay(self, value: Optional["TimeValue"]) -> None:
        """
        Set delay with validation.

        Args:
            value: The delay to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._delay = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"delay must be TimeValue or None, got {type(value).__name__}"
            )
        self._delay = value
        # This represents introductory documentation about the entry.
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
        # Relative position in the schedule table.
        # The first entry the schedule table is 0.
        self._positionInTable: Optional["Integer"] = None

    @property
    def position_in_table(self) -> Optional["Integer"]:
        """Get positionInTable (Pythonic accessor)."""
        return self._positionInTable

    @position_in_table.setter
    def position_in_table(self, value: Optional["Integer"]) -> None:
        """
        Set positionInTable with validation.

        Args:
            value: The positionInTable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._positionInTable = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"positionInTable must be Integer or None, got {type(value).__name__}"
            )
        self._positionInTable = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDelay(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for delay.

        Returns:
            The delay value

        Note:
            Delegates to delay property (CODING_RULE_V2_00017)
        """
        return self.delay  # Delegates to property

    def setDelay(self, value: "TimeValue") -> "ScheduleTableEntry":
        """
        AUTOSAR-compliant setter for delay with method chaining.

        Args:
            value: The delay to set

        Returns:
            self for method chaining

        Note:
            Delegates to delay property setter (gets validation automatically)
        """
        self.delay = value  # Delegates to property setter
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

    def setIntroduction(self, value: "DocumentationBlock") -> "ScheduleTableEntry":
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

    def getPositionInTable(self) -> "Integer":
        """
        AUTOSAR-compliant getter for positionInTable.

        Returns:
            The positionInTable value

        Note:
            Delegates to position_in_table property (CODING_RULE_V2_00017)
        """
        return self.position_in_table  # Delegates to property

    def setPositionInTable(self, value: "Integer") -> "ScheduleTableEntry":
        """
        AUTOSAR-compliant setter for positionInTable with method chaining.

        Args:
            value: The positionInTable to set

        Returns:
            self for method chaining

        Note:
            Delegates to position_in_table property setter (gets validation automatically)
        """
        self.position_in_table = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_delay(self, value: Optional["TimeValue"]) -> "ScheduleTableEntry":
        """
        Set delay and return self for chaining.

        Args:
            value: The delay to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_delay("value")
        """
        self.delay = value  # Use property setter (gets validation)
        return self

    def with_introduction(self, value: Optional["DocumentationBlock"]) -> "ScheduleTableEntry":
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

    def with_position_in_table(self, value: Optional["Integer"]) -> "ScheduleTableEntry":
        """
        Set positionInTable and return self for chaining.

        Args:
            value: The positionInTable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_position_in_table("value")
        """
        self.position_in_table = value  # Use property setter (gets validation)
        return self

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import ScheduleTableEntry

    RefType,
)


class ApplicationEntry(ScheduleTableEntry):
    """
    Schedule table entry for application messages.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 433, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the LinFrame that will be transmitted in this.
        self._frameTriggering: RefType = None

    @property
    def frame_triggering(self) -> RefType:
        """Get frameTriggering (Pythonic accessor)."""
        return self._frameTriggering

    @frame_triggering.setter
    def frame_triggering(self, value: RefType) -> None:
        """
        Set frameTriggering with validation.

        Args:
            value: The frameTriggering to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._frameTriggering = None
            return

        self._frameTriggering = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFrameTriggering(self) -> RefType:
        """
        AUTOSAR-compliant getter for frameTriggering.

        Returns:
            The frameTriggering value

        Note:
            Delegates to frame_triggering property (CODING_RULE_V2_00017)
        """
        return self.frame_triggering  # Delegates to property

    def setFrameTriggering(self, value: RefType) -> "ApplicationEntry":
        """
        AUTOSAR-compliant setter for frameTriggering with method chaining.

        Args:
            value: The frameTriggering to set

        Returns:
            self for method chaining

        Note:
            Delegates to frame_triggering property setter (gets validation automatically)
        """
        self.frame_triggering = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_frame_triggering(self, value: Optional[RefType]) -> "ApplicationEntry":
        """
        Set frameTriggering and return self for chaining.

        Args:
            value: The frameTriggering to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_frame_triggering("value")
        """
        self.frame_triggering = value  # Use property setter (gets validation)
        return self

from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import (
    ScheduleTableEntry,
)


class FreeFormatEntry(ScheduleTableEntry, ABC):
    """
    FreeFormat transmits a fixed master request frame with the eight data bytes
    provided. This may for instance be used to issue user specific fixed frames.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 433, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is FreeFormatEntry:
            raise TypeError("FreeFormatEntry is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import (
    ScheduleTableEntry,
)


class LinConfigurationEntry(ScheduleTableEntry, ABC):
    """
    A ScheduleTableEntry which contains LIN specific assignments.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 434, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is LinConfigurationEntry:
            raise TypeError("LinConfigurationEntry is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The LIN slaves controller who is target of this assignment.
        # in case LinConfigurationEntry.
        # assignedLinSlave.
        self._assigned: Optional["LinSlave"] = None

    @property
    def assigned(self) -> Optional["LinSlave"]:
        """Get assigned (Pythonic accessor)."""
        return self._assigned

    @assigned.setter
    def assigned(self, value: Optional["LinSlave"]) -> None:
        """
        Set assigned with validation.

        Args:
            value: The assigned to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._assigned = None
            return

        if not isinstance(value, LinSlave):
            raise TypeError(
                f"assigned must be LinSlave or None, got {type(value).__name__}"
            )
        self._assigned = value
        # The LIN slave that is target of this assignment.
        # note that this reference is redundant to the Ecu Extract of the LinMaster the
                # LinSlave Ecus shall available.
        # that is described here is necessary in the for the configuration of the
                # LinMaster.
        self._assignedLin: Optional["LinSlaveConfigIdent"] = None

    @property
    def assigned_lin(self) -> Optional["LinSlaveConfigIdent"]:
        """Get assignedLin (Pythonic accessor)."""
        return self._assignedLin

    @assigned_lin.setter
    def assigned_lin(self, value: Optional["LinSlaveConfigIdent"]) -> None:
        """
        Set assignedLin with validation.

        Args:
            value: The assignedLin to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._assignedLin = None
            return

        if not isinstance(value, LinSlaveConfigIdent):
            raise TypeError(
                f"assignedLin must be LinSlaveConfigIdent or None, got {type(value).__name__}"
            )
        self._assignedLin = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAssigned(self) -> "LinSlave":
        """
        AUTOSAR-compliant getter for assigned.

        Returns:
            The assigned value

        Note:
            Delegates to assigned property (CODING_RULE_V2_00017)
        """
        return self.assigned  # Delegates to property

    def setAssigned(self, value: "LinSlave") -> "LinConfigurationEntry":
        """
        AUTOSAR-compliant setter for assigned with method chaining.

        Args:
            value: The assigned to set

        Returns:
            self for method chaining

        Note:
            Delegates to assigned property setter (gets validation automatically)
        """
        self.assigned = value  # Delegates to property setter
        return self

    def getAssignedLin(self) -> "LinSlaveConfigIdent":
        """
        AUTOSAR-compliant getter for assignedLin.

        Returns:
            The assignedLin value

        Note:
            Delegates to assigned_lin property (CODING_RULE_V2_00017)
        """
        return self.assigned_lin  # Delegates to property

    def setAssignedLin(self, value: "LinSlaveConfigIdent") -> "LinConfigurationEntry":
        """
        AUTOSAR-compliant setter for assignedLin with method chaining.

        Args:
            value: The assignedLin to set

        Returns:
            self for method chaining

        Note:
            Delegates to assigned_lin property setter (gets validation automatically)
        """
        self.assigned_lin = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_assigned(self, value: Optional["LinSlave"]) -> "LinConfigurationEntry":
        """
        Set assigned and return self for chaining.

        Args:
            value: The assigned to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_assigned("value")
        """
        self.assigned = value  # Use property setter (gets validation)
        return self

    def with_assigned_lin(self, value: Optional["LinSlaveConfigIdent"]) -> "LinConfigurationEntry":
        """
        Set assignedLin and return self for chaining.

        Args:
            value: The assignedLin to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_assigned_lin("value")
        """
        self.assigned_lin = value  # Use property setter (gets validation)
        return self

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import LinConfigurationEntry

    RefType,
)


class AssignFrameId(LinConfigurationEntry):
    """
    Schedule entry for an Assign Frame Id master request.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 436, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The frame whose identifier is set by this assignment.
        self._assignedFrame: RefType = None

    @property
    def assigned_frame(self) -> RefType:
        """Get assignedFrame (Pythonic accessor)."""
        return self._assignedFrame

    @assigned_frame.setter
    def assigned_frame(self, value: RefType) -> None:
        """
        Set assignedFrame with validation.

        Args:
            value: The assignedFrame to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._assignedFrame = None
            return

        self._assignedFrame = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAssignedFrame(self) -> RefType:
        """
        AUTOSAR-compliant getter for assignedFrame.

        Returns:
            The assignedFrame value

        Note:
            Delegates to assigned_frame property (CODING_RULE_V2_00017)
        """
        return self.assigned_frame  # Delegates to property

    def setAssignedFrame(self, value: RefType) -> "AssignFrameId":
        """
        AUTOSAR-compliant setter for assignedFrame with method chaining.

        Args:
            value: The assignedFrame to set

        Returns:
            self for method chaining

        Note:
            Delegates to assigned_frame property setter (gets validation automatically)
        """
        self.assigned_frame = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_assigned_frame(self, value: Optional[RefType]) -> "AssignFrameId":
        """
        Set assignedFrame and return self for chaining.

        Args:
            value: The assignedFrame to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_assigned_frame("value")
        """
        self.assigned_frame = value  # Use property setter (gets validation)
        return self

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import LinConfigurationEntry

    RefType,
)


class UnassignFrameId(LinConfigurationEntry):
    """
    Schedule entry for an Unassign Frame Id master request where the protected
    identifier is assigned the value 0x40. This will disable
    reception/transmission of a previously dynamically assigned frame
    identifier.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 436, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The frame whose identifier is reset by this assignment.
        self._unassigned: RefType = None

    @property
    def unassigned(self) -> RefType:
        """Get unassigned (Pythonic accessor)."""
        return self._unassigned

    @unassigned.setter
    def unassigned(self, value: RefType) -> None:
        """
        Set unassigned with validation.

        Args:
            value: The unassigned to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._unassigned = None
            return

        self._unassigned = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getUnassigned(self) -> RefType:
        """
        AUTOSAR-compliant getter for unassigned.

        Returns:
            The unassigned value

        Note:
            Delegates to unassigned property (CODING_RULE_V2_00017)
        """
        return self.unassigned  # Delegates to property

    def setUnassigned(self, value: RefType) -> "UnassignFrameId":
        """
        AUTOSAR-compliant setter for unassigned with method chaining.

        Args:
            value: The unassigned to set

        Returns:
            self for method chaining

        Note:
            Delegates to unassigned property setter (gets validation automatically)
        """
        self.unassigned = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_unassigned(self, value: Optional[RefType]) -> "UnassignFrameId":
        """
        Set unassigned and return self for chaining.

        Args:
            value: The unassigned to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_unassigned("value")
        """
        self.unassigned = value  # Use property setter (gets validation)
        return self

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import (
    LinConfigurationEntry,
)


class AssignFrameIdRange(LinConfigurationEntry):
    """
    AssignFrameIdRange generates an assign frame PID range request.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 437, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # the request.
        # The frame_PIDs are ordered.
        self._framePid: "FramePid" = None

    @property
    def frame_pid(self) -> "FramePid":
        """Get framePid (Pythonic accessor)."""
        return self._framePid

    @frame_pid.setter
    def frame_pid(self, value: "FramePid") -> None:
        """
        Set framePid with validation.

        Args:
            value: The framePid to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, FramePid):
            raise TypeError(
                f"framePid must be FramePid, got {type(value).__name__}"
            )
        self._framePid = value
        # The startIndex sets the index to the first frame to assign a.
        self._startIndex: Optional["Integer"] = None

    @property
    def start_index(self) -> Optional["Integer"]:
        """Get startIndex (Pythonic accessor)."""
        return self._startIndex

    @start_index.setter
    def start_index(self, value: Optional["Integer"]) -> None:
        """
        Set startIndex with validation.

        Args:
            value: The startIndex to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._startIndex = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"startIndex must be Integer or None, got {type(value).__name__}"
            )
        self._startIndex = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFramePid(self) -> "FramePid":
        """
        AUTOSAR-compliant getter for framePid.

        Returns:
            The framePid value

        Note:
            Delegates to frame_pid property (CODING_RULE_V2_00017)
        """
        return self.frame_pid  # Delegates to property

    def setFramePid(self, value: "FramePid") -> "AssignFrameIdRange":
        """
        AUTOSAR-compliant setter for framePid with method chaining.

        Args:
            value: The framePid to set

        Returns:
            self for method chaining

        Note:
            Delegates to frame_pid property setter (gets validation automatically)
        """
        self.frame_pid = value  # Delegates to property setter
        return self

    def getStartIndex(self) -> "Integer":
        """
        AUTOSAR-compliant getter for startIndex.

        Returns:
            The startIndex value

        Note:
            Delegates to start_index property (CODING_RULE_V2_00017)
        """
        return self.start_index  # Delegates to property

    def setStartIndex(self, value: "Integer") -> "AssignFrameIdRange":
        """
        AUTOSAR-compliant setter for startIndex with method chaining.

        Args:
            value: The startIndex to set

        Returns:
            self for method chaining

        Note:
            Delegates to start_index property setter (gets validation automatically)
        """
        self.start_index = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_frame_pid(self, value: "FramePid") -> "AssignFrameIdRange":
        """
        Set framePid and return self for chaining.

        Args:
            value: The framePid to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_frame_pid("value")
        """
        self.frame_pid = value  # Use property setter (gets validation)
        return self

    def with_start_index(self, value: Optional["Integer"]) -> "AssignFrameIdRange":
        """
        Set startIndex and return self for chaining.

        Args:
            value: The startIndex to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_start_index("value")
        """
        self.start_index = value  # Use property setter (gets validation)
        return self

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class FramePid(ARObject):
    """
    Frame_PIDs that are included in the request. The "pid" attribute describes
    the value and the "index" attribute the position of the frame_PID in the
    request.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 437, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute is used to order the frame_PIDs.
        # The values shall be unique within one AssignFrameIdRange.
        self._index: Optional["Integer"] = None

    @property
    def index(self) -> Optional["Integer"]:
        """Get index (Pythonic accessor)."""
        return self._index

    @index.setter
    def index(self, value: Optional["Integer"]) -> None:
        """
        Set index with validation.

        Args:
            value: The index to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._index = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"index must be Integer or None, got {type(value).__name__}"
            )
        self._index = value
        # Frame_PID value.
        self._pid: Optional["PositiveInteger"] = None

    @property
    def pid(self) -> Optional["PositiveInteger"]:
        """Get pid (Pythonic accessor)."""
        return self._pid

    @pid.setter
    def pid(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set pid with validation.

        Args:
            value: The pid to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pid = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"pid must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._pid = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIndex(self) -> "Integer":
        """
        AUTOSAR-compliant getter for index.

        Returns:
            The index value

        Note:
            Delegates to index property (CODING_RULE_V2_00017)
        """
        return self.index  # Delegates to property

    def setIndex(self, value: "Integer") -> "FramePid":
        """
        AUTOSAR-compliant setter for index with method chaining.

        Args:
            value: The index to set

        Returns:
            self for method chaining

        Note:
            Delegates to index property setter (gets validation automatically)
        """
        self.index = value  # Delegates to property setter
        return self

    def getPid(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for pid.

        Returns:
            The pid value

        Note:
            Delegates to pid property (CODING_RULE_V2_00017)
        """
        return self.pid  # Delegates to property

    def setPid(self, value: "PositiveInteger") -> "FramePid":
        """
        AUTOSAR-compliant setter for pid with method chaining.

        Args:
            value: The pid to set

        Returns:
            self for method chaining

        Note:
            Delegates to pid property setter (gets validation automatically)
        """
        self.pid = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_index(self, value: Optional["Integer"]) -> "FramePid":
        """
        Set index and return self for chaining.

        Args:
            value: The index to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_index("value")
        """
        self.index = value  # Use property setter (gets validation)
        return self

    def with_pid(self, value: Optional["PositiveInteger"]) -> "FramePid":
        """
        Set pid and return self for chaining.

        Args:
            value: The pid to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pid("value")
        """
        self.pid = value  # Use property setter (gets validation)
        return self

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import (
    LinConfigurationEntry,
)


class AssignNad(LinConfigurationEntry):
    """
    Schedule entry for an Assign NAD master request.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 438, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The newly assigned NAD value.
        self._newNad: Optional["Integer"] = None

    @property
    def new_nad(self) -> Optional["Integer"]:
        """Get newNad (Pythonic accessor)."""
        return self._newNad

    @new_nad.setter
    def new_nad(self, value: Optional["Integer"]) -> None:
        """
        Set newNad with validation.

        Args:
            value: The newNad to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._newNad = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"newNad must be Integer or None, got {type(value).__name__}"
            )
        self._newNad = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNewNad(self) -> "Integer":
        """
        AUTOSAR-compliant getter for newNad.

        Returns:
            The newNad value

        Note:
            Delegates to new_nad property (CODING_RULE_V2_00017)
        """
        return self.new_nad  # Delegates to property

    def setNewNad(self, value: "Integer") -> "AssignNad":
        """
        AUTOSAR-compliant setter for newNad with method chaining.

        Args:
            value: The newNad to set

        Returns:
            self for method chaining

        Note:
            Delegates to new_nad property setter (gets validation automatically)
        """
        self.new_nad = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_new_nad(self, value: Optional["Integer"]) -> "AssignNad":
        """
        Set newNad and return self for chaining.

        Args:
            value: The newNad to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_new_nad("value")
        """
        self.new_nad = value  # Use property setter (gets validation)
        return self

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import (
    LinConfigurationEntry,
)


class ConditionalChangeNad(LinConfigurationEntry):
    """
    Generates an conditional change NAD request. See ISO 17987 protocol
    specification for more information.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 438, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Byte Position of Data Byte that should be used for the with Invert and the
        # bitwise AND with Mask.
        self._byte: Optional["Integer"] = None

    @property
    def byte(self) -> Optional["Integer"]:
        """Get byte (Pythonic accessor)."""
        return self._byte

    @byte.setter
    def byte(self, value: Optional["Integer"]) -> None:
        """
        Set byte with validation.

        Args:
            value: The byte to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._byte = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"byte must be Integer or None, got {type(value).__name__}"
            )
        self._byte = value
        # Byte Position of Id.
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"id must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._id = value
        # Byte Position of Invert.
        self._invert: Optional["Integer"] = None

    @property
    def invert(self) -> Optional["Integer"]:
        """Get invert (Pythonic accessor)."""
        return self._invert

    @invert.setter
    def invert(self, value: Optional["Integer"]) -> None:
        """
        Set invert with validation.

        Args:
            value: The invert to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._invert = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"invert must be Integer or None, got {type(value).__name__}"
            )
        self._invert = value
        # Byte Position of Mask.
        self._mask: Optional["Integer"] = None

    @property
    def mask(self) -> Optional["Integer"]:
        """Get mask (Pythonic accessor)."""
        return self._mask

    @mask.setter
    def mask(self, value: Optional["Integer"]) -> None:
        """
        Set mask with validation.

        Args:
            value: The mask to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mask = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"mask must be Integer or None, got {type(value).__name__}"
            )
        self._mask = value
        # The newly assigned NAD value (Byte Position).
        self._newNad: Optional["Integer"] = None

    @property
    def new_nad(self) -> Optional["Integer"]:
        """Get newNad (Pythonic accessor)."""
        return self._newNad

    @new_nad.setter
    def new_nad(self, value: Optional["Integer"]) -> None:
        """
        Set newNad with validation.

        Args:
            value: The newNad to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._newNad = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"newNad must be Integer or None, got {type(value).__name__}"
            )
        self._newNad = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getByte(self) -> "Integer":
        """
        AUTOSAR-compliant getter for byte.

        Returns:
            The byte value

        Note:
            Delegates to byte property (CODING_RULE_V2_00017)
        """
        return self.byte  # Delegates to property

    def setByte(self, value: "Integer") -> "ConditionalChangeNad":
        """
        AUTOSAR-compliant setter for byte with method chaining.

        Args:
            value: The byte to set

        Returns:
            self for method chaining

        Note:
            Delegates to byte property setter (gets validation automatically)
        """
        self.byte = value  # Delegates to property setter
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

    def setId(self, value: "PositiveInteger") -> "ConditionalChangeNad":
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

    def getInvert(self) -> "Integer":
        """
        AUTOSAR-compliant getter for invert.

        Returns:
            The invert value

        Note:
            Delegates to invert property (CODING_RULE_V2_00017)
        """
        return self.invert  # Delegates to property

    def setInvert(self, value: "Integer") -> "ConditionalChangeNad":
        """
        AUTOSAR-compliant setter for invert with method chaining.

        Args:
            value: The invert to set

        Returns:
            self for method chaining

        Note:
            Delegates to invert property setter (gets validation automatically)
        """
        self.invert = value  # Delegates to property setter
        return self

    def getMask(self) -> "Integer":
        """
        AUTOSAR-compliant getter for mask.

        Returns:
            The mask value

        Note:
            Delegates to mask property (CODING_RULE_V2_00017)
        """
        return self.mask  # Delegates to property

    def setMask(self, value: "Integer") -> "ConditionalChangeNad":
        """
        AUTOSAR-compliant setter for mask with method chaining.

        Args:
            value: The mask to set

        Returns:
            self for method chaining

        Note:
            Delegates to mask property setter (gets validation automatically)
        """
        self.mask = value  # Delegates to property setter
        return self

    def getNewNad(self) -> "Integer":
        """
        AUTOSAR-compliant getter for newNad.

        Returns:
            The newNad value

        Note:
            Delegates to new_nad property (CODING_RULE_V2_00017)
        """
        return self.new_nad  # Delegates to property

    def setNewNad(self, value: "Integer") -> "ConditionalChangeNad":
        """
        AUTOSAR-compliant setter for newNad with method chaining.

        Args:
            value: The newNad to set

        Returns:
            self for method chaining

        Note:
            Delegates to new_nad property setter (gets validation automatically)
        """
        self.new_nad = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_byte(self, value: Optional["Integer"]) -> "ConditionalChangeNad":
        """
        Set byte and return self for chaining.

        Args:
            value: The byte to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_byte("value")
        """
        self.byte = value  # Use property setter (gets validation)
        return self

    def with_id(self, value: Optional["PositiveInteger"]) -> "ConditionalChangeNad":
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

    def with_invert(self, value: Optional["Integer"]) -> "ConditionalChangeNad":
        """
        Set invert and return self for chaining.

        Args:
            value: The invert to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_invert("value")
        """
        self.invert = value  # Use property setter (gets validation)
        return self

    def with_mask(self, value: Optional["Integer"]) -> "ConditionalChangeNad":
        """
        Set mask and return self for chaining.

        Args:
            value: The mask to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mask("value")
        """
        self.mask = value  # Use property setter (gets validation)
        return self

    def with_new_nad(self, value: Optional["Integer"]) -> "ConditionalChangeNad":
        """
        Set newNad and return self for chaining.

        Args:
            value: The newNad to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_new_nad("value")
        """
        self.new_nad = value  # Use property setter (gets validation)
        return self

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import (
    LinConfigurationEntry,
)


class SaveConfigurationEntry(LinConfigurationEntry):
    """
    This service is used to notify a slave node to store its configuration.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 439, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import (
    LinConfigurationEntry,
)


class DataDumpEntry(LinConfigurationEntry):
    """
    This service is reserved for initial configuration of a slave node by the
    slave node supplier and the format of this message is supplier specific.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 439, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Supplier specific format.
        self._byteValue: List["Integer"] = []

    @property
    def byte_value(self) -> List["Integer"]:
        """Get byteValue (Pythonic accessor)."""
        return self._byteValue

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getByteValue(self) -> List["Integer"]:
        """
        AUTOSAR-compliant getter for byteValue.

        Returns:
            The byteValue value

        Note:
            Delegates to byte_value property (CODING_RULE_V2_00017)
        """
        return self.byte_value  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import (
    FreeFormatEntry,
)


class FreeFormat(FreeFormatEntry):
    """
    Representing freely defined data.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 439, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The integer Value of a freely defined data byte.
        self._byteValue: List["Integer"] = []

    @property
    def byte_value(self) -> List["Integer"]:
        """Get byteValue (Pythonic accessor)."""
        return self._byteValue

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getByteValue(self) -> List["Integer"]:
        """
        AUTOSAR-compliant getter for byteValue.

        Returns:
            The byteValue value

        Note:
            Delegates to byte_value property (CODING_RULE_V2_00017)
        """
        return self.byte_value  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
