from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken, Numerical, RefType, VerbatimStringPlain
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import MultilanguageReferrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Enumerations import XmlSpaceEnum
from typing import List, Optional


class Sd(ARObject):
    """
    This class represents a primitive element in a special data group.
    """

    # Sd method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.22, p.91
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getGID       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setGID       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getValue     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setValue     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getXmlSpace  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setXmlSpace  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This attributes specifies an identifier. Gid comes from the SGML/XML-Term "Generic Identifier" which is the element name in XML. The role of this attribute is the same as the name of an XML - element.
        self.gid: Optional[NameToken] = None

        # This is the value of the special data.
        self.value: Optional[VerbatimStringPlain] = None

        # This attribute is used to signal an intention that in that element, white space should be preserved by applications. It is defined according to xml:space as declared by W3C.
        self.xmlSpace: Optional[XmlSpaceEnum] = None

    def getGID(self) -> Optional[NameToken]:
        """
        This attributes specifies an identifier. Gid comes from the SGML/XML-Term "Generic Identifier" which is the element name in XML. The role of this attribute is the same as the name of an XML - element.
        """
        return self.gid

    def setGID(self, value: Optional[NameToken]) -> "Sd":
        """
        This attributes specifies an identifier. Gid comes from the SGML/XML-Term "Generic Identifier" which is the element name in XML. The role of this attribute is the same as the name of an XML - element. A None value is a no-op and does not overwrite an existing gid.
        """
        if value is not None:
            self.gid = value
        return self

    def getValue(self) -> Optional[VerbatimStringPlain]:
        """
        This is the value of the special data.
        """
        return self.value

    def setValue(self, value: Optional[VerbatimStringPlain]) -> "Sd":
        """
        This is the value of the special data. A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.value = value
        return self

    def getXmlSpace(self) -> Optional[XmlSpaceEnum]:
        """
        This attribute is used to signal an intention that in that element, white space should be preserved by applications. It is defined according to xml:space as declared by W3C.
        """
        return self.xmlSpace

    def setXmlSpace(self, value: Optional[XmlSpaceEnum]) -> "Sd":
        """
        This attribute is used to signal an intention that in that element, white space should be preserved by applications. It is defined according to xml:space as declared by W3C. A None value is a no-op and does not overwrite an existing xmlSpace.
        """
        if value is not None:
            self.xmlSpace = value
        return self


class SdgCaption(MultilanguageReferrable):
    """
    This meta-class represents the caption of a special data group. This allows to have some parts of special data as identifiable.
    """

    # SdgCaption method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.21, p.91
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDesc      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDesc      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # This represents a general but brief (one paragraph) description what the special data in question is about. It is only one paragraph! Desc is intended to be collected into overview tables. This property helps a human reader to identify the special data in question.
        self.desc: Optional[MultiLanguageOverviewParagraph] = None

    def getDesc(self) -> Optional[MultiLanguageOverviewParagraph]:
        """
        This represents a general but brief (one paragraph) description what the special data in question is about. It is only one paragraph! Desc is intended to be collected into overview tables. This property helps a human reader to identify the special data in question.
        """
        return self.desc

    def setDesc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "SdgCaption":
        """
        This represents a general but brief (one paragraph) description what the special data in question is about. It is only one paragraph! Desc is intended to be collected into overview tables. This property helps a human reader to identify the special data in question. A None value is a no-op and does not overwrite an existing desc.
        """
        if value is not None:
            self.desc = value
        return self


class Sdf(ARObject):
    """
    This class represents a numerical value in a special data group which may be subject to variability.
    """

    # Sdf method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.23, p.92
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getGID       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setGID       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getValue     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setValue     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This attributes specifies an identifier. Gid comes from the SGML/XML-Term "Generic Identifier" which is the element name in XML. The role of this attribute is the same as the name of an XML - element.
        self.gid: Optional[NameToken] = None

        # This is the value of the special data.
        self.value: Optional[Numerical] = None

    def getGID(self) -> Optional[NameToken]:
        """
        This attributes specifies an identifier. Gid comes from the SGML/XML-Term "Generic Identifier" which is the element name in XML. The role of this attribute is the same as the name of an XML - element.
        """
        return self.gid

    def setGID(self, value: Optional[NameToken]) -> "Sdf":
        """
        This attributes specifies an identifier. Gid comes from the SGML/XML-Term "Generic Identifier" which is the element name in XML. The role of this attribute is the same as the name of an XML - element. A None value is a no-op and does not overwrite an existing gid.
        """
        if value is not None:
            self.gid = value
        return self

    def getValue(self) -> Optional[Numerical]:
        """
        This is the value of the special data.
        """
        return self.value

    def setValue(self, value: Optional[Numerical]) -> "Sdf":
        """
        This is the value of the special data. A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.value = value
        return self


