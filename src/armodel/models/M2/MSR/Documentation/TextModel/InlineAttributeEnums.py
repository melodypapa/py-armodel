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


class ShowResourceAliasNameEnum(AREnum):
    """
    This enumerator specifies if the alias names of the reference target shall be rendered with the xref.
    """

    # ShowResourceAliasNameEnum method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.48, p.323
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on Xref.showResourceAliasName (SHOW-RESOURCE-ALIAS-NAME attribute)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # This indicates that alias names of the referenced object shall not be rendered at the place of the reference. Tags: atp.EnumerationLiteralIndex=0
    NO_SHOW_ALIAS_NAME = "NO-SHOW-ALIAS-NAME"

    # This indicates that the alias names of the referenced object shall be rendered at the place of the reference. Tags: atp.EnumerationLiteralIndex=1
    SHOW_ALIAS_NAME = "SHOW-ALIAS-NAME"

    def __init__(self):
        super().__init__((ShowResourceAliasNameEnum.NO_SHOW_ALIAS_NAME, ShowResourceAliasNameEnum.SHOW_ALIAS_NAME))


class ShowResourceCategoryEnum(AREnum):
    """
    This enumerator specifies if the category of the reference target shall be rendered with the xref.
    """

    # ShowResourceCategoryEnum method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.49, p.323
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on Xref.showResourceCategory (SHOW-RESOURCE-CATEGORY attribute)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # The category of the target is not rendered at the place of the reference. Tags: atp.EnumerationLiteralIndex=0
    NO_SHOW_CATEGORY = "NO-SHOW-CATEGORY"

    # The category of the target is rendered at the place of the reference. Tags: atp.EnumerationLiteralIndex=1
    SHOW_CATEGORY = "SHOW-CATEGORY"

    def __init__(self):
        super().__init__((ShowResourceCategoryEnum.NO_SHOW_CATEGORY, ShowResourceCategoryEnum.SHOW_CATEGORY))


class ShowResourceLongNameEnum(AREnum):
    """
    This enumerator specifies if the long name of the reference target shall be rendered with the xref.
    """

    # ShowResourceLongNameEnum method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.50, p.323
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on Xref.showResourceLongName (SHOW-RESOURCE-LONG-NAME attribute)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # The long name of the target is not rendered at the place of the reference. Tags: atp.EnumerationLiteralIndex=0
    NO_SHOW_LONG_NAME = "NO-SHOW-LONG-NAME"

    # The long name of the target is rendered at the place of the reference. Tags: atp.EnumerationLiteralIndex=1
    SHOW_LONG_NAME = "SHOW-LONG-NAME"

    def __init__(self):
        super().__init__((ShowResourceLongNameEnum.NO_SHOW_LONG_NAME, ShowResourceLongNameEnum.SHOW_LONG_NAME))


class ShowResourceNumberEnum(AREnum):
    """
    This enumerator specifies if the number (e.g. chapter number) of the reference target shall be rendered with the xref.
    """

    # ShowResourceNumberEnum method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.51, p.324
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on Xref.showResourceNumber (SHOW-RESOURCE-NUMBER attribute)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # The number of the target is not rendered at the place of the reference. Tags: atp.EnumerationLiteralIndex=0
    NO_SHOW_NUMBER = "NO-SHOW-NUMBER"

    # The number of the target is rendered at the place of the reference. Tags: atp.EnumerationLiteralIndex=1
    SHOW_NUMBER = "SHOW-NUMBER"

    def __init__(self):
        super().__init__((ShowResourceNumberEnum.NO_SHOW_NUMBER, ShowResourceNumberEnum.SHOW_NUMBER))


class ShowResourcePageEnum(AREnum):
    """
    This enumerator specifies if the page number of the reference target shall be rendered with the xref.
    """

    # ShowResourcePageEnum method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.52, p.324
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on Xref.showResourcePage (SHOW-RESOURCE-PAGE attribute)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # The page number of the target is not rendered at the place of the reference. Tags: atp.EnumerationLiteralIndex=0
    NO_SHOW_PAGE = "NO-SHOW-PAGE"

    # The page number of the target is rendered at the place of the reference. Tags: atp.EnumerationLiteralIndex=1
    SHOW_PAGE = "SHOW-PAGE"

    def __init__(self):
        super().__init__((ShowResourcePageEnum.NO_SHOW_PAGE, ShowResourcePageEnum.SHOW_PAGE))


class ShowResourceShortNameEnum(AREnum):
    """
    This enumerator specifies if the short name of the reference target shall be rendered with the xref.
    """

    # ShowResourceShortNameEnum method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.53, p.324
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on Xref.showResourceShortName (SHOW-RESOURCE-SHORT-NAME attribute)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # The short name of the target is not rendered at the place of the reference. Tags: atp.EnumerationLiteralIndex=0
    NO_SHOW_SHORT_NAME = "NO-SHOW-SHORT-NAME"

    # The short name of the target is rendered at the place of the reference. Tags: atp.EnumerationLiteralIndex=1
    SHOW_SHORT_NAME = "SHOW-SHORT-NAME"

    def __init__(self):
        super().__init__((ShowResourceShortNameEnum.NO_SHOW_SHORT_NAME, ShowResourceShortNameEnum.SHOW_SHORT_NAME))


class ShowResourceTypeEnum(AREnum):
    """
    This enumerator specifies if the type (e.g. derived from the class) of the reference target shall be rendered with the xref.
    """

    # ShowResourceTypeEnum method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.54, p.324
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on Xref.showResourceType (SHOW-RESOURCE-TYPE attribute)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # The type of the target is not rendered at the place of the reference. Tags: atp.EnumerationLiteralIndex=0
    NO_SHOW_TYPE = "NO-SHOW-TYPE"

    # The type of the target is rendered at the place of the reference. Tags: atp.EnumerationLiteralIndex=1
    SHOW_TYPE = "SHOW-TYPE"

    def __init__(self):
        super().__init__((ShowResourceTypeEnum.NO_SHOW_TYPE, ShowResourceTypeEnum.SHOW_TYPE))


class ShowSeeEnum(AREnum):
    """
    This enumerator specifies if the word "see" shall be rendered before the xref.
    """

    # ShowSeeEnum method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.55, p.325
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on Xref.showSee (SHOW-SEE attribute)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # The word "see" is not rendered before the reference. Tags: atp.EnumerationLiteralIndex=0
    NO_SHOW_SEE = "NO-SHOW-SEE"

    # The word "see"is rendered before the reference. Tags: atp.EnumerationLiteralIndex=1
    SHOW_SEE = "SHOW-SEE"

    def __init__(self):
        super().__init__((ShowSeeEnum.NO_SHOW_SEE, ShowSeeEnum.SHOW_SEE))
