from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    AbstractMultiplicityRestriction,
    ARObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ModelRestrictionTypes import (
    AbstractValueRestriction,
    AbstractVariationRestriction,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    NameToken,
    RefType,
)


class SdgElementWithGid(ARObject, ABC):
    """
    A special data group element with gid is an abstract element that shall have a name (gid, "Generic Identifier").
    """

    # SdgElementWithGid method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.25, p.99
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] getGid    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setGid    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    # Class-level default — the ONLY initialization (VariationPointCapable mixin
    # pattern): the repo's Referrable.__init__ calls ARObject.__init__ directly
    # (bypassing super()), so a mixin __init__ may never run under combined
    # inheritance — this mixin has no __init__ at all.
    # Specifies the name that identifies the element.
    gid: Optional[NameToken] = None

    def getGid(self) -> Optional[NameToken]:
        """
        Specifies the name that identifies the element.

        Returns:
            The gid, or None if not set
        """
        return self.gid

    def setGid(self, value: Optional[NameToken]):
        """
        Specifies the name that identifies the element.

        Args:
            value: The gid to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.gid = value
        return self


class SdgAttribute(Identifiable, AbstractMultiplicityRestriction, ABC):
    """
    Describes the attributes of an Sdg.
    """

    # SdgAttribute method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.27, p.100
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent, short_name: str):
        if type(self) is SdgAttribute:
            raise TypeError("SdgAttribute is an abstract class.")

        super().__init__(parent, short_name)


class SdgClass(SdgElementWithGid, Identifiable):
    """
    An SdgClass specifies the name and structure of the SDG that may be used to store proprietary data in an AUTOSAR model. The SdgClass is similar to an UML stereotype.
    """

    # SdgClass method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.26, p.100
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] addAttribute          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAttributes         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getCaption            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCaption            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getExtendsMetaClass   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setExtendsMetaClass   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addSdgConstraintRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSdgConstraintRefs  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        # Defintion of the structure of the Sdg Tags: xml.sequenceOffset=30
        self.attributes: List[SdgAttribute] = []

        # Specifies if a caption is required. Note: only Sdgs that have a caption can be referenced Tags: xml.sequenceOffset=20
        self.caption: Optional[Boolean] = None

        # The AUTOSAR Meta-Class that may be extended by this SdgClass. Tags: xml.sequenceOffset=10
        self.extendsMetaClass: Optional[str] = None

        # Semantic constraints that restrict the structure of the special data group. Tags: xml.sequenceOffset=40
        self.sdgConstraintRefs: List[RefType] = []

    def addAttribute(self, value: SdgAttribute):
        """
        Defintion of the structure of the Sdg Tags: xml.sequenceOffset=30

        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.attributes.append(value)
        return self

    def getAttributes(self) -> List[SdgAttribute]:
        """
        Defintion of the structure of the Sdg Tags: xml.sequenceOffset=30

        Returns:
            The list of Sdg attributes
        """
        return self.attributes

    def getCaption(self) -> Optional[Boolean]:
        """
        Specifies if a caption is required. Note: only Sdgs that have a caption can be referenced Tags: xml.sequenceOffset=20

        Returns:
            The caption flag, or None if not set
        """
        return self.caption

    def setCaption(self, value: Optional[Boolean]):
        """
        Specifies if a caption is required. Note: only Sdgs that have a caption can be referenced Tags: xml.sequenceOffset=20

        A None value is a no-op and does not overwrite an existing caption.
        """
        if value is not None:
            self.caption = value
        return self

    def getExtendsMetaClass(self) -> Optional[str]:
        """
        The AUTOSAR Meta-Class that may be extended by this SdgClass. Tags: xml.sequenceOffset=10

        Returns:
            The extended meta-class name, or None if not set
        """
        return self.extendsMetaClass

    def setExtendsMetaClass(self, value: Optional[str]):
        """
        The AUTOSAR Meta-Class that may be extended by this SdgClass. Tags: xml.sequenceOffset=10

        A None value is a no-op and does not overwrite an existing extendsMetaClass.
        """
        if value is not None:
            self.extendsMetaClass = value
        return self

    def addSdgConstraintRef(self, value: RefType):
        """
        Semantic constraints that restrict the structure of the special data group. Tags: xml.sequenceOffset=40

        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.sdgConstraintRefs.append(value)
        return self

    def getSdgConstraintRefs(self) -> List[RefType]:
        """
        Semantic constraints that restrict the structure of the special data group. Tags: xml.sequenceOffset=40

        Returns:
            The list of Sdg constraint references
        """
        return self.sdgConstraintRefs


class SdgAbstractPrimitiveAttribute(SdgElementWithGid, SdgAttribute, AbstractValueRestriction, ABC):
    """
    Describes primitive attributes of a special data group.
    """

    # SdgAbstractPrimitiveAttribute method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.28, p.100
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self, parent, short_name: str):
        if type(self) is SdgAbstractPrimitiveAttribute:
            raise TypeError("SdgAbstractPrimitiveAttribute is an abstract class.")

        super().__init__(parent, short_name)


class SdgPrimitiveAttribute(SdgAbstractPrimitiveAttribute):
    """
    Describes primitive special data attributes without variation. This class accepts a special data "sd" attribute.
    """

    # SdgPrimitiveAttribute method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.29, p.101
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)


class SdgPrimitiveAttributeWithVariation(SdgAbstractPrimitiveAttribute, AbstractVariationRestriction):
    """
    Describes a primitive numerical special data attribute with variation. This class accepts a special data "sdf" element.
    """

    # SdgPrimitiveAttributeWithVariation method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.30, p.101
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)


class SdgAggregationWithVariation(SdgElementWithGid, SdgAttribute, AbstractVariationRestriction):
    """
    Describes that the Sdg may contain another Sdg. The gid of the nested Sdg is defined by subSdg. Represents 'sdg'.
    """

    # SdgAggregationWithVariation method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.31, p.101
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getSubSdgRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSubSdgRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        # Supported sub Sdg Class
        self.subSdgRef: Optional[RefType] = None

    def getSubSdgRef(self) -> Optional[RefType]:
        """
        Supported sub Sdg Class

        Returns:
            The sub Sdg class reference, or None if not set
        """
        return self.subSdgRef

    def setSubSdgRef(self, value: Optional[RefType]):
        """
        Supported sub Sdg Class

        Args:
            value: The sub Sdg class reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.subSdgRef = value
        return self