class SdgContents(ARObject):
    """
    This meta-class represents the possible contents of a special data group. It can be an arbitrary mix of references, of primitive special data and nested special data groups.
    """

    # SdgContents method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.20, p.91
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addSd        [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getSds       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addSdf       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getSdfs      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addSdg       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getSdgs      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addSdxRef    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getSdxRefs   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addSdxfRef   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getSdxfRefs  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self):
        super().__init__()

        # This is one particular special data element.
        self.sd: List[Sd] = []

        # This is one particular special data element.
        self.sdf: List[Sdf] = []

        # This aggregation allows to express nested special data groups. By this, any structure can be represented in SpeicalData.
        self.sdg: List["Sdg"] = []

        # Reference to any identifiable element. This allows to use Sdg even to establish arbitrary relationships.
        self.sdxRefs: List[RefType] = []

        # Additional reference with variant support.
        self.sdxfRefs: List[RefType] = []

    def addSd(self, sd: Optional[Sd]) -> "SdgContents":
        """
        This is one particular special data element. A None value is a no-op and is not appended.
        """
        if sd is not None:
            self.sd.append(sd)
        return self

    def getSds(self) -> List[Sd]:
        """
        This is one particular special data element.
        """
        return self.sd

    def addSdf(self, sdf: Optional[Sdf]) -> "SdgContents":
        """
        This is one particular special data element. A None value is a no-op and is not appended.
        """
        if sdf is not None:
            self.sdf.append(sdf)
        return self

    def getSdfs(self) -> List[Sdf]:
        """
        This is one particular special data element.
        """
        return self.sdf

    def addSdg(self, sdg: Optional["Sdg"]) -> "SdgContents":
        """
        This aggregation allows to express nested special data groups. By this, any structure can be represented in SpeicalData. A None value is a no-op and is not appended.
        """
        if sdg is not None:
            self.sdg.append(sdg)
        return self

    def getSdgs(self) -> List["Sdg"]:
        """
        This aggregation allows to express nested special data groups. By this, any structure can be represented in SpeicalData.
        """
        return self.sdg

    def addSdxRef(self, value: Optional[RefType]) -> "SdgContents":
        """
        Reference to any identifiable element. This allows to use Sdg even to establish arbitrary relationships. A None value is a no-op and is not appended.
        """
        if value is not None:
            self.sdxRefs.append(value)
        return self

    def getSdxRefs(self) -> List[RefType]:
        """
        Reference to any identifiable element. This allows to use Sdg even to establish arbitrary relationships.
        """
        return self.sdxRefs

    def addSdxfRef(self, value: Optional[RefType]) -> "SdgContents":
        """
        Additional reference with variant support. A None value is a no-op and is not appended.
        """
        if value is not None:
            self.sdxfRefs.append(value)
        return self

    def getSdxfRefs(self) -> List[RefType]:
        """
        Additional reference with variant support.
        """
        return self.sdxfRefs


class Sdg(ARObject, VariationPointCapable):
    """
    Sdg (SpecialDataGroup) is a generic model which can be used to keep arbitrary information which is not explicitly modeled in the meta-model. Sdg can have various contents as defined by sdgContentsType. Special Data should only be used moderately since all elements should be defined in the meta-model. Thereby SDG should be considered as a temporary solution when no explicit model is available. If an sdg Caption is available, it is possible to establish a reference to the sdg structure.
    """

    # Sdg method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.19, p.90
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getGID              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setGID              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSdgCaption       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createSdgCaption    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSdgContentsType  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSdgContentsType  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This attributes specifies an identifier. Gid comes from the SGML/XML-Term "Generic Identifier" which is the element name in XML. The role of this attribute is the same as the name of an XML - element.
        self.gid: Optional[NameToken] = None

        # This aggregation allows to assign the properties of Identifiable to the sdg. By this, a shortName etc. can be assigned to the Sdg.
        self.sdgCaption: Optional[SdgCaption] = None

        # This is the content of the Sdg.
        self.sdgContentsType: Optional[SdgContents] = None

    def getGID(self) -> Optional[NameToken]:
        """
        This attributes specifies an identifier. Gid comes from the SGML/XML-Term "Generic Identifier" which is the element name in XML. The role of this attribute is the same as the name of an XML - element.
        """
        return self.gid

    def setGID(self, value: Optional[NameToken]) -> "Sdg":
        """
        This attributes specifies an identifier. Gid comes from the SGML/XML-Term "Generic Identifier" which is the element name in XML. The role of this attribute is the same as the name of an XML - element. A None value is a no-op and does not overwrite an existing gid.
        """
        if value is not None:
            self.gid = value
        return self

    def getSdgCaption(self) -> Optional[SdgCaption]:
        """
        This aggregation allows to assign the properties of Identifiable to the sdg. By this, a shortName etc. can be assigned to the Sdg.
        """
        return self.sdgCaption

    def createSdgCaption(self, short_name: str) -> SdgCaption:
        """
        This aggregation allows to assign the properties of Identifiable to the sdg. By this, a shortName etc. can be assigned to the Sdg.
        """
        caption = SdgCaption(self, short_name)
        self.sdgCaption = caption
        return caption

    def getSdgContentsType(self) -> Optional[SdgContents]:
        """
        This is the content of the Sdg.
        """
        return self.sdgContentsType

    def setSdgContentsType(self, value: Optional[SdgContents]) -> "Sdg":
        """
        This is the content of the Sdg. A None value is a no-op and does not overwrite an existing sdgContentsType.
        """
        if value is not None:
            self.sdgContentsType = value
        return self
