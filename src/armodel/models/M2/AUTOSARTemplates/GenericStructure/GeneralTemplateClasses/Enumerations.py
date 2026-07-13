"""
This module contains enumeration classes for AUTOSAR models
in the GenericStructure module. These enumerations are used to specify
various configuration and behavior options throughout the AUTOSAR model.
"""

from enum import Enum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum


class AutoCollectEnum(Enum):
    """
    Enumeration for auto-collect settings in AUTOSAR collections.
    This enum defines the different auto-collection behaviors that can
    be applied to collections.
    """
    # AutoCollectEnum method parity checklist:
    # (no methods)

    AUTO_COLLECT_OFF = "OFF"
    AUTO_COLLECT_ON = "ON"
    AUTO_COLLECT_AUTO = "AUTO"


class BindingTimeEnum(AREnum):
    """
    Enumeration for binding time in AUTOSAR variant handling.

    This class specifies the point in time when a variant condition
    may be evaluated at earliest. At this point in time, all referenced
    system constants shall have a value.

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling
    """
    # BindingTimeEnum method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test


    def __init__(self):
        super().__init__([
            "codeGenerationTime",
            "linkTime",
            "preCompileTime",
            "systemDesignTime"
        ])
