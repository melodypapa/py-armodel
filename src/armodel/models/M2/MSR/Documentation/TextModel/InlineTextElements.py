from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import SingleLanguageReferrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, DateTime, NameToken, RefType, String
from armodel.models.M2.MSR.Documentation.TextModel.InlineAttributeEnums import (
    ResolutionPolicyEnum,
    ShowContentEnum,
    ShowResourceAliasNameEnum,
    ShowResourceCategoryEnum,
    ShowResourceLongNameEnum,
    ShowResourceNumberEnum,
    ShowResourcePageEnum,
    ShowResourceShortNameEnum,
    ShowResourceTypeEnum,
    ShowSeeEnum,
)
from armodel.models.M2.MSR.Documentation.BlockElements import Url

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.TextModel.SingleLanguageData import SingleLanguageLongName


class Br(ARObject):
    """
    This element is the same as function here as in a HTML document i.e. it forces a line break.
    """

    # Br method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.33, p.316
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()


class Std(SingleLanguageReferrable):
    """
    This represents a reference to external standards.
    """

    # Std method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.37, p.318
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDate      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDate      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPosition  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPosition  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getState     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setState     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSubtitle  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSubtitle  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUrl       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUrl       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This element specifies the release date of the external standard if applicable. Tags: xml.sequenceOffset=50
        self.date: Optional[DateTime] = None

        # This represents the reference to the relevant positions of a standard. Kept as a string. Tags: xml.sequenceOffset=70
        self.position: Optional[String] = None

        # This represents version and state of a standard. Kept as a string. Tags: xml.sequenceOffset=40
        self.state: Optional[String] = None

        # This represents the subtitle of the standard. Tags: xml.sequenceOffset=30
        self.subtitle: Optional[String] = None

        # This represents the URL of the standard. Tags: xml.sequenceOffset=60
        self.url: Optional[Url] = None

    def getDate(self) -> Optional[DateTime]:
        """
        This element specifies the release date of the external standard if applicable. Tags: xml.sequenceOffset=50
        """
        return self.date

    def setDate(self, value: Optional[DateTime]) -> Std:
        """
        This element specifies the release date of the external standard if applicable. Tags: xml.sequenceOffset=50. A None value is a no-op and does not overwrite an existing date.
        """
        if value is not None:
            self.date = value
        return self

    def getPosition(self) -> Optional[String]:
        """
        This represents the reference to the relevant positions of a standard. Kept as a string. Tags: xml.sequenceOffset=70
        """
        return self.position

    def setPosition(self, value: Optional[String]) -> Std:
        """
        This represents the reference to the relevant positions of a standard. Kept as a string. Tags: xml.sequenceOffset=70. A None value is a no-op and does not overwrite an existing position.
        """
        if value is not None:
            self.position = value
        return self

    def getState(self) -> Optional[String]:
        """
        This represents version and state of a standard. Kept as a string. Tags: xml.sequenceOffset=40
        """
        return self.state

    def setState(self, value: Optional[String]) -> Std:
        """
        This represents version and state of a standard. Kept as a string. Tags: xml.sequenceOffset=40. A None value is a no-op and does not overwrite an existing state.
        """
        if value is not None:
            self.state = value
        return self

    def getSubtitle(self) -> Optional[String]:
        """
        This represents the subtitle of the standard. Tags: xml.sequenceOffset=30
        """
        return self.subtitle

    def setSubtitle(self, value: Optional[String]) -> Std:
        """
        This represents the subtitle of the standard. Tags: xml.sequenceOffset=30. A None value is a no-op and does not overwrite an existing subtitle.
        """
        if value is not None:
            self.subtitle = value
        return self

    def getUrl(self) -> Optional[Url]:
        """
        This represents the URL of the standard. Tags: xml.sequenceOffset=60
        """
        return self.url

    def setUrl(self, value: Optional[Url]) -> Std:
        """
        This represents the URL of the standard. Tags: xml.sequenceOffset=60. A None value is a no-op and does not overwrite an existing url.
        """
        if value is not None:
            self.url = value
        return self


