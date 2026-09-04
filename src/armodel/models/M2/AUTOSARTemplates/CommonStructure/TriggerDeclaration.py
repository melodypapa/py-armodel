"""
This module contains classes for representing AUTOSAR trigger declaration structures
in the CommonStructure module. Triggers define events that can initiate specific
behaviors or actions in AUTOSAR components and systems.
"""

from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import MultidimensionalTime
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwImplPolicyEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class Trigger(AtpStructureElement, VariationPointCapable):
    """A trigger which is provided (i.e. released) or required (i.e. used to activate something) in the given context."""

    # Trigger method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.13, p.109 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getSwImplPolicy   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwImplPolicy   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTriggerPeriod  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTriggerPeriod  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute, when set to value queued, allows for a queued processing of Triggers.
        self.swImplPolicy: Optional[SwImplPolicyEnum] = None

        # Optional definition of a period in case of a periodically (time or angle) driven external trigger.
        self.triggerPeriod: Optional[MultidimensionalTime] = None

    def getSwImplPolicy(self) -> Optional[SwImplPolicyEnum]:
        """
        This attribute, when set to value queued, allows for a queued processing of Triggers.
        """
        return self.swImplPolicy

    def setSwImplPolicy(self, value: Optional[SwImplPolicyEnum]) -> "Trigger":
        """
        This attribute, when set to value queued, allows for a queued processing of Triggers. A None value is a no-op and is not set.
        """
        if value is not None:
            self.swImplPolicy = value
        return self

    def getTriggerPeriod(self) -> Optional[MultidimensionalTime]:
        """
        Optional definition of a period in case of a periodically (time or angle) driven external trigger.
        """
        return self.triggerPeriod

    def setTriggerPeriod(self, value: Optional[MultidimensionalTime]) -> "Trigger":
        """
        Optional definition of a period in case of a periodically (time or angle) driven external trigger. A None value is a no-op and is not set.
        """
        if value is not None:
            self.triggerPeriod = value
        return self


class TriggerMapping(ARObject):
    """
    Represents a mapping between triggers in AUTOSAR models.
    This class defines relationships between different triggers across system boundaries or components.
    """

    # TriggerMapping method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getFirstTriggerRef           [x] impl  [x] docstring  [x] test
    # [x] setFirstTriggerRef           [x] impl  [x] docstring  [x] test
    # [x] getSecondTriggerRef          [x] impl  [x] docstring  [x] test
    # [x] setSecondTriggerRef          [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the TriggerMapping with default values.
        """
        super().__init__()

        # Reference to the first trigger in the mapping
        self.firstTriggerRef: RefType = None
        # Reference to the second trigger in the mapping
        self.secondTriggerRef: RefType = None

    def getFirstTriggerRef(self):
        """
        Gets the reference to the first trigger in the mapping.

        Returns:
            RefType: The first trigger reference
        """
        return self.firstTriggerRef

    def setFirstTriggerRef(self, value):
        """
        Sets the reference to the first trigger in the mapping.
        Only sets the value if it is not None.

        Args:
            value: The first trigger reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.firstTriggerRef = value
        return self

    def getSecondTriggerRef(self):
        """
        Gets the reference to the second trigger in the mapping.

        Returns:
            RefType: The second trigger reference
        """
        return self.secondTriggerRef

    def setSecondTriggerRef(self, value):
        """
        Sets the reference to the second trigger in the mapping.
        Only sets the value if it is not None.

        Args:
            value: The second trigger reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.secondTriggerRef = value
        return self
