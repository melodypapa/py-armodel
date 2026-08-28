"""

This module contains the BSW level timing description event classes
(spec package CommonStructure::Timing::TimingDescription::TimingDescriptionEvents::TDEventBsw).
"""

from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription import (
    TimingDescriptionEvent,
)


class TDEventBsw(TimingDescriptionEvent):
    """
    This is used to describe timing events related to BSW modules.
    """

    # TDEventBsw method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table D.56, p.251
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getBswModuleDescriptionRef        [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setBswModuleDescriptionRef        [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self, parent, short_name):
        if type(self) is TDEventBsw:
            raise TypeError("TDEventBsw is an abstract class.")
        super().__init__(parent, short_name)

        # The scope of this timing event.
        self.bswModuleDescriptionRef: Optional[RefType] = None

    def getBswModuleDescriptionRef(self) -> Optional[RefType]:
        """The scope of this timing event."""
        return self.bswModuleDescriptionRef

    def setBswModuleDescriptionRef(self, value: Optional[RefType]) -> "TDEventBsw":
        """The scope of this timing event. A None value is a no-op and does not overwrite an existing bswModuleDescriptionRef."""
        if value is not None:
            self.bswModuleDescriptionRef = value
        return self


class TDEventBswModuleTypeEnum(AREnum):
    """
    This is used to describe the specific event type of a TDEventBswModule.
    """

    # TDEventBswModuleTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.45, p.76
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on TDEventBswModule.tdEventBswModuleType
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # A point in time where the associated BswModuleEntry has been called. Tags: atp.EnumerationLiteralIndex=0
    BSW_M_ENTRY_CALLED = "bswMEntryCalled"

    # A point in time where the call of the associated BswModuleEntry has returned. Tags: atp.EnumerationLiteralIndex=1
    BSW_M_ENTRY_CALL_RETURNED = "bswMEntryCallReturned"

    def __init__(self):
        """
        Initializes the TDEventBswModuleTypeEnum with valid values.
        """
        super().__init__(
            (
                TDEventBswModuleTypeEnum.BSW_M_ENTRY_CALLED,
                TDEventBswModuleTypeEnum.BSW_M_ENTRY_CALL_RETURNED,
            )
        )


class TDEventBswModeDeclarationTypeEnum(AREnum):
    """
    This is used to describe the specific event type of a TDEventBswModeDeclaration.
    """

    # TDEventBswModeDeclarationTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.47, p.77
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on TDEventBswModeDeclaration.tdEventBswModeDeclarationType
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # A point in time where the associated ModeDeclarationGroupPrototype has been requested. Tags: atp.EnumerationLiteralIndex=0
    MODE_DECLARATION_REQUESTED = "modeDeclarationRequested"

    # A point in time where the switch to the associated ModeDeclarationGroupPrototype has been completed. Tags: atp.EnumerationLiteralIndex=1
    MODE_DECLARATION_SWITCH_COMPLETED = "modeDeclarationSwitchCompleted"

    # A point in time where the switch to the associated ModeDeclarationGroupPrototype has been initiated by the BswM. Tags: atp.EnumerationLiteralIndex=2
    MODE_DECLARATION_SWITCH_INITIATED = "modeDeclarationSwitchInitiated"

    def __init__(self):
        """
        Initializes the TDEventBswModeDeclarationTypeEnum with valid values.
        """
        super().__init__(
            (
                TDEventBswModeDeclarationTypeEnum.MODE_DECLARATION_REQUESTED,
                TDEventBswModeDeclarationTypeEnum.MODE_DECLARATION_SWITCH_COMPLETED,
                TDEventBswModeDeclarationTypeEnum.MODE_DECLARATION_SWITCH_INITIATED,
            )
        )


class TDEventBswModule(TDEventBsw):
    """
    This is used to describe timing events related to the interaction between BSW modules.
    """

    # TDEventBswModule method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.44, p.75
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getBswModuleEntryRef          [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setBswModuleEntryRef          [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getTdEventBswModuleType       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setTdEventBswModuleType       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # The scope of this timing event.
        self.bswModuleEntryRef: Optional[RefType] = None

        # The specific type of this timing event.
        self.tdEventBswModuleType: Optional[TDEventBswModuleTypeEnum] = None

    def getBswModuleEntryRef(self) -> Optional[RefType]:
        """The scope of this timing event."""
        return self.bswModuleEntryRef

    def setBswModuleEntryRef(self, value: Optional[RefType]) -> "TDEventBswModule":
        """The scope of this timing event. A None value is a no-op and does not overwrite an existing bswModuleEntryRef."""
        if value is not None:
            self.bswModuleEntryRef = value
        return self

    def getTdEventBswModuleType(self) -> Optional[TDEventBswModuleTypeEnum]:
        """The specific type of this timing event."""
        return self.tdEventBswModuleType

    def setTdEventBswModuleType(self, value: Optional[TDEventBswModuleTypeEnum]) -> "TDEventBswModule":
        """The specific type of this timing event. A None value is a no-op and does not overwrite an existing tdEventBswModuleType."""
        if value is not None:
            self.tdEventBswModuleType = value
        return self


class TDEventBswModeDeclaration(TDEventBsw):
    """
    This is used to describe timing events related to the mode communication on BSW level.
    """

    # TDEventBswModeDeclaration method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.46, p.77
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getEntryModeDeclarationRef            [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setEntryModeDeclarationRef            [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getExitModeDeclarationRef             [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setExitModeDeclarationRef             [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getModeDeclarationRef                 [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setModeDeclarationRef                 [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getTdEventBswModeDeclarationType      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setTdEventBswModeDeclarationType      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # Optional parameter which refines the scope of the TDEventBswModeDeclaration. If the parameter is set, the event occurs only if the mode declaration group prototype instance shall enter into the referenced ModeDeclaration.
        self.entryModeDeclarationRef: Optional[RefType] = None

        # Optional parameter which refines the scope of the TDEventBswModeDeclaration. If the parameter is set, the event occurs only if the mode declaration group prototype instance shall exit from the referenced ModeDeclaration.
        self.exitModeDeclarationRef: Optional[RefType] = None

        # The scope of this timing event.
        self.modeDeclarationRef: Optional[RefType] = None

        # The specific type of this timing event.
        self.tdEventBswModeDeclarationType: Optional[TDEventBswModeDeclarationTypeEnum] = None

    def getEntryModeDeclarationRef(self) -> Optional[RefType]:
        """Optional parameter which refines the scope of the TDEventBswModeDeclaration. If the parameter is set, the event occurs only if the mode declaration group prototype instance shall enter into the referenced ModeDeclaration."""
        return self.entryModeDeclarationRef

    def setEntryModeDeclarationRef(self, value: Optional[RefType]) -> "TDEventBswModeDeclaration":
        """Optional parameter which refines the scope of the TDEventBswModeDeclaration. If the parameter is set, the event occurs only if the mode declaration group prototype instance shall enter into the referenced ModeDeclaration. A None value is a no-op and does not overwrite an existing entryModeDeclarationRef."""
        if value is not None:
            self.entryModeDeclarationRef = value
        return self

    def getExitModeDeclarationRef(self) -> Optional[RefType]:
        """Optional parameter which refines the scope of the TDEventBswModeDeclaration. If the parameter is set, the event occurs only if the mode declaration group prototype instance shall exit from the referenced ModeDeclaration."""
        return self.exitModeDeclarationRef

    def setExitModeDeclarationRef(self, value: Optional[RefType]) -> "TDEventBswModeDeclaration":
        """Optional parameter which refines the scope of the TDEventBswModeDeclaration. If the parameter is set, the event occurs only if the mode declaration group prototype instance shall exit from the referenced ModeDeclaration. A None value is a no-op and does not overwrite an existing exitModeDeclarationRef."""
        if value is not None:
            self.exitModeDeclarationRef = value
        return self

    def getModeDeclarationRef(self) -> Optional[RefType]:
        """The scope of this timing event."""
        return self.modeDeclarationRef

    def setModeDeclarationRef(self, value: Optional[RefType]) -> "TDEventBswModeDeclaration":
        """The scope of this timing event. A None value is a no-op and does not overwrite an existing modeDeclarationRef."""
        if value is not None:
            self.modeDeclarationRef = value
        return self

    def getTdEventBswModeDeclarationType(self) -> Optional[TDEventBswModeDeclarationTypeEnum]:
        """The specific type of this timing event."""
        return self.tdEventBswModeDeclarationType

    def setTdEventBswModeDeclarationType(self, value: Optional[TDEventBswModeDeclarationTypeEnum]) -> "TDEventBswModeDeclaration":
        """The specific type of this timing event. A None value is a no-op and does not overwrite an existing tdEventBswModeDeclarationType."""
        if value is not None:
            self.tdEventBswModeDeclarationType = value
        return self
