#!/usr/bin/env python3
"""
Script to refactor CommonStructure V2 module.
- Convert V1 imports to V2 imports
- Add __all__ to __init__.py files
"""

import os
import re
from pathlib import Path

# Define import path mappings
IMPORT_MAPPINGS = {
    # GenericStructure mappings
    "from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import":
    "from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import",

    "from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import":
    "from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import",

    "from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import":
    "from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import",

    "from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import":
    "from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import",

    "from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.":
    "from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.",

    # CommonStructure mappings - parent directory files
    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationElementInParameterInstanceRef import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ImplementationElementInParameterInstanceRef import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.McDataAccessDetails import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.McDataAccessDetails import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.McDataInstance import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.McDataInstance import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.McFunction import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.McFunction import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.McParameterElementGroup import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.McParameterElementGroup import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.McSwEmulationMethodSupport import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.McSwEmulationMethodSupport import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.RoleBasedMcDataAssignment import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.RoleBasedMcDataAssignment import",

    # CommonStructure mappings - MeasurementCalibrationSupport
    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.",

    # CommonStructure mappings - Constants
    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Constants import",

    # CommonStructure mappings - SignalServiceTranslation
    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.SignalServiceTranslationControlEnum import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.SignalServiceTranslation.SignalServiceTranslationControlEnum import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.SignalServiceTranslationElementProps import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.SignalServiceTranslation.SignalServiceTranslationElementProps import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.SignalServiceTranslationEventProps import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.SignalServiceTranslation.SignalServiceTranslationEventProps import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.SignalServiceTranslationProps import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.SignalServiceTranslation.SignalServiceTranslationProps import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.SignalServiceTranslationPropsSet import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.SignalServiceTranslation.SignalServiceTranslationPropsSet import",

    # CommonStructure - ValueSpecification
    "from armodel.models.M2.AUTOSARTemplates.CommonStructure import ValueSpecification":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Constants import ValueSpecification",

    # CommonStructure - ResourceConsumption
    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import",

    # CommonStructure - StandardizationTemplate
    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintGenerator import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintGenerator.BlueprintGenerator import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import AtpBlueprintable":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.AtpBlueprint import AtpBlueprintable",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.AtpBlueprint import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintMappingSet import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintMapping.BlueprintMappingSet import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintDedicated.PortPrototypeBlueprint import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintDedicated.PortPrototypeBlueprint.PortPrototypeBlueprint import",

    # CommonStructure - Timing (parent to subdirs)
    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TDLETZoneClock import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.TDLETZoneClock import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.TimingClock import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClockSyncAccuracy import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.TimingClockSyncAccuracy import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.ModeInBswInstanceRef import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.ModeInBswInstanceRef import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.ModeInSwcInstanceRef import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.ModeInSwcInstanceRef import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.TimingCondition import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConditionFormula import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.TimingConditionFormula import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensionResource import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.TimingExtensionResource import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingModeInstance import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.TimingModeInstance import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.Traceable import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.Traceable.Traceable import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.TimingConstraint import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.TimingConstraint import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.AgeConstraint import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.AgeConstraint import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionTimeConstraint import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionTimeConstraint import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.LatencyTimingConstraint import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.LatencyTimingConstraint import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.OffsetConstraint import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.OffsetConstraint import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.SynchronizationPointConstraint import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.SynchronizationPointConstraint import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.SynchronizationTiming import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.SynchronizationTiming import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.TimingConstraint import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import",

    # SWComponentTemplate
    "from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import":
    "from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import",

    "from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import":
    "from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import",

    "from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import":
    "from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import",

    "from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import":
    "from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import",

    # MSR DataDictionary
    "from armodel.models.M2.MSR.DataDictionary.DataDefProperties import":
    "from armodel.v2.models.M2.MSR.DataDictionary.DataDefProperties import",

    "from armodel.models.M2.MSR.DataDictionary":
    "from armodel.v2.models.M2.MSR.DataDictionary",

    # Remaining CommonStructure mappings
    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.McSupportData import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.McSupportData import",

    # RptSupport subdirectory files
    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptAccessEnum import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.RptAccessEnum import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptEnablerImplTypeEnum import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.RptEnablerImplTypeEnum import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptExecutionControlEnum import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.RptExecutionControlEnum import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptPreparationEnum import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.RptPreparationEnum import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.AtpBlueprint import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.AtpBlueprint import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.HeapUsage import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.HeapUsage import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.MemorySectionUsage import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.MemorySectionUsage import",

    "from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.HardwareConfiguration import":
    "from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.HardwareConfiguration import",

    # SWComponentTemplate - InternalBehavior
    "from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import":
    "from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import",
}


