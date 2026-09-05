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
    """Defines the mapping of two particular unequally named Triggers in the given context."""

    # TriggerMapping method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.31, p.134 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # Reader/writer note: dedicated readTriggerMapping/writeTriggerMapping (matched name
    # pair, Rule 0013.2) read/write FIRST-TRIGGER-REF → SECOND-TRIGGER-REF in XSD order;
    # the TRIGGER-MAPPINGS wrapper is owned by TriggerInterfaceMapping (Table 4.30) and
    # its reader/writer construct the TriggerMapping children. No
    # readIdentifiable/writeIdentifiable call — spec Base = ARObject (no Referrable members).
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getFirstTriggerRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFirstTriggerRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSecondTriggerRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSecondTriggerRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # A Trigger to be mapped.
        self.firstTriggerRef: Optional[RefType] = None

        # A Trigger to be mapped.
        self.secondTriggerRef: Optional[RefType] = None

    def getFirstTriggerRef(self) -> Optional[RefType]:
        """A Trigger to be mapped."""
        return self.firstTriggerRef

    def setFirstTriggerRef(self, value: Optional[RefType]) -> "TriggerMapping":
        """A Trigger to be mapped. A None value is a no-op and is not set."""
        if value is not None:
            self.firstTriggerRef = value
        return self

    def getSecondTriggerRef(self) -> Optional[RefType]:
        """A Trigger to be mapped."""
        return self.secondTriggerRef

    def setSecondTriggerRef(self, value: Optional[RefType]) -> "TriggerMapping":
        """A Trigger to be mapped. A None value is a no-op and is not set."""
        if value is not None:
            self.secondTriggerRef = value
        return self
