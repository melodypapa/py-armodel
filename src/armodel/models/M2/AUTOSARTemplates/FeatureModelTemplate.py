from abc import ABC
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.FormulaLanguage import FormulaExpression
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import SwSystemconstDependentFormula
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

__all__ = ["FMConditionByFeaturesAndAttributes", "FMConditionByFeaturesAndSwSystemconsts", "FMFormulaByFeaturesAndAttributes", "FMFormulaByFeaturesAndSwSystemconsts"]


class FMFormulaByFeaturesAndAttributes(FormulaExpression, ABC):
    """An expression that has the syntax of the AUTOSAR formula language but uses only references to features or feature attributes (not system constants) as operands."""

    # FMFormulaByFeaturesAndAttributes method parity checklist:
    # Spec: R23-11/AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf, Table 7.1, p.61 (R23-11)
    # Spec verified: R23-11 (2026-09-27, user 9b confirmation)
    # (section 7.2.1; R4.3.1 reproduction Table 7.1 has the same rows (p.61,
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAttributeRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAttributeRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFeatureRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFeatureRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is FMFormulaByFeaturesAndAttributes:
            raise TypeError("FMFormulaByFeaturesAndAttributes is an abstract class.")

        super().__init__()

        # An expression of type FMFormulaByFeaturesAndAttributes may refer to attributes of FMFeatures.
        self.attributeRef: Optional[RefType] = None

        # An expression of type FMFormulaByFeaturesAndAttributes may refer to FMFeatures.
        self.featureRef: Optional[RefType] = None

    def getAttributeRef(self) -> Optional[RefType]:
        """An expression of type FMFormulaByFeaturesAndAttributes may refer to attributes of FMFeatures."""
        return self.attributeRef

    def setAttributeRef(self, value: Optional[RefType]) -> "FMFormulaByFeaturesAndAttributes":
        """An expression of type FMFormulaByFeaturesAndAttributes may refer to attributes of FMFeatures. A None value is a no-op and does not overwrite an existing attributeRef."""
        if value is not None:
            self.attributeRef = value
        return self

    def getFeatureRef(self) -> Optional[RefType]:
        """An expression of type FMFormulaByFeaturesAndAttributes may refer to FMFeatures."""
        return self.featureRef

    def setFeatureRef(self, value: Optional[RefType]) -> "FMFormulaByFeaturesAndAttributes":
        """An expression of type FMFormulaByFeaturesAndAttributes may refer to FMFeatures. A None value is a no-op and does not overwrite an existing featureRef."""
        if value is not None:
            self.featureRef = value
        return self


class FMConditionByFeaturesAndAttributes(FMFormulaByFeaturesAndAttributes):
    """A boolean expression that has the syntax of the AUTOSAR formula language but uses only references to features or feature attributes (not system constants) as operands."""

    # FMConditionByFeaturesAndAttributes method parity checklist:
    # Spec: R23-11/AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf, Table 7.2, p.62 (R23-11)
    # Spec verified: R23-11 (2026-09-27, user 9b confirmation)
    # (section 7.2.2; R4.3.1 reproduction Table 7.2 has the same rows (p.62, AUTOSAR_TPS_

    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # (no methods — Table 7.2 declares no attribute rows; getMixedString / setMixedString
    # provided by the AtpMixedString mixin and get/addAtpReference(s) inherited from
    # FormulaExpression — no spec rows; get/setAttributeRef and get/setFeatureRef are
    # inherited from FMFormulaByFeaturesAndAttributes (Table 7.1) — no Table 7.2 rows;
    # the class-level reader/writer coverage lives in the own helper pair, test-pinned by
    # tests/test_armodel/parser/test_parser_fm_condition_by_features_and_attributes.py
    # and tests/test_armodel/writer/test_writer_fm_condition_by_features_and_attributes.py)

    def __init__(self):
        super().__init__()


class FMFormulaByFeaturesAndSwSystemconsts(SwSystemconstDependentFormula, ABC):
    """An expression that has the syntax of the AUTOSAR formula language and may use references to features or system constants as operands.

    [constr_3667] Multiplicity of FMFormulaByFeaturesAndSwSystemconsts.feature ⎡ For each FMFormulaByFeaturesAndSwSystemconsts the reference in the role feature shall exist. ⎤ ()
    """

    # FMFormulaByFeaturesAndSwSystemconsts method parity checklist:
    # Spec: R23-11/AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf, Table 7.3, p.63 (R23-11)
    # Spec verified: R23-11 (2026-09-27, user 9b confirmation)
    # (section 7.2.3; R4.3.1 reproduction Table 7.3 has the same rows (p.63,
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getFeatureRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFeatureRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is FMFormulaByFeaturesAndSwSystemconsts:
            raise TypeError("FMFormulaByFeaturesAndSwSystemconsts is an abstract class.")

        super().__init__()

        # An expression of type FMFormulaByFeaturesAndSwSystemconsts may refer to FMFeatures.
        self.featureRef: Optional[RefType] = None

    def getFeatureRef(self) -> Optional[RefType]:
        """An expression of type FMFormulaByFeaturesAndSwSystemconsts may refer to FMFeatures."""
        return self.featureRef

    def setFeatureRef(self, value: Optional[RefType]) -> "FMFormulaByFeaturesAndSwSystemconsts":
        """An expression of type FMFormulaByFeaturesAndSwSystemconsts may refer to FMFeatures. A None value is a no-op and does not overwrite an existing featureRef."""
        if value is not None:
            self.featureRef = value
        return self


class FMConditionByFeaturesAndSwSystemconsts(FMFormulaByFeaturesAndSwSystemconsts):
    """A boolean expression that has the syntax of the AUTOSAR formula language and may use references to features or system constants as operands.

    [TPS_FMDT_00050] The result of FMConditionByFeaturesAndSwSystemconsts is interpreted as a boolean value. The result of a formula of class FMConditionByFeaturesAndSwSystemconsts shall be interpreted as a boolean value.
    """

    # FMConditionByFeaturesAndSwSystemconsts method parity checklist:
    # Spec: R23-11/AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf, Table 7.4, p.63 (R23-11)
    # Spec verified: R23-11 (2026-09-27, user 9b confirmation)
    # (section 7.2.4; R4.3.1 reproduction Table 7.4 has the same rows (p.63,
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # (no methods - Table 7.4 declares no attribute rows; getMixedString /
    # setMixedString provided by the AtpMixedString mixin, get/setFeatureRef
    # inherited from FMFormulaByFeaturesAndSwSystemconsts (Table 7.3), and
    # get/setSyscRef + get/setSyscStringRef inherited from
    # SwSystemconstDependentFormula (Table 7.10, stamped) - no Table 7.4 rows;
    # the class-level reader/writer coverage lives in the own helper pair.)

    def __init__(self):
        super().__init__()
