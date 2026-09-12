from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum


class ResolutionPolicyEnum(AREnum):
    """
    This specifies if the content of the xref element follow a dedicated resolution policy.
    """

    # ResolutionPolicyEnum method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.46, p.322
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on Xref.resolutionPolicy (RESOLUTION-POLICY attribute)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # The content of the xref element is not linked by a sloppy reference. Tags: atp.EnumerationLiteralIndex=0
    NO_SLOPPY = "NO-SLOPPY"

    # The content of the xref element is linked by a sloppy reference. Tags: atp.EnumerationLiteralIndex=1
    SLOPPY = "SLOPPY"

    def __init__(self):
        super().__init__((ResolutionPolicyEnum.NO_SLOPPY, ResolutionPolicyEnum.SLOPPY))


class ShowContentEnum(AREnum):
    """
    This specifies if the content of the xref element shall be rendered.
    """

    # ShowContentEnum method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.47, p.323
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on Xref.showContent (SHOW-CONTENT attribute)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # The content of the Xref.label is not rendered at the place of the reference. Tags: atp.EnumerationLiteralIndex=0
    NO_SHOW_CONTENT = "NO-SHOW-CONTENT"

    # The content of the element is rendered at the place of the reference. Tags: atp.EnumerationLiteralIndex=1
    SHOW_CONTENT = "SHOW-CONTENT"

    def __init__(self):
        super().__init__((ShowContentEnum.NO_SHOW_CONTENT, ShowContentEnum.SHOW_CONTENT))
