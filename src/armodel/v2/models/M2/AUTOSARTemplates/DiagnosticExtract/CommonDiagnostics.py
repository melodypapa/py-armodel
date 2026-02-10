"""
AUTOSAR Package - CommonDiagnostics

Package: M2::AUTOSARTemplates::DiagnosticExtract::CommonDiagnostics
"""

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import (
    IdentCaption,
)


class DiagnosticCommonElement(ARElement, ABC):
    """
    This meta-class represents a common base class for all diagnostic elements.
    It does not contribute any specific functionality other than the ability to
    become the target of a reference.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::CommonDiagnostics::DiagnosticCommonElement

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 32, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticCommonElement:
            raise TypeError("DiagnosticCommonElement is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    def with_sub_element(self, value):
        """
        Set sub_element and return self for chaining.

        Args:
            value: The sub_element to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sub_element("value")
        """
        self.sub_element = value  # Use property setter (gets validation)
        return self

    def with_sub_element(self, value):
        """
        Set sub_element and return self for chaining.

        Args:
            value: The sub_element to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sub_element("value")
        """
        self.sub_element = value  # Use property setter (gets validation)
        return self

    def with_request(self, value):
        """
        Set request and return self for chaining.

        Args:
            value: The request to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_request("value")
        """
        self.request = value  # Use property setter (gets validation)
        return self

    def with_response(self, value):
        """
        Set response and return self for chaining.

        Args:
            value: The response to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_response("value")
        """
        self.response = value  # Use property setter (gets validation)
        return self

    def with_request(self, value):
        """
        Set request and return self for chaining.

        Args:
            value: The request to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_request("value")
        """
        self.request = value  # Use property setter (gets validation)
        return self

    def with_response(self, value):
        """
        Set response and return self for chaining.

        Args:
            value: The response to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_response("value")
        """
        self.response = value  # Use property setter (gets validation)
        return self

    def with_request(self, value):
        """
        Set request and return self for chaining.

        Args:
            value: The request to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_request("value")
        """
        self.request = value  # Use property setter (gets validation)
        return self

    def with_response(self, value):
        """
        Set response and return self for chaining.

        Args:
            value: The response to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_response("value")
        """
        self.response = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticParameterElement(Identifiable):
    """
    This meta-class represents an element of a DiagnosticParameter if the
    DiagnosticParameter represents a structure.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::CommonDiagnostics::DiagnosticParameterElement

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 36, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute indicates that the enclosing Diagnostic an array and
        # configures size in terms of the number of elements of the.
        self._arraySize: Optional["PositiveInteger"] = None

    @property
    def array_size(self) -> Optional["PositiveInteger"]:
        """Get arraySize (Pythonic accessor)."""
        return self._arraySize

    @array_size.setter
    def array_size(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set arraySize with validation.

        Args:
            value: The arraySize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._arraySize = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"arraySize must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._arraySize = value
        self._subElement: List["DiagnosticParameter"] = []

    @property
    def sub_element(self) -> List["DiagnosticParameter"]:
        """Get subElement (Pythonic accessor)."""
        return self._subElement

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArraySize(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for arraySize.

        Returns:
            The arraySize value

        Note:
            Delegates to array_size property (CODING_RULE_V2_00017)
        """
        return self.array_size  # Delegates to property

    def setArraySize(self, value: "PositiveInteger") -> "DiagnosticParameterElement":
        """
        AUTOSAR-compliant setter for arraySize with method chaining.

        Args:
            value: The arraySize to set

        Returns:
            self for method chaining

        Note:
            Delegates to array_size property setter (gets validation automatically)
        """
        self.array_size = value  # Delegates to property setter
        return self

    def getSubElement(self) -> List["DiagnosticParameter"]:
        """
        AUTOSAR-compliant getter for subElement.

        Returns:
            The subElement value

        Note:
            Delegates to sub_element property (CODING_RULE_V2_00017)
        """
        return self.sub_element  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_array_size(self, value: Optional["PositiveInteger"]) -> "DiagnosticParameterElement":
        """
        Set arraySize and return self for chaining.

        Args:
            value: The arraySize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_array_size("value")
        """
        self.array_size = value  # Use property setter (gets validation)
        return self



class DiagnosticParameterIdent(IdentCaption):
    """
    This meta-class has been created to introduce the ability to become
    referenced into the meta-class AbstractDiagnosticParameter without breaking
    backwards compatibility.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::CommonDiagnostics::DiagnosticParameterIdent

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 37, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This collection represents the subElements on the top.
        self._subElement: List["DiagnosticParameter"] = []

    @property
    def sub_element(self) -> List["DiagnosticParameter"]:
        """Get subElement (Pythonic accessor)."""
        return self._subElement

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSubElement(self) -> List["DiagnosticParameter"]:
        """
        AUTOSAR-compliant getter for subElement.

        Returns:
            The subElement value

        Note:
            Delegates to sub_element property (CODING_RULE_V2_00017)
        """
        return self.sub_element  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticAbstractParameter(ARObject, ABC):
    """
    This meta-class represents an abstract base class for modeling a diagnostic
    parameter.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::CommonDiagnostics::DiagnosticAbstractParameter

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 37, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticAbstractParameter:
            raise TypeError("DiagnosticAbstractParameter is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the bitOffset of the DiagnosticParameter.
        # of the bitOffset shall always be interpreted as the start of the enclosing
                # DiagnosticData or Diagnostic.
        self._bitOffset: Optional["PositiveInteger"] = None

    @property
    def bit_offset(self) -> Optional["PositiveInteger"]:
        """Get bitOffset (Pythonic accessor)."""
        return self._bitOffset

    @bit_offset.setter
    def bit_offset(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set bitOffset with validation.

        Args:
            value: The bitOffset to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bitOffset = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"bitOffset must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._bitOffset = value
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
                # relevant if there is a gap between parameter and the following diagnostic the
                # tail of the telegram).
        # The unit is bit and shall be multiples of 8.
        self._parameterSize: Optional["PositiveInteger"] = None

    @property
    def parameter_size(self) -> Optional["PositiveInteger"]:
        """Get parameterSize (Pythonic accessor)."""
        return self._parameterSize

    @parameter_size.setter
    def parameter_size(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set parameterSize with validation.

        Args:
            value: The parameterSize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._parameterSize = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"parameterSize must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._parameterSize = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBitOffset(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for bitOffset.

        Returns:
            The bitOffset value

        Note:
            Delegates to bit_offset property (CODING_RULE_V2_00017)
        """
        return self.bit_offset  # Delegates to property

    def setBitOffset(self, value: "PositiveInteger") -> "DiagnosticAbstractParameter":
        """
        AUTOSAR-compliant setter for bitOffset with method chaining.

        Args:
            value: The bitOffset to set

        Returns:
            self for method chaining

        Note:
            Delegates to bit_offset property setter (gets validation automatically)
        """
        self.bit_offset = value  # Delegates to property setter
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

    def setDataElement(self, value: "DiagnosticDataElement") -> "DiagnosticAbstractParameter":
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

    def getParameterSize(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for parameterSize.

        Returns:
            The parameterSize value

        Note:
            Delegates to parameter_size property (CODING_RULE_V2_00017)
        """
        return self.parameter_size  # Delegates to property

    def setParameterSize(self, value: "PositiveInteger") -> "DiagnosticAbstractParameter":
        """
        AUTOSAR-compliant setter for parameterSize with method chaining.

        Args:
            value: The parameterSize to set

        Returns:
            self for method chaining

        Note:
            Delegates to parameter_size property setter (gets validation automatically)
        """
        self.parameter_size = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bit_offset(self, value: Optional["PositiveInteger"]) -> "DiagnosticAbstractParameter":
        """
        Set bitOffset and return self for chaining.

        Args:
            value: The bitOffset to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bit_offset("value")
        """
        self.bit_offset = value  # Use property setter (gets validation)
        return self

    def with_data_element(self, value: Optional["DiagnosticDataElement"]) -> "DiagnosticAbstractParameter":
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

    def with_parameter_size(self, value: Optional["PositiveInteger"]) -> "DiagnosticAbstractParameter":
        """
        Set parameterSize and return self for chaining.

        Args:
            value: The parameterSize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_parameter_size("value")
        """
        self.parameter_size = value  # Use property setter (gets validation)
        return self



class DiagnosticDataElement(Identifiable):
    """
    This meta-class represents the ability to describe a concrete piece of data
    to be taken into account for diagnostic purposes.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::CommonDiagnostics::DiagnosticDataElement

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 41, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 982, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute controls the meaning of the value of the array size.
        self._arraySize: Optional["ArraySizeSemantics"] = None

    @property
    def array_size(self) -> Optional["ArraySizeSemantics"]:
        """Get arraySize (Pythonic accessor)."""
        return self._arraySize

    @array_size.setter
    def array_size(self, value: Optional["ArraySizeSemantics"]) -> None:
        """
        Set arraySize with validation.

        Args:
            value: The arraySize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._arraySize = None
            return

        if not isinstance(value, ArraySizeSemantics):
            raise TypeError(
                f"arraySize must be ArraySizeSemantics or None, got {type(value).__name__}"
            )
        self._arraySize = value
        # The attribute determines the size of the terms of how many elements the array
                # can take.
        self._maxNumberOf: Optional["PositiveInteger"] = None

    @property
    def max_number_of(self) -> Optional["PositiveInteger"]:
        """Get maxNumberOf (Pythonic accessor)."""
        return self._maxNumberOf

    @max_number_of.setter
    def max_number_of(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxNumberOf with validation.

        Args:
            value: The maxNumberOf to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxNumberOf = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxNumberOf must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maxNumberOf = value
        # DiagnosticReadScalingDataBy.
        self._scalingInfoSize: Optional["PositiveInteger"] = None

    @property
    def scaling_info_size(self) -> Optional["PositiveInteger"]:
        """Get scalingInfoSize (Pythonic accessor)."""
        return self._scalingInfoSize

    @scaling_info_size.setter
    def scaling_info_size(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set scalingInfoSize with validation.

        Args:
            value: The scalingInfoSize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._scalingInfoSize = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"scalingInfoSize must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._scalingInfoSize = value
                # the definition of e.
        # g.
        # computation data constraints.
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

    def getArraySize(self) -> "ArraySizeSemantics":
        """
        AUTOSAR-compliant getter for arraySize.

        Returns:
            The arraySize value

        Note:
            Delegates to array_size property (CODING_RULE_V2_00017)
        """
        return self.array_size  # Delegates to property

    def setArraySize(self, value: "ArraySizeSemantics") -> "DiagnosticDataElement":
        """
        AUTOSAR-compliant setter for arraySize with method chaining.

        Args:
            value: The arraySize to set

        Returns:
            self for method chaining

        Note:
            Delegates to array_size property setter (gets validation automatically)
        """
        self.array_size = value  # Delegates to property setter
        return self

    def getMaxNumberOf(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxNumberOf.

        Returns:
            The maxNumberOf value

        Note:
            Delegates to max_number_of property (CODING_RULE_V2_00017)
        """
        return self.max_number_of  # Delegates to property

    def setMaxNumberOf(self, value: "PositiveInteger") -> "DiagnosticDataElement":
        """
        AUTOSAR-compliant setter for maxNumberOf with method chaining.

        Args:
            value: The maxNumberOf to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_number_of property setter (gets validation automatically)
        """
        self.max_number_of = value  # Delegates to property setter
        return self

    def getScalingInfoSize(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for scalingInfoSize.

        Returns:
            The scalingInfoSize value

        Note:
            Delegates to scaling_info_size property (CODING_RULE_V2_00017)
        """
        return self.scaling_info_size  # Delegates to property

    def setScalingInfoSize(self, value: "PositiveInteger") -> "DiagnosticDataElement":
        """
        AUTOSAR-compliant setter for scalingInfoSize with method chaining.

        Args:
            value: The scalingInfoSize to set

        Returns:
            self for method chaining

        Note:
            Delegates to scaling_info_size property setter (gets validation automatically)
        """
        self.scaling_info_size = value  # Delegates to property setter
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

    def setSwDataDef(self, value: "SwDataDefProps") -> "DiagnosticDataElement":
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

    def with_array_size(self, value: Optional["ArraySizeSemantics"]) -> "DiagnosticDataElement":
        """
        Set arraySize and return self for chaining.

        Args:
            value: The arraySize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_array_size("value")
        """
        self.array_size = value  # Use property setter (gets validation)
        return self

    def with_max_number_of(self, value: Optional["PositiveInteger"]) -> "DiagnosticDataElement":
        """
        Set maxNumberOf and return self for chaining.

        Args:
            value: The maxNumberOf to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_number_of("value")
        """
        self.max_number_of = value  # Use property setter (gets validation)
        return self

    def with_scaling_info_size(self, value: Optional["PositiveInteger"]) -> "DiagnosticDataElement":
        """
        Set scalingInfoSize and return self for chaining.

        Args:
            value: The scalingInfoSize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_scaling_info_size("value")
        """
        self.scaling_info_size = value  # Use property setter (gets validation)
        return self

    def with_sw_data_def(self, value: Optional["SwDataDefProps"]) -> "DiagnosticDataElement":
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



class DiagnosticRoutineSubfunction(Identifiable, ABC):
    """
    This meta-class acts as an abstract base class to routine subfunctions.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::CommonDiagnostics::DiagnosticRoutineSubfunction

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 121, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticRoutineSubfunction:
            raise TypeError("DiagnosticRoutineSubfunction is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference represents the access permission of the owning routine
        # subfunction.
        self._access: Optional["DiagnosticAccess"] = None

    @property
    def access(self) -> Optional["DiagnosticAccess"]:
        """Get access (Pythonic accessor)."""
        return self._access

    @access.setter
    def access(self, value: Optional["DiagnosticAccess"]) -> None:
        """
        Set access with validation.

        Args:
            value: The access to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._access = None
            return

        if not isinstance(value, DiagnosticAccess):
            raise TypeError(
                f"access must be DiagnosticAccess or None, got {type(value).__name__}"
            )
        self._access = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAccess(self) -> "DiagnosticAccess":
        """
        AUTOSAR-compliant getter for access.

        Returns:
            The access value

        Note:
            Delegates to access property (CODING_RULE_V2_00017)
        """
        return self.access  # Delegates to property

    def setAccess(self, value: "DiagnosticAccess") -> "DiagnosticRoutineSubfunction":
        """
        AUTOSAR-compliant setter for access with method chaining.

        Args:
            value: The access to set

        Returns:
            self for method chaining

        Note:
            Delegates to access property setter (gets validation automatically)
        """
        self.access = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_access(self, value: Optional["DiagnosticAccess"]) -> "DiagnosticRoutineSubfunction":
        """
        Set access and return self for chaining.

        Args:
            value: The access to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_access("value")
        """
        self.access = value  # Use property setter (gets validation)
        return self



class DiagnosticParameterSupportInfo(ARObject):
    """
    This represents a way to define which bit of the supportInfo is representing
    this part of the PID

    Package: M2::AUTOSARTemplates::DiagnosticExtract::CommonDiagnostics::DiagnosticParameterSupportInfo

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 149, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # defines the bit in the SupportInfo byte, which represents DataElement pidSize
                # / position / size.
        # Unit: byte.
        self._supportInfoBit: Optional["PositiveInteger"] = None

    @property
    def support_info_bit(self) -> Optional["PositiveInteger"]:
        """Get supportInfoBit (Pythonic accessor)."""
        return self._supportInfoBit

    @support_info_bit.setter
    def support_info_bit(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set supportInfoBit with validation.

        Args:
            value: The supportInfoBit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._supportInfoBit = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"supportInfoBit must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._supportInfoBit = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSupportInfoBit(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for supportInfoBit.

        Returns:
            The supportInfoBit value

        Note:
            Delegates to support_info_bit property (CODING_RULE_V2_00017)
        """
        return self.support_info_bit  # Delegates to property

    def setSupportInfoBit(self, value: "PositiveInteger") -> "DiagnosticParameterSupportInfo":
        """
        AUTOSAR-compliant setter for supportInfoBit with method chaining.

        Args:
            value: The supportInfoBit to set

        Returns:
            self for method chaining

        Note:
            Delegates to support_info_bit property setter (gets validation automatically)
        """
        self.support_info_bit = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_support_info_bit(self, value: Optional["PositiveInteger"]) -> "DiagnosticParameterSupportInfo":
        """
        Set supportInfoBit and return self for chaining.

        Args:
            value: The supportInfoBit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_support_info_bit("value")
        """
        self.support_info_bit = value  # Use property setter (gets validation)
        return self



class DiagnosticSupportInfoByte(ARObject):
    """
    This meta-class defines the support information (typically byte A) to
    declare the usability of the Data Elements within the so-called packeted
    PIDs (e.g. PID$68).

    Package: M2::AUTOSARTemplates::DiagnosticExtract::CommonDiagnostics::DiagnosticSupportInfoByte

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 150, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the position of the supportInfo in the PID.
        self._position: Optional["PositiveInteger"] = None

    @property
    def position(self) -> Optional["PositiveInteger"]:
        """Get position (Pythonic accessor)."""
        return self._position

    @position.setter
    def position(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set position with validation.

        Args:
            value: The position to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._position = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"position must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._position = value
        self._size: Optional["PositiveInteger"] = None

    @property
    def size(self) -> Optional["PositiveInteger"]:
        """Get size (Pythonic accessor)."""
        return self._size

    @size.setter
    def size(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set size with validation.

        Args:
            value: The size to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._size = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"size must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._size = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPosition(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for position.

        Returns:
            The position value

        Note:
            Delegates to position property (CODING_RULE_V2_00017)
        """
        return self.position  # Delegates to property

    def setPosition(self, value: "PositiveInteger") -> "DiagnosticSupportInfoByte":
        """
        AUTOSAR-compliant setter for position with method chaining.

        Args:
            value: The position to set

        Returns:
            self for method chaining

        Note:
            Delegates to position property setter (gets validation automatically)
        """
        self.position = value  # Delegates to property setter
        return self

    def getSize(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for size.

        Returns:
            The size value

        Note:
            Delegates to size property (CODING_RULE_V2_00017)
        """
        return self.size  # Delegates to property

    def setSize(self, value: "PositiveInteger") -> "DiagnosticSupportInfoByte":
        """
        AUTOSAR-compliant setter for size with method chaining.

        Args:
            value: The size to set

        Returns:
            self for method chaining

        Note:
            Delegates to size property setter (gets validation automatically)
        """
        self.size = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_position(self, value: Optional["PositiveInteger"]) -> "DiagnosticSupportInfoByte":
        """
        Set position and return self for chaining.

        Args:
            value: The position to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_position("value")
        """
        self.position = value  # Use property setter (gets validation)
        return self

    def with_size(self, value: Optional["PositiveInteger"]) -> "DiagnosticSupportInfoByte":
        """
        Set size and return self for chaining.

        Args:
            value: The size to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_size("value")
        """
        self.size = value  # Use property setter (gets validation)
        return self



class DiagnosticAbstractDataIdentifier(DiagnosticCommonElement, ABC):
    """
    This meta-class represents an abstract base class for the modeling of a
    diagnostic data identifier (DID).

    Package: M2::AUTOSARTemplates::DiagnosticExtract::CommonDiagnostics::DiagnosticAbstractDataIdentifier

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 34, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticAbstractDataIdentifier:
            raise TypeError("DiagnosticAbstractDataIdentifier is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the numerical identifier used to identify the the scope of.
        self._id: Optional["PositiveInteger"] = None

    @property
    def id(self) -> Optional["PositiveInteger"]:
        """Get id (Pythonic accessor)."""
        return self._id

    @id.setter
    def id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set id with validation.

        Args:
            value: The id to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._id = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"id must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._id = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for id.

        Returns:
            The id value

        Note:
            Delegates to id property (CODING_RULE_V2_00017)
        """
        return self.id  # Delegates to property

    def setId(self, value: "PositiveInteger") -> "DiagnosticAbstractDataIdentifier":
        """
        AUTOSAR-compliant setter for id with method chaining.

        Args:
            value: The id to set

        Returns:
            self for method chaining

        Note:
            Delegates to id property setter (gets validation automatically)
        """
        self.id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_id(self, value: Optional["PositiveInteger"]) -> "DiagnosticAbstractDataIdentifier":
        """
        Set id and return self for chaining.

        Args:
            value: The id to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_id("value")
        """
        self.id = value  # Use property setter (gets validation)
        return self



class DiagnosticRoutine(DiagnosticCommonElement):
    """
    This meta-class represents the ability to define a diagnostic routine.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::CommonDiagnostics::DiagnosticRoutine

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 124, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the numerical identifier used to identify the the scope of diagnostic
        # workflow.
        self._id: Optional["PositiveInteger"] = None

    @property
    def id(self) -> Optional["PositiveInteger"]:
        """Get id (Pythonic accessor)."""
        return self._id

    @id.setter
    def id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set id with validation.

        Args:
            value: The id to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._id = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"id must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._id = value
        self._requestResult: Optional["DiagnosticRequest"] = None

    @property
    def request_result(self) -> Optional["DiagnosticRequest"]:
        """Get requestResult (Pythonic accessor)."""
        return self._requestResult

    @request_result.setter
    def request_result(self, value: Optional["DiagnosticRequest"]) -> None:
        """
        Set requestResult with validation.

        Args:
            value: The requestResult to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._requestResult = None
            return

        if not isinstance(value, DiagnosticRequest):
            raise TypeError(
                f"requestResult must be DiagnosticRequest or None, got {type(value).__name__}"
            )
        self._requestResult = value
        # The info byte manufacturer-specific value (for the record identifiers) that
                # is reported to the cases for this attribute are mentioned in ISO ISO 26021.
        self._routineInfo: Optional["PositiveInteger"] = None

    @property
    def routine_info(self) -> Optional["PositiveInteger"]:
        """Get routineInfo (Pythonic accessor)."""
        return self._routineInfo

    @routine_info.setter
    def routine_info(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set routineInfo with validation.

        Args:
            value: The routineInfo to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._routineInfo = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"routineInfo must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._routineInfo = value
        self._start: Optional["DiagnosticStartRoutine"] = None

    @property
    def start(self) -> Optional["DiagnosticStartRoutine"]:
        """Get start (Pythonic accessor)."""
        return self._start

    @start.setter
    def start(self, value: Optional["DiagnosticStartRoutine"]) -> None:
        """
        Set start with validation.

        Args:
            value: The start to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._start = None
            return

        if not isinstance(value, DiagnosticStartRoutine):
            raise TypeError(
                f"start must be DiagnosticStartRoutine or None, got {type(value).__name__}"
            )
        self._start = value
        self._stop: Optional["DiagnosticStopRoutine"] = None

    @property
    def stop(self) -> Optional["DiagnosticStopRoutine"]:
        """Get stop (Pythonic accessor)."""
        return self._stop

    @stop.setter
    def stop(self, value: Optional["DiagnosticStopRoutine"]) -> None:
        """
        Set stop with validation.

        Args:
            value: The stop to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._stop = None
            return

        if not isinstance(value, DiagnosticStopRoutine):
            raise TypeError(
                f"stop must be DiagnosticStopRoutine or None, got {type(value).__name__}"
            )
        self._stop = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for id.

        Returns:
            The id value

        Note:
            Delegates to id property (CODING_RULE_V2_00017)
        """
        return self.id  # Delegates to property

    def setId(self, value: "PositiveInteger") -> "DiagnosticRoutine":
        """
        AUTOSAR-compliant setter for id with method chaining.

        Args:
            value: The id to set

        Returns:
            self for method chaining

        Note:
            Delegates to id property setter (gets validation automatically)
        """
        self.id = value  # Delegates to property setter
        return self

    def getRequestResult(self) -> "DiagnosticRequest":
        """
        AUTOSAR-compliant getter for requestResult.

        Returns:
            The requestResult value

        Note:
            Delegates to request_result property (CODING_RULE_V2_00017)
        """
        return self.request_result  # Delegates to property

    def setRequestResult(self, value: "DiagnosticRequest") -> "DiagnosticRoutine":
        """
        AUTOSAR-compliant setter for requestResult with method chaining.

        Args:
            value: The requestResult to set

        Returns:
            self for method chaining

        Note:
            Delegates to request_result property setter (gets validation automatically)
        """
        self.request_result = value  # Delegates to property setter
        return self

    def getRoutineInfo(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for routineInfo.

        Returns:
            The routineInfo value

        Note:
            Delegates to routine_info property (CODING_RULE_V2_00017)
        """
        return self.routine_info  # Delegates to property

    def setRoutineInfo(self, value: "PositiveInteger") -> "DiagnosticRoutine":
        """
        AUTOSAR-compliant setter for routineInfo with method chaining.

        Args:
            value: The routineInfo to set

        Returns:
            self for method chaining

        Note:
            Delegates to routine_info property setter (gets validation automatically)
        """
        self.routine_info = value  # Delegates to property setter
        return self

    def getStart(self) -> "DiagnosticStartRoutine":
        """
        AUTOSAR-compliant getter for start.

        Returns:
            The start value

        Note:
            Delegates to start property (CODING_RULE_V2_00017)
        """
        return self.start  # Delegates to property

    def setStart(self, value: "DiagnosticStartRoutine") -> "DiagnosticRoutine":
        """
        AUTOSAR-compliant setter for start with method chaining.

        Args:
            value: The start to set

        Returns:
            self for method chaining

        Note:
            Delegates to start property setter (gets validation automatically)
        """
        self.start = value  # Delegates to property setter
        return self

    def getStop(self) -> "DiagnosticStopRoutine":
        """
        AUTOSAR-compliant getter for stop.

        Returns:
            The stop value

        Note:
            Delegates to stop property (CODING_RULE_V2_00017)
        """
        return self.stop  # Delegates to property

    def setStop(self, value: "DiagnosticStopRoutine") -> "DiagnosticRoutine":
        """
        AUTOSAR-compliant setter for stop with method chaining.

        Args:
            value: The stop to set

        Returns:
            self for method chaining

        Note:
            Delegates to stop property setter (gets validation automatically)
        """
        self.stop = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_id(self, value: Optional["PositiveInteger"]) -> "DiagnosticRoutine":
        """
        Set id and return self for chaining.

        Args:
            value: The id to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_id("value")
        """
        self.id = value  # Use property setter (gets validation)
        return self

    def with_request_result(self, value: Optional["DiagnosticRequest"]) -> "DiagnosticRoutine":
        """
        Set requestResult and return self for chaining.

        Args:
            value: The requestResult to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_request_result("value")
        """
        self.request_result = value  # Use property setter (gets validation)
        return self

    def with_routine_info(self, value: Optional["PositiveInteger"]) -> "DiagnosticRoutine":
        """
        Set routineInfo and return self for chaining.

        Args:
            value: The routineInfo to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_routine_info("value")
        """
        self.routine_info = value  # Use property setter (gets validation)
        return self

    def with_start(self, value: Optional["DiagnosticStartRoutine"]) -> "DiagnosticRoutine":
        """
        Set start and return self for chaining.

        Args:
            value: The start to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_start("value")
        """
        self.start = value  # Use property setter (gets validation)
        return self

    def with_stop(self, value: Optional["DiagnosticStopRoutine"]) -> "DiagnosticRoutine":
        """
        Set stop and return self for chaining.

        Args:
            value: The stop to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_stop("value")
        """
        self.stop = value  # Use property setter (gets validation)
        return self



class DiagnosticParameterIdentifier(DiagnosticCommonElement):
    """
    This meta-class represents the ability to model a diagnostic parameter
    identifier (PID) for the purpose of executing on-board diagnostics (OBD).

    Package: M2::AUTOSARTemplates::DiagnosticExtract::CommonDiagnostics::DiagnosticParameterIdentifier

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 149, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the data carried by the Diagnostic atpVariation.
        self._dataElement: List["DiagnosticParameter"] = []

    @property
    def data_element(self) -> List["DiagnosticParameter"]:
        """Get dataElement (Pythonic accessor)."""
        return self._dataElement
        # This is the numerical identifier used to identify the the scope of diagnostic
        # SAE J1979-DA).
        self._id: Optional["PositiveInteger"] = None

    @property
    def id(self) -> Optional["PositiveInteger"]:
        """Get id (Pythonic accessor)."""
        return self._id

    @id.setter
    def id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set id with validation.

        Args:
            value: The id to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._id = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"id must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._id = value
        # padding might be applied.
        self._pidSize: Optional["PositiveInteger"] = None

    @property
    def pid_size(self) -> Optional["PositiveInteger"]:
        """Get pidSize (Pythonic accessor)."""
        return self._pidSize

    @pid_size.setter
    def pid_size(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set pidSize with validation.

        Args:
            value: The pidSize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pidSize = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"pidSize must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._pidSize = value
        # DiagnosticParameterIdentifier.
        self._supportInfoByte: Optional["DiagnosticSupportInfo"] = None

    @property
    def support_info_byte(self) -> Optional["DiagnosticSupportInfo"]:
        """Get supportInfoByte (Pythonic accessor)."""
        return self._supportInfoByte

    @support_info_byte.setter
    def support_info_byte(self, value: Optional["DiagnosticSupportInfo"]) -> None:
        """
        Set supportInfoByte with validation.

        Args:
            value: The supportInfoByte to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._supportInfoByte = None
            return

        if not isinstance(value, DiagnosticSupportInfo):
            raise TypeError(
                f"supportInfoByte must be DiagnosticSupportInfo or None, got {type(value).__name__}"
            )
        self._supportInfoByte = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataElement(self) -> List["DiagnosticParameter"]:
        """
        AUTOSAR-compliant getter for dataElement.

        Returns:
            The dataElement value

        Note:
            Delegates to data_element property (CODING_RULE_V2_00017)
        """
        return self.data_element  # Delegates to property

    def getId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for id.

        Returns:
            The id value

        Note:
            Delegates to id property (CODING_RULE_V2_00017)
        """
        return self.id  # Delegates to property

    def setId(self, value: "PositiveInteger") -> "DiagnosticParameterIdentifier":
        """
        AUTOSAR-compliant setter for id with method chaining.

        Args:
            value: The id to set

        Returns:
            self for method chaining

        Note:
            Delegates to id property setter (gets validation automatically)
        """
        self.id = value  # Delegates to property setter
        return self

    def getPidSize(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for pidSize.

        Returns:
            The pidSize value

        Note:
            Delegates to pid_size property (CODING_RULE_V2_00017)
        """
        return self.pid_size  # Delegates to property

    def setPidSize(self, value: "PositiveInteger") -> "DiagnosticParameterIdentifier":
        """
        AUTOSAR-compliant setter for pidSize with method chaining.

        Args:
            value: The pidSize to set

        Returns:
            self for method chaining

        Note:
            Delegates to pid_size property setter (gets validation automatically)
        """
        self.pid_size = value  # Delegates to property setter
        return self

    def getSupportInfoByte(self) -> "DiagnosticSupportInfo":
        """
        AUTOSAR-compliant getter for supportInfoByte.

        Returns:
            The supportInfoByte value

        Note:
            Delegates to support_info_byte property (CODING_RULE_V2_00017)
        """
        return self.support_info_byte  # Delegates to property

    def setSupportInfoByte(self, value: "DiagnosticSupportInfo") -> "DiagnosticParameterIdentifier":
        """
        AUTOSAR-compliant setter for supportInfoByte with method chaining.

        Args:
            value: The supportInfoByte to set

        Returns:
            self for method chaining

        Note:
            Delegates to support_info_byte property setter (gets validation automatically)
        """
        self.support_info_byte = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_id(self, value: Optional["PositiveInteger"]) -> "DiagnosticParameterIdentifier":
        """
        Set id and return self for chaining.

        Args:
            value: The id to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_id("value")
        """
        self.id = value  # Use property setter (gets validation)
        return self

    def with_pid_size(self, value: Optional["PositiveInteger"]) -> "DiagnosticParameterIdentifier":
        """
        Set pidSize and return self for chaining.

        Args:
            value: The pidSize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pid_size("value")
        """
        self.pid_size = value  # Use property setter (gets validation)
        return self

    def with_support_info_byte(self, value: Optional["DiagnosticSupportInfo"]) -> "DiagnosticParameterIdentifier":
        """
        Set supportInfoByte and return self for chaining.

        Args:
            value: The supportInfoByte to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_support_info_byte("value")
        """
        self.support_info_byte = value  # Use property setter (gets validation)
        return self



class DiagnosticInfoType(DiagnosticCommonElement):
    """
    This meta-class represents the ability to model an OBD info type.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::CommonDiagnostics::DiagnosticInfoType

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 160, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the data associated with the enclosing data.
        self._dataElement: List["DiagnosticParameter"] = []

    @property
    def data_element(self) -> List["DiagnosticParameter"]:
        """Get dataElement (Pythonic accessor)."""
        return self._dataElement
        # This attribute represents the value of InfoType (see SAE.
        self._id: Optional["PositiveInteger"] = None

    @property
    def id(self) -> Optional["PositiveInteger"]:
        """Get id (Pythonic accessor)."""
        return self._id

    @id.setter
    def id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set id with validation.

        Args:
            value: The id to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._id = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"id must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._id = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataElement(self) -> List["DiagnosticParameter"]:
        """
        AUTOSAR-compliant getter for dataElement.

        Returns:
            The dataElement value

        Note:
            Delegates to data_element property (CODING_RULE_V2_00017)
        """
        return self.data_element  # Delegates to property

    def getId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for id.

        Returns:
            The id value

        Note:
            Delegates to id property (CODING_RULE_V2_00017)
        """
        return self.id  # Delegates to property

    def setId(self, value: "PositiveInteger") -> "DiagnosticInfoType":
        """
        AUTOSAR-compliant setter for id with method chaining.

        Args:
            value: The id to set

        Returns:
            self for method chaining

        Note:
            Delegates to id property setter (gets validation automatically)
        """
        self.id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_id(self, value: Optional["PositiveInteger"]) -> "DiagnosticInfoType":
        """
        Set id and return self for chaining.

        Args:
            value: The id to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_id("value")
        """
        self.id = value  # Use property setter (gets validation)
        return self



class DiagnosticParameter(DiagnosticAbstractParameter):
    """
    This meta-class represents the ability to describe information relevant for
    the execution of a specific diagnostic service, i.e. it can be taken to
    parameterize the service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::CommonDiagnostics::DiagnosticParameter

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 36, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The aggregation in the role ident provides the ability to the
                # DiagnosticAbstractParameter identifiable.
        # semantical point of view, the AbstractDiagnostic considered a first-class
                # Identifiable and aggregation in the role ident shall always it may be
                # possible to let AbstractDiagnostic inherit from Identifiable).
        self._ident: Optional["DiagnosticParameter"] = None

    @property
    def ident(self) -> Optional["DiagnosticParameter"]:
        """Get ident (Pythonic accessor)."""
        return self._ident

    @ident.setter
    def ident(self, value: Optional["DiagnosticParameter"]) -> None:
        """
        Set ident with validation.

        Args:
            value: The ident to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ident = None
            return

        if not isinstance(value, DiagnosticParameter):
            raise TypeError(
                f"ident must be DiagnosticParameter or None, got {type(value).__name__}"
            )
        self._ident = value
        # byte is representing this part of the PID.
        self._supportInfo: Optional["DiagnosticParameter"] = None

    @property
    def support_info(self) -> Optional["DiagnosticParameter"]:
        """Get supportInfo (Pythonic accessor)."""
        return self._supportInfo

    @support_info.setter
    def support_info(self, value: Optional["DiagnosticParameter"]) -> None:
        """
        Set supportInfo with validation.

        Args:
            value: The supportInfo to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._supportInfo = None
            return

        if not isinstance(value, DiagnosticParameter):
            raise TypeError(
                f"supportInfo must be DiagnosticParameter or None, got {type(value).__name__}"
            )
        self._supportInfo = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIdent(self) -> "DiagnosticParameter":
        """
        AUTOSAR-compliant getter for ident.

        Returns:
            The ident value

        Note:
            Delegates to ident property (CODING_RULE_V2_00017)
        """
        return self.ident  # Delegates to property

    def setIdent(self, value: "DiagnosticParameter") -> "DiagnosticParameter":
        """
        AUTOSAR-compliant setter for ident with method chaining.

        Args:
            value: The ident to set

        Returns:
            self for method chaining

        Note:
            Delegates to ident property setter (gets validation automatically)
        """
        self.ident = value  # Delegates to property setter
        return self

    def getSupportInfo(self) -> "DiagnosticParameter":
        """
        AUTOSAR-compliant getter for supportInfo.

        Returns:
            The supportInfo value

        Note:
            Delegates to support_info property (CODING_RULE_V2_00017)
        """
        return self.support_info  # Delegates to property

    def setSupportInfo(self, value: "DiagnosticParameter") -> "DiagnosticParameter":
        """
        AUTOSAR-compliant setter for supportInfo with method chaining.

        Args:
            value: The supportInfo to set

        Returns:
            self for method chaining

        Note:
            Delegates to support_info property setter (gets validation automatically)
        """
        self.support_info = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ident(self, value: Optional["DiagnosticParameter"]) -> "DiagnosticParameter":
        """
        Set ident and return self for chaining.

        Args:
            value: The ident to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ident("value")
        """
        self.ident = value  # Use property setter (gets validation)
        return self

    def with_support_info(self, value: Optional["DiagnosticParameter"]) -> "DiagnosticParameter":
        """
        Set supportInfo and return self for chaining.

        Args:
            value: The supportInfo to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_support_info("value")
        """
        self.support_info = value  # Use property setter (gets validation)
        return self



class DiagnosticStartRoutine(DiagnosticRoutineSubfunction):
    """
    This represents the ability to start a diagnostic routine.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::CommonDiagnostics::DiagnosticStartRoutine

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 124, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the request parameters.
        self._request: List["DiagnosticParameter"] = []

    @property
    def request(self) -> List["DiagnosticParameter"]:
        """Get request (Pythonic accessor)."""
        return self._request
        # This represents the response parameters.
        self._response: List["DiagnosticParameter"] = []

    @property
    def response(self) -> List["DiagnosticParameter"]:
        """Get response (Pythonic accessor)."""
        return self._response

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRequest(self) -> List["DiagnosticParameter"]:
        """
        AUTOSAR-compliant getter for request.

        Returns:
            The request value

        Note:
            Delegates to request property (CODING_RULE_V2_00017)
        """
        return self.request  # Delegates to property

    def getResponse(self) -> List["DiagnosticParameter"]:
        """
        AUTOSAR-compliant getter for response.

        Returns:
            The response value

        Note:
            Delegates to response property (CODING_RULE_V2_00017)
        """
        return self.response  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticStopRoutine(DiagnosticRoutineSubfunction):
    """
    This represents the ability to stop a diagnostic routine.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::CommonDiagnostics::DiagnosticStopRoutine

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 125, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the request parameters.
        self._request: List["DiagnosticParameter"] = []

    @property
    def request(self) -> List["DiagnosticParameter"]:
        """Get request (Pythonic accessor)."""
        return self._request
        # This represents the response parameters.
        self._response: List["DiagnosticParameter"] = []

    @property
    def response(self) -> List["DiagnosticParameter"]:
        """Get response (Pythonic accessor)."""
        return self._response

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRequest(self) -> List["DiagnosticParameter"]:
        """
        AUTOSAR-compliant getter for request.

        Returns:
            The request value

        Note:
            Delegates to request property (CODING_RULE_V2_00017)
        """
        return self.request  # Delegates to property

    def getResponse(self) -> List["DiagnosticParameter"]:
        """
        AUTOSAR-compliant getter for response.

        Returns:
            The response value

        Note:
            Delegates to response property (CODING_RULE_V2_00017)
        """
        return self.response  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticRequestRoutineResults(DiagnosticRoutineSubfunction):
    """
    This meta-class represents the ability to define the result of a diagnostic
    routine execution.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::CommonDiagnostics::DiagnosticRequestRoutineResults

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 125, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the request parameters.
        self._request: List["DiagnosticParameter"] = []

    @property
    def request(self) -> List["DiagnosticParameter"]:
        """Get request (Pythonic accessor)."""
        return self._request
        # This represents the response parameters.
        self._response: List["DiagnosticParameter"] = []

    @property
    def response(self) -> List["DiagnosticParameter"]:
        """Get response (Pythonic accessor)."""
        return self._response

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRequest(self) -> List["DiagnosticParameter"]:
        """
        AUTOSAR-compliant getter for request.

        Returns:
            The request value

        Note:
            Delegates to request property (CODING_RULE_V2_00017)
        """
        return self.request  # Delegates to property

    def getResponse(self) -> List["DiagnosticParameter"]:
        """
        AUTOSAR-compliant getter for response.

        Returns:
            The response value

        Note:
            Delegates to response property (CODING_RULE_V2_00017)
        """
        return self.response  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticDataIdentifier(DiagnosticAbstractDataIdentifier):
    """
    This meta-class represents the ability to model a diagnostic data identifier
    (DID) that is fully specified regarding the payload at configuration-time.
    (cid:53) 33 of 719 Document ID 673: AUTOSAR_CP_TPS_DiagnosticExtractTemplate
    Diagnostic Extract Template AUTOSAR CP R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::DiagnosticExtract::CommonDiagnostics::DiagnosticDataIdentifier

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 33, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the dataElement associated with the Diagnostic atpVariation.
        self._dataElement: List["DiagnosticParameter"] = []

    @property
    def data_element(self) -> List["DiagnosticParameter"]:
        """Get dataElement (Pythonic accessor)."""
        return self._dataElement
        # This attribute indicates the size in bytes of the Diagnostic.
        self._didSize: Optional["PositiveInteger"] = None

    @property
    def did_size(self) -> Optional["PositiveInteger"]:
        """Get didSize (Pythonic accessor)."""
        return self._didSize

    @did_size.setter
    def did_size(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set didSize with validation.

        Args:
            value: The didSize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._didSize = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"didSize must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._didSize = value
        # identification.
        self._representsVin: Optional["Boolean"] = None

    @property
    def represents_vin(self) -> Optional["Boolean"]:
        """Get representsVin (Pythonic accessor)."""
        return self._representsVin

    @represents_vin.setter
    def represents_vin(self, value: Optional["Boolean"]) -> None:
        """
        Set representsVin with validation.

        Args:
            value: The representsVin to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._representsVin = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"representsVin must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._representsVin = value
        # DiagnosticDataIdentifier.
        self._supportInfoByte: Optional["DiagnosticSupportInfo"] = None

    @property
    def support_info_byte(self) -> Optional["DiagnosticSupportInfo"]:
        """Get supportInfoByte (Pythonic accessor)."""
        return self._supportInfoByte

    @support_info_byte.setter
    def support_info_byte(self, value: Optional["DiagnosticSupportInfo"]) -> None:
        """
        Set supportInfoByte with validation.

        Args:
            value: The supportInfoByte to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._supportInfoByte = None
            return

        if not isinstance(value, DiagnosticSupportInfo):
            raise TypeError(
                f"supportInfoByte must be DiagnosticSupportInfo or None, got {type(value).__name__}"
            )
        self._supportInfoByte = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataElement(self) -> List["DiagnosticParameter"]:
        """
        AUTOSAR-compliant getter for dataElement.

        Returns:
            The dataElement value

        Note:
            Delegates to data_element property (CODING_RULE_V2_00017)
        """
        return self.data_element  # Delegates to property

    def getDidSize(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for didSize.

        Returns:
            The didSize value

        Note:
            Delegates to did_size property (CODING_RULE_V2_00017)
        """
        return self.did_size  # Delegates to property

    def setDidSize(self, value: "PositiveInteger") -> "DiagnosticDataIdentifier":
        """
        AUTOSAR-compliant setter for didSize with method chaining.

        Args:
            value: The didSize to set

        Returns:
            self for method chaining

        Note:
            Delegates to did_size property setter (gets validation automatically)
        """
        self.did_size = value  # Delegates to property setter
        return self

    def getRepresentsVin(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for representsVin.

        Returns:
            The representsVin value

        Note:
            Delegates to represents_vin property (CODING_RULE_V2_00017)
        """
        return self.represents_vin  # Delegates to property

    def setRepresentsVin(self, value: "Boolean") -> "DiagnosticDataIdentifier":
        """
        AUTOSAR-compliant setter for representsVin with method chaining.

        Args:
            value: The representsVin to set

        Returns:
            self for method chaining

        Note:
            Delegates to represents_vin property setter (gets validation automatically)
        """
        self.represents_vin = value  # Delegates to property setter
        return self

    def getSupportInfoByte(self) -> "DiagnosticSupportInfo":
        """
        AUTOSAR-compliant getter for supportInfoByte.

        Returns:
            The supportInfoByte value

        Note:
            Delegates to support_info_byte property (CODING_RULE_V2_00017)
        """
        return self.support_info_byte  # Delegates to property

    def setSupportInfoByte(self, value: "DiagnosticSupportInfo") -> "DiagnosticDataIdentifier":
        """
        AUTOSAR-compliant setter for supportInfoByte with method chaining.

        Args:
            value: The supportInfoByte to set

        Returns:
            self for method chaining

        Note:
            Delegates to support_info_byte property setter (gets validation automatically)
        """
        self.support_info_byte = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_did_size(self, value: Optional["PositiveInteger"]) -> "DiagnosticDataIdentifier":
        """
        Set didSize and return self for chaining.

        Args:
            value: The didSize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_did_size("value")
        """
        self.did_size = value  # Use property setter (gets validation)
        return self

    def with_represents_vin(self, value: Optional["Boolean"]) -> "DiagnosticDataIdentifier":
        """
        Set representsVin and return self for chaining.

        Args:
            value: The representsVin to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_represents_vin("value")
        """
        self.represents_vin = value  # Use property setter (gets validation)
        return self

    def with_support_info_byte(self, value: Optional["DiagnosticSupportInfo"]) -> "DiagnosticDataIdentifier":
        """
        Set supportInfoByte and return self for chaining.

        Args:
            value: The supportInfoByte to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_support_info_byte("value")
        """
        self.support_info_byte = value  # Use property setter (gets validation)
        return self



class DiagnosticDynamicDataIdentifier(DiagnosticAbstractDataIdentifier):
    """
    This meta-class represents the ability to define a diagnostic data
    identifier (DID) at run-time.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::CommonDiagnostics::DiagnosticDynamicDataIdentifier

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 34, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
