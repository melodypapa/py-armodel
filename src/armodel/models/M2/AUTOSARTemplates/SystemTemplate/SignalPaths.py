from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum


class SwcToSwcOperationArgumentsDirectionEnum(AREnum):
    """
    Direction addressed by this element.
    """

    # SwcToSwcOperationArgumentsDirectionEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.39, p.254
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — serialized as value form on SwcToSwcOperationArguments.direction
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # IN (all IN and INOUT arguments) Tags: atp.EnumerationLiteralIndex=0
    IN = "IN"

    # OUT (all OUT and INOUT arguments) . Tags: atp.EnumerationLiteralIndex=1
    OUT = "OUT"

    def __init__(self):
        super().__init__(
            (
                SwcToSwcOperationArgumentsDirectionEnum.IN,
                SwcToSwcOperationArgumentsDirectionEnum.OUT,
            )
        )
