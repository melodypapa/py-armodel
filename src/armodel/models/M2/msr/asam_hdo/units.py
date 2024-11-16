
from ....ar_ref import RefType
from ....ar_object import ARFloat, ARLiteral, ARNumerical, ARObject
from ....general_structure import ARElement
class PhysicalDimension(ARElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.currentExp = None                      # type: ARNumerical
        self.lengthExp = None                       # type: ARNumerical
        self.luminousIntensityExp = None            # type: ARNumerical
        self.massExp = None                         # type: ARNumerical
        self.molarAmountExp = None                  # type: ARNumerical
        self.temperatureExp = None                  # type: ARNumerical
        self.timeExp = None                         # type: ARNumerical

    def getCurrentExp(self):
        return self.currentExp

    def setCurrentExp(self, value):
        self.currentExp = value
        return self

    def getLengthExp(self):
        return self.lengthExp

    def setLengthExp(self, value):
        self.lengthExp = value
        return self

    def getLuminousIntensityExp(self):
        return self.luminousIntensityExp

    def setLuminousIntensityExp(self, value):
        self.luminousIntensityExp = value
        return self

    def getMassExp(self):
        return self.massExp

    def setMassExp(self, value):
        self.massExp = value
        return self

    def getMolarAmountExp(self):
        return self.molarAmountExp

    def setMolarAmountExp(self, value):
        self.molarAmountExp = value
        return self

    def getTemperatureExp(self):
        return self.temperatureExp

    def setTemperatureExp(self, value):
        self.temperatureExp = value
        return self

    def getTimeExp(self):
        return self.timeExp

    def setTimeExp(self, value):
        self.timeExp = value
        return self

class SingleLanguageUnitNames(ARLiteral):
    def __init__(self) -> None:
        super().__init__()

class Unit(ARElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.displayName = None                 # type: SingleLanguageUnitNames
        self.factorSiToUnit = None              # type: ARFloat
        self.offsetSiToUnit = None              # type: ARFloat
        self.physicalDimensionRef = None        # type: RefType

    def getDisplayName(self):
        return self.displayName

    def setDisplayName(self, value):
        self.displayName = value
        return self

    def getFactorSiToUnit(self):
        return self.factorSiToUnit

    def setFactorSiToUnit(self, value):
        self.factorSiToUnit = value
        return self

    def getOffsetSiToUnit(self):
        return self.offsetSiToUnit

    def setOffsetSiToUnit(self, value):
        self.offsetSiToUnit = value
        return self

    def getPhysicalDimensionRef(self):
        return self.physicalDimensionRef

    def setPhysicalDimensionRef(self, value):
        self.physicalDimensionRef = value
        return self
