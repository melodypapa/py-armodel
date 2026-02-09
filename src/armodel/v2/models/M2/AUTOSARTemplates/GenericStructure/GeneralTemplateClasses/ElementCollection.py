"""
AUTOSAR Package - ElementCollection

Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ElementCollection
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    NameToken,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class AutoCollectEnum(AREnum):
    """
    AutoCollectEnum enumeration

This enumerator defines the possible approaches to determine the final set of elements in a collection. Aggregated by Collection.autoCollect

Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ElementCollection
    """
    # All objects being referenced (recursively) from the objects mentioned directly in the collection are also considered as part of the collection.
    refAll = "0"

    # This indicates that only those objects mentioned directly in the collection are part of the collection. No other objects are considered further.
    refNone = "1"

    # This indicates that non standard objects ([TPS_GST_00088]) referenced (recursively) by the objects mentioned directly in the collection are also considered to be part of the collection.
    refNonStandard = "2"

    def __init__(self):
        super().__init__([
            AutoCollectEnum.refAll,
            AutoCollectEnum.refNone,
            AutoCollectEnum.refNonStandard,
        ])

    def __eq__(self, other: object) -> bool:
        """
        Compare AutoCollectEnum with other objects.

        Args:
            other: The object to compare with

        Returns:
            True if the other object is an AutoCollectEnum with the same value or a string matching the value
        """
        if isinstance(other, AutoCollectEnum):
            return self.value == other.value
        elif isinstance(other, str):
            return self.value == other
        return False


class CollectableElement(Identifiable, ABC):
    """
    This meta-class specifies the ability to be part of a specific AUTOSAR
    collection of ARPackages or ARElements. The scope of collection has been
    extended beyond CollectableElement with Revision 4.0.3. For compatibility
    reasons the name of this meta Class was not changed.

    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ElementCollection::CollectableElement

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 399, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is CollectableElement:
            raise TypeError("CollectableElement is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====