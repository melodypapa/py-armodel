"""
AUTOSAR Package - AbstractStructure

Package: M2::AUTOSARTemplates::GenericStructure::AbstractStructure
"""

from abc import ABC
from typing import List

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class AtpInstanceRef(ARObject, ABC):
    """
    An M0 instance of a classifier may be represented as a tree rooted at that
    instance, where under each node come the sub-trees representing the
    instances which act as features under that node. An instance ref specifies a
    navigation path from any M0 tree-instance of the base (which is a
    classifier) to a leaf (which is an instance of the target).

    Package: M2::AUTOSARTemplates::GenericStructure::AbstractStructure::AtpInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 301, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 971, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2000, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 206, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 174, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is AtpInstanceRef:
            raise TypeError("AtpInstanceRef is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the base from which the navigaion path starts.
        # atpDerived.
        self._atpBase: "AtpClassifier" = None

    @property
    def atp_base(self) -> "AtpClassifier":
        """Get atpBase (Pythonic accessor)."""
        return self._atpBase

    @atp_base.setter
    def atp_base(self, value: "AtpClassifier") -> None:
        """
        Set atpBase with validation.

        Args:
            value: The atpBase to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, AtpClassifier):
            raise TypeError(
                f"atpBase must be AtpClassifier, got {type(value).__name__}"
            )
        self._atpBase = value
        # atpAbstract (ordered).
        self._atpContext: List["RefType"] = []

    @property
    def atp_context(self) -> List["RefType"]:
        """Get atpContext (Pythonic accessor)."""
        return self._atpContext
        # This is the target of the instance ref.
        # In other words it is of the navigation path.
        self._atpTarget: "AtpFeature" = None

    @property
    def atp_target(self) -> "AtpFeature":
        """Get atpTarget (Pythonic accessor)."""
        return self._atpTarget

    @atp_target.setter
    def atp_target(self, value: "AtpFeature") -> None:
        """
        Set atpTarget with validation.

        Args:
            value: The atpTarget to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, AtpFeature):
            raise TypeError(
                f"atpTarget must be AtpFeature, got {type(value).__name__}"
            )
        self._atpTarget = value

    def with_atp_context(self, value):
        """
        Set atp_context and return self for chaining.

        Args:
            value: The atp_context to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_atp_context("value")
        """
        self.atp_context = value  # Use property setter (gets validation)
        return self

    def with_atp_feature(self, value):
        """
        Set atp_feature and return self for chaining.

        Args:
            value: The atp_feature to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_atp_feature("value")
        """
        self.atp_feature = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAtpBase(self) -> "AtpClassifier":
        """
        AUTOSAR-compliant getter for atpBase.

        Returns:
            The atpBase value

        Note:
            Delegates to atp_base property (CODING_RULE_V2_00017)
        """
        return self.atp_base  # Delegates to property

    def setAtpBase(self, value: "AtpClassifier") -> "AtpInstanceRef":
        """
        AUTOSAR-compliant setter for atpBase with method chaining.

        Args:
            value: The atpBase to set

        Returns:
            self for method chaining

        Note:
            Delegates to atp_base property setter (gets validation automatically)
        """
        self.atp_base = value  # Delegates to property setter
        return self

    def getAtpContext(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for atpContext.

        Returns:
            The atpContext value

        Note:
            Delegates to atp_context property (CODING_RULE_V2_00017)
        """
        return self.atp_context  # Delegates to property

    def getAtpTarget(self) -> "AtpFeature":
        """
        AUTOSAR-compliant getter for atpTarget.

        Returns:
            The atpTarget value

        Note:
            Delegates to atp_target property (CODING_RULE_V2_00017)
        """
        return self.atp_target  # Delegates to property

    def setAtpTarget(self, value: "AtpFeature") -> "AtpInstanceRef":
        """
        AUTOSAR-compliant setter for atpTarget with method chaining.

        Args:
            value: The atpTarget to set

        Returns:
            self for method chaining

        Note:
            Delegates to atp_target property setter (gets validation automatically)
        """
        self.atp_target = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_atp_base(self, value: "AtpClassifier") -> "AtpInstanceRef":
        """
        Set atpBase and return self for chaining.

        Args:
            value: The atpBase to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_atp_base("value")
        """
        self.atp_base = value  # Use property setter (gets validation)
        return self

    def with_atp_target(self, value: "AtpFeature") -> "AtpInstanceRef":
        """
        Set atpTarget and return self for chaining.

        Args:
            value: The atpTarget to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_atp_target("value")
        """
        self.atp_target = value  # Use property setter (gets validation)
        return self



