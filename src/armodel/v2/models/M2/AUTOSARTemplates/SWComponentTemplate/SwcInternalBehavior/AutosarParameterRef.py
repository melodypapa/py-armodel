from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class AutosarParameterRef(ARObject):
    """
    This class represents a reference to a parameter within AUTOSAR which can be
    one of the following use cases: localParameter: • localParameter which is
    used as whole (e.g. sharedAxis for curve) autosarVariable: • a parameter
    provided via PortPrototype which is used as whole (e.g. parameterAccess) •
    an element inside of a composite local parameter typed by
    ApplicationDatatype (e.g. sharedAxis for a curve) • an element inside of a
    composite parameter provided via Port and typed by ApplicationDatatype (e.g.
    sharedAxis for a curve) autosarParameterInImplDatatype: • an element inside
    of a composite local parameter typed by ImplementationDatatype • an element
    inside of a composite parameter provided via PortPrototype and typed by
    Implementation Datatype

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::DataElements::AutosarParameterRef

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 306, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 317, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # is either imported via a port or is part of a structure.
        # by: ParameterInAtomicSWC 381 Document ID 89:
                # AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module Description Template
                # R23-11.
        self._autosar: RefType = None

    @property
    def autosar(self) -> RefType:
        """Get autosar (Pythonic accessor)."""
        return self._autosar

    @autosar.setter
    def autosar(self, value: RefType) -> None:
        """
        Set autosar with validation.

        Args:
            value: The autosar to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._autosar = None
            return

        self._autosar = value
        # In the majority of cases this reference goes to Parameter than
                # VariableDataPrototypes.
        # reference to a VariableDataPrototype is special use cases, e.
        # g.
        # if the AutosarParameter used in the context of an SwAxisGrouped.
        # is used if the arParameter is local to the it would technically also be
                # feasible to use an this case.
        # However, the InstanceRef have a contextElement (because the current the
                # context).
        # local instance is a special case which may optimization.
        # Therefore an explicit provided for this case.
        self._localParameter: RefType = None

    @property
    def local_parameter(self) -> RefType:
        """Get localParameter (Pythonic accessor)."""
        return self._localParameter

    @local_parameter.setter
    def local_parameter(self, value: RefType) -> None:
        """
        Set localParameter with validation.

        Args:
            value: The localParameter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._localParameter = None
            return

        self._localParameter = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAutosar(self) -> RefType:
        """
        AUTOSAR-compliant getter for autosar.

        Returns:
            The autosar value

        Note:
            Delegates to autosar property (CODING_RULE_V2_00017)
        """
        return self.autosar  # Delegates to property

    def setAutosar(self, value: RefType) -> "AutosarParameterRef":
        """
        AUTOSAR-compliant setter for autosar with method chaining.

        Args:
            value: The autosar to set

        Returns:
            self for method chaining

        Note:
            Delegates to autosar property setter (gets validation automatically)
        """
        self.autosar = value  # Delegates to property setter
        return self

    def getLocalParameter(self) -> RefType:
        """
        AUTOSAR-compliant getter for localParameter.

        Returns:
            The localParameter value

        Note:
            Delegates to local_parameter property (CODING_RULE_V2_00017)
        """
        return self.local_parameter  # Delegates to property

    def setLocalParameter(self, value: RefType) -> "AutosarParameterRef":
        """
        AUTOSAR-compliant setter for localParameter with method chaining.

        Args:
            value: The localParameter to set

        Returns:
            self for method chaining

        Note:
            Delegates to local_parameter property setter (gets validation automatically)
        """
        self.local_parameter = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_autosar(self, value: Optional[RefType]) -> "AutosarParameterRef":
        """
        Set autosar and return self for chaining.

        Args:
            value: The autosar to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_autosar("value")
        """
        self.autosar = value  # Use property setter (gets validation)
        return self

    def with_local_parameter(self, value: Optional[RefType]) -> "AutosarParameterRef":
        """
        Set localParameter and return self for chaining.

        Args:
            value: The localParameter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_local_parameter("value")
        """
        self.local_parameter = value  # Use property setter (gets validation)
        return self
