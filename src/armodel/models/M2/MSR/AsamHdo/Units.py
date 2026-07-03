from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARFloat,
    ARNumerical,
    RefType,
    ARLiteral,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement,
)


class PhysicalDimension(ARElement):
    """
    Represents a physical dimension with exponents for SI base units.
    Base: ARElement
    """

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.currentExp: Optional[ARNumerical] = None
        self.lengthExp: Optional[ARNumerical] = None
        self.luminousIntensityExp: Optional[ARNumerical] = None
        self.massExp: Optional[ARNumerical] = None
        self.molarAmountExp: Optional[ARNumerical] = None
        self.temperatureExp: Optional[ARNumerical] = None
        self.timeExp: Optional[ARNumerical] = None

    def getCurrentExp(self) -> Optional[ARNumerical]:
        return self.currentExp

    def setCurrentExp(self, value: ARNumerical):
        self.currentExp = value
        return self

    def getLengthExp(self) -> Optional[ARNumerical]:
        return self.lengthExp

    def setLengthExp(self, value: ARNumerical):
        self.lengthExp = value
        return self

    def getLuminousIntensityExp(self) -> Optional[ARNumerical]:
        return self.luminousIntensityExp

    def setLuminousIntensityExp(self, value: ARNumerical):
        self.luminousIntensityExp = value
        return self

    def getMassExp(self) -> Optional[ARNumerical]:
        return self.massExp

    def setMassExp(self, value: ARNumerical):
        self.massExp = value
        return self

    def getMolarAmountExp(self) -> Optional[ARNumerical]:
        return self.molarAmountExp

    def setMolarAmountExp(self, value: ARNumerical):
        self.molarAmountExp = value
        return self

    def getTemperatureExp(self) -> Optional[ARNumerical]:
        return self.temperatureExp

    def setTemperatureExp(self, value: ARNumerical):
        self.temperatureExp = value
        return self

    def getTimeExp(self) -> Optional[ARNumerical]:
        return self.timeExp

    def setTimeExp(self, value: ARNumerical):
        self.timeExp = value
        return self


class SingleLanguageUnitNames(ARLiteral):
    """
    Represents single language unit names.
    Base: ARLiteral
    """

    def __init__(self) -> None:
        super().__init__()


class Unit(ARElement):
    """
    Represents a unit with display name, conversion factor, and physical dimension reference.
    Base: ARElement
    """

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.displayName: Optional[SingleLanguageUnitNames] = None
        self.factorSiToUnit: Optional[ARFloat] = None
        self.offsetSiToUnit: Optional[ARFloat] = None
        self.physicalDimensionRef: Optional[RefType] = None

    def getDisplayName(self) -> Optional[SingleLanguageUnitNames]:
        return self.displayName

    def setDisplayName(self, value: SingleLanguageUnitNames):
        self.displayName = value
        return self

    def getFactorSiToUnit(self) -> Optional[ARFloat]:
        return self.factorSiToUnit

    def setFactorSiToUnit(self, value: ARFloat):
        self.factorSiToUnit = value
        return self

    def getOffsetSiToUnit(self) -> Optional[ARFloat]:
        return self.offsetSiToUnit

    def setOffsetSiToUnit(self, value: ARFloat):
        self.offsetSiToUnit = value
        return self

    def getPhysicalDimensionRef(self) -> Optional[RefType]:
        return self.physicalDimensionRef

    def setPhysicalDimensionRef(self, value: RefType):
        self.physicalDimensionRef = value
        return self


class UnitGroup(ARElement):
    """
    Represents a group of units in the AUTOSAR model.

    This class is used to group related units together for organizational purposes.

    Attributes:
        parent (ARObject): The parent object in the AUTOSAR model hierarchy.
        short_name (str): The short name of the unit group.
        units (List[Unit]): A list of units in the group.
    """

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.units: List[Unit] = []

    def getUnits(self) -> List[Unit]:
        return self.units

    def addUnit(self, value: Unit):
        if value is not None:
            self.units.append(value)
        return self
