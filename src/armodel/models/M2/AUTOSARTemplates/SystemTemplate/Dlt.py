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
