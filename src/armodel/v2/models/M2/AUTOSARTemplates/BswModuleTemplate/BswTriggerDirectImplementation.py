from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class BswTriggerDirectImplementation(ARObject):
    """
    Specifies a released trigger to be directly implemented via OS calls, for
    example in a Complex Driver module.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswTriggerDirectImplementation

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 102, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The name of the OS category 2 ISR, which is controlled referred trigger.
        # This means, that the module category 2 ISR (e.
        # g.
        # according hardware enabling of ISR).
        # Instead of calling an SchM API to raise the appropriate events in modules
                # receiving the trigger, this ISR the triggered ExecutableEntitys.
        # The is required by the integrator to map the Bsw RTEEvents to this ISR.
        self._cat2Isr: Optional["Identifier"] = None

    @property
    def cat2_isr(self) -> Optional["Identifier"]:
        """Get cat2Isr (Pythonic accessor)."""
        return self._cat2Isr

    @cat2_isr.setter
    def cat2_isr(self, value: Optional["Identifier"]) -> None:
        """
        Set cat2Isr with validation.

        Args:
            value: The cat2Isr to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cat2Isr = None
            return

        if not isinstance(value, Identifier):
            raise TypeError(
                f"cat2Isr must be Identifier or None, got {type(value).__name__}"
            )
        self._cat2Isr = value
        # The trigger which is directly mastered by this module.
        # be several different BswTriggerDirect the same Trigger.
        # This may e.
        # g.
        # due to memory partitioning.
        self._masteredTrigger: RefType = None

    @property
    def mastered_trigger(self) -> RefType:
        """Get masteredTrigger (Pythonic accessor)."""
        return self._masteredTrigger

    @mastered_trigger.setter
    def mastered_trigger(self, value: RefType) -> None:
        """
        Set masteredTrigger with validation.

        Args:
            value: The masteredTrigger to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._masteredTrigger = None
            return

        self._masteredTrigger = value
        # The name of the OS task, which is controlled by the This means, that the
                # module uses the to directly activate an OS task instead of API of the
                # BswScheduler.
        # The task name is the RTE generator resp.
        # BswScheduler to appropriate events in components or modules trigger.
        self._task: Optional["Identifier"] = None

    @property
    def task(self) -> Optional["Identifier"]:
        """Get task (Pythonic accessor)."""
        return self._task

    @task.setter
    def task(self, value: Optional["Identifier"]) -> None:
        """
        Set task with validation.

        Args:
            value: The task to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._task = None
            return

        if not isinstance(value, Identifier):
            raise TypeError(
                f"task must be Identifier or None, got {type(value).__name__}"
            )
        self._task = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCat2Isr(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for cat2Isr.

        Returns:
            The cat2Isr value

        Note:
            Delegates to cat2_isr property (CODING_RULE_V2_00017)
        """
        return self.cat2_isr  # Delegates to property

    def setCat2Isr(self, value: "Identifier") -> "BswTriggerDirectImplementation":
        """
        AUTOSAR-compliant setter for cat2Isr with method chaining.

        Args:
            value: The cat2Isr to set

        Returns:
            self for method chaining

        Note:
            Delegates to cat2_isr property setter (gets validation automatically)
        """
        self.cat2_isr = value  # Delegates to property setter
        return self

    def getMasteredTrigger(self) -> RefType:
        """
        AUTOSAR-compliant getter for masteredTrigger.

        Returns:
            The masteredTrigger value

        Note:
            Delegates to mastered_trigger property (CODING_RULE_V2_00017)
        """
        return self.mastered_trigger  # Delegates to property

    def setMasteredTrigger(self, value: RefType) -> "BswTriggerDirectImplementation":
        """
        AUTOSAR-compliant setter for masteredTrigger with method chaining.

        Args:
            value: The masteredTrigger to set

        Returns:
            self for method chaining

        Note:
            Delegates to mastered_trigger property setter (gets validation automatically)
        """
        self.mastered_trigger = value  # Delegates to property setter
        return self

    def getTask(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for task.

        Returns:
            The task value

        Note:
            Delegates to task property (CODING_RULE_V2_00017)
        """
        return self.task  # Delegates to property

    def setTask(self, value: "Identifier") -> "BswTriggerDirectImplementation":
        """
        AUTOSAR-compliant setter for task with method chaining.

        Args:
            value: The task to set

        Returns:
            self for method chaining

        Note:
            Delegates to task property setter (gets validation automatically)
        """
        self.task = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_cat2_isr(self, value: Optional["Identifier"]) -> "BswTriggerDirectImplementation":
        """
        Set cat2Isr and return self for chaining.

        Args:
            value: The cat2Isr to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cat2_isr("value")
        """
        self.cat2_isr = value  # Use property setter (gets validation)
        return self

    def with_mastered_trigger(self, value: Optional[RefType]) -> "BswTriggerDirectImplementation":
        """
        Set masteredTrigger and return self for chaining.

        Args:
            value: The masteredTrigger to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mastered_trigger("value")
        """
        self.mastered_trigger = value  # Use property setter (gets validation)
        return self

    def with_task(self, value: Optional["Identifier"]) -> "BswTriggerDirectImplementation":
        """
        Set task and return self for chaining.

        Args:
            value: The task to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_task("value")
        """
        self.task = value  # Use property setter (gets validation)
        return self
