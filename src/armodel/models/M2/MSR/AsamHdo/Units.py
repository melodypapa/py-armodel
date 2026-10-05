from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
    Numerical,
    RefType,
)
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import MixedContentForUnitNames
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement


class PhysicalDimension(ARElement):
    """
    This class represents a physical dimension. If the physical dimension of two units is identical, then a conversion between them is possible. The conversion between units is related to the definition of the physical dimension. Note that the equivalence of the exponents does not per se define the convertibility. For example Energy and Torque share the same exponents (Nm). Please note further the value of an exponent does not necessarily have to be an integer number. It is also possible that the value yields a rational number, e.g. to compute the square root of a given physical quantity. In this case the exponent value would be a rational number where the numerator value is 1 and the denominator value is 2. Tags: atp.recommendedPackage=PhysicalDimensions
    """

    # PhysicalDimension method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.76, p.398
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCurrentExp             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCurrentExp             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getLengthExp              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setLengthExp              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getLuminousIntensityExp   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setLuminousIntensityExp   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMassExp                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMassExp                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMolarAmountExp         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMolarAmountExp         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTemperatureExp         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTemperatureExp         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimeExp                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimeExp                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute represents the exponent of the physical dimension "electric current". Tags: xml.sequenceOffset=50
        self.currentExp: Optional[Numerical] = None

        # The exponent of the physical dimension "length". Tags: xml.sequenceOffset=20
        self.lengthExp: Optional[Numerical] = None

        # The exponent of the physical dimension "luminous intensity". Tags: xml.sequenceOffset=80
        self.luminousIntensityExp: Optional[Numerical] = None

        # The exponent of the physical dimension "mass". Tags: xml.sequenceOffset=30
        self.massExp: Optional[Numerical] = None

        # The exponent of the physical dimension "quantity of substance". Tags: xml.sequenceOffset=70
        self.molarAmountExp: Optional[Numerical] = None

        # The exponent of the physical dimension "temperature". Tags: xml.sequenceOffset=60
        self.temperatureExp: Optional[Numerical] = None

        # The exponent of the physical dimension "time". Tags: xml.sequenceOffset=40
        self.timeExp: Optional[Numerical] = None

    def getCurrentExp(self) -> Optional[Numerical]:
        """
        This attribute represents the exponent of the physical dimension "electric current". Tags: xml.sequenceOffset=50
        """
        return self.currentExp

    def setCurrentExp(self, value: Optional[Numerical]) -> "PhysicalDimension":
        """
        This attribute represents the exponent of the physical dimension "electric current". Tags: xml.sequenceOffset=50 A None value is a no-op and does not overwrite an existing currentExp.
        """
        if value is not None:
            self.currentExp = value
        return self

    def getLengthExp(self) -> Optional[Numerical]:
        """
        The exponent of the physical dimension "length". Tags: xml.sequenceOffset=20
        """
        return self.lengthExp

    def setLengthExp(self, value: Optional[Numerical]) -> "PhysicalDimension":
        """
        The exponent of the physical dimension "length". Tags: xml.sequenceOffset=20 A None value is a no-op and does not overwrite an existing lengthExp.
        """
        if value is not None:
            self.lengthExp = value
        return self

    def getLuminousIntensityExp(self) -> Optional[Numerical]:
        """
        The exponent of the physical dimension "luminous intensity". Tags: xml.sequenceOffset=80
        """
        return self.luminousIntensityExp

    def setLuminousIntensityExp(self, value: Optional[Numerical]) -> "PhysicalDimension":
        """
        The exponent of the physical dimension "luminous intensity". Tags: xml.sequenceOffset=80 A None value is a no-op and does not overwrite an existing luminousIntensityExp.
        """
        if value is not None:
            self.luminousIntensityExp = value
        return self

    def getMassExp(self) -> Optional[Numerical]:
        """
        The exponent of the physical dimension "mass". Tags: xml.sequenceOffset=30
        """
        return self.massExp

    def setMassExp(self, value: Optional[Numerical]) -> "PhysicalDimension":
        """
        The exponent of the physical dimension "mass". Tags: xml.sequenceOffset=30 A None value is a no-op and does not overwrite an existing massExp.
        """
        if value is not None:
            self.massExp = value
        return self

    def getMolarAmountExp(self) -> Optional[Numerical]:
        """
        The exponent of the physical dimension "quantity of substance". Tags: xml.sequenceOffset=70
        """
        return self.molarAmountExp

    def setMolarAmountExp(self, value: Optional[Numerical]) -> "PhysicalDimension":
        """
        The exponent of the physical dimension "quantity of substance". Tags: xml.sequenceOffset=70 A None value is a no-op and does not overwrite an existing molarAmountExp.
        """
        if value is not None:
            self.molarAmountExp = value
        return self

    def getTemperatureExp(self) -> Optional[Numerical]:
        """
        The exponent of the physical dimension "temperature". Tags: xml.sequenceOffset=60
        """
        return self.temperatureExp

    def setTemperatureExp(self, value: Optional[Numerical]) -> "PhysicalDimension":
        """
        The exponent of the physical dimension "temperature". Tags: xml.sequenceOffset=60 A None value is a no-op and does not overwrite an existing temperatureExp.
        """
        if value is not None:
            self.temperatureExp = value
        return self

    def getTimeExp(self) -> Optional[Numerical]:
        """
        The exponent of the physical dimension "time". Tags: xml.sequenceOffset=40
        """
        return self.timeExp

    def setTimeExp(self, value: Optional[Numerical]) -> "PhysicalDimension":
        """
        The exponent of the physical dimension "time". Tags: xml.sequenceOffset=40 A None value is a no-op and does not overwrite an existing timeExp.
        """
        if value is not None:
            self.timeExp = value
        return self


