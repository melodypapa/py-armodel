"""
AUTOSAR Package - EnvironmentalCondition

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::EnvironmentalCondition
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import (
    DiagnosticCommonElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Referrable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)




class DiagnosticEnvironmentalCondition(DiagnosticCommonElement):
    """
    The meta-class DiagnosticEnvironmentalCondition formalizes the idea of a
    condition which is evaluated during runtime of the ECU by looking at
    "environmental" states (e.g. one such condition is that the vehicle is not
    driving, i.e. vehicle speed == 0).
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::EnvironmentalCondition::DiagnosticEnvironmentalCondition
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 79, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents the formula part of the.
        self._formula: Optional["DiagnosticEnvCondition"] = None

    @property
    def formula(self) -> Optional["DiagnosticEnvCondition"]:
        """Get formula (Pythonic accessor)."""
        return self._formula

    @formula.setter
    def formula(self, value: Optional["DiagnosticEnvCondition"]) -> None:
        """
        Set formula with validation.
        
        Args:
            value: The formula to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._formula = None
            return

        if not isinstance(value, DiagnosticEnvCondition):
            raise TypeError(
                f"formula must be DiagnosticEnvCondition or None, got {type(value).__name__}"
            )
        self._formula = value
        # This aggregation contains a representation of Mode in the context of a
        # DiagnosticEnvironmental.
        self._modeElement: List["DiagnosticEnvMode"] = []

    @property
    def mode_element(self) -> List["DiagnosticEnvMode"]:
        """Get modeElement (Pythonic accessor)."""
        return self._modeElement

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFormula(self) -> "DiagnosticEnvCondition":
        """
        AUTOSAR-compliant getter for formula.
        
        Returns:
            The formula value
        
        Note:
            Delegates to formula property (CODING_RULE_V2_00017)
        """
        return self.formula  # Delegates to property

    def setFormula(self, value: "DiagnosticEnvCondition") -> "DiagnosticEnvironmentalCondition":
        """
        AUTOSAR-compliant setter for formula with method chaining.
        
        Args:
            value: The formula to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to formula property setter (gets validation automatically)
        """
        self.formula = value  # Delegates to property setter
        return self

    def getModeElement(self) -> List["DiagnosticEnvMode"]:
        """
        AUTOSAR-compliant getter for modeElement.
        
        Returns:
            The modeElement value
        
        Note:
            Delegates to mode_element property (CODING_RULE_V2_00017)
        """
        return self.mode_element  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_formula(self, value: Optional["DiagnosticEnvCondition"]) -> "DiagnosticEnvironmentalCondition":
        """
        Set formula and return self for chaining.
        
        Args:
            value: The formula to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_formula("value")
        """
        self.formula = value  # Use property setter (gets validation)
        return self



class DiagnosticEnvConditionFormulaPart(ARObject, ABC):
    """
    A DiagnosticEnvConditionFormulaPart can either be a atomic condition, e.g. a
    DiagnosticEnvCompare Condition, or a DiagnosticEnvConditionFormula, again,
    which allows arbitrary nesting.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::EnvironmentalCondition::DiagnosticEnvConditionFormulaPart
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 80, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticEnvConditionFormulaPart:
            raise TypeError("DiagnosticEnvConditionFormulaPart is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticEnvModeElement(Referrable, ABC):
    """
    All ModeDeclarations that are referenced in a DiagnosticEnvModeCondition
    shall be defined as a DiagnosticEnvModeElement of this
    DiagnosticEnvironmentalCondition. This concept keeps the ARXML clean: It
    avoids that the DiagnosticEnvConditionFormula is cluttered by lengthy
    InstanceRef definitions. Furthermore, it allows that an InstanceRef only
    needs to be defined once and can be used multiple times in the different
    DiagnosticEnvModeConditions.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::EnvironmentalCondition::DiagnosticEnvModeElement
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 89, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticEnvModeElement:
            raise TypeError("DiagnosticEnvModeElement is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticEnvConditionFormula(DiagnosticEnvConditionFormulaPart):
    """
    A DiagnosticEnvConditionFormula embodies the computation instruction that is
    to be evaluated at runtime to determine if the
    DiagnosticEnvironmentalCondition is currently present (i.e. the formula is
    evaluated to true) or not (otherwise). The formula itself consists of parts
    which are combined by the logical operations specified by
    DiagnosticEnvConditionFormula.op. If a diagnostic functionality cannot be
    executed because an environmental condition fails then the diagnostic stack
    shall send a negative response code (NRC) back to the client. The value of
    the NRC is directly related to the specific formula and is therefore
    formalized in the attribute DiagnosticEnvCondition Formula.nrcValue.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::EnvironmentalCondition::DiagnosticEnvConditionFormula
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 80, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents the concrete NRC value that returned if the
        # condition fails.
        self._nrcValue: Optional["PositiveInteger"] = None

    @property
    def nrc_value(self) -> Optional["PositiveInteger"]:
        """Get nrcValue (Pythonic accessor)."""
        return self._nrcValue

    @nrc_value.setter
    def nrc_value(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set nrcValue with validation.
        
        Args:
            value: The nrcValue to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nrcValue = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"nrcValue must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._nrcValue = value
        # This attribute represents the concrete operator operators: and, or) of the
                # condition formula.
        # DiagnosticEnvCondition * aggr This aggregation represents the collection of
                # formula that can be combined by logical operators.
        self._op: Optional["DiagnosticLogical"] = None

    @property
    def op(self) -> Optional["DiagnosticLogical"]:
        """Get op (Pythonic accessor)."""
        return self._op

    @op.setter
    def op(self, value: Optional["DiagnosticLogical"]) -> None:
        """
        Set op with validation.
        
        Args:
            value: The op to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._op = None
            return

        if not isinstance(value, DiagnosticLogical):
            raise TypeError(
                f"op must be DiagnosticLogical or None, got {type(value).__name__}"
            )
        self._op = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNrcValue(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for nrcValue.
        
        Returns:
            The nrcValue value
        
        Note:
            Delegates to nrc_value property (CODING_RULE_V2_00017)
        """
        return self.nrc_value  # Delegates to property

    def setNrcValue(self, value: "PositiveInteger") -> "DiagnosticEnvConditionFormula":
        """
        AUTOSAR-compliant setter for nrcValue with method chaining.
        
        Args:
            value: The nrcValue to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to nrc_value property setter (gets validation automatically)
        """
        self.nrc_value = value  # Delegates to property setter
        return self

    def getOp(self) -> "DiagnosticLogical":
        """
        AUTOSAR-compliant getter for op.
        
        Returns:
            The op value
        
        Note:
            Delegates to op property (CODING_RULE_V2_00017)
        """
        return self.op  # Delegates to property

    def setOp(self, value: "DiagnosticLogical") -> "DiagnosticEnvConditionFormula":
        """
        AUTOSAR-compliant setter for op with method chaining.
        
        Args:
            value: The op to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to op property setter (gets validation automatically)
        """
        self.op = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_nrc_value(self, value: Optional["PositiveInteger"]) -> "DiagnosticEnvConditionFormula":
        """
        Set nrcValue and return self for chaining.
        
        Args:
            value: The nrcValue to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_nrc_value("value")
        """
        self.nrc_value = value  # Use property setter (gets validation)
        return self

    def with_op(self, value: Optional["DiagnosticLogical"]) -> "DiagnosticEnvConditionFormula":
        """
        Set op and return self for chaining.
        
        Args:
            value: The op to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_op("value")
        """
        self.op = value  # Use property setter (gets validation)
        return self



class DiagnosticEnvCompareCondition(DiagnosticEnvConditionFormulaPart, ABC):
    """
    DiagnosticCompareConditions are atomic conditions. They are based on the
    idea of a comparison at runtime of some variable data with something
    constant. The type of the comparison (==, !=, <, <=, ...) is specified in
    DiagnosticCompareCondition.compareType.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::EnvironmentalCondition::DiagnosticEnvCompareCondition
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 82, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticEnvCompareCondition:
            raise TypeError("DiagnosticEnvCompareCondition is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attributes represents the concrete type of the.
        self._compareType: Optional["DiagnosticCompare"] = None

    @property
    def compare_type(self) -> Optional["DiagnosticCompare"]:
        """Get compareType (Pythonic accessor)."""
        return self._compareType

    @compare_type.setter
    def compare_type(self, value: Optional["DiagnosticCompare"]) -> None:
        """
        Set compareType with validation.
        
        Args:
            value: The compareType to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._compareType = None
            return

        if not isinstance(value, DiagnosticCompare):
            raise TypeError(
                f"compareType must be DiagnosticCompare or None, got {type(value).__name__}"
            )
        self._compareType = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCompareType(self) -> "DiagnosticCompare":
        """
        AUTOSAR-compliant getter for compareType.
        
        Returns:
            The compareType value
        
        Note:
            Delegates to compare_type property (CODING_RULE_V2_00017)
        """
        return self.compare_type  # Delegates to property

    def setCompareType(self, value: "DiagnosticCompare") -> "DiagnosticEnvCompareCondition":
        """
        AUTOSAR-compliant setter for compareType with method chaining.
        
        Args:
            value: The compareType to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to compare_type property setter (gets validation automatically)
        """
        self.compare_type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_compare_type(self, value: Optional["DiagnosticCompare"]) -> "DiagnosticEnvCompareCondition":
        """
        Set compareType and return self for chaining.
        
        Args:
            value: The compareType to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_compare_type("value")
        """
        self.compare_type = value  # Use property setter (gets validation)
        return self



class DiagnosticEnvSwcModeElement(DiagnosticEnvModeElement):
    """
    This meta-class represents the ability to refer to a ModeDeclaration in a
    concrete System context.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::EnvironmentalCondition::DiagnosticEnvSwcModeElement
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 89, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # the ModeDeclaration for the specific mode by: PModeInSystemInstance.
        self._mode: Optional["ModeDeclaration"] = None

    @property
    def mode(self) -> Optional["ModeDeclaration"]:
        """Get mode (Pythonic accessor)."""
        return self._mode

    @mode.setter
    def mode(self, value: Optional["ModeDeclaration"]) -> None:
        """
        Set mode with validation.
        
        Args:
            value: The mode to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mode = None
            return

        if not isinstance(value, ModeDeclaration):
            raise TypeError(
                f"mode must be ModeDeclaration or None, got {type(value).__name__}"
            )
        self._mode = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMode(self) -> "ModeDeclaration":
        """
        AUTOSAR-compliant getter for mode.
        
        Returns:
            The mode value
        
        Note:
            Delegates to mode property (CODING_RULE_V2_00017)
        """
        return self.mode  # Delegates to property

    def setMode(self, value: "ModeDeclaration") -> "DiagnosticEnvSwcModeElement":
        """
        AUTOSAR-compliant setter for mode with method chaining.
        
        Args:
            value: The mode to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to mode property setter (gets validation automatically)
        """
        self.mode = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mode(self, value: Optional["ModeDeclaration"]) -> "DiagnosticEnvSwcModeElement":
        """
        Set mode and return self for chaining.
        
        Args:
            value: The mode to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_mode("value")
        """
        self.mode = value  # Use property setter (gets validation)
        return self



class DiagnosticEnvBswModeElement(DiagnosticEnvModeElement):
    """
    This meta-class represents the ability to refer to a specific
    ModeDeclaration in the scope of a BswModule Description.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::EnvironmentalCondition::DiagnosticEnvBswModeElement
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 90, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # the ModeDeclaration for the specific mode by: ModeInBswModule.
        self._mode: Optional["ModeDeclaration"] = None

    @property
    def mode(self) -> Optional["ModeDeclaration"]:
        """Get mode (Pythonic accessor)."""
        return self._mode

    @mode.setter
    def mode(self, value: Optional["ModeDeclaration"]) -> None:
        """
        Set mode with validation.
        
        Args:
            value: The mode to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mode = None
            return

        if not isinstance(value, ModeDeclaration):
            raise TypeError(
                f"mode must be ModeDeclaration or None, got {type(value).__name__}"
            )
        self._mode = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMode(self) -> "ModeDeclaration":
        """
        AUTOSAR-compliant getter for mode.
        
        Returns:
            The mode value
        
        Note:
            Delegates to mode property (CODING_RULE_V2_00017)
        """
        return self.mode  # Delegates to property

    def setMode(self, value: "ModeDeclaration") -> "DiagnosticEnvBswModeElement":
        """
        AUTOSAR-compliant setter for mode with method chaining.
        
        Args:
            value: The mode to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to mode property setter (gets validation automatically)
        """
        self.mode = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mode(self, value: Optional["ModeDeclaration"]) -> "DiagnosticEnvBswModeElement":
        """
        Set mode and return self for chaining.
        
        Args:
            value: The mode to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_mode("value")
        """
        self.mode = value  # Use property setter (gets validation)
        return self



class DiagnosticEnvDataCondition(DiagnosticEnvCompareCondition):
    """
    A DiagnosticEnvDataCondition is an atomic condition that compares the
    current value of the referenced DiagnosticDataElement with a constant value
    defined by the ValueSpecification. All compareTypes are supported.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::EnvironmentalCondition::DiagnosticEnvDataCondition
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 84, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents a fixed compare value taken to compare condition.
        self._compareValue: Optional["ValueSpecification"] = None

    @property
    def compare_value(self) -> Optional["ValueSpecification"]:
        """Get compareValue (Pythonic accessor)."""
        return self._compareValue

    @compare_value.setter
    def compare_value(self, value: Optional["ValueSpecification"]) -> None:
        """
        Set compareValue with validation.
        
        Args:
            value: The compareValue to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._compareValue = None
            return

        if not isinstance(value, ValueSpecification):
            raise TypeError(
                f"compareValue must be ValueSpecification or None, got {type(value).__name__}"
            )
        self._compareValue = value
        # This reference represents the related diagnostic data.
        self._dataElement: Optional["DiagnosticDataElement"] = None

    @property
    def data_element(self) -> Optional["DiagnosticDataElement"]:
        """Get dataElement (Pythonic accessor)."""
        return self._dataElement

    @data_element.setter
    def data_element(self, value: Optional["DiagnosticDataElement"]) -> None:
        """
        Set dataElement with validation.
        
        Args:
            value: The dataElement to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataElement = None
            return

        if not isinstance(value, DiagnosticDataElement):
            raise TypeError(
                f"dataElement must be DiagnosticDataElement or None, got {type(value).__name__}"
            )
        self._dataElement = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCompareValue(self) -> "ValueSpecification":
        """
        AUTOSAR-compliant getter for compareValue.
        
        Returns:
            The compareValue value
        
        Note:
            Delegates to compare_value property (CODING_RULE_V2_00017)
        """
        return self.compare_value  # Delegates to property

    def setCompareValue(self, value: "ValueSpecification") -> "DiagnosticEnvDataCondition":
        """
        AUTOSAR-compliant setter for compareValue with method chaining.
        
        Args:
            value: The compareValue to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to compare_value property setter (gets validation automatically)
        """
        self.compare_value = value  # Delegates to property setter
        return self

    def getDataElement(self) -> "DiagnosticDataElement":
        """
        AUTOSAR-compliant getter for dataElement.
        
        Returns:
            The dataElement value
        
        Note:
            Delegates to data_element property (CODING_RULE_V2_00017)
        """
        return self.data_element  # Delegates to property

    def setDataElement(self, value: "DiagnosticDataElement") -> "DiagnosticEnvDataCondition":
        """
        AUTOSAR-compliant setter for dataElement with method chaining.
        
        Args:
            value: The dataElement to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to data_element property setter (gets validation automatically)
        """
        self.data_element = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_compare_value(self, value: Optional["ValueSpecification"]) -> "DiagnosticEnvDataCondition":
        """
        Set compareValue and return self for chaining.
        
        Args:
            value: The compareValue to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_compare_value("value")
        """
        self.compare_value = value  # Use property setter (gets validation)
        return self

    def with_data_element(self, value: Optional["DiagnosticDataElement"]) -> "DiagnosticEnvDataCondition":
        """
        Set dataElement and return self for chaining.
        
        Args:
            value: The dataElement to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_data_element("value")
        """
        self.data_element = value  # Use property setter (gets validation)
        return self



class DiagnosticEnvDataElementCondition(DiagnosticEnvCompareCondition):
    """
    This meta-class represents the ability to formulate a diagnostic environment
    condition based on the value of a data element owned by the application
    software.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::EnvironmentalCondition::DiagnosticEnvDataElementCondition
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 85, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation represents the definition of the compare which the value
        # taken from the application be compared.
        self._compareValue: Optional["ValueSpecification"] = None

    @property
    def compare_value(self) -> Optional["ValueSpecification"]:
        """Get compareValue (Pythonic accessor)."""
        return self._compareValue

    @compare_value.setter
    def compare_value(self, value: Optional["ValueSpecification"]) -> None:
        """
        Set compareValue with validation.
        
        Args:
            value: The compareValue to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._compareValue = None
            return

        if not isinstance(value, ValueSpecification):
            raise TypeError(
                f"compareValue must be ValueSpecification or None, got {type(value).__name__}"
            )
        self._compareValue = value
        # by the application software on the platform.
        # by: DataPrototypeInSystem.
        self._dataPrototype: Optional["RefType"] = None

    @property
    def data_prototype(self) -> Optional["RefType"]:
        """Get dataPrototype (Pythonic accessor)."""
        return self._dataPrototype

    @data_prototype.setter
    def data_prototype(self, value: Optional["RefType"]) -> None:
        """
        Set dataPrototype with validation.
        
        Args:
            value: The dataPrototype to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataPrototype = None
            return

        self._dataPrototype = value
        # Via this aggregation it is possible to describe the of the data that is
        # obtained from the application environmental condition.
        self._swDataDef: Optional["SwDataDefProps"] = None

    @property
    def sw_data_def(self) -> Optional["SwDataDefProps"]:
        """Get swDataDef (Pythonic accessor)."""
        return self._swDataDef

    @sw_data_def.setter
    def sw_data_def(self, value: Optional["SwDataDefProps"]) -> None:
        """
        Set swDataDef with validation.
        
        Args:
            value: The swDataDef to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swDataDef = None
            return

        if not isinstance(value, SwDataDefProps):
            raise TypeError(
                f"swDataDef must be SwDataDefProps or None, got {type(value).__name__}"
            )
        self._swDataDef = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCompareValue(self) -> "ValueSpecification":
        """
        AUTOSAR-compliant getter for compareValue.
        
        Returns:
            The compareValue value
        
        Note:
            Delegates to compare_value property (CODING_RULE_V2_00017)
        """
        return self.compare_value  # Delegates to property

    def setCompareValue(self, value: "ValueSpecification") -> "DiagnosticEnvDataElementCondition":
        """
        AUTOSAR-compliant setter for compareValue with method chaining.
        
        Args:
            value: The compareValue to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to compare_value property setter (gets validation automatically)
        """
        self.compare_value = value  # Delegates to property setter
        return self

    def getDataPrototype(self) -> "RefType":
        """
        AUTOSAR-compliant getter for dataPrototype.
        
        Returns:
            The dataPrototype value
        
        Note:
            Delegates to data_prototype property (CODING_RULE_V2_00017)
        """
        return self.data_prototype  # Delegates to property

    def setDataPrototype(self, value: "RefType") -> "DiagnosticEnvDataElementCondition":
        """
        AUTOSAR-compliant setter for dataPrototype with method chaining.
        
        Args:
            value: The dataPrototype to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to data_prototype property setter (gets validation automatically)
        """
        self.data_prototype = value  # Delegates to property setter
        return self

    def getSwDataDef(self) -> "SwDataDefProps":
        """
        AUTOSAR-compliant getter for swDataDef.
        
        Returns:
            The swDataDef value
        
        Note:
            Delegates to sw_data_def property (CODING_RULE_V2_00017)
        """
        return self.sw_data_def  # Delegates to property

    def setSwDataDef(self, value: "SwDataDefProps") -> "DiagnosticEnvDataElementCondition":
        """
        AUTOSAR-compliant setter for swDataDef with method chaining.
        
        Args:
            value: The swDataDef to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_data_def property setter (gets validation automatically)
        """
        self.sw_data_def = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_compare_value(self, value: Optional["ValueSpecification"]) -> "DiagnosticEnvDataElementCondition":
        """
        Set compareValue and return self for chaining.
        
        Args:
            value: The compareValue to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_compare_value("value")
        """
        self.compare_value = value  # Use property setter (gets validation)
        return self

    def with_data_prototype(self, value: Optional[RefType]) -> "DiagnosticEnvDataElementCondition":
        """
        Set dataPrototype and return self for chaining.
        
        Args:
            value: The dataPrototype to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_data_prototype("value")
        """
        self.data_prototype = value  # Use property setter (gets validation)
        return self

    def with_sw_data_def(self, value: Optional["SwDataDefProps"]) -> "DiagnosticEnvDataElementCondition":
        """
        Set swDataDef and return self for chaining.
        
        Args:
            value: The swDataDef to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_data_def("value")
        """
        self.sw_data_def = value  # Use property setter (gets validation)
        return self



class DiagnosticEnvModeCondition(DiagnosticEnvCompareCondition):
    """
    DiagnosticEnvModeCondition are atomic condition based on the comparison of
    the active Mode Declaration in a ModeDeclarationGroupProtoype with the
    constant value of a ModeDeclaration. The formulation of this condition uses
    only one DiagnosticEnvElement, which contains enough information to deduce
    the variable part (i.e. the part that changes at runtime) as well as the
    constant part of the comparison. Only DiagnosticCompareTypeEnum.isEqual or
    DiagnosticCompareTypeEnum.isNotEqual are eligible values for
    DiagnosticAtomicCondition.compareType.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::EnvironmentalCondition::DiagnosticEnvModeCondition
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 88, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference represents both the ModeDeclaration and the ModeDeclaration
        # relevant for the.
        self._modeElement: Optional["DiagnosticEnvMode"] = None

    @property
    def mode_element(self) -> Optional["DiagnosticEnvMode"]:
        """Get modeElement (Pythonic accessor)."""
        return self._modeElement

    @mode_element.setter
    def mode_element(self, value: Optional["DiagnosticEnvMode"]) -> None:
        """
        Set modeElement with validation.
        
        Args:
            value: The modeElement to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._modeElement = None
            return

        if not isinstance(value, DiagnosticEnvMode):
            raise TypeError(
                f"modeElement must be DiagnosticEnvMode or None, got {type(value).__name__}"
            )
        self._modeElement = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getModeElement(self) -> "DiagnosticEnvMode":
        """
        AUTOSAR-compliant getter for modeElement.
        
        Returns:
            The modeElement value
        
        Note:
            Delegates to mode_element property (CODING_RULE_V2_00017)
        """
        return self.mode_element  # Delegates to property

    def setModeElement(self, value: "DiagnosticEnvMode") -> "DiagnosticEnvModeCondition":
        """
        AUTOSAR-compliant setter for modeElement with method chaining.
        
        Args:
            value: The modeElement to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to mode_element property setter (gets validation automatically)
        """
        self.mode_element = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mode_element(self, value: Optional["DiagnosticEnvMode"]) -> "DiagnosticEnvModeCondition":
        """
        Set modeElement and return self for chaining.
        
        Args:
            value: The modeElement to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_mode_element("value")
        """
        self.mode_element = value  # Use property setter (gets validation)
        return self


class DiagnosticLogicalOperatorEnum(AREnum):
    """
    DiagnosticLogicalOperatorEnum enumeration

Logical AND and OR operation (&&, ||) Aggregated by DiagnosticEnvConditionFormula.op

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::EnvironmentalCondition
    """
    # Logical AND
    logicalAnd = "0"

    # Logical OR
    logicalOr = "1"



class DiagnosticCompareTypeEnum(AREnum):
    """
    DiagnosticCompareTypeEnum enumeration

Enumeration for the type of a comparison of values usually expressed by the following operators: ==, !=, <, <=, >, >= Aggregated by DiagnosticEnvCompareCondition.compareType

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::EnvironmentalCondition
    """
    # equal isGreaterOrEqual greater than or equal isGreaterThan greater than isLessOrEqual less than or equal isLessThan less than isNotEqual not equal
    isEqual = "1"
