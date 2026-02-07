from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class BuildActionIoElement(ARObject):
    """
    that the reference to the definition denotes the right for a build action to
    read and/or write values for the given definition and all contained
    definitions. engineering BuildEngineeringObject 0..1 aggr This represents an
    artifact applicable to the build action. Object foreignModel
    ForeignModelReference 0..1 aggr This is a reference to a foreign model
    element. Note that Reference it is not modeled as an association because it
    should also be able to refer also to non AUTOSAR models. (cid:53) 368 of 535
    Document ID 202: AUTOSAR_FO_TPS_GenericStructureTemplate Generic Structure
    Template AUTOSAR FO R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::GenericStructure::BuildActionManifest::BuildActionIoElement

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 368, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This element assigns a category to the parent element.
        # It to specialize the usage and/or the content of Such a specialization may
                # also impose constraints on the entire substructure.
        # Identifiable.
        self._category: "NameToken" = None

    @property
    def category(self) -> "NameToken":
        """Get category (Pythonic accessor)."""
        return self._category

    @category.setter
    def category(self, value: "NameToken") -> None:
        """
        Set category with validation.

        Args:
            value: The category to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, NameToken):
            raise TypeError(
                f"category must be NameToken, got {type(value).__name__}"
            )
        self._category = value
        # This association denotes an ECUC parameter definition.
        # referenced parameters are subject of the build.
        self._ecucDefinition: Optional["EcucDefinitionElement"] = None

    @property
    def ecuc_definition(self) -> Optional["EcucDefinitionElement"]:
        """Get ecucDefinition (Pythonic accessor)."""
        return self._ecucDefinition

    @ecuc_definition.setter
    def ecuc_definition(self, value: Optional["EcucDefinitionElement"]) -> None:
        """
        Set ecucDefinition with validation.

        Args:
            value: The ecucDefinition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecucDefinition = None
            return

        if not isinstance(value, EcucDefinitionElement):
            raise TypeError(
                f"ecucDefinition must be EcucDefinitionElement or None, got {type(value).__name__}"
            )
        self._ecucDefinition = value
        # This attribute allows to denote a particular role of the that the applicable
        # semantics shall be between the two parties.
        self._role: Optional["Identifier"] = None

    @property
    def role(self) -> Optional["Identifier"]:
        """Get role (Pythonic accessor)."""
        return self._role

    @role.setter
    def role(self, value: Optional["Identifier"]) -> None:
        """
        Set role with validation.

        Args:
            value: The role to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._role = None
            return

        if not isinstance(value, Identifier):
            raise TypeError(
                f"role must be Identifier or None, got {type(value).__name__}"
            )
        self._role = value
        # This special data group allows to denote specific data.
        # is subject of mutual agreement.
        self._sdg: List["Sdg"] = []

    @property
    def sdg(self) -> List["Sdg"]:
        """Get sdg (Pythonic accessor)."""
        return self._sdg

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCategory(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for category.

        Returns:
            The category value

        Note:
            Delegates to category property (CODING_RULE_V2_00017)
        """
        return self.category  # Delegates to property

    def setCategory(self, value: "NameToken") -> "BuildActionIoElement":
        """
        AUTOSAR-compliant setter for category with method chaining.

        Args:
            value: The category to set

        Returns:
            self for method chaining

        Note:
            Delegates to category property setter (gets validation automatically)
        """
        self.category = value  # Delegates to property setter
        return self

    def getEcucDefinition(self) -> "EcucDefinitionElement":
        """
        AUTOSAR-compliant getter for ecucDefinition.

        Returns:
            The ecucDefinition value

        Note:
            Delegates to ecuc_definition property (CODING_RULE_V2_00017)
        """
        return self.ecuc_definition  # Delegates to property

    def setEcucDefinition(self, value: "EcucDefinitionElement") -> "BuildActionIoElement":
        """
        AUTOSAR-compliant setter for ecucDefinition with method chaining.

        Args:
            value: The ecucDefinition to set

        Returns:
            self for method chaining

        Note:
            Delegates to ecuc_definition property setter (gets validation automatically)
        """
        self.ecuc_definition = value  # Delegates to property setter
        return self

    def getRole(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for role.

        Returns:
            The role value

        Note:
            Delegates to role property (CODING_RULE_V2_00017)
        """
        return self.role  # Delegates to property

    def setRole(self, value: "Identifier") -> "BuildActionIoElement":
        """
        AUTOSAR-compliant setter for role with method chaining.

        Args:
            value: The role to set

        Returns:
            self for method chaining

        Note:
            Delegates to role property setter (gets validation automatically)
        """
        self.role = value  # Delegates to property setter
        return self

    def getSdg(self) -> List["Sdg"]:
        """
        AUTOSAR-compliant getter for sdg.

        Returns:
            The sdg value

        Note:
            Delegates to sdg property (CODING_RULE_V2_00017)
        """
        return self.sdg  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_category(self, value: "NameToken") -> "BuildActionIoElement":
        """
        Set category and return self for chaining.

        Args:
            value: The category to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_category("value")
        """
        self.category = value  # Use property setter (gets validation)
        return self

    def with_ecuc_definition(self, value: Optional["EcucDefinitionElement"]) -> "BuildActionIoElement":
        """
        Set ecucDefinition and return self for chaining.

        Args:
            value: The ecucDefinition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ecuc_definition("value")
        """
        self.ecuc_definition = value  # Use property setter (gets validation)
        return self

    def with_role(self, value: Optional["Identifier"]) -> "BuildActionIoElement":
        """
        Set role and return self for chaining.

        Args:
            value: The role to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_role("value")
        """
        self.role = value  # Use property setter (gets validation)
        return self
