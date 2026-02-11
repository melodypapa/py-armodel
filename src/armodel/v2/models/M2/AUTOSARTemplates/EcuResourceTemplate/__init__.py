"""
Ecu Resource Template package.

This module imports and re-exports classes from EcuResourceTemplate modules.
"""

from armodel.v2.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory import (
    HwAttributeDef,
    HwAttributeLiteralDef,
    HwAttributeValue,
    HwCategory,
    HwType,
)
from armodel.v2.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwAttributeDef import (
    HwDescriptionEntity,
)
from armodel.v2.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwPin import (
    HwPin,
)
from armodel.v2.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwPinConnector import (
    HwElementConnector,
    HwPinConnector,
)
from armodel.v2.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwPinGroup import (
    HwPinGroup,
)
from armodel.v2.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwPinGroupConnector import (
    HwPinGroupConnector,
)
from armodel.v2.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwPinGroupContent import (
    HwPinGroupContent,
)
from armodel.v2.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElement import (
    HwElement,
)

__all__ = [
    HwAttributeDef,
    HwAttributeLiteralDef,
    HwAttributeValue,
    HwCategory,
    HwType,
    HwDescriptionEntity,
    HwPin,
    HwElementConnector,
    HwPinConnector,
    HwPinGroup,
    HwPinGroupConnector,
    HwPinGroupContent,
    HwElement,
]