class SingleLanguageUnitNames(MixedContentForUnitNames):
    """
    This represents the ability to express a display name.
    """

    # SingleLanguageUnitNames method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.80, p.400
    # Spec verified: R23-11
    # 2026-09-25 drift fix (Rule 0012.3): re-parented ARLiteral → MixedContentForUnitNames per the
    # markdown-verified Base row (ARObject , MixedContentForUnitNames) — see docs/plan/atp_mixed_string_hierarchy.md
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # (zero own members — Table 5.80 Attribute column "-": sub/sup inherited from MixedContentForUnitNames;
    #  2026-09-27 unification: the mixed text rides the AtpMixedString mixin (mixedString) inherited from
    #  MixedContentForUnitNames — SlOverviewParagraph/LVerbatim shape; the concrete `value` member and
    #  getValue/setValue are removed; stereotype-inherent, no spec row)

    def __init__(self):
        super().__init__()


class Unit(ARElement):
    """
    This is a physical measurement unit. All units that might be defined should stem from SI units. In order to convert one unit into another factor and offset are defined. For the calculation from SI-unit to the defined unit the factor (factorSiToUnit ) and the offset (offsetSiTo Unit ) are applied as follows: x [{unit}] := y * [{siUnit}] * factorSiToUnit [[unit]/{siUnit}] + offsetSiToUnit [{unit}] For the calculation from a unit to SI-unit the reciprocal of the factor (factorSiToUnit ) and the negation of the offset (offsetSiToUnit ) are applied. y {siUnit} := (x*{unit} - offsetSiToUnit [{unit}]) / (factorSiToUnit [[unit]/{siUnit}]
    """

    # Unit method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.79, p.400
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDisplayName          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDisplayName          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getFactorSiToUnit       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFactorSiToUnit       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getOffsetSiToUnit       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setOffsetSiToUnit       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPhysicalDimensionRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPhysicalDimensionRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This specifies how the unit shall be displayed in documents or in user interfaces of tools.The displayName corresponds to the Unit.Display in an ASAM MCD-2MC file.
        self.displayName: Optional[SingleLanguageUnitNames] = None

        # This is the factor for the conversion from SI Units to units. The inverse is used for conversion from units to SI Units.
        self.factorSiToUnit: Optional[Float] = None

        # This is the offset for the conversion from and to siUnits.
        self.offsetSiToUnit: Optional[Float] = None

        # This association represents the physical dimension to which the unit belongs to. Note that only values with units of the same physical dimensions might be converted.
        self.physicalDimensionRef: Optional[RefType] = None

    def getDisplayName(self) -> Optional[SingleLanguageUnitNames]:
        """
        This specifies how the unit shall be displayed in documents or in user interfaces of tools.The displayName corresponds to the Unit.Display in an ASAM MCD-2MC file.
        """
        return self.displayName

    def setDisplayName(self, value: Optional[SingleLanguageUnitNames]) -> "Unit":
        """
        This specifies how the unit shall be displayed in documents or in user interfaces of tools.The displayName corresponds to the Unit.Display in an ASAM MCD-2MC file. A None value is a no-op and does not overwrite an existing displayName.
        """
        if value is not None:
            self.displayName = value
        return self

    def getFactorSiToUnit(self) -> Optional[Float]:
        """
        This is the factor for the conversion from SI Units to units. The inverse is used for conversion from units to SI Units.
        """
        return self.factorSiToUnit

    def setFactorSiToUnit(self, value: Optional[Float]) -> "Unit":
        """
        This is the factor for the conversion from SI Units to units. The inverse is used for conversion from units to SI Units. A None value is a no-op and does not overwrite an existing factorSiToUnit.
        """
        if value is not None:
            self.factorSiToUnit = value
        return self

    def getOffsetSiToUnit(self) -> Optional[Float]:
        """
        This is the offset for the conversion from and to siUnits.
        """
        return self.offsetSiToUnit

    def setOffsetSiToUnit(self, value: Optional[Float]) -> "Unit":
        """
        This is the offset for the conversion from and to siUnits. A None value is a no-op and does not overwrite an existing offsetSiToUnit.
        """
        if value is not None:
            self.offsetSiToUnit = value
        return self

    def getPhysicalDimensionRef(self) -> Optional[RefType]:
        """
        This association represents the physical dimension to which the unit belongs to. Note that only values with units of the same physical dimensions might be converted.
        """
        return self.physicalDimensionRef

    def setPhysicalDimensionRef(self, value: Optional[RefType]) -> "Unit":
        """
        This association represents the physical dimension to which the unit belongs to. Note that only values with units of the same physical dimensions might be converted. A None value is a no-op and does not overwrite an existing physicalDimensionRef.
        """
        if value is not None:
            self.physicalDimensionRef = value
        return self