class Xdoc(SingleLanguageReferrable):
    """
    This meta-class represents the ability to refer to an external document which can be rendered as printed matter.
    """

    # Xdoc method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.40, p.319
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDate      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDate      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNumber    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNumber    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPosition  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPosition  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPublisher [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPublisher [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getState     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setState     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUrl       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUrl       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This element specifies the release date of the external document if applicable. Tags: xml.sequenceOffset=50
        self.date: Optional[DateTime] = None

        # This represents document number of an external document that is referenced. Kept as a string. Tags: xml.sequenceOffset=30
        self.number: Optional[String] = None

        # This represents the reference to the relevant positions of a standard. Kept as a string. Tags: xml.sequenceOffset=80
        self.position: Optional[String] = None

        # This represents the publisher of an external document that is being referenced. Kept as a string. Tags: xml.sequenceOffset=60
        self.publisher: Optional[String] = None

        # This represents version and state of the external document. Kept as a string. Tags: xml.sequenceOffset=40
        self.state: Optional[String] = None

        # This specifies the URL of the external document. Tags: xml.sequenceOffset=70
        self.url: Optional[Url] = None

    def getDate(self) -> Optional[DateTime]:
        """This element specifies the release date of the external document if applicable. Tags: xml.sequenceOffset=50"""
        return self.date

    def setDate(self, value: Optional[DateTime]) -> Xdoc:
        """This element specifies the release date of the external document if applicable. Tags: xml.sequenceOffset=50. A None value is a no-op and does not overwrite an existing date."""
        if value is not None:
            self.date = value
        return self

    def getNumber(self) -> Optional[String]:
        """This represents document number of an external document that is referenced. Kept as a string. Tags: xml.sequenceOffset=30"""
        return self.number

    def setNumber(self, value: Optional[String]) -> Xdoc:
        """This represents document number of an external document that is referenced. Kept as a string. Tags: xml.sequenceOffset=30. A None value is a no-op and does not overwrite an existing number."""
        if value is not None:
            self.number = value
        return self

    def getPosition(self) -> Optional[String]:
        """This represents the reference to the relevant positions of a standard. Kept as a string. Tags: xml.sequenceOffset=80"""
        return self.position

    def setPosition(self, value: Optional[String]) -> Xdoc:
        """This represents the reference to the relevant positions of a standard. Kept as a string. Tags: xml.sequenceOffset=80. A None value is a no-op and does not overwrite an existing position."""
        if value is not None:
            self.position = value
        return self

    def getPublisher(self) -> Optional[String]:
        """This represents the publisher of an external document that is being referenced. Kept as a string. Tags: xml.sequenceOffset=60"""
        return self.publisher

    def setPublisher(self, value: Optional[String]) -> Xdoc:
        """This represents the publisher of an external document that is being referenced. Kept as a string. Tags: xml.sequenceOffset=60. A None value is a no-op and does not overwrite an existing publisher."""
        if value is not None:
            self.publisher = value
        return self

    def getState(self) -> Optional[String]:
        """This represents version and state of the external document. Kept as a string. Tags: xml.sequenceOffset=40"""
        return self.state

    def setState(self, value: Optional[String]) -> Xdoc:
        """This represents version and state of the external document. Kept as a string. Tags: xml.sequenceOffset=40. A None value is a no-op and does not overwrite an existing state."""
        if value is not None:
            self.state = value
        return self

    def getUrl(self) -> Optional[Url]:
        """This specifies the URL of the external document. Tags: xml.sequenceOffset=70"""
        return self.url

    def setUrl(self, value: Optional[Url]) -> Xdoc:
        """This specifies the URL of the external document. Tags: xml.sequenceOffset=70. A None value is a no-op and does not overwrite an existing url."""
        if value is not None:
            self.url = value
        return self


class Xfile(SingleLanguageReferrable):
    """
    This represents to reference an external file within a documentation.
    """

    # Xfile method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.41, p.320
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTool           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTool           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getToolVersion    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setToolVersion    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUrl            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUrl            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This element describes the tool which was used to generate the corresponding Xfile . Kept as a string since no specific syntax can be provided to denote a tool. Tags: xml.sequenceOffset=50
        self.tool: Optional[String] = None

        # This element describes the tool version which was used to generate the corresponding xfile. Kept as a string, since no specific syntax can be specified. Tags: xml.sequenceOffset=60
        self.toolVersion: Optional[String] = None

        # This represents the URL of the external file. Tags: xml.sequenceOffset=30
        self.url: Optional[Url] = None

    def getTool(self) -> Optional[String]:
        """This element describes the tool which was used to generate the corresponding Xfile . Kept as a string since no specific syntax can be provided to denote a tool. Tags: xml.sequenceOffset=50"""
        return self.tool

    def setTool(self, value: Optional[String]) -> Xfile:
        """This element describes the tool which was used to generate the corresponding Xfile . Kept as a string since no specific syntax can be provided to denote a tool. Tags: xml.sequenceOffset=50. A None value is a no-op and does not overwrite an existing tool."""
        if value is not None:
            self.tool = value
        return self

    def getToolVersion(self) -> Optional[String]:
        """This element describes the tool version which was used to generate the corresponding xfile. Kept as a string, since no specific syntax can be specified. Tags: xml.sequenceOffset=60"""
        return self.toolVersion

    def setToolVersion(self, value: Optional[String]) -> Xfile:
        """This element describes the tool version which was used to generate the corresponding xfile. Kept as a string, since no specific syntax can be specified. Tags: xml.sequenceOffset=60. A None value is a no-op and does not overwrite an existing toolVersion."""
        if value is not None:
            self.toolVersion = value
        return self

    def getUrl(self) -> Optional[Url]:
        """This represents the URL of the external file. Tags: xml.sequenceOffset=30"""
        return self.url

    def setUrl(self, value: Optional[Url]) -> Xfile:
        """This represents the URL of the external file. Tags: xml.sequenceOffset=30. A None value is a no-op and does not overwrite an existing url."""
        if value is not None:
            self.url = value
        return self


class XrefTarget(SingleLanguageReferrable):
    """
    This element specifies a reference target which can be scattered throughout the text.
    """

    # XrefTarget method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.43, p.321
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class Xref(ARObject):
    """
    This represents a cross-reference within documentation.
    """

    # Xref method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.42, p.321
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getLabel1  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setLabel1  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getReferrableRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setReferrableRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getResolutionPolicy  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setResolutionPolicy  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getShowContent  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setShowContent  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getShowResourceAliasName  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setShowResourceAliasName  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getShowResourceCategory  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setShowResourceCategory  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getShowResourceLongName  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setShowResourceLongName  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getShowResourceNumber  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setShowResourceNumber  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getShowResourcePage  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setShowResourcePage  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getShowResourceShortName  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setShowResourceShortName  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getShowResourceType  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setShowResourceType  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getShowSee  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setShowSee  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This allows to specify a replacement text which shall be rendered if showContent is selected.
        self.label1: Optional[SingleLanguageLongName] = None

        # This establishes the reference in Autosar style.
        self.referrableRef: Optional[RefType] = None

        # Indicates if the content of the xref element follow a dedicated resolution policy. The default is "NO-SLOPPY". Tags: xml.attribute=true
        self.resolutionPolicy: Optional[ResolutionPolicyEnum] = None

        # Indicates if the content of the xref element shall be rendered. The default is "NO-SHOW-CONTENT". Tags: xml.attribute=true
        self.showContent: Optional[ShowContentEnum] = None

        # This indicates if the alias names of the referenced objects shall be rendered. This means this is some kind of backward searching: look whether there is an alias for the referenced object, if yes, print it. If there is more than one AliasNameSet, Xref might render all of those. If no alias is found and showResourceShortName is set to NoShowShortName, then the shortName of the reference target shall be displayed. By this showResourceAliasName is similar to showResourceShortName but shows the aliasName instead of the shortName. Default is NO-SHOW-ALIAS-NAME. Tags: xml.attribute=true
        self.showResourceAliasName: Optional[ShowResourceAliasNameEnum] = None

        # Indicates if the category of the referenced resource shall be rendered. Default is "NO-SHOW-CATEGORY". Tags: xml.attribute=true
        self.showResourceCategory: Optional[ShowResourceCategoryEnum] = None

        # Indicates if the longName of the referenced resource shall be rendered. Default is "SHOW-LONG-NAME". Tags: xml.attribute=true
        self.showResourceLongName: Optional[ShowResourceLongNameEnum] = None

        # Indicates if the Number of the referenced resource shall be shown. Default is "SHOW-NUMBER" Tags: xml.attribute=true
        self.showResourceNumber: Optional[ShowResourceNumberEnum] = None

        # Indicates if the page number of the referenced resource shall be shown. Default is "SHOW-PAGE" Tags: xml.attribute=true
        self.showResourcePage: Optional[ShowResourcePageEnum] = None

        # Indicates if the shortJName of the referenced resource shall be shown. Default is "SHOW-SHORT-NAME" Tags: xml.attribute=true
        self.showResourceShortName: Optional[ShowResourceShortNameEnum] = None

        # Indicates if the type of the referenced Resource shall be shown. Default is "SHOW-TYPE" Tags: xml.attribute=true
        self.showResourceType: Optional[ShowResourceTypeEnum] = None

        # Indicates if the word "see " shall be shown before the reference. Default is "NO-SHOW-SEE". Note that this is there for compatibility reasons only. Tags: xml.attribute=true
        self.showSee: Optional[ShowSeeEnum] = None

    def getLabel1(self) -> Optional[SingleLanguageLongName]:
        """This allows to specify a replacement text which shall be rendered if showContent is selected."""
        return self.label1

    def setLabel1(self, value: Optional[SingleLanguageLongName]) -> Xref:
        """This allows to specify a replacement text which shall be rendered if showContent is selected. A None value is a no-op and does not overwrite an existing label1."""
        if value is not None:
            self.label1 = value
        return self

    def getReferrableRef(self) -> Optional[RefType]:
        """This establishes the reference in Autosar style."""
        return self.referrableRef

    def setReferrableRef(self, value: Optional[RefType]) -> Xref:
        """This establishes the reference in Autosar style. A None value is a no-op and does not overwrite an existing referrable."""
        if value is not None:
            self.referrableRef = value
        return self

    def getResolutionPolicy(self) -> Optional[ResolutionPolicyEnum]:
        """Indicates if the content of the xref element follow a dedicated resolution policy. The default is "NO-SLOPPY". Tags: xml.attribute=true"""
        return self.resolutionPolicy

    def setResolutionPolicy(self, value: Optional[ResolutionPolicyEnum]) -> Xref:
        """Indicates if the content of the xref element follow a dedicated resolution policy. The default is "NO-SLOPPY". Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing resolutionPolicy."""
        if value is not None:
            self.resolutionPolicy = value
        return self

    def getShowContent(self) -> Optional[ShowContentEnum]:
        """Indicates if the content of the xref element shall be rendered. The default is "NO-SHOW-CONTENT". Tags: xml.attribute=true"""
        return self.showContent

    def setShowContent(self, value: Optional[ShowContentEnum]) -> Xref:
        """Indicates if the content of the xref element shall be rendered. The default is "NO-SHOW-CONTENT". Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing showContent."""
        if value is not None:
            self.showContent = value
        return self

    def getShowResourceAliasName(self) -> Optional[ShowResourceAliasNameEnum]:
        """This indicates if the alias names of the referenced objects shall be rendered. This means this is some kind of backward searching: look whether there is an alias for the referenced object, if yes, print it. If there is more than one AliasNameSet, Xref might render all of those. If no alias is found and showResourceShortName is set to NoShowShortName, then the shortName of the reference target shall be displayed. By this showResourceAliasName is similar to showResourceShortName but shows the aliasName instead of the shortName. Default is NO-SHOW-ALIAS-NAME. Tags: xml.attribute=true"""
        return self.showResourceAliasName

    def setShowResourceAliasName(self, value: Optional[ShowResourceAliasNameEnum]) -> Xref:
        """This indicates if the alias names of the referenced objects shall be rendered. This means this is some kind of backward searching: look whether there is an alias for the referenced object, if yes, print it. If there is more than one AliasNameSet, Xref might render all of those. If no alias is found and showResourceShortName is set to NoShowShortName, then the shortName of the reference target shall be displayed. By this showResourceAliasName is similar to showResourceShortName but shows the aliasName instead of the shortName. Default is NO-SHOW-ALIAS-NAME. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing showResourceAliasName."""
        if value is not None:
            self.showResourceAliasName = value
        return self

    def getShowResourceCategory(self) -> Optional[ShowResourceCategoryEnum]:
        """Indicates if the category of the referenced resource shall be rendered. Default is "NO-SHOW-CATEGORY". Tags: xml.attribute=true"""
        return self.showResourceCategory

    def setShowResourceCategory(self, value: Optional[ShowResourceCategoryEnum]) -> Xref:
        """Indicates if the category of the referenced resource shall be rendered. Default is "NO-SHOW-CATEGORY". Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing showResourceCategory."""
        if value is not None:
            self.showResourceCategory = value
        return self

    def getShowResourceLongName(self) -> Optional[ShowResourceLongNameEnum]:
        """Indicates if the longName of the referenced resource shall be rendered. Default is "SHOW-LONG-NAME". Tags: xml.attribute=true"""
        return self.showResourceLongName

    def setShowResourceLongName(self, value: Optional[ShowResourceLongNameEnum]) -> Xref:
        """Indicates if the longName of the referenced resource shall be rendered. Default is "SHOW-LONG-NAME". Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing showResourceLongName."""
        if value is not None:
            self.showResourceLongName = value
        return self

    def getShowResourceNumber(self) -> Optional[ShowResourceNumberEnum]:
        """Indicates if the Number of the referenced resource shall be shown. Default is "SHOW-NUMBER" Tags: xml.attribute=true"""
        return self.showResourceNumber

    def setShowResourceNumber(self, value: Optional[ShowResourceNumberEnum]) -> Xref:
        """Indicates if the Number of the referenced resource shall be shown. Default is "SHOW-NUMBER" Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing showResourceNumber."""
        if value is not None:
            self.showResourceNumber = value
        return self

    def getShowResourcePage(self) -> Optional[ShowResourcePageEnum]:
        """Indicates if the page number of the referenced resource shall be shown. Default is "SHOW-PAGE" Tags: xml.attribute=true"""
        return self.showResourcePage

    def setShowResourcePage(self, value: Optional[ShowResourcePageEnum]) -> Xref:
        """Indicates if the page number of the referenced resource shall be shown. Default is "SHOW-PAGE" Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing showResourcePage."""
        if value is not None:
            self.showResourcePage = value
        return self

    def getShowResourceShortName(self) -> Optional[ShowResourceShortNameEnum]:
        """Indicates if the shortJName of the referenced resource shall be shown. Default is "SHOW-SHORT-NAME" Tags: xml.attribute=true"""
        return self.showResourceShortName

    def setShowResourceShortName(self, value: Optional[ShowResourceShortNameEnum]) -> Xref:
        """Indicates if the shortJName of the referenced resource shall be shown. Default is "SHOW-SHORT-NAME" Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing showResourceShortName."""
        if value is not None:
            self.showResourceShortName = value
        return self

    def getShowResourceType(self) -> Optional[ShowResourceTypeEnum]:
        """Indicates if the type of the referenced Resource shall be shown. Default is "SHOW-TYPE" Tags: xml.attribute=true"""
        return self.showResourceType

    def setShowResourceType(self, value: Optional[ShowResourceTypeEnum]) -> Xref:
        """Indicates if the type of the referenced Resource shall be shown. Default is "SHOW-TYPE" Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing showResourceType."""
        if value is not None:
            self.showResourceType = value
        return self

    def getShowSee(self) -> Optional[ShowSeeEnum]:
        """Indicates if the word "see " shall be shown before the reference. Default is "NO-SHOW-SEE". Note that this is there for compatibility reasons only. Tags: xml.attribute=true"""
        return self.showSee

    def setShowSee(self, value: Optional[ShowSeeEnum]) -> Xref:
        """Indicates if the word "see " shall be shown before the reference. Default is "NO-SHOW-SEE". Note that this is there for compatibility reasons only. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing showSee."""
        if value is not None:
            self.showSee = value
        return self


class Superscript(ARLiteral):
    """
    This is text which is rendered superscript or subscript depending on the role.
    """

    # Superscript method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.38, p.318
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        super().__init__()


class Tt(ARObject):
    """
    This meta-class represents the ability to express specific technical terms. The kind of term is denoted in the attribute "type".
    """

    # Tt method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.39, p.319
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getValue     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setValue     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTexRender [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTexRender [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getType      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setType      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This is the term itself.
        self.value: String = None

        # This attribute holds information how the content (represented by attribute "term") of the particular technical term is rendered using LaTeX. This allows to inject specific LaTeX commands such as \sep{}. An example is to render "MyClass" as "My\sep{}Class". Default is the value of the attribute "term".
        self.texRender: Optional[String] = None

        # This attribute specifies the type of the technical term. Values are such as "VARIABLE" "CALPRM". It is no longer an enum in order to support process specific extensions.
        self.type: Optional[NameToken] = None

    def getValue(self) -> String:
        """
        This is the term itself.

        Returns:
            The term itself
        """
        return self.value

    def setValue(self, value: String) -> Tt:
        """
        This is the term itself. A None value is a no-op and does not overwrite an existing value.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.value = value
        return self

    def getTexRender(self) -> Optional[String]:
        r"""
        This attribute holds information how the content (represented by attribute "term") of the particular technical term is rendered using LaTeX. This allows to inject specific LaTeX commands such as \sep{}. An example is to render "MyClass" as "My\sep{}Class". Default is the value of the attribute "term".

        Returns:
            The LaTeX rendering information
        """
        return self.texRender

    def setTexRender(self, value: Optional[String]) -> Tt:
        r"""
        This attribute holds information how the content (represented by attribute "term") of the particular technical term is rendered using LaTeX. This allows to inject specific LaTeX commands such as \sep{}. An example is to render "MyClass" as "My\sep{}Class". Default is the value of the attribute "term". A None value is a no-op and does not overwrite an existing texRender.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.texRender = value
        return self

    def getType(self) -> Optional[NameToken]:
        """
        This attribute specifies the type of the technical term. Values are such as "VARIABLE" "CALPRM". It is no longer an enum in order to support process specific extensions.

        Returns:
            The type of the technical term
        """
        return self.type

    def setType(self, value: Optional[NameToken]) -> Tt:
        """
        This attribute specifies the type of the technical term. Values are such as "VARIABLE" "CALPRM". It is no longer an enum in order to support process specific extensions. A None value is a no-op and does not overwrite an existing type.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.type = value
        return self


class IndexEntry(ARObject):
    """
    This class represents an index entry.
    """

    # IndexEntry method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.36, p.317
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getValue     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setValue     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSub       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSub       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSup       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSup       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # The text content of the index entry.
        self.value: String = None

        # This is subscript text.
        self.sub: Optional[Superscript] = None

        # This is superscript text.
        self.sup: Optional[Superscript] = None

    def getValue(self) -> String:
        """
        Gets the text content of the index entry.

        Returns:
            The text content of the index entry
        """
        return self.value

    def setValue(self, value: String) -> IndexEntry:
        """
        Sets the text content of the index entry. A None value is a no-op and does not overwrite an existing value.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.value = value
        return self

    def getSub(self) -> Optional[Superscript]:
        """
        This is subscript text.

        Returns:
            The subscript text
        """
        return self.sub

    def setSub(self, value: Optional[Superscript]) -> IndexEntry:
        """
        This is subscript text. A None value is a no-op and does not overwrite an existing sub.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.sub = value
        return self

    def getSup(self) -> Optional[Superscript]:
        """
        This is superscript text.

        Returns:
            The superscript text
        """
        return self.sup

    def setSup(self, value: Optional[Superscript]) -> IndexEntry:
        """
        This is superscript text. A None value is a no-op and does not overwrite an existing sup.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.sup = value
        return self


class EmphasisText(ARObject):
    """
    This is an emphasized text. As a compromise it contains some rendering oriented attributes such as color and font.
    """

    # EmphasisText method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.34, p.317
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getValue     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setValue     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getColor     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setColor     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getFont      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFont      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSub       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSub       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSup       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSup       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTt        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTt        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getType      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setType      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # The text content of the emphasized text.
        self.value: String = None

        # This allows to recommend a color of the emphasis. It is specified bases on 6 digits RGB hex-code.
        self.color: Optional[String] = None

        # This specifies the font style in which the emphasized text shall be rendered.
        self.font: Optional[ARLiteral] = None

        # this is subscript text
        self.sub: Optional[Superscript] = None

        # This is superscript text
        self.sup: Optional[Superscript] = None

        # This is a technical term.
        self.tt: Optional[Tt] = None

        # Indicates how the text may be emphasized. Note that this is only a proposal which can be overridden or ignored by particular formatting engines. Default is BOLD.
        self.type: Optional[ARLiteral] = None

    def getValue(self) -> String:
        """
        Gets the text content of the emphasized text.

        Returns:
            The text content of the emphasized text
        """
        return self.value

    def setValue(self, value: String) -> EmphasisText:
        """
        Sets the text content of the emphasized text. A None value is a no-op and does not overwrite an existing value.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.value = value
        return self

    def getColor(self) -> Optional[String]:
        """
        This allows to recommend a color of the emphasis. It is specified bases on 6 digits RGB hex-code.

        Returns:
            The recommended color of the emphasis
        """
        return self.color

    def setColor(self, value: Optional[String]) -> EmphasisText:
        """
        This allows to recommend a color of the emphasis. It is specified bases on 6 digits RGB hex-code. A None value is a no-op and does not overwrite an existing color.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.color = value
        return self

    def getFont(self) -> Optional[ARLiteral]:
        """
        This specifies the font style in which the emphasized text shall be rendered.

        Returns:
            The font style in which the emphasized text shall be rendered
        """
        return self.font

    def setFont(self, value: Optional[ARLiteral]) -> EmphasisText:
        """
        This specifies the font style in which the emphasized text shall be rendered. A None value is a no-op and does not overwrite an existing font.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.font = value
        return self

    def getSub(self) -> Optional[Superscript]:
        """
        this is subscript text

        Returns:
            The subscript text
        """
        return self.sub

    def setSub(self, value: Optional[Superscript]) -> EmphasisText:
        """
        this is subscript text. A None value is a no-op and does not overwrite an existing sub.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.sub = value
        return self

    def getSup(self) -> Optional[Superscript]:
        """
        This is superscript text

        Returns:
            The superscript text
        """
        return self.sup

    def setSup(self, value: Optional[Superscript]) -> EmphasisText:
        """
        This is superscript text. A None value is a no-op and does not overwrite an existing sup.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.sup = value
        return self

    def getTt(self) -> Optional[Tt]:
        """
        This is a technical term.

        Returns:
            The technical term
        """
        return self.tt

    def setTt(self, value: Optional[Tt]) -> EmphasisText:
        """
        This is a technical term. A None value is a no-op and does not overwrite an existing tt.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.tt = value
        return self

    def getType(self) -> Optional[ARLiteral]:
        """
        Indicates how the text may be emphasized. Note that this is only a proposal which can be overridden or ignored by particular formatting engines. Default is BOLD.

        Returns:
            How the text may be emphasized
        """
        return self.type

    def setType(self, value: Optional[ARLiteral]) -> EmphasisText:
        """
        Indicates how the text may be emphasized. Note that this is only a proposal which can be overridden or ignored by particular formatting engines. Default is BOLD. A None value is a no-op and does not overwrite an existing type.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.type = value
        return self
