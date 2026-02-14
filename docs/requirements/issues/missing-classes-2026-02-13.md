
## Missing Classes in BswImplementation.py

- Line 106: List["EcucModule"]
- Line 114: List["EcucModule"]

## Missing Classes in BswInterfaces.py

- Line 326: Optional["SwServiceImplPolicy"]
- Line 334: Optional["SwServiceImplPolicy"]
- Line 826: Optional["SwServiceImplPolicy"]

## Missing Classes in GlobalConstraints.py

- Line 1254: Optional["MultiLanguageOverview"]
- Line 1257: Optional["MultiLanguageOverview"]
- Line 1262: Optional["MultiLanguageOverview"]
- Line 1398: "MultiLanguageOverview"
- Line 1410: "MultiLanguageOverview"
- Line 1540: Optional["MultiLanguageOverview"]
- Line 1368: Optional["ScaleConstrValidity"]
- Line 1371: Optional["ScaleConstrValidity"]
- Line 1376: Optional["ScaleConstrValidity"]
- Line 1510: "ScaleConstrValidity"
- Line 1522: "ScaleConstrValidity"
- Line 1604: Optional["ScaleConstrValidity"]

## Missing Classes in SpecialData.py

- Line 670: Optional["MultiLanguageOverviewParagraph"]
- Line 673: Optional["MultiLanguageOverviewParagraph"]
- Line 678: Optional["MultiLanguageOverviewParagraph"]
- Line 700: "MultiLanguageOverviewParagraph"
- Line 712: "MultiLanguageOverviewParagraph"
- Line 730: Optional["MultiLanguageOverviewParagraph"]

## Missing Classes in ComputationMethod.py

- Line 746: Optional["MultiLanguageOverviewParagraph"]
- Line 749: Optional["MultiLanguageOverviewParagraph"]
- Line 754: Optional["MultiLanguageOverviewParagraph"]
- Line 1007: "MultiLanguageOverviewParagraph"
- Line 1019: "MultiLanguageOverviewParagraph"
- Line 1225: Optional["MultiLanguageOverviewParagraph"]
- Line 1406: "CompuNominatorDenominator"

## Missing Classes from String Annotation Fix (2026-02-14)

### DiagnosticExtract Classes
- Diagnostic (DiagnosticTestResult.py) - Used in DiagnosticTestResult.monitored property
- TimeBaseResource (IntrusionDetectionSystem.py) - Used in IdsPlatformInstantiation.timeBase property

### ECUCDescriptionTemplate Classes
- EcucConfiguration (ECUCDescriptionTemplate.py) - Used in EcucModuleConfigurationValues.implementation property. Context suggests this should be EcucConfigurationVariantEnum based on comments about "VariantPreCompile, VariantLink".

### MSR Documentation Classes
- TraceableTable (Chapters.py)
- OrientEnum (OasisExchangeTable.py)
- DateTime (RequirementsTracing.py)
- NameTokens (PaginationAndView.py)
- PgwideEnum (Figure.py)
- MultiLanguageOverview (ListElements.py)
- MultiLanguageOverviewParagraph (Note.py)
- MultiLanguageOverviewParagraph (GerneralParameters.py)
- ScaleConstrValidity (GlobalConstraints.py)
- CompuNominatorDenominator (ComputationMethod.py)

### MSR AsamHdo Classes
- ScaleConstrValidity (BaseTypes.py)
- MultiLanguageOverview (GlobalConstraints.py)
- MultiLanguageOverviewParagraph (AuxillaryObjects.py)
- ScaleConstrValidity (RecordLayout.py)

### AUTOSAR SystemTemplate Classes
- EcucModule (ECUResourceMapping.py)
- SwServiceImplPolicy (RteEventToOsTaskMapping.py)
- Various classes in SWmapping.py, PncMapping.py, DoIP.py, Dlt.py
- Multiple classes in InstanceRefs.py, TransportProtocols, Fibex modules
- Multiple classes in Transformer, SoftwareCluster modules
