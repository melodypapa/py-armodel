from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class SwValues(ARObject):
    """
    that numerical values and textual values should not be mixed.
    
    Package: M2::MSR::CalibrationData::CalibrationValue::SwValues
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 458, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is a non variant Value.
        # It is provided for sake of ASAM CDF.
        self._v: Optional["Numerical"] = None

    @property
    def v(self) -> Optional["Numerical"]:
        """Get v (Pythonic accessor)."""
        return self._v

    @v.setter
    def v(self, value: Optional["Numerical"]) -> None:
        """
        Set v with validation.
        
        Args:
            value: The v to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._v = None
            return

        if not isinstance(value, Numerical):
            raise TypeError(
                f"v must be Numerical or None, got {type(value).__name__}"
            )
        self._v = value
        # This allows to specify the value as VariationPoint.
        # It is non variant for sake of compatibility to 2.
        # 0.
        self._vf: Optional["Numerical"] = None

    @property
    def vf(self) -> Optional["Numerical"]:
        """Get vf (Pythonic accessor)."""
        return self._vf

    @vf.setter
    def vf(self, value: Optional["Numerical"]) -> None:
        """
        Set vf with validation.
        
        Args:
            value: The vf to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vf = None
            return

        if not isinstance(value, Numerical):
            raise TypeError(
                f"vf must be Numerical or None, got {type(value).__name__}"
            )
        self._vf = value
        # This allows to have intersections in the values in order to rendering (eg.
        # using stylesheets).
        # For is important that the v values are always the same (flattened) order and
                # the tool is interpret it without respecting vg.
        self._vg: RefType = None

    @property
    def vg(self) -> RefType:
        """Get vg (Pythonic accessor)."""
        return self._vg

    @vg.setter
    def vg(self, value: RefType) -> None:
        """
        Set vg with validation.
        
        Args:
            value: The vg to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vg = None
            return

        self._vg = value
        # This represents the values of textual data elements that vt uses the | to
        # separate the values for bitfield masks in case that the semantics of
        # DataPrototype is described by means of a the associated CompuMethod.
        self._vt: Optional["VerbatimString"] = None

    @property
    def vt(self) -> Optional["VerbatimString"]:
        """Get vt (Pythonic accessor)."""
        return self._vt

    @vt.setter
    def vt(self, value: Optional["VerbatimString"]) -> None:
        """
        Set vt with validation.
        
        Args:
            value: The vt to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vt = None
            return

        if not isinstance(value, VerbatimString):
            raise TypeError(
                f"vt must be VerbatimString or None, got {type(value).__name__}"
            )
        self._vt = value
        # This aggregation represents the ability to provide a value either numerical
                # or text which existence is subject formal point of view, the aggregation
                # needs to multiplicity 1 because SwValues is modelled with Nevertheless, the
                # existence of optional and subject to constraints.
        # atpVariation.
        self._vtf: Optional["NumericalOrText"] = None

    @property
    def vtf(self) -> Optional["NumericalOrText"]:
        """Get vtf (Pythonic accessor)."""
        return self._vtf

    @vtf.setter
    def vtf(self, value: Optional["NumericalOrText"]) -> None:
        """
        Set vtf with validation.
        
        Args:
            value: The vtf to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vtf = None
            return

        if not isinstance(value, NumericalOrText):
            raise TypeError(
                f"vtf must be NumericalOrText or None, got {type(value).__name__}"
            )
        self._vtf = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getV(self) -> "Numerical":
        """
        AUTOSAR-compliant getter for v.
        
        Returns:
            The v value
        
        Note:
            Delegates to v property (CODING_RULE_V2_00017)
        """
        return self.v  # Delegates to property

    def setV(self, value: "Numerical") -> "SwValues":
        """
        AUTOSAR-compliant setter for v with method chaining.
        
        Args:
            value: The v to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to v property setter (gets validation automatically)
        """
        self.v = value  # Delegates to property setter
        return self

    def getVf(self) -> "Numerical":
        """
        AUTOSAR-compliant getter for vf.
        
        Returns:
            The vf value
        
        Note:
            Delegates to vf property (CODING_RULE_V2_00017)
        """
        return self.vf  # Delegates to property

    def setVf(self, value: "Numerical") -> "SwValues":
        """
        AUTOSAR-compliant setter for vf with method chaining.
        
        Args:
            value: The vf to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to vf property setter (gets validation automatically)
        """
        self.vf = value  # Delegates to property setter
        return self

    def getVg(self) -> RefType:
        """
        AUTOSAR-compliant getter for vg.
        
        Returns:
            The vg value
        
        Note:
            Delegates to vg property (CODING_RULE_V2_00017)
        """
        return self.vg  # Delegates to property

    def setVg(self, value: RefType) -> "SwValues":
        """
        AUTOSAR-compliant setter for vg with method chaining.
        
        Args:
            value: The vg to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to vg property setter (gets validation automatically)
        """
        self.vg = value  # Delegates to property setter
        return self

    def getVt(self) -> "VerbatimString":
        """
        AUTOSAR-compliant getter for vt.
        
        Returns:
            The vt value
        
        Note:
            Delegates to vt property (CODING_RULE_V2_00017)
        """
        return self.vt  # Delegates to property

    def setVt(self, value: "VerbatimString") -> "SwValues":
        """
        AUTOSAR-compliant setter for vt with method chaining.
        
        Args:
            value: The vt to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to vt property setter (gets validation automatically)
        """
        self.vt = value  # Delegates to property setter
        return self

    def getVtf(self) -> "NumericalOrText":
        """
        AUTOSAR-compliant getter for vtf.
        
        Returns:
            The vtf value
        
        Note:
            Delegates to vtf property (CODING_RULE_V2_00017)
        """
        return self.vtf  # Delegates to property

    def setVtf(self, value: "NumericalOrText") -> "SwValues":
        """
        AUTOSAR-compliant setter for vtf with method chaining.
        
        Args:
            value: The vtf to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to vtf property setter (gets validation automatically)
        """
        self.vtf = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_v(self, value: Optional["Numerical"]) -> "SwValues":
        """
        Set v and return self for chaining.
        
        Args:
            value: The v to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_v("value")
        """
        self.v = value  # Use property setter (gets validation)
        return self

    def with_vf(self, value: Optional["Numerical"]) -> "SwValues":
        """
        Set vf and return self for chaining.
        
        Args:
            value: The vf to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_vf("value")
        """
        self.vf = value  # Use property setter (gets validation)
        return self

    def with_vg(self, value: Optional[RefType]) -> "SwValues":
        """
        Set vg and return self for chaining.
        
        Args:
            value: The vg to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_vg("value")
        """
        self.vg = value  # Use property setter (gets validation)
        return self

    def with_vt(self, value: Optional["VerbatimString"]) -> "SwValues":
        """
        Set vt and return self for chaining.
        
        Args:
            value: The vt to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_vt("value")
        """
        self.vt = value  # Use property setter (gets validation)
        return self

    def with_vtf(self, value: Optional["NumericalOrText"]) -> "SwValues":
        """
        Set vtf and return self for chaining.
        
        Args:
            value: The vtf to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_vtf("value")
        """
        self.vtf = value  # Use property setter (gets validation)
        return self