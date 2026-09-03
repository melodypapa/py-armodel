"""
This module contains abstract structure classes for AUTOSAR models
in the GenericStructure module.
"""

from abc import ABC
from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class AtpInstanceRef(ARObject, ABC):
    """
    An M0 instance of a classifier may be represented as a tree rooted at that instance, where under each node come the sub-trees representing the instances which act as features under that node. An instance ref specifies a navigation path from any M0 tree-instance of the base (which is a classifier) to a leaf (which is an instance of the target).
    """

    # AtpInstanceRef method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 5.3, p.174
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getAtpBaseRef             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAtpBaseRef             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getAtpContextElementRefs  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addAtpContextElementRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getAtpTargetRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAtpTargetRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        if type(self) is AtpInstanceRef:
            raise TypeError("AtpInstanceRef is an abstract class.")

        super().__init__()

        # This is the base from which the navigaion path starts. Stereotypes: atpAbstract; atpDerived
        self.atpBaseRef: Optional[RefType] = None

        # This is one particular step in the navigation path. Stereotypes: atpAbstract
        self.atpContextElementRefs: List[RefType] = []

        # This is the target of the instance ref. In other words it is the terminal of the navigation path. Stereotypes: atpAbstract
        self.atpTargetRef: Optional[RefType] = None

    def getAtpBaseRef(self) -> Optional[RefType]:
        """
        This is the base from which the navigaion path starts. Stereotypes: atpAbstract; atpDerived
        """
        return self.atpBaseRef

    def setAtpBaseRef(self, value: Optional[RefType]) -> "AtpInstanceRef":
        """
        This is the base from which the navigaion path starts. Stereotypes: atpAbstract; atpDerived
        A None value is a no-op and does not overwrite an existing atpBaseRef.
        """
        if value is not None:
            self.atpBaseRef = value
        return self

    def getAtpContextElementRefs(self) -> List[RefType]:
        """
        This is one particular step in the navigation path. Stereotypes: atpAbstract
        """
        return self.atpContextElementRefs

    def addAtpContextElementRef(self, value: Optional[RefType]) -> "AtpInstanceRef":
        """
        This is one particular step in the navigation path. Stereotypes: atpAbstract
        """
        if value is not None:
            self.atpContextElementRefs.append(value)
        return self

    def getAtpTargetRef(self) -> Optional[RefType]:
        """
        This is the target of the instance ref. In other words it is the terminal of the navigation path. Stereotypes: atpAbstract
        """
        return self.atpTargetRef

    def setAtpTargetRef(self, value: Optional[RefType]) -> "AtpInstanceRef":
        """
        This is the target of the instance ref. In other words it is the terminal of the navigation path. Stereotypes: atpAbstract
        A None value is a no-op and does not overwrite an existing atpTargetRef.
        """
        if value is not None:
            self.atpTargetRef = value
        return self


class AtpFeature(Identifiable, ABC):
    """
    Features are properties via which a classifier classifies instances. Or: a classifier has features and every M0 instance of it will have those features.
    """

    # AtpFeature method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 5.2, p.174
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AtpFeature:
            raise TypeError("AtpFeature is an abstract class.")
        super().__init__(parent, short_name)


class AtpClassifier(Identifiable, ABC):
    """
    A classifier classifies M0 instances according to their features. Or: a classifier is something that has instances - an M1 classifier has M0 instances.
    """

    # AtpClassifier method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 5.1, p.173
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getAtpFeatures               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addAtpFeature                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AtpClassifier:
            raise TypeError("AtpClassifier is an abstract class.")
        super().__init__(parent, short_name)

        # This is a feature of the classifier. Stereotypes: atpDerived
        self.atpFeatures: List[AtpFeature] = []

    def getAtpFeatures(self) -> List[AtpFeature]:
        """
        This is a feature of the classifier. Stereotypes: atpDerived
        """
        return self.atpFeatures

    def addAtpFeature(self, value: Optional[AtpFeature]) -> "AtpClassifier":
        """
        This is a feature of the classifier. Stereotypes: atpDerived
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.atpFeatures.append(value)
        return self


class AtpType(AtpClassifier, ABC):
    """A type is a classifier that may serve to type prototypes. It is a reusable classifier."""

    # AtpType method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 5.6, p.175
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AtpType:
            raise TypeError("AtpType is an abstract class.")
        super().__init__(parent, short_name)


class AtpPrototype(AtpFeature, ABC):
    """A prototype is a typed feature. A prototype in a classifier indicates that instances of that classifier will have a feature, and the structure of that feature is given by the its type. An instance of that type will play the role indicated by the feature in the owning classifier. A feature is not an instance but an indication of an instance-to-be."""

    # AtpPrototype method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 5.4, p.175
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAtpTypeRef               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setAtpTypeRef               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AtpPrototype:
            raise TypeError("AtpPrototype is an abstract class.")
        super().__init__(parent, short_name)

        # This is the type of the feature.
        self.atpTypeRef: Optional[RefType] = None

    def getAtpTypeRef(self) -> Optional[RefType]:
        """
        This is the type of the feature.
        """
        return self.atpTypeRef

    def setAtpTypeRef(self, value: Optional[RefType]) -> "AtpPrototype":
        """
        This is the type of the feature.
        A None value is a no-op and does not overwrite an existing atpTypeRef.
        """
        if value is not None:
            self.atpTypeRef = value
        return self


class AtpStructureElement(AtpClassifier, AtpFeature, ABC):
    """A structure element is both a classifier and a feature. As a feature, its structure is given by the feature it owns as a classifier."""

    # AtpStructureElement method parity checklist:
    # Spec: R23-11/AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 5.5, p.175 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    #
    # Table 5.5 lists no Attribute rows; the XSD group ATP-STRUCTURE-ELEMENT is an
    # empty <xsd:sequence/>, so the class reduces to __init__ alone (inherited
    # atpFeatures lives in the AtpClassifier checklist, Table 5.1).
    # Heritage: Base closure = ARObject, AtpClassifier, AtpFeature, Identifiable,
    # MultilanguageReferrable, Referrable. AtpClassifier (Table 5.1) and AtpFeature
    # (Table 5.2) are parallel branches off Identifiable, so both are direct bases;
    # AtpBlueprintable is NOT in the closure.

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AtpStructureElement:
            raise TypeError("AtpStructureElement is an abstract class.")

        super().__init__(parent, short_name)
