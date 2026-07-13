"""
This module defines BSW entry relationship enum in AUTOSAR.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum


class BswEntryRelationshipEnum(AREnum):
    """
    Enumeration for BSW entry relationship types.
    """
    # BswEntryRelationshipEnum method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test


    READS = "reads"
    WRITES = "writes"
    CALLS = "calls"
    TRIGGERS = "triggers"

    def __init__(self):
        super().__init__((
            BswEntryRelationshipEnum.READS,
            BswEntryRelationshipEnum.WRITES,
            BswEntryRelationshipEnum.CALLS,
            BswEntryRelationshipEnum.TRIGGERS,
        ))
