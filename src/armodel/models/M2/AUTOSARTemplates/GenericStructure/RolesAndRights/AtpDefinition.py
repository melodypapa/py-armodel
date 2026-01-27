"""
This module contains the AtpDefinition abstract class for AUTOSAR models
in the GenericStructure module.
"""

from abc import ABC
from ..GeneralTemplateClasses.Identifiable import Referrable


class AtpDefinition(Referrable, ABC):
    """
    Abstract base class for AUTOSAR Template (ATP) definition elements.
    
    AtpDefinition represents definition elements in the AUTOSAR system. Definitions
    provide formal specifications or constraints that define characteristics or
    behavior of AUTOSAR elements.
    
    This class extends Referrable with definition-specific functionality for
    managing definition-based elements.
    
    Note:
        This is an abstract class and cannot be instantiated directly.
        AtpDefinition is the parent of various AUTOSAR definition elements:
        - HwCategory (hardware element categories)
        - SwSystemconst (system constants)
        - PostBuildVariantCriterion (post-build variant criteria)
    
    Attributes:
        Inherits all attributes from Referrable including shortName, adminData,
        and reference management capabilities.
    """
    
    def __init__(self, parent, short_name: str):
        if type(self) is AtpDefinition:
            raise TypeError("AtpDefinition is an abstract class.")
        super().__init__(parent, short_name)