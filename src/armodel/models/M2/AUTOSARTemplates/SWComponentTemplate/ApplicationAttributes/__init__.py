"""
This module contains application attribute classes for AUTOSAR software components.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum


class DataLimitKindEnum(AREnum):
    """
    Enumeration for data limit kinds in AUTOSAR.
    """
    # DataLimitKindEnum method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test


    UNLIMITED = "unlimited"
    LIMITED = "limited"

    def __init__(self):
        super().__init__((
            DataLimitKindEnum.UNLIMITED,
            DataLimitKindEnum.LIMITED,
        ))


class FilterDebouncingEnum(AREnum):
    """
    Enumeration for filter debouncing in AUTOSAR.
    """
    # FilterDebouncingEnum method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test


    FILTER = "filter"
    DEBOUNCE = "debounce"
    NONE = "none"

    def __init__(self):
        super().__init__((
            FilterDebouncingEnum.FILTER,
            FilterDebouncingEnum.DEBOUNCE,
            FilterDebouncingEnum.NONE,
        ))


class ProcessingKindEnum(AREnum):
    """
    Enumeration for processing kinds in AUTOSAR.
    """
    # ProcessingKindEnum method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test


    EVENT_TRIGGERED = "event-triggered"
    PERIODIC = "periodic"
    DATA_TRIGGERED = "data-triggered"

    def __init__(self):
        super().__init__((
            ProcessingKindEnum.EVENT_TRIGGERED,
            ProcessingKindEnum.PERIODIC,
            ProcessingKindEnum.DATA_TRIGGERED,
        ))


class PulseTestEnum(AREnum):
    """
    Enumeration for pulse test in AUTOSAR.
    """
    # PulseTestEnum method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test


    PULSE = "pulse"
    TEST = "test"
    NONE = "none"

    def __init__(self):
        super().__init__((
            PulseTestEnum.PULSE,
            PulseTestEnum.TEST,
            PulseTestEnum.NONE,
        ))


class SignalFanEnum(AREnum):
    """
    Enumeration for signal fan in AUTOSAR.
    """
    # SignalFanEnum method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test


    IN = "in"
    OUT = "out"
    IN_OUT = "in-out"

    def __init__(self):
        super().__init__((
            SignalFanEnum.IN,
            SignalFanEnum.OUT,
            SignalFanEnum.IN_OUT,
        ))


__all__ = [
    'DataLimitKindEnum',
    'FilterDebouncingEnum',
    'ProcessingKindEnum',
    'PulseTestEnum',
    'SignalFanEnum',
]
