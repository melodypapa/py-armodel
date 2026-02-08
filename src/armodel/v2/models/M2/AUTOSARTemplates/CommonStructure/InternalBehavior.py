from abc import ABC
from typing import List

from armodel.v2.models.M2.AUTOSARTemplates import (
    ConstantSpecification,
    ExclusiveAreaNesting,
    ParameterData,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class InternalBehavior(Identifiable, ABC):
    """
    Common base class (abstract) for the internal behavior of both software
    components and basic software modules/clusters.

    Package: M2::AUTOSARTemplates::CommonStructure::InternalBehavior::InternalBehavior

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 64, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 319, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 516, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2033, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 231, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 453, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is InternalBehavior:
            raise TypeError("InternalBehavior is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Describes a read only memory object containing characteristic value(s)
                # implemented by this Internal of ParameterDataPrototype has to be the ”C’
                # identifier of the described constant.
        # value(s) might be shared between Sw the same SwComponentType.
        # of constantMemory is subject to the purpose to support variability in the or
                # module implementations.
        # algorithms in the implementation are number of memory objects.
        # atpVariation.
        self._constant: List["ParameterData"] = []

    @property
    def constant(self) -> List["ParameterData"]:
        """Get constant (Pythonic accessor)."""
        return self._constant
        # Reference to the ConstantSpecificationMapping to be applied for the
        # particular InternalBehavior.
        self._constantValue: List["ConstantSpecification"] = []

    @property
    def constant_value(self) -> List["ConstantSpecification"]:
        """Get constantValue (Pythonic accessor)."""
        return self._constantValue
        # Reference to the DataTypeMapping to be applied for the InternalBehavior.
        self._dataType: List[RefType] = []

    @property
    def data_type(self) -> List[RefType]:
        """Get dataType (Pythonic accessor)."""
        return self._dataType
        # This represents the set of ExclusiveAreaNestingOrder owned by the
                # InternalBehavior.
        # atpVariation 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate
                # Module Description Template R23-11.
        self._exclusiveArea: List["ExclusiveAreaNesting"] = []

    @property
    def exclusive_area(self) -> List["ExclusiveAreaNesting"]:
        """Get exclusiveArea (Pythonic accessor)."""
        return self._exclusiveArea
        # Describes a read and writeable static memory object variables implemented by
                # component.
        # The term "static" is used in the "non-temporary" and does not necessarily
                # linker encapsulation.
        # This kind of memory is if supportsMultipleInstantiation is FALSE.
        # of the VariableDataPrototype has to be the ”C’ identifier of the described
                # variable.
        # of staticMemory is subject to variability purpose to support variability in
                # the software algorithms in the implementation are number of memory objects.
        # atpVariation.
        self._staticMemory: List[RefType] = []

    @property
    def static_memory(self) -> List[RefType]:
        """Get staticMemory (Pythonic accessor)."""
        return self._staticMemory

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConstant(self) -> List["ParameterData"]:
        """
        AUTOSAR-compliant getter for constant.

        Returns:
            The constant value

        Note:
            Delegates to constant property (CODING_RULE_V2_00017)
        """
        return self.constant  # Delegates to property

    def getConstantValue(self) -> List["ConstantSpecification"]:
        """
        AUTOSAR-compliant getter for constantValue.

        Returns:
            The constantValue value

        Note:
            Delegates to constant_value property (CODING_RULE_V2_00017)
        """
        return self.constant_value  # Delegates to property

    def getDataType(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for dataType.

        Returns:
            The dataType value

        Note:
            Delegates to data_type property (CODING_RULE_V2_00017)
        """
        return self.data_type  # Delegates to property

    def getExclusiveArea(self) -> List["ExclusiveAreaNesting"]:
        """
        AUTOSAR-compliant getter for exclusiveArea.

        Returns:
            The exclusiveArea value

        Note:
            Delegates to exclusive_area property (CODING_RULE_V2_00017)
        """
        return self.exclusive_area  # Delegates to property

    def getStaticMemory(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for staticMemory.

        Returns:
            The staticMemory value

        Note:
            Delegates to static_memory property (CODING_RULE_V2_00017)
        """
        return self.static_memory  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
