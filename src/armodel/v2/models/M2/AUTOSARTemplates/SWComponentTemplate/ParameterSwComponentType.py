from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
    SwComponentType,
)

    RefType,
)


class ParameterSwComponentType(SwComponentType):
    """
    The ParameterSwComponentType defines parameters and characteristic values
    accessible via provided Ports. The provided values are the same for all
    connected SwComponentPrototypes

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 41, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2043, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the ConstantSpecificationMapping to be applied for the
        # particular ParameterSwComponentType.
        self._constant: List["ConstantSpecification"] = []

    @property
    def constant(self) -> List["ConstantSpecification"]:
        """Get constant (Pythonic accessor)."""
        return self._constant
        # Reference to the DataTypeMapping to be applied for the
        # ParameterSwComponentType.
        self._dataType: List[RefType] = []

    @property
    def data_type(self) -> List[RefType]:
        """Get dataType (Pythonic accessor)."""
        return self._dataType
        # The purpose of this is that within the context of a given SwComponentType
                # some data def properties of individual be modified.
        # of InstantiationDataDefProps is subject with the purpose to support the
                # conditional PortPrototypes atpVariation.
        self._instantiation: List["InstantiationDataDef"] = []

    @property
    def instantiation(self) -> List["InstantiationDataDef"]:
        """Get instantiation (Pythonic accessor)."""
        return self._instantiation

    def with_constant(self, value):
        """
        Set constant and return self for chaining.

        Args:
            value: The constant to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_constant("value")
        """
        self.constant = value  # Use property setter (gets validation)
        return self

    def with_data_type(self, value):
        """
        Set data_type and return self for chaining.

        Args:
            value: The data_type to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_type("value")
        """
        self.data_type = value  # Use property setter (gets validation)
        return self

    def with_instantiation(self, value):
        """
        Set instantiation and return self for chaining.

        Args:
            value: The instantiation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_instantiation("value")
        """
        self.instantiation = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConstant(self) -> List["ConstantSpecification"]:
        """
        AUTOSAR-compliant getter for constant.

        Returns:
            The constant value

        Note:
            Delegates to constant property (CODING_RULE_V2_00017)
        """
        return self.constant  # Delegates to property

    def getDataType(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for dataType.

        Returns:
            The dataType value

        Note:
            Delegates to data_type property (CODING_RULE_V2_00017)
        """
        return self.data_type  # Delegates to property

    def getInstantiation(self) -> List["InstantiationDataDef"]:
        """
        AUTOSAR-compliant getter for instantiation.

        Returns:
            The instantiation value

        Note:
            Delegates to instantiation property (CODING_RULE_V2_00017)
        """
        return self.instantiation  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
