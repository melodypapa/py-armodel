from __future__ import annotations

from abc import ABC
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Enumerations import BindingTimeEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    IntervalTypeEnum,
    PrimitiveIdentifier,
    String,
)


class AttributeValueVariationPoint(ARObject, ABC):
    """
    This class represents the ability to derive the value of the Attribute from a system constant (by SwSystemconstDependentFormula). It also provides a bindingTime.

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::AttributeValueVariationPoints
    Base: ARObject, FormulaExpression, SwSystemconstDependentFormula
    Stereotypes: atpMixedString

    Attributes:
        bindingTime (BindingTimeEnum): This is the binding time in which the attribute value needs to be bound. If this attribute is missing, the attribute is not a variation point. In particular this means that It needs to be a single value according to the type specified in the pure model. It is an error if it is still a formula. (Multiplicity: 0..1)
        blueprintValue (String): This represents a description that documents how the value shall be defined when deriving objects from the blueprint. (Multiplicity: 0..1)
        sd (String): This special data is provided to allow synchronization of Attribute value variation points with variant management systems. The usage is subject of agreement between the involved parties. (Multiplicity: 0..1)
        shortLabel (PrimitiveIdentifier): This allows to identify the variation point. It is also intended to allow RTE support for CompileTime Variation points. (Multiplicity: 0..1)
    """

    # AttributeValueVariationPoint method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 7.2, p.210
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getBindingTime    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setBindingTime    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getBlueprintValue [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setBlueprintValue [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSd             [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setSd             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getShortLabel     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setShortLabel     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getText           [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setText           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        if type(self) is AttributeValueVariationPoint:
            raise TypeError("AttributeValueVariationPoint is an abstract class.")

        super().__init__()

        # This is the binding time in which the attribute value needs to be bound. If this attribute is missing, the attribute is not a variation point. In particular this means that It needs to be a single value according to the type specified in the pure model. It is an error if it is still a formula. Tags: xml.attribute=true
        self.bindingTime: Optional[BindingTimeEnum] = None

        # This represents a description that documents how the value shall be defined when deriving objects from the blueprint. Tags: xml.attribute=true
        self.blueprintValue: Optional[String] = None

        # This special data is provided to allow synchronization of Attribute value variation points with variant management systems. The usage is subject of agreement between the involved parties. Tags: xml.attribute=true
        self.sd: Optional[String] = None

        # This allows to identify the variation point. It is also intended to allow RTE support for CompileTime Variation points. Tags: xml.attribute=true
        self.shortLabel: Optional[PrimitiveIdentifier] = None

        self._text: Optional[str] = None

    def getBindingTime(self) -> Optional[BindingTimeEnum]:
        """
        This is the binding time in which the attribute value needs to be bound. If this attribute is missing, the attribute is not a variation point. In particular this means that It needs to be a single value according to the type specified in the pure model. It is an error if it is still a formula. Tags: xml.attribute=true
        """
        return self.bindingTime

    def setBindingTime(self, value: Optional[BindingTimeEnum]) -> "AttributeValueVariationPoint":
        """
        This is the binding time in which the attribute value needs to be bound. If this attribute is missing, the attribute is not a variation point. In particular this means that It needs to be a single value according to the type specified in the pure model. It is an error if it is still a formula. Tags: xml.attribute=true A None value is a no-op and does not overwrite an existing bindingTime.
        """
        if value is not None:
            self.bindingTime = value
        return self

    def getBlueprintValue(self) -> Optional[String]:
        """
        This represents a description that documents how the value shall be defined when deriving objects from the blueprint. Tags: xml.attribute=true
        """
        return self.blueprintValue

    def setBlueprintValue(self, value: Optional[String]) -> "AttributeValueVariationPoint":
        """
        This represents a description that documents how the value shall be defined when deriving objects from the blueprint. Tags: xml.attribute=true A None value is a no-op and does not overwrite an existing blueprintValue.
        """
        if value is not None:
            self.blueprintValue = value
        return self

    def getSd(self) -> Optional[String]:
        """
        This special data is provided to allow synchronization of Attribute value variation points with variant management systems. The usage is subject of agreement between the involved parties. Tags: xml.attribute=true
        """
        return self.sd

    def setSd(self, value: Optional[String]) -> "AttributeValueVariationPoint":
        """
        This special data is provided to allow synchronization of Attribute value variation points with variant management systems. The usage is subject of agreement between the involved parties. Tags: xml.attribute=true A None value is a no-op and does not overwrite an existing sd.
        """
        if value is not None:
            self.sd = value
        return self

    def getShortLabel(self) -> Optional[PrimitiveIdentifier]:
        """
        This allows to identify the variation point. It is also intended to allow RTE support for CompileTime Variation points. Tags: xml.attribute=true
        """
        return self.shortLabel

    def setShortLabel(self, value: Optional[PrimitiveIdentifier]) -> "AttributeValueVariationPoint":
        """
        This allows to identify the variation point. It is also intended to allow RTE support for CompileTime Variation points. Tags: xml.attribute=true A None value is a no-op and does not overwrite an existing shortLabel.
        """
        if value is not None:
            self.shortLabel = value
        return self

    def getText(self) -> Optional[str]:
        """Returns the mixed string content (the actual value, e.g. the numerical literal) of this <<atpMixedString>> element."""
        return self._text

    def setText(self, value: Optional[str]) -> "AttributeValueVariationPoint":
        """Sets the mixed string content (the actual value, e.g. the numerical literal) of this <<atpMixedString>> element. A None value is a no-op and does not overwrite an existing value."""
        if value is not None:
            self._text = value
        return self


class AbstractNumericalVariationPoint(AttributeValueVariationPoint):
    """
    This is an abstract NumericalValueVariationPoint. It is introduced to support the case that additional attributes are required for particular purposes.

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::AttributeValueVariationPoints
    Base: ARObject, AttributeValueVariationPoint, FormulaExpression, SwSystemconstDependentFormula
    Stereotypes: atpMixedString
    """

    # AbstractNumericalVariationPoint method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 7.11, p.240
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        if type(self) is AbstractNumericalVariationPoint:
            raise TypeError("AbstractNumericalVariationPoint is an abstract class.")

        super().__init__()


class NumericalValueVariationPoint(AbstractNumericalVariationPoint):
    """
    This class represents an attribute value variation point for Numerical attributes. Note that this class might be used in the extended meta-model only.

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::AttributeValueVariationPoints
    Base: ARObject, AbstractNumericalVariationPoint, AttributeValueVariationPoint, FormulaExpression, SwSystemconstDependentFormula
    Stereotypes: atpMixedString
    """

    # NumericalValueVariationPoint method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 7.16, p.241
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        super().__init__()


class LimitValueVariationPoint(AbstractNumericalVariationPoint):
    """
    This class represents the ability to express a numerical limit. Note that this is in fact a NumericalValuation Point but has the additional attribute intervalType. Note that the xml.name is "LIMIT" for backward compatibility reasons. Tags: xml.name=LIMIT

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::AttributeValueVariationPoints
    Base: ARObject, AbstractNumericalVariationPoint, AttributeValueVariationPoint, FormulaExpression, SwSystemconstDependentFormula
    Stereotypes: atpMixedString
    """

    # LimitValueVariationPoint method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 7.15, p.241
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getIntervalType   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setIntervalType   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This specifies the type of the interval.
        self.intervalType: Optional[IntervalTypeEnum] = None

    def getIntervalType(self) -> Optional[IntervalTypeEnum]:
        """This specifies the type of the interval."""
        return self.intervalType

    def setIntervalType(self, value: Optional[IntervalTypeEnum]) -> "LimitValueVariationPoint":
        """This specifies the type of the interval. A None value is a no-op and does not overwrite an existing intervalType."""
        if value is not None:
            self.intervalType = value
        return self


class BooleanValueVariationPoint(AttributeValueVariationPoint):
    """
    This class represents an attribute value variation point for Boolean attributes. Note that this class might be used in the extended meta-model on

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::AttributeValueVariationPoints
    Base: ARObject, AttributeValueVariationPoint, FormulaExpression, SwSystemconstDependentFormula
    Stereotypes: atpMixedString
    """

    # BooleanValueVariationPoint method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 7.12, p.240
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        super().__init__()


class FloatValueVariationPoint(AttributeValueVariationPoint):
    """
    This class represents an attribute value variation point for Float attributes. Note that this class might be used in the extended meta-model only.

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::AttributeValueVariationPoints
    Base: ARObject, AttributeValueVariationPoint, FormulaExpression, SwSystemconstDependentFormula
    Stereotypes: atpMixedString
    """

    # FloatValueVariationPoint method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 7.13, p.240
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        super().__init__()


class IntegerValueVariationPoint(AttributeValueVariationPoint):
    """
    This class represents an attribute value variation point for Integer attributes. Note that this class might be used in the extended meta-model only.

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::AttributeValueVariationPoints
    Base: ARObject, AttributeValueVariationPoint, FormulaExpression, SwSystemconstDependentFormula
    Stereotypes: atpMixedString
    """

    # IntegerValueVariationPoint method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 7.14, p.241
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        super().__init__()


class PositiveIntegerValueVariationPoint(AttributeValueVariationPoint):
    """
    This class represents an attribute value variation point for positive Integer attributes.
    Note that this class might be used in the extended meta-model only.

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::AttributeValueVariationPoints
    Base: ARObject, AttributeValueVariationPoint, FormulaExpression, SwSystemconstDependentFormula
    Stereotypes: atpMixedString
    """

    # PositiveIntegerValueVariationPoint method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 7.17, p.241
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        super().__init__()


class UnlimitedIntegerValueVariationPoint(AttributeValueVariationPoint):
    """
    This class represents an attribute value variation point for unlimited Integer attributes. Note that this class might be used in the extended meta-model only.

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::AttributeValueVariationPoints
    Base: ARObject, AttributeValueVariationPoint, FormulaExpression, SwSystemconstDependentFormula
    Stereotypes: atpMixedString
    """

    # UnlimitedIntegerValueVariationPoint method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 7.18, p.242
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        super().__init__()


class TimeValueValueVariationPoint(AttributeValueVariationPoint):
    """
    This class represents the ability to express a formula for a numerical time value.

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::AttributeValueVariationPoints
    Base: ARObject, AttributeValueVariationPoint, FormulaExpression, SwSystemconstDependentFormula
    Stereotypes: atpMixedString
    """

    # TimeValueValueVariationPoint method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 7.19, p.242
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        super().__init__()
