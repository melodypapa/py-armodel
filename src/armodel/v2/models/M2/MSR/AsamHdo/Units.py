from typing import List, Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARFloat,
    ARLiteral,
    ARNumerical,
    RefType,
)


class PhysicalDimension(ARElement):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass    """
    Represents a physical dimension with exponents for SI base units.
    Base: ARElement
    """

    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.currentExp: Union[Union[ARNumerical, None] , None] = None
        self.lengthExp: Union[Union[ARNumerical, None] , None] = None
        self.luminousIntensityExp: Union[Union[ARNumerical, None] , None] = None
        self.massExp: Union[Union[ARNumerical, None] , None] = None
        self.molarAmountExp: Union[Union[ARNumerical, None] , None] = None
        self.temperatureExp: Union[Union[ARNumerical, None] , None] = None
        self.timeExp: Union[Union[ARNumerical, None] , None] = None

    def getCurrentExp(self) -> ARNumerical:
        return self.currentExp

    def setCurrentExp(self, value: ARNumerical):
        self.currentExp = value
        return self

    def getLengthExp(self) -> ARNumerical:
        return self.lengthExp

    def setLengthExp(self, value: ARNumerical):
        self.lengthExp = value
        return self

    def getLuminousIntensityExp(self) -> ARNumerical:
        return self.luminousIntensityExp

    def setLuminousIntensityExp(self, value: ARNumerical):
        self.luminousIntensityExp = value
        return self

    def getMassExp(self) -> ARNumerical:
        return self.massExp

    def setMassExp(self, value: ARNumerical):
        self.massExp = value
        return self

    def getMolarAmountExp(self) -> ARNumerical:
        return self.molarAmountExp

    def setMolarAmountExp(self, value: ARNumerical):
        self.molarAmountExp = value
        return self

    def getTemperatureExp(self) -> ARNumerical:
        return self.temperatureExp

    def setTemperatureExp(self, value: ARNumerical):
        self.temperatureExp = value
        return self

    def getTimeExp(self) -> ARNumerical:
        return self.timeExp

    def setTimeExp(self, value: ARNumerical):
        self.timeExp = value
        return self


class SingleLanguageUnitNames(ARLiteral):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass    """
    Represents single language unit names.
    Base: ARLiteral
    """

    def __init__(self) -> None:
        super().__init__()


class Unit(ARElement):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass    """
    Represents a unit with display name, conversion factor, and physical dimension reference.
    Base: ARElement
    """

    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.displayName: Union[Union[SingleLanguageUnitNames, None] , None] = None
        self.factorSiToUnit: Union[Union[ARFloat, None] , None] = None
        self.offsetSiToUnit: Union[Union[ARFloat, None] , None] = None
        self.physicalDimensionRef: Union[Union[RefType, None] , None] = None

    def getDisplayName(self) -> SingleLanguageUnitNames:
        return self.displayName

    def setDisplayName(self, value: SingleLanguageUnitNames):
        self.displayName = value
        return self

    def getFactorSiToUnit(self) -> ARFloat:
        return self.factorSiToUnit

    def setFactorSiToUnit(self, value: ARFloat):
        self.factorSiToUnit = value
        return self

    def getOffsetSiToUnit(self) -> ARFloat:
        return self.offsetSiToUnit

    def setOffsetSiToUnit(self, value: ARFloat):
        self.offsetSiToUnit = value
        return self

    def getPhysicalDimensionRef(self) -> RefType:
        return self.physicalDimensionRef

    def setPhysicalDimensionRef(self, value: RefType):
        self.physicalDimensionRef = value
        return self


class UnitGroup(ARElement):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass    """
    Represents a group of units in the AUTOSAR model.

    This class is used to group related units together for organizational purposes.

    Attributes:
        parent (ARObject): The parent object in the AUTOSAR model hierarchy.
        short_name (str): The short name of the unit group.
        units (List[Unit]): A list of units in the group.
    """

    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.units: List[Unit] = []

    def getUnits(self) -> List[Unit]:
        return self.units

    def addUnit(self, value: Unit):
        if value is not None:
            self.units.append(value)
        return self
