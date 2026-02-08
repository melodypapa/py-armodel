from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class DocRevision(ARObject):
    """
    This meta-class represents the ability to maintain information which relates
    to revision management of documents or objects.

    Package: M2::MSR::AsamHdo::AdminData

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 293, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 85, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This specifies the date and time, when the object in released.
        self._date: "DateTime" = None

    @property
    def date(self) -> "DateTime":
        """Get date (Pythonic accessor)."""
        return self._date

    @date.setter
    def date(self, value: "DateTime") -> None:
        """
        Set date with validation.

        Args:
            value: The date to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, DateTime):
            raise TypeError(
                f"date must be DateTime, got {type(value).__name__}"
            )
        self._date = value
        # This is the name of an individual or an organization who current revision of
        # the document or document.
        self._issuedBy: Optional["String"] = None

    @property
    def issued_by(self) -> Optional["String"]:
        """Get issuedBy (Pythonic accessor)."""
        return self._issuedBy

    @issued_by.setter
    def issued_by(self, value: Optional["String"]) -> None:
        """
        Set issuedBy with validation.

        Args:
            value: The issuedBy to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._issuedBy = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"issuedBy must be String or None, got {type(value).__name__}"
            )
        self._issuedBy = value
        # This property represents one particular modification in its predecessor.
        self._modification: List["Modification"] = []

    @property
    def modification(self) -> List["Modification"]:
        """Get modification (Pythonic accessor)."""
        return self._modification
        # This attribute represents the version number of the object.
        self._revisionLabel: Optional["RevisionLabelString"] = None

    @property
    def revision_label(self) -> Optional["RevisionLabelString"]:
        """Get revisionLabel (Pythonic accessor)."""
        return self._revisionLabel

    @revision_label.setter
    def revision_label(self, value: Optional["RevisionLabelString"]) -> None:
        """
        Set revisionLabel with validation.

        Args:
            value: The revisionLabel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._revisionLabel = None
            return

        if not isinstance(value, RevisionLabelString):
            raise TypeError(
                f"revisionLabel must be RevisionLabelString or None, got {type(value).__name__}"
            )
        self._revisionLabel = value
        # This attribute represents the version number of the first the object.
        self._revisionLabelP1: Optional["RevisionLabelString"] = None

    @property
    def revision_label_p1(self) -> Optional["RevisionLabelString"]:
        """Get revisionLabelP1 (Pythonic accessor)."""
        return self._revisionLabelP1

    @revision_label_p1.setter
    def revision_label_p1(self, value: Optional["RevisionLabelString"]) -> None:
        """
        Set revisionLabelP1 with validation.

        Args:
            value: The revisionLabelP1 to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._revisionLabelP1 = None
            return

        if not isinstance(value, RevisionLabelString):
            raise TypeError(
                f"revisionLabelP1 must be RevisionLabelString or None, got {type(value).__name__}"
            )
        self._revisionLabelP1 = value
        # This attribute represents the version number of the of the object.
        # is used if the object is the result of a merge which two branches are merged
                # in to one new.
        self._revisionLabelP2: Optional["RevisionLabelString"] = None

    @property
    def revision_label_p2(self) -> Optional["RevisionLabelString"]:
        """Get revisionLabelP2 (Pythonic accessor)."""
        return self._revisionLabelP2

    @revision_label_p2.setter
    def revision_label_p2(self, value: Optional["RevisionLabelString"]) -> None:
        """
        Set revisionLabelP2 with validation.

        Args:
            value: The revisionLabelP2 to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._revisionLabelP2 = None
            return

        if not isinstance(value, RevisionLabelString):
            raise TypeError(
                f"revisionLabelP2 must be RevisionLabelString or None, got {type(value).__name__}"
            )
        self._revisionLabelP2 = value
        # The attribute state represents the current state of the according to the
        # configuration management is a NameToken until possible states are.
        self._state: Optional["NameToken"] = None

    @property
    def state(self) -> Optional["NameToken"]:
        """Get state (Pythonic accessor)."""
        return self._state

    @state.setter
    def state(self, value: Optional["NameToken"]) -> None:
        """
        Set state with validation.

        Args:
            value: The state to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._state = None
            return

        if not isinstance(value, NameToken):
            raise TypeError(
                f"state must be NameToken or None, got {type(value).__name__}"
            )
        self._state = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDate(self) -> "DateTime":
        """
        AUTOSAR-compliant getter for date.

        Returns:
            The date value

        Note:
            Delegates to date property (CODING_RULE_V2_00017)
        """
        return self.date  # Delegates to property

    def setDate(self, value: "DateTime") -> "DocRevision":
        """
        AUTOSAR-compliant setter for date with method chaining.

        Args:
            value: The date to set

        Returns:
            self for method chaining

        Note:
            Delegates to date property setter (gets validation automatically)
        """
        self.date = value  # Delegates to property setter
        return self

    def getIssuedBy(self) -> "String":
        """
        AUTOSAR-compliant getter for issuedBy.

        Returns:
            The issuedBy value

        Note:
            Delegates to issued_by property (CODING_RULE_V2_00017)
        """
        return self.issued_by  # Delegates to property

    def setIssuedBy(self, value: "String") -> "DocRevision":
        """
        AUTOSAR-compliant setter for issuedBy with method chaining.

        Args:
            value: The issuedBy to set

        Returns:
            self for method chaining

        Note:
            Delegates to issued_by property setter (gets validation automatically)
        """
        self.issued_by = value  # Delegates to property setter
        return self

    def getModification(self) -> List["Modification"]:
        """
        AUTOSAR-compliant getter for modification.

        Returns:
            The modification value

        Note:
            Delegates to modification property (CODING_RULE_V2_00017)
        """
        return self.modification  # Delegates to property

    def getRevisionLabel(self) -> "RevisionLabelString":
        """
        AUTOSAR-compliant getter for revisionLabel.

        Returns:
            The revisionLabel value

        Note:
            Delegates to revision_label property (CODING_RULE_V2_00017)
        """
        return self.revision_label  # Delegates to property

    def setRevisionLabel(self, value: "RevisionLabelString") -> "DocRevision":
        """
        AUTOSAR-compliant setter for revisionLabel with method chaining.

        Args:
            value: The revisionLabel to set

        Returns:
            self for method chaining

        Note:
            Delegates to revision_label property setter (gets validation automatically)
        """
        self.revision_label = value  # Delegates to property setter
        return self

    def getRevisionLabelP1(self) -> "RevisionLabelString":
        """
        AUTOSAR-compliant getter for revisionLabelP1.

        Returns:
            The revisionLabelP1 value

        Note:
            Delegates to revision_label_p1 property (CODING_RULE_V2_00017)
        """
        return self.revision_label_p1  # Delegates to property

    def setRevisionLabelP1(self, value: "RevisionLabelString") -> "DocRevision":
        """
        AUTOSAR-compliant setter for revisionLabelP1 with method chaining.

        Args:
            value: The revisionLabelP1 to set

        Returns:
            self for method chaining

        Note:
            Delegates to revision_label_p1 property setter (gets validation automatically)
        """
        self.revision_label_p1 = value  # Delegates to property setter
        return self

    def getRevisionLabelP2(self) -> "RevisionLabelString":
        """
        AUTOSAR-compliant getter for revisionLabelP2.

        Returns:
            The revisionLabelP2 value

        Note:
            Delegates to revision_label_p2 property (CODING_RULE_V2_00017)
        """
        return self.revision_label_p2  # Delegates to property

    def setRevisionLabelP2(self, value: "RevisionLabelString") -> "DocRevision":
        """
        AUTOSAR-compliant setter for revisionLabelP2 with method chaining.

        Args:
            value: The revisionLabelP2 to set

        Returns:
            self for method chaining

        Note:
            Delegates to revision_label_p2 property setter (gets validation automatically)
        """
        self.revision_label_p2 = value  # Delegates to property setter
        return self

    def getState(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for state.

        Returns:
            The state value

        Note:
            Delegates to state property (CODING_RULE_V2_00017)
        """
        return self.state  # Delegates to property

    def setState(self, value: "NameToken") -> "DocRevision":
        """
        AUTOSAR-compliant setter for state with method chaining.

        Args:
            value: The state to set

        Returns:
            self for method chaining

        Note:
            Delegates to state property setter (gets validation automatically)
        """
        self.state = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_date(self, value: "DateTime") -> "DocRevision":
        """
        Set date and return self for chaining.

        Args:
            value: The date to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_date("value")
        """
        self.date = value  # Use property setter (gets validation)
        return self

    def with_issued_by(self, value: Optional["String"]) -> "DocRevision":
        """
        Set issuedBy and return self for chaining.

        Args:
            value: The issuedBy to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_issued_by("value")
        """
        self.issued_by = value  # Use property setter (gets validation)
        return self

    def with_revision_label(self, value: Optional["RevisionLabelString"]) -> "DocRevision":
        """
        Set revisionLabel and return self for chaining.

        Args:
            value: The revisionLabel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_revision_label("value")
        """
        self.revision_label = value  # Use property setter (gets validation)
        return self

    def with_revision_label_p1(self, value: Optional["RevisionLabelString"]) -> "DocRevision":
        """
        Set revisionLabelP1 and return self for chaining.

        Args:
            value: The revisionLabelP1 to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_revision_label_p1("value")
        """
        self.revision_label_p1 = value  # Use property setter (gets validation)
        return self

    def with_revision_label_p2(self, value: Optional["RevisionLabelString"]) -> "DocRevision":
        """
        Set revisionLabelP2 and return self for chaining.

        Args:
            value: The revisionLabelP2 to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_revision_label_p2("value")
        """
        self.revision_label_p2 = value  # Use property setter (gets validation)
        return self

    def with_state(self, value: Optional["NameToken"]) -> "DocRevision":
        """
        Set state and return self for chaining.

        Args:
            value: The state to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_state("value")
        """
        self.state = value  # Use property setter (gets validation)
        return self
