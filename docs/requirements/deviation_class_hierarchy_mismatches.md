# Class Hierarchy Mismatches

This report shows classes that have incorrect parent or abstract status
compared to the documented AUTOSAR M2 class hierarchy.

## Total Mismatches: 15

| Status | Class | Hierarchy | Notes |
|--------|-------|-----------|-------|
| ⚠ MISMATCH | AUTOSARTemplates.AutosarTopLevelStructure.AUTOSAR | **Documented:**<br>Parent: ARObject<br>Type: Concrete<br><br>**Actual:**<br>Parent: AbstractAUTOSAR<br>Type: Concrete | parent mismatch (expected ARObject, got AbstractAUTOSAR) |
| ⚠ MISMATCH | AUTOSARTemplates.GenericStructure.RolesAndRights.AtpDefinition.AtpDefinition | **Documented:**<br>Parent: Referrable<br>Type: Abstract<br><br>**Actual:**<br>Parent: Identifiable<br>Type: Abstract | parent mismatch (expected Referrable, got Identifiable) |
| ⚠ MISMATCH | AUTOSARTemplates.GenericStructure.AbstractStructure.AtpPrototype | **Documented:**<br>Parent: AtpFeature<br>Type: Abstract<br><br>**Actual:**<br>Parent: AtpBlueprintable<br>Type: Abstract | parent mismatch (expected AtpFeature, got AtpBlueprintable) |
| ⚠ MISMATCH | AUTOSARTemplates.GenericStructure.AbstractStructure.AtpStructureElement | **Documented:**<br>Parent: AtpFeature<br>Type: Abstract<br><br>**Actual:**<br>Parent: AtpBlueprintable<br>Type: Abstract | parent mismatch (expected AtpFeature, got AtpBlueprintable) |
| ⚠ MISMATCH | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.CollectableElement | **Documented:**<br>Parent: Identifiable<br>Type: Abstract<br><br>**Actual:**<br>Parent: ARObject<br>Type: Abstract | parent mismatch (expected Identifiable, got ARObject) |
| ⚠ MISMATCH | AUTOSARTemplates.ECUCParameterDefTemplate.EcucConditionFormula | **Documented:**<br>Parent: FormulaExpression<br>Type: Concrete<br><br>**Actual:**<br>Parent: ARObject<br>Type: Concrete | parent mismatch (expected FormulaExpression, got ARObject) |
| ⚠ MISMATCH | AUTOSARTemplates.ECUCParameterDefTemplate.EcucParameterDerivationFormula | **Documented:**<br>Parent: FormulaExpression<br>Type: Concrete<br><br>**Actual:**<br>Parent: ARObject<br>Type: Concrete | parent mismatch (expected FormulaExpression, got ARObject) |
| ⚠ MISMATCH | MSR.Documentation.TextModel.LanguageDataModel.LLongName | **Documented:**<br>Parent: MixedContentForLongName<br>Type: Concrete<br><br>**Actual:**<br>Parent: LanguageSpecific<br>Type: Concrete | parent mismatch (expected MixedContentForLongName, got LanguageSpecific) |
| ⚠ MISMATCH | MSR.Documentation.TextModel.LanguageDataModel.LOverviewParagraph | **Documented:**<br>Parent: MixedContentForOverviewParagraph<br>Type: Concrete<br><br>**Actual:**<br>Parent: LanguageSpecific<br>Type: Concrete | parent mismatch (expected MixedContentForOverviewParagraph, got LanguageSpecific) |
| ⚠ MISMATCH | MSR.Documentation.TextModel.LanguageDataModel.LParagraph | **Documented:**<br>Parent: MixedContentForParagraph<br>Type: Concrete<br><br>**Actual:**<br>Parent: LanguageSpecific<br>Type: Concrete | parent mismatch (expected MixedContentForParagraph, got LanguageSpecific) |
| ⚠ MISMATCH | MSR.Documentation.TextModel.LanguageDataModel.LPlainText | **Documented:**<br>Parent: MixedContentForPlainText<br>Type: Concrete<br><br>**Actual:**<br>Parent: LanguageSpecific<br>Type: Concrete | parent mismatch (expected MixedContentForPlainText, got LanguageSpecific) |
| ⚠ MISMATCH | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.PackageableElement | **Documented:**<br>Parent: CollectableElement<br>Type: Abstract<br><br>**Actual:**<br>Parent: Identifiable<br>Type: Abstract | parent mismatch (expected CollectableElement, got Identifiable) |
| ⚠ MISMATCH | AUTOSARTemplates.CommonStructure.ServiceNeeds.ServiceDependency | **Documented:**<br>Parent: ARObject<br>Type: Abstract<br><br>**Actual:**<br>Parent: Identifiable<br>Type: Abstract | parent mismatch (expected ARObject, got Identifiable) |
| ⚠ MISMATCH | MSR.AsamHdo.Units.SingleLanguageUnitNames | **Documented:**<br>Parent: MixedContentForUnitNames<br>Type: Concrete<br><br>**Actual:**<br>Parent: ARLiteral<br>Type: Concrete | parent mismatch (expected MixedContentForUnitNames, got ARLiteral) |
| ⚠ MISMATCH | AUTOSARTemplates.CommonStructure.Timing.Traceable.Traceable | **Documented:**<br>Parent: MultilanguageReferrable<br>Type: Abstract<br><br>**Actual:**<br>Parent: Identifiable<br>Type: Abstract | parent mismatch (expected MultilanguageReferrable, got Identifiable) |

## Legend

- ⚠ MISMATCH: Class has wrong parent or abstract status

## Related Reports

- [Summary](deviation_class_hierarchy_summary.md) - Overall summary and statistics
- [Extra Classes](deviation_class_hierarchy_extra_classes.md) - Classes that exist but are not documented
