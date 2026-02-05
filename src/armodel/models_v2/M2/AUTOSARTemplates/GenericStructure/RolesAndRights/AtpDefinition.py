"""
This module contains the AtpDefinition abstract class for AUTOSAR models
in the GenericStructure module.
"""

from abc import ABC
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable


class AtpDefinition(Identifiable, ABC):
    """
    Abstract base class for AUTOSAR Template (ATP) definition elements.

    AtpDefinition represents definition elements in the AUTOSAR system. Definitions
    provide formal specifications or constraints that define characteristics or
    behavior of AUTOSAR elements.

    This class extends Identifiable with definition-specific functionality for
    managing definition-based elements.

    Note:
        This is an abstract class and cannot be instantiated directly.
        AtpDefinition is the parent of various AUTOSAR definition elements:
        - HwCategory (hardware element categories)
        - SwSystemconst (system constants)
        - PostBuildVariantCriterion (post-build variant criteria)

    Attributes:
        Inherits all attributes from Identifiable including shortName, adminData,
        longName, category, and reference management capabilities.
    """

    def __init__(self, parent, short_name: str):
        if type(self) is AtpDefinition:
            raise TypeError("AtpDefinition is an abstract class.")
        super().__init__(parent, short_name)
