"""
AUTOSAR Package - InlineAttributeEnums

Package: M2::MSR::Documentation::TextModel::InlineAttributeEnums
"""

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    ARLiteral,
)


class EEnumFont(AREnum):
    """
    EEnumFont enumeration

This specifies the possible kind of fonts to be used for emphasis. Aggregated by EmphasisText.font

Package: M2::MSR::Documentation::TextModel::InlineAttributeEnums
    """
    # The emphasis uses the default font.
    default = "0"

    # The emphasis uses a monospaced font.
    mono = "1"



class EEnum(AREnum):
    """
    EEnum enumeration

This specifies the possible kinds of emphasis as proposal how to render it on paper or screen. Note that it would have been better to use plain, weak (italic), strong (bold), veryStrong (bolditalic) ... But users complained about this. Aggregated by EmphasisText.type

Package: M2::MSR::Documentation::TextModel::InlineAttributeEnums
    """
    # The emphasis is preferably represented in boldface font.
    bold = "0"

    # The emphasis is preferably represented in boldface plus italic font.
    bolditalic = "1"

    # The emphasis is preferably represented in italic font.
    italic = "2"

    # The emphasis has no specific rendering. It is used if e.g. semantic information is applied to the emphasis text.
    plain = "3"



class ResolutionPolicyEnum(AREnum):
    """
    ResolutionPolicyEnum enumeration

This specifies if the content of the xref element follow a dedicated resolution policy. Aggregated by Xref.resolutionPolicy

Package: M2::MSR::Documentation::TextModel::InlineAttributeEnums
    """
    # The content of the xref element is not linked by a sloppy reference.
    noSloppy = "0"

    # The content of the xref element is linked by a sloppy reference.
    sloppy = "1"



class ShowContentEnum(AREnum):
    """
    ShowContentEnum enumeration

This specifies if the content of the xref element shall be rendered. Aggregated by Xref.showContent (cid:53) 322 of 535 Document ID 202: AUTOSAR_FO_TPS_GenericStructureTemplate Generic Structure Template AUTOSAR FO R23-11 (cid:52)

Package: M2::MSR::Documentation::TextModel::InlineAttributeEnums
    """
    # The content of the Xref.label is not rendered at the place of the reference.
    noShowContent = "0"

    # The content of the element is rendered at the place of the reference.
    showContent = "1"



class ShowResourceAliasNameEnum(AREnum):
    """
    ShowResourceAliasNameEnum enumeration

This enumerator specifies if the alias names of the reference target shall be rendered with the xref. Aggregated by Xref.showResourceAliasName

Package: M2::MSR::Documentation::TextModel::InlineAttributeEnums
    """
    # This indicates that alias names of the referenced object shall not be rendered at the place of the
    noShowAliasName = "0"

    # This indicates that the alias names of the referenced object shall be rendered at the place of the
    showAliasName = "1"



class ShowResourceCategoryEnum(AREnum):
    """
    ShowResourceCategoryEnum enumeration

This enumerator specifies if the category of the reference target shall be rendered with the xref. Aggregated by Xref.showResourceCategory

Package: M2::MSR::Documentation::TextModel::InlineAttributeEnums
    """
    # The category of the target is not rendered at the place of the reference.
    noShowCategory = "0"

    # The category of the target is rendered at the place of the reference.
    showCategory = "1"



class ShowResourceLongNameEnum(AREnum):
    """
    ShowResourceLongNameEnum enumeration

This enumerator specifies if the long name of the reference target shall be rendered with the xref. Aggregated by Xref.showResourceLongName

Package: M2::MSR::Documentation::TextModel::InlineAttributeEnums
    """
    # The long name of the target is not rendered at the place of the reference.
    noShowLongName = "0"

    # The long name of the target is rendered at the place of the reference.
    showLongName = "1"



class ShowResourceNumberEnum(AREnum):
    """
    ShowResourceNumberEnum enumeration

This enumerator specifies if the number (e.g. chapter number) of the reference target shall be rendered with the xref. Aggregated by Xref.showResourceNumber

Package: M2::MSR::Documentation::TextModel::InlineAttributeEnums
    """
    # The number of the target is not rendered at the place of the reference.
    noShowNumber = "0"

    # The number of the target is rendered at the place of the reference.
    showNumber = "1"



class ShowResourcePageEnum(AREnum):
    """
    ShowResourcePageEnum enumeration

This enumerator specifies if the page number of the reference target shall be rendered with the xref. Aggregated by Xref.showResourcePage

Package: M2::MSR::Documentation::TextModel::InlineAttributeEnums
    """
    # The page number of the target is not rendered at the place of the reference.
    noShowPage = "0"

    # The page number of the target is rendered at the place of the reference.
    showPage = "1"



class ShowResourceShortNameEnum(AREnum):
    """
    ShowResourceShortNameEnum enumeration

This enumerator specifies if the short name of the reference target shall be rendered with the xref. Aggregated by Xref.showResourceShortName

Package: M2::MSR::Documentation::TextModel::InlineAttributeEnums
    """
    # The short name of the target is not rendered at the place of the reference.
    noShowShortName = "0"

    # The short name of the target is rendered at the place of the reference.
    showShortName = "1"



class ShowResourceTypeEnum(AREnum):
    """
    ShowResourceTypeEnum enumeration

This enumerator specifies if the type (e.g. derived from the class) of the reference target shall be rendered with the xref. Aggregated by Xref.showResourceType

Package: M2::MSR::Documentation::TextModel::InlineAttributeEnums
    """
    # The type of the target is not rendered at the place of the reference.
    noShowType = "0"

    # The type of the target is rendered at the place of the reference.
    showType = "1"



class ShowSeeEnum(AREnum):
    """
    ShowSeeEnum enumeration

This enumerator specifies if the word "see" shall be rendered before the xref. Aggregated by Xref.showSee

Package: M2::MSR::Documentation::TextModel::InlineAttributeEnums
    """
    # The word "see" is not rendered before the reference.
    noShowSee = "0"

    # The word "see"is rendered before the reference.
    showSee = "1"



class ExtIdClassEnum(ARLiteral):
    """
    ExtIdClassEnum primitive type

This is in fact an enumerator. The possible values are all legal XML names of identifiable objects even those of other XML files. If the schemas of all questionable files are generated from a common meta-model, this is something like an IdentifiableSubtypesEnum. Maybe a future version of the Schema generator can generate such an enum. As of now it is specified as string. Tags: xml.xsd.customType=EXT-ID-CLASS-ENUM xml.xsd.type=string Table 9.35: ExtIdClassEnum

Package: M2::MSR::Documentation::TextModel::InlineAttributeEnums
    """
    pass