def refactor_file(file_path: Path, dry_run: bool = False) -> dict:
    """Refactor a single Python file."""
    changes = {
        "v1_imports_fixed": 0,
        "wildcard_removed": 0,
        "all_added": False
    }

    with open(file_path, 'r') as f:
        content = f.read()

    original_content = content

    # Fix V1 imports
    for v1_import, v2_import in IMPORT_MAPPINGS.items():
        if v1_import in content:
            content = content.replace(v1_import, v2_import)
            count = original_content.count(v1_import)
            changes["v1_imports_fixed"] += count

    # Remove wildcard imports in __init__.py files
    if file_path.name == "__init__.py":
        if "from . import *" in content:
            content = content.replace("from . import *", "")
            changes["wildcard_removed"] = 1

        # Check if __all__ exists
        if "__all__" not in content:
            # Try to extract classes to export
            classes = re.findall(r'^class (\w+)\(', content, re.MULTILINE)
            if classes and not dry_run:
                # Add __all__ after docstring
                all_str = "\n__all__ = [\n"
                for cls in sorted(classes):
                    all_str += f"    '{cls}',\n"
                all_str += "]\n"

                # Find end of docstring
                doc_end = content.find('"""')
                if doc_end != -1:
                    doc_end = content.find('"""', doc_end + 3) + 3
                    # Find next newline
                    next_newline = content.find('\n', doc_end)
                    if next_newline != -1:
                        content = content[:next_newline+1] + all_str + "\n" + content[next_newline+1:]
                        changes["all_added"] = True

    # Only write if changed
    if content != original_content and not dry_run:
        with open(file_path, 'w') as f:
            f.write(content)

    return changes


def main():
    """Main entry point."""
    base_path = Path("/Users/ray/Workspace/py-armodel/src/armodel/models_v2/M2/AUTOSARTemplates/CommonStructure")

    if not base_path.exists():
        print(f"Error: Path {base_path} does not exist")
        return 1

    print("Refactoring CommonStructure V2 module...")
    print(f"Base path: {base_path}")
    print()

    total_files = 0
    total_v1_imports = 0
    total_wildcards_removed = 0
    total_all_added = 0

    # Find all Python files
    for py_file in base_path.rglob("*.py"):
        changes = refactor_file(py_file, dry_run=False)

        if changes["v1_imports_fixed"] > 0 or changes["wildcard_removed"] > 0 or changes["all_added"]:
            total_files += 1
            total_v1_imports += changes["v1_imports_fixed"]
            total_wildcards_removed += changes["wildcard_removed"]
            if changes["all_added"]:
                total_all_added += 1

            rel_path = py_file.relative_to(base_path)
            print(f"✓ {rel_path}")
            if changes["v1_imports_fixed"] > 0:
                print(f"  - Fixed {changes['v1_imports_fixed']} V1 imports")
            if changes["wildcard_removed"] > 0:
                print(f"  - Removed wildcard import")
            if changes["all_added"]:
                print(f"  - Added __all__ export list")

    print()
    print(f"Summary:")
    print(f"  Files modified: {total_files}")
    print(f"  V1 imports fixed: {total_v1_imports}")
    print(f"  Wildcard imports removed: {total_wildcards_removed}")
    print(f"  __all__ lists added: {total_all_added}")

    return 0


if __name__ == "__main__":
    exit(main())