class SdgReference(SdgAttribute):
    """
    Describes an attribute of a SdgClass which is used on the definition side to model a reference from one Sdg to another Sdg on the value side.
    """

    # SdgReference method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.32, p.101
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getDestSdgRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDestSdgRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        # Refers to a SdgClass which is used on the definition side to model the destination type of the referenced Sdg. On the value side the reference is realized by means of the originating Sdg defining an sdgx attribute which refers to the sdgCaption of the referenced Sdg.
        self.destSdgRef: Optional[RefType] = None

    def getDestSdgRef(self) -> Optional[RefType]:
        """
        Refers to a SdgClass which is used on the definition side to model the destination type of the referenced Sdg. On the value side the reference is realized by means of the originating Sdg defining an sdgx attribute which refers to the sdgCaption of the referenced Sdg.

        Returns:
            The destination Sdg class reference, or None if not set
        """
        return self.destSdgRef

    def setDestSdgRef(self, value: Optional[RefType]):
        """
        Refers to a SdgClass which is used on the definition side to model the destination type of the referenced Sdg. On the value side the reference is realized by means of the originating Sdg defining an sdgx attribute which refers to the sdgCaption of the referenced Sdg.

        Args:
            value: The destination Sdg class reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.destSdgRef = value
        return self


class SdgAbstractForeignReference(SdgElementWithGid, SdgAttribute, ABC):
    """
    An abstract reference that can point to any referrable object in an AUTOSAR Model.
    """

    # SdgAbstractForeignReference method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.33, p.102
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getDestMetaClass  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDestMetaClass  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent, short_name: str):
        if type(self) is SdgAbstractForeignReference:
            raise TypeError("SdgAbstractForeignReference is an abstract class.")

        super().__init__(parent, short_name)

        # specifies the destination meta-class of the reference.
        self.destMetaClass: Optional[str] = None

    def getDestMetaClass(self) -> Optional[str]:
        """
        specifies the destination meta-class of the reference.

        Returns:
            The destination meta-class name, or None if not set
        """
        return self.destMetaClass

    def setDestMetaClass(self, value: Optional[str]):
        """
        specifies the destination meta-class of the reference.

        Args:
            value: The destination meta-class name to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.destMetaClass = value
        return self


class SdgForeignReference(SdgAbstractForeignReference):
    """
    A reference without variation support that can point to any referrable object in an AUTOSAR Model. This class accepts the special data "Sdx" reference.
    """

    # SdgForeignReference method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.34, p.102
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)


class SdgForeignReferenceWithVariation(SdgAbstractForeignReference, AbstractVariationRestriction):
    """
    A reference with variation support that can point to any referrable object in an AUTOSAR Model. This class accepts the special data "Sdxf" reference.
    """

    # SdgForeignReferenceWithVariation method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.35, p.102
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)


class SdgDef(ARElement):
    """
    A SdgDef groups several SdgClasses which belong to the same extension. The concept of an SdgDef is similiar to an UML Profile. Tags: atp.recommendedPackage=SdgDefs
    """

    # SdgDef method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.24, p.99
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addSdgClass     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSdgClasses   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        # The owned sdgClasses which define the structure of the Sdgs Tags: xml.namePlural=SDG-CLASSES
        self.sdgClasses: List[SdgClass] = []

    def addSdgClass(self, value: SdgClass):
        """
        The owned sdgClasses which define the structure of the Sdgs Tags: xml.namePlural=SDG-CLASSES

        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.sdgClasses.append(value)
        return self

    def getSdgClasses(self) -> List[SdgClass]:
        """
        The owned sdgClasses which define the structure of the Sdgs Tags: xml.namePlural=SDG-CLASSES

        Returns:
            The list of owned Sdg classes
        """
        return self.sdgClasses
