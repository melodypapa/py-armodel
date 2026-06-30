"""
Test to verify all model classes can be imported from armodel directly.

This test ensures that all model classes defined in the codebase can be
imported from the top-level `armodel` module, confirming that wildcard imports
are properly configured throughout the package structure.

Known limitation: 13 classes in subdirectories with name collisions cannot be
directly imported and are excluded from this test:
- BswBehavior/*.py files (9 classes)
- BswInterfaces/*.py files (3 classes)
- BswOverview/InstanceRefs/*.py files (1 class)
"""

import ast
import os
from pathlib import Path
import pytest

import armodel


# Classes that cannot be imported directly due to name collisions
# These are accessible via their full import paths instead
KNOWN_NAME_COLLISION_CLASSES = {
    # BswBehavior/*.py files (9 classes)
    "BswAsynchronousServerCallReturnsEvent",
    "BswExclusiveAreaPolicy",
    "BswInterruptEvent",
    "BswModeManagerErrorEvent",
    "BswModeReceiverPolicy",
    "BswSchedulerNamePrefix",
    "BswServiceDependency",
    "BswTriggerDirectImplementation",
    "RoleBasedBswModuleEntryAssignment",
    # BswInterfaces/*.py files (3 classes)
    "BswEntryRelationship",
    "BswEntryRelationshipEnum",
    "BswEntryRelationshipSet",
    # BswOverview/InstanceRefs/*.py files (1 class)
    "ModeInBswModuleDescriptionInstanceRef",
}

# Classes in modules that are intentionally NOT exported from armodel
# These are either incomplete, experimental, or for internal use only
INTENTIONALLY_UNEXPORTED_MODULES = {
    # AdaptivePlatform - incomplete/experimental AUTOSAR Adaptive Platform support
    "AgeConstraint",
    "ApplicationDeferredDataType",
    "ApplicationInterface",
    "ArbitraryEventTriggering",
    "BurstPatternEventTriggering",
    "ConcretePatternEventTriggering",
    "ConfidenceInterval",
    "CryptoKeySlot",
    "CryptoKeySlotContent",
    "EventOccurrenceKindEnum",
    "EventTriggeringConstraint",
    "ExecutionTimeConstraint",
    "ExecutionTimeTypeEnum",
    "Field",
    "FirewallRule",
    "FirewallRuleProps",
    "IdsPlatformInstantiation",
    "IdsmModuleInstantiation",
    "LatencyConstraintTypeEnum",
    "LatencyTimingConstraint",
    "McDataAccessDetails",
    "McDataInstance",
    "McFunction",
    "McFunctionDataRefSet",
    "McGroup",
    "McGroupDataRefSet",
    "McParameterElementGroup",
    "McSupportData",
    "McSwEmulationMethodSupport",
    "ModeErrorBehavior",
    "ModeErrorReactionPolicyEnum",
    "ModeInBswInstanceRef",
    "ModeInSwcInstanceRef",
    "ModeTransition",
    "OffsetTimingConstraint",
    "PeriodicEventTriggering",
    "PlatformModuleEthernetEndpointConfiguration",
    "RoleBasedMcDataAssignment",
    "RptAccessEnum",
    "RptComponent",
    "RptEnablerImplTypeEnum",
    "RptExecutableEntity",
    "RptExecutableEntityEvent",
    "RptExecutionContext",
    "RptExecutionControlEnum",
    "RptPreparationEnum",
    "RptServicePoint",
    "RptSupportData",
    "RptSwPrototypingAccess",
    "SignalServiceTranslationControlEnum",
    "SignalServiceTranslationElementProps",
    "SignalServiceTranslationEventProps",
    "SignalServiceTranslationProps",
    "SignalServiceTranslationPropsSet",
    "SporadicEventTriggering",
    "StateDependentFirewall",
    "SynchronizationPointConstraint",
    "SynchronizationTimingConstraint",
    "SynchronizationTypeEnum",
    "TDLETZoneClock",
    "TimingClock",
    "TimingClockSyncAccuracy",
    "TimingCondition",
    "TimingConditionFormula",
    "TimingExtensionResource",
    "TimingModeInstance",
    # Blueprint/Standardization - incomplete/experimental
    "BlueprintGenerator",
    "BlueprintMappingSet",
    "ImplementationElementInParameterInstanceRef",
}


def get_class_info(filepath):
    """Extract class names from a Python file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            source = f.read()
        tree = ast.parse(source, filename=filepath)
    except (SyntaxError, UnicodeDecodeError):
        return []

    classes = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            classes.append(node.name)
    return classes


def discover_model_classes():
    """Scan all model Python files and return all class definitions."""
    base_dir = Path(__file__).parent.parent.parent / "src" / "armodel" / "models"
    classes = set()

    for root, dirs, files in os.walk(base_dir):
        # Exclude build directory and __pycache__
        dirs[:] = [d for d in dirs if d not in ("__pycache__", "build")]

        for fname in sorted(files):
            if not fname.endswith(".py"):
                continue
            if fname == "__init__.py":
                continue

            filepath = os.path.join(root, fname)
            file_classes = get_class_info(filepath)
            classes.update(file_classes)

    return classes


class TestModelImports:
    """Test that all model classes can be imported from armodel directly."""

    def test_all_model_classes_importable(self):
        """Verify all model classes can be imported from armodel."""
        discovered_classes = discover_model_classes()

        # Remove known name collision classes and intentionally unexported modules
        testable_classes = (
            discovered_classes
            - KNOWN_NAME_COLLISION_CLASSES
            - INTENTIONALLY_UNEXPORTED_MODULES
        )

        # Track any missing imports
        missing_imports = []

        for class_name in sorted(testable_classes):
            try:
                assert hasattr(armodel, class_name), (
                    f"Class '{class_name}' cannot be imported from armodel. "
                    f"Ensure it's properly exported via wildcard imports."
                )
            except AssertionError:
                missing_imports.append(class_name)

        # Report all missing imports at once for easier debugging
        if missing_imports:
            pytest.fail(
                f"\n{len(missing_imports)} model classes cannot be imported from armodel:\n"
                f"{', '.join(sorted(missing_imports))}\n\n"
                f"Check that these classes are properly exported in the "
                f"wildcard import chain: armodel -> armodel.models -> M2 modules"
            )

        # Sanity check - ensure we're testing something
        assert len(testable_classes) > 100, (
            f"Test discovered only {len(testable_classes)} classes, "
            "which seems unexpectedly low. Check discovery logic."
        )
