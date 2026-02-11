"""
AUTOSAR Package - DataExchangePoint

Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint
"""


from __future__ import annotations
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class DataExchangePoint(ARElement):
    """
    The Data Exchange Point describes the relationship between a work product
    and its intended use in the methodology with a tailoring of the AUTOSAR
    templates. An informal description is provided by the ’desc’ and
    ’introduction’ attributes of the DataExchangePoint. The informal description
    SHOULD include the subject that is described by this data exchange point.
    E.g. • producible data of tool A, version x • consumable data of tool B,
    version y • agreed profile between partner A and partner B in project xyz

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::DataExchangePoint

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 78, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # tailoring to the Autosar Exchange Data Format The and tailoring of the
        # templates specifications Sdgs, Constraints, SpecItems).
        self._dataFormat: Optional["DataFormatTailoring"] = None

    @property
    def data_format(self) -> Optional["DataFormatTailoring"]:
        """Get dataFormat (Pythonic accessor)."""
        return self._dataFormat

    @data_format.setter
    def data_format(self, value: Optional["DataFormatTailoring"]) -> None:
        """
        Set dataFormat with validation.

        Args:
            value: The dataFormat to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataFormat = None
            return

        if not isinstance(value, DataFormatTailoring):
            raise TypeError(
                f"dataFormat must be DataFormatTailoring or None, got {type(value).__name__}"
            )
        self._dataFormat = value
        # It provides if this DataExchangePoint represents output of a tool that
                # produce data, input of a tool that consumes data or agreed profile.
        self._kind: DataExchangePoint = None

    @property
    def kind(self) -> DataExchangePoint:
        """Get kind (Pythonic accessor)."""
        return self._kind

    @kind.setter
    def kind(self, value: DataExchangePoint) -> None:
        """
        Set kind with validation.

        Args:
            value: The kind to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, DataExchangePoint):
            raise TypeError(
                f"kind must be DataExchangePoint, got {type(value).__name__}"
            )
        self._kind = value
        # Exchange Point.
        self._referenced: Baseline = None

    @property
    def referenced(self) -> Baseline:
        """Get referenced (Pythonic accessor)."""
        return self._referenced

    @referenced.setter
    def referenced(self, value: Baseline) -> None:
        """
        Set referenced with validation.

        Args:
            value: The referenced to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Baseline):
            raise TypeError(
                f"referenced must be Baseline, got {type(value).__name__}"
            )
        self._referenced = value
        # specifications.
        self._specification: Optional["SpecificationScope"] = None

    @property
    def specification(self) -> Optional["SpecificationScope"]:
        """Get specification (Pythonic accessor)."""
        return self._specification

    @specification.setter
    def specification(self, value: Optional["SpecificationScope"]) -> None:
        """
        Set specification with validation.

        Args:
            value: The specification to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._specification = None
            return

        if not isinstance(value, SpecificationScope):
            raise TypeError(
                f"specification must be SpecificationScope or None, got {type(value).__name__}"
            )
        self._specification = value

    def with_custom_sdg_def(self, value):
        """
        Set custom_sdg_def and return self for chaining.

        Args:
            value: The custom_sdg_def to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_custom_sdg_def("value")
        """
        self.custom_sdg_def = value  # Use property setter (gets validation)
        return self

    def with_custom(self, value):
        """
        Set custom and return self for chaining.

        Args:
            value: The custom to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_custom("value")
        """
        self.custom = value  # Use property setter (gets validation)
        return self

    def with_standard(self, value):
        """
        Set standard and return self for chaining.

        Args:
            value: The standard to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_standard("value")
        """
        self.standard = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataFormat(self) -> "DataFormatTailoring":
        """
        AUTOSAR-compliant getter for dataFormat.

        Returns:
            The dataFormat value

        Note:
            Delegates to data_format property (CODING_RULE_V2_00017)
        """
        return self.data_format  # Delegates to property

    def setDataFormat(self, value: "DataFormatTailoring") -> DataExchangePoint:
        """
        AUTOSAR-compliant setter for dataFormat with method chaining.

        Args:
            value: The dataFormat to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_format property setter (gets validation automatically)
        """
        self.data_format = value  # Delegates to property setter
        return self

    def getKind(self) -> DataExchangePoint:
        """
        AUTOSAR-compliant getter for kind.

        Returns:
            The kind value

        Note:
            Delegates to kind property (CODING_RULE_V2_00017)
        """
        return self.kind  # Delegates to property

    def setKind(self, value: DataExchangePoint) -> DataExchangePoint:
        """
        AUTOSAR-compliant setter for kind with method chaining.

        Args:
            value: The kind to set

        Returns:
            self for method chaining

        Note:
            Delegates to kind property setter (gets validation automatically)
        """
        self.kind = value  # Delegates to property setter
        return self

    def getReferenced(self) -> Baseline:
        """
        AUTOSAR-compliant getter for referenced.

        Returns:
            The referenced value

        Note:
            Delegates to referenced property (CODING_RULE_V2_00017)
        """
        return self.referenced  # Delegates to property

    def setReferenced(self, value: Baseline) -> DataExchangePoint:
        """
        AUTOSAR-compliant setter for referenced with method chaining.

        Args:
            value: The referenced to set

        Returns:
            self for method chaining

        Note:
            Delegates to referenced property setter (gets validation automatically)
        """
        self.referenced = value  # Delegates to property setter
        return self

    def getSpecification(self) -> "SpecificationScope":
        """
        AUTOSAR-compliant getter for specification.

        Returns:
            The specification value

        Note:
            Delegates to specification property (CODING_RULE_V2_00017)
        """
        return self.specification  # Delegates to property

    def setSpecification(self, value: "SpecificationScope") -> DataExchangePoint:
        """
        AUTOSAR-compliant setter for specification with method chaining.

        Args:
            value: The specification to set

        Returns:
            self for method chaining

        Note:
            Delegates to specification property setter (gets validation automatically)
        """
        self.specification = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_format(self, value: Optional["DataFormatTailoring"]) -> DataExchangePoint:
        """
        Set dataFormat and return self for chaining.

        Args:
            value: The dataFormat to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_format("value")
        """
        self.data_format = value  # Use property setter (gets validation)
        return self

    def with_kind(self, value: DataExchangePoint) -> DataExchangePoint:
        """
        Set kind and return self for chaining.

        Args:
            value: The kind to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_kind("value")
        """
        self.kind = value  # Use property setter (gets validation)
        return self

    def with_referenced(self, value: Baseline) -> DataExchangePoint:
        """
        Set referenced and return self for chaining.

        Args:
            value: The referenced to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_referenced("value")
        """
        self.referenced = value  # Use property setter (gets validation)
        return self

    def with_specification(self, value: Optional["SpecificationScope"]) -> DataExchangePoint:
        """
        Set specification and return self for chaining.

        Args:
            value: The specification to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_specification("value")
        """
        self.specification = value  # Use property setter (gets validation)
        return self



class Baseline(ARObject):
    """
    Specification of the baseline of the AUTOSAR standard this Data Exchange
    Point relates to. The baseline is specified by listing the AUTOSAR products
    and their revisions. Custom defined functionality and deviations to the
    standard can be provided as well. All references to specification elements
    in this Data Exchange Point refer to specification elements that are part of
    this specification baseline.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Baseline

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 79, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to custom SdgDefs that extend the data format baseline,.
        self._customSdgDef: List["SdgDef"] = []

    @property
    def custom_sdg_def(self) -> List["SdgDef"]:
        """Get customSdgDef (Pythonic accessor)."""
        return self._customSdgDef
        # Reference to custom specifications that extend this.
        self._custom: List["Documentation"] = []

    @property
    def custom(self) -> List["Documentation"]:
        """Get custom (Pythonic accessor)."""
        return self._custom
        # Specifies a combination of revisions of AUTOSAR that are used as the
                # specification baseline of Exchange Point.
        # All standard specification are referenced by this Profile of Data have to be
                # part of specifications that the defined AUTOSAR standards.
        self._standard: List["String"] = []

    @property
    def standard(self) -> List["String"]:
        """Get standard (Pythonic accessor)."""
        return self._standard

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCustomSdgDef(self) -> List["SdgDef"]:
        """
        AUTOSAR-compliant getter for customSdgDef.

        Returns:
            The customSdgDef value

        Note:
            Delegates to custom_sdg_def property (CODING_RULE_V2_00017)
        """
        return self.custom_sdg_def  # Delegates to property

    def getCustom(self) -> List["Documentation"]:
        """
        AUTOSAR-compliant getter for custom.

        Returns:
            The custom value

        Note:
            Delegates to custom property (CODING_RULE_V2_00017)
        """
        return self.custom  # Delegates to property

    def getStandard(self) -> List["String"]:
        """
        AUTOSAR-compliant getter for standard.

        Returns:
            The standard value

        Note:
            Delegates to standard property (CODING_RULE_V2_00017)
        """
        return self.standard  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====


class DataExchangePointKind(AREnum):
    """
    DataExchangePointKind enumeration

Specifies the kind of a DataExchangePoint. Aggregated by DataExchangePoint.kind

Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint
    """
    # the data exchange point description represents the agreed data exchange point that should be used during data exchange consumer the data exchange point description represents the input of a consuming tool. producer the data exchange point description represents the output of a producing tool.
    agreed = "0"



class SeverityEnum(AREnum):
    """
    SeverityEnum enumeration

Definition of severity levels. Aggregated by RestrictionWithSeverity.severity

Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint
    """
    # Something is not right. High risk of interoperability issues.
    error = "2"

    # Something was found that is worth mentioning. Low risk of interoperability issues.
    info = "0"

    # Something might be wrong depending on the context. Medium risk of interoperability issues.
    warning = "1"