class UnitGroup(ARElement):
    """
    This meta-class represents the ability to specify a logical grouping of units.The category denotes the unit system that the referenced units are associated to. In this way, e.g. country-specific unit systems (CATEGORY="COUNTRY") can be defined as well as specific unit systems for certain application domains. In the same way a group of equivalent units, can be defined which are used in different countries, by setting CATEGORY="EQUIV_UNITS". KmPerHour and MilesPerHour could such be combined to one group named "vehicle_speed". The unit MeterPerSec would not belong to this group because it is normally not used for vehicle speed. But all of the mentioned units could be combined to one group named "speed". Note that the UnitGroup does not ensure the physical compliance of the units. This is maintained by the physical dimension. Tags: atp.recommendedPackage=UnitGroups
    """

    # UnitGroup method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.81, p.402
    # Spec verified: R23-11 (2026-09-27, user 9b confirmation)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getUnitRefs   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addUnitRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents one particular unit in the UnitGroup. Tags: xml.sequenceOffset=20
        self.unitRefs: List[RefType] = []

    def getUnitRefs(self) -> List[RefType]:
        """
        This represents one particular unit in the UnitGroup. Tags: xml.sequenceOffset=20.
        """
        return self.unitRefs

    def addUnitRef(self, value: Optional[RefType]) -> "UnitGroup":
        """
        This represents one particular unit in the UnitGroup. Tags: xml.sequenceOffset=20. A None value is a no-op and is not appended.
        """
        if value is not None:
            self.unitRefs.append(value)
        return self
