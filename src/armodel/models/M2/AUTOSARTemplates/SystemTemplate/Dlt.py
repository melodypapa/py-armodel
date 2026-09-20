from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum


class DltDefaultTraceStateEnum(AREnum):
    """
    This enumeration defines the supported values for the Dlt default trace state.
    """

    # DltDefaultTraceStateEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.337, p.723 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on DltLogChannel.defaultTraceState (Steps 5/6 N/A: standalone AREnum)

    # The default trace state is disabled Tags: atp.EnumerationLiteralIndex=1
    DEFAULT_TRACE_STATE_DISABLED = "DefaultTraceStateDisabled"

    # The default trace state is enabled Tags: atp.EnumerationLiteralIndex=0
    DEFAULT_TRACE_STATE_ENABLED = "DefaultTraceStateEnabled"

    def __init__(self):
        super().__init__(
            (
                DltDefaultTraceStateEnum.DEFAULT_TRACE_STATE_DISABLED,
                DltDefaultTraceStateEnum.DEFAULT_TRACE_STATE_ENABLED,
            )
        )


class LogTraceDefaultLogLevelEnum(AREnum):
    """
    This enum defines available log&trace log levels that may be used to define the severity level of a log message.
    """

    # LogTraceDefaultLogLevelEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.338, p.724 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on DltLogChannel.logTraceDefaultLogThreshold (Steps 5/6 N/A: standalone AREnum)

    # Detailed information for programmers Tags: atp.EnumerationLiteralIndex=4
    DEBUG = "debug"

    # Error with impact to correct functionality Tags: atp.EnumerationLiteralIndex=1
    ERROR = "error"

    # Fatal error Tags: atp.EnumerationLiteralIndex=0
    FATAL = "fatal"

    # High level information Tags: atp.EnumerationLiteralIndex=3
    INFO = "info"

    # logging is turned off Tags: atp.EnumerationLiteralIndex=6
    OFF = "off"

    # Verbose debug message Tags: atp.EnumerationLiteralIndex=5
    VERBOSE = "verbose"

    # Warning if correct behavior cannot be ensured Tags: atp.EnumerationLiteralIndex=2
    WARN = "warn"

    def __init__(self):
        super().__init__(
            (
                LogTraceDefaultLogLevelEnum.DEBUG,
                LogTraceDefaultLogLevelEnum.ERROR,
                LogTraceDefaultLogLevelEnum.FATAL,
                LogTraceDefaultLogLevelEnum.INFO,
                LogTraceDefaultLogLevelEnum.OFF,
                LogTraceDefaultLogLevelEnum.VERBOSE,
                LogTraceDefaultLogLevelEnum.WARN,
            )
        )
