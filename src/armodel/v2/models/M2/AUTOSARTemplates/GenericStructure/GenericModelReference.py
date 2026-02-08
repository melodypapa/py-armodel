from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class GenericModelReference(ARObject):
    """
    This meta-class represents the ability to express a late binding reference
    to a model element. The model element can be from every model. Even if it is
    modeled according to the association representation, it is not limited to
    refer to AUTOSAR model elements.

    Package: M2::AUTOSARTemplates::GenericStructure::BuildActionManifest::GenericModelReference

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 449, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This establishes the reference base.
        self._base: "NameToken" = None

    @property
    def base(self) -> "NameToken":
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: "NameToken") -> None:
        """
        Set base with validation.

        Args:
            value: The base to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, NameToken):
            raise TypeError(
                f"base must be NameToken, got {type(value).__name__}"
            )
        self._base = value
        # This attribute represents the class of the referenced It is a String, since
                # the model element in any model.
        # Therefore we cannot have any.
        self._dest: "NameToken" = None

    @property
    def dest(self) -> "NameToken":
        """Get dest (Pythonic accessor)."""
        return self._dest

    @dest.setter
    def dest(self, value: "NameToken") -> None:
        """
        Set dest with validation.

        Args:
            value: The dest to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, NameToken):
            raise TypeError(
                f"dest must be NameToken, got {type(value).__name__}"
            )
        self._dest = value
        # This is the full qualified name of the model element.
        self._ref: RefType = None

    @property
    def ref(self) -> RefType:
        """Get ref (Pythonic accessor)."""
        return self._ref

    @ref.setter
    def ref(self, value: RefType) -> None:
        """
        Set ref with validation.

        Args:
            value: The ref to set

        Raises:
            TypeError: If value type is incorrect
        """
        self._ref = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBase(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for base.

        Returns:
            The base value

        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: "NameToken") -> "GenericModelReference":
        """
        AUTOSAR-compliant setter for base with method chaining.

        Args:
            value: The base to set

        Returns:
            self for method chaining

        Note:
            Delegates to base property setter (gets validation automatically)
        """
        self.base = value  # Delegates to property setter
        return self

    def getDest(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for dest.

        Returns:
            The dest value

        Note:
            Delegates to dest property (CODING_RULE_V2_00017)
        """
        return self.dest  # Delegates to property

    def setDest(self, value: "NameToken") -> "GenericModelReference":
        """
        AUTOSAR-compliant setter for dest with method chaining.

        Args:
            value: The dest to set

        Returns:
            self for method chaining

        Note:
            Delegates to dest property setter (gets validation automatically)
        """
        self.dest = value  # Delegates to property setter
        return self

    def getRef(self) -> RefType:
        """
        AUTOSAR-compliant getter for ref.

        Returns:
            The ref value

        Note:
            Delegates to ref property (CODING_RULE_V2_00017)
        """
        return self.ref  # Delegates to property

    def setRef(self, value: RefType) -> "GenericModelReference":
        """
        AUTOSAR-compliant setter for ref with method chaining.

        Args:
            value: The ref to set

        Returns:
            self for method chaining

        Note:
            Delegates to ref property setter (gets validation automatically)
        """
        self.ref = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base(self, value: "NameToken") -> "GenericModelReference":
        """
        Set base and return self for chaining.

        Args:
            value: The base to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_base("value")
        """
        self.base = value  # Use property setter (gets validation)
        return self

    def with_dest(self, value: "NameToken") -> "GenericModelReference":
        """
        Set dest and return self for chaining.

        Args:
            value: The dest to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dest("value")
        """
        self.dest = value  # Use property setter (gets validation)
        return self

    def with_ref(self, value: RefType) -> "GenericModelReference":
        """
        Set ref and return self for chaining.

        Args:
            value: The ref to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ref("value")
        """
        self.ref = value  # Use property setter (gets validation)
        return self