class AtpClassifier(Identifiable, ABC):
    """
    A classifier classifies M0 instances according to their features. Or: a
    classifier is something that has instances - an M1 classifier has M0
    instances.

    Package: M2::AUTOSARTemplates::GenericStructure::AbstractStructure::AtpClassifier

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 173, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is AtpClassifier:
            raise TypeError("AtpClassifier is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is a feature of the classifier.
        self._atpFeature: List["AtpFeature"] = []

    @property
    def atp_feature(self) -> List["AtpFeature"]:
        """Get atpFeature (Pythonic accessor)."""
        return self._atpFeature

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAtpFeature(self) -> List["AtpFeature"]:
        """
        AUTOSAR-compliant getter for atpFeature.

        Returns:
            The atpFeature value

        Note:
            Delegates to atp_feature property (CODING_RULE_V2_00017)
        """
        return self.atp_feature  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class AtpFeature(Identifiable, ABC):
    """
    Features are properties via which a classifier classifies instances. Or: a
    classifier has features and every M0 instance of it will have those
    features.

    Package: M2::AUTOSARTemplates::GenericStructure::AbstractStructure::AtpFeature

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 173, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is AtpFeature:
            raise TypeError("AtpFeature is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class AtpPrototype(Identifiable, ABC):
    """
    A prototype is a typed feature. A prototype in a classifier indicates that
    instances of that classifier will have a feature, and the structure of that
    feature is given by the its type. An instance of that type will play the
    role indicated by the feature in the owning classifier. A feature is not an
    instance but an indication of an instance-to-be.

    Package: M2::AUTOSARTemplates::GenericStructure::AbstractStructure::AtpPrototype

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 175, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is AtpPrototype:
            raise TypeError("AtpPrototype is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the type of the feature.
        self._atpType: "AtpType" = None

    @property
    def atp_type(self) -> "AtpType":
        """Get atpType (Pythonic accessor)."""
        return self._atpType

    @atp_type.setter
    def atp_type(self, value: "AtpType") -> None:
        """
        Set atpType with validation.

        Args:
            value: The atpType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, AtpType):
            raise TypeError(
                f"atpType must be AtpType, got {type(value).__name__}"
            )
        self._atpType = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAtpType(self) -> "AtpType":
        """
        AUTOSAR-compliant getter for atpType.

        Returns:
            The atpType value

        Note:
            Delegates to atp_type property (CODING_RULE_V2_00017)
        """
        return self.atp_type  # Delegates to property

    def setAtpType(self, value: "AtpType") -> "AtpPrototype":
        """
        AUTOSAR-compliant setter for atpType with method chaining.

        Args:
            value: The atpType to set

        Returns:
            self for method chaining

        Note:
            Delegates to atp_type property setter (gets validation automatically)
        """
        self.atp_type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_atp_type(self, value: "AtpType") -> "AtpPrototype":
        """
        Set atpType and return self for chaining.

        Args:
            value: The atpType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_atp_type("value")
        """
        self.atp_type = value  # Use property setter (gets validation)
        return self



class AtpStructureElement(Identifiable, ABC):
    """
    A structure element is both a classifier and a feature. As a feature, its
    structure is given by the feature it owns as a classifier.

    Package: M2::AUTOSARTemplates::GenericStructure::AbstractStructure::AtpStructureElement

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 175, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is AtpStructureElement:
            raise TypeError("AtpStructureElement is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class AtpType(Identifiable, ABC):
    """
    A type is a classifier that may serve to type prototypes. It is a reusable
    classifier.

    Package: M2::AUTOSARTemplates::GenericStructure::AbstractStructure::AtpType

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 175, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is AtpType:
            raise TypeError("AtpType is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
