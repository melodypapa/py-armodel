# Missing Classes Documentation

## Summary (Updated 2026-02-14)
- **Total unique undefined classes**: 428
- **Classes fixed in this session**: 12
- **New missing classes found**: 1 (TraceableTable)
- **Top missing classes by frequency**:
  - TimeValue (679 references) - EXISTS in V2, needs import
  - MultidimensionalTime (219 references)
  - SwComponent (131 references)
  - DiagnosticEvent (108 references)
  - SwDataDefProps (98 references)
  - DocumentationBlock (98 references)

## Classes Fixed in This Session

### CryptoKeySlotContent
- **Required in**: `src/armodel/v2/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/CryptoDeployment.py`
- **Context**: Used in `CryptoKeySlot` class for `keySlotContent` property
- **Type**: Class (Identifiable)
- **Date**: 2026-02-14
- **Usage**: Represents restriction of allowed usage of a key stored to the slot
- **Status**: ✅ Created in CryptoDeployment.py
- **Source**: Migrated from V1 `src/armodel/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/CryptoDeployment/CryptoKeySlotContent.py`

### ModeDeclaration
- **Required in**: `src/armodel/v2/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall.py`
- **Context**: Used in `StateDependentFirewall` class for `firewallState` property
- **Type**: Class (AtpStructureElement)
- **Date**: 2026-02-14
- **Usage**: Represents a mode declaration in AUTOSAR models
- **Status**: ✅ Added import to Firewall.py
- **Source**: Exists in V2 `src/armodel/v2/models/M2/AUTOSARTemplates/CommonStructure/ModeDeclaration.py`

### FirewallActionEnum
- **Required in**: `src/armodel/v2/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall.py`
- **Context**: Used in `StateDependentFirewall` and `FirewallRuleProps` classes
- **Type**: Enumeration (ARObject)
- **Date**: 2026-02-14
- **Usage**: Enumeration for firewall actions
- **Status**: ✅ Created in Firewall.py
- **Note**: Class doesn't exist in V1, created as placeholder

### DataLinkLayerRule
- **Required in**: `src/armodel/v2/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall.py`
- **Context**: Used in `FirewallRule` class for `dataLinkLayer` property
- **Type**: Class (ARObject)
- **Date**: 2026-02-14
- **Usage**: Configuration of rules on the Data Link Layer
- **Status**: ✅ Created in Firewall.py
- **Note**: Class doesn't exist in V1, created as placeholder

### NetworkLayerRule
- **Required in**: `src/armodel/v2/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall.py`
- **Context**: Used in `FirewallRule` class for `networkLayer` property
- **Type**: Class (ARObject)
- **Date**: 2026-02-14
- **Usage**: Configuration of rules on the Network Layer
- **Status**: ✅ Created in Firewall.py
- **Note**: Class doesn't exist in V1, created as placeholder

### TransportLayerRule
- **Required in**: `src/armodel/v2/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall.py`
- **Context**: Used in `FirewallRule` class for `transportLayer` property
- **Type**: Class (ARObject)
- **Date**: 2026-02-14
- **Usage**: Configuration of rules on the Transport Layer
- **Status**: ✅ Created in Firewall.py
- **Note**: Class doesn't exist in V1, created as placeholder

### DdsRule
- **Required in**: `src/armodel/v2/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall.py`
- **Context**: Used in `FirewallRule` class for `ddsRule` property
- **Type**: Class (ARObject)
- **Date**: 2026-02-14
- **Usage**: Configuration of firewall rules for DDS
- **Status**: ✅ Created in Firewall.py
- **Note**: Class doesn't exist in V1, created as placeholder

### DoIpRule
- **Required in**: `src/armodel/v2/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall.py`
- **Context**: Used in `FirewallRule` class for `doIpRule` property
- **Type**: Class (ARObject)
- **Date**: 2026-02-14
- **Usage**: Configuration of firewall rules for DoIP messages
- **Status**: ✅ Created in Firewall.py
- **Note**: Class doesn't exist in V1, created as placeholder

### SomeipProtocolRule
- **Required in**: `src/armodel/v2/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall.py`
- **Context**: Used in `FirewallRule` class for `someipRule` property
- **Type**: Class (ARObject)
- **Date**: 2026-02-14
- **Usage**: Configuration of firewall rules for SOME/IP messages
- **Status**: ✅ Created in Firewall.py
- **Note**: Class doesn't exist in V1, created as placeholder

### SomeipSdRule
- **Required in**: `src/armodel/v2/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall.py`
- **Context**: Used in `FirewallRule` class for `someipSdRule` property
- **Type**: Class (ARObject)
- **Date**: 2026-02-14
- **Usage**: Configuration of firewall rules for SOME/IP Service Discovery
- **Status**: ✅ Created in Firewall.py
- **Note**: Class doesn't exist in V1, created as placeholder

### PayloadBytePattern
- **Required in**: `src/armodel/v2/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall.py`
- **Context**: Used in `FirewallRule` class for `payloadByte` property
- **Type**: Class (ARObject)
- **Date**: 2026-02-14
- **Usage**: Configuration of generic firewall rules
- **Status**: ✅ Created in Firewall.py
- **Note**: Class doesn't exist in V1, created as placeholder

### PlatformModule
- **Required in**: `src/armodel/v2/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/IntrusionDetectionSystem.py`
- **Context**: Used in `IdsPlatformInstantiation` class for `network` property
- **Type**: Class (Identifiable)
- **Date**: 2026-02-14
- **Usage**: Platform module configuration
- **Status**: ✅ Created in IntrusionDetectionSystem.py
- **Note**: Class doesn't exist in V1, created as placeholder

### TimeBaseResource
- **Required in**: `src/armodel/v2/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/IntrusionDetectionSystem.py`
- **Context**: Used in `IdsPlatformInstantiation` class for `timeBase` property
- **Type**: Class (Identifiable)
- **Date**: 2026-02-14
- **Usage**: Time base resource configuration
- **Status**: ✅ Created in IntrusionDetectionSystem.py
- **Note**: Class doesn't exist in V1, created as placeholder

## Remaining Missing Classes from Previous Session

### OrientEnum
- **Required in**: `src/armodel/v2/models/M2/MSR/Documentation/BlockElements/OasisExchangeTable.py`
- **Context**: Used in `Table` class for `orient` property (line 156, 159, 164, 430, 442, 636)
- **Type**: Enumeration (AREnum)
- **Date**: 2026-02-14
- **Usage**: Represents table orientation (landscape/portrait)
- **Status**: ✅ Created in OasisExchangeTable.py

### HwAttributeValue
- **Required in**: `src/armodel/v2/models/M2/AUTOSARTemplates/EcuResourceTemplate/__init__.py`
- **Context**: Used in `HwDescriptionEntity` class for `hw_attributes` property
- **Type**: Class
- **Date**: 2026-02-14
- **Usage**: Represents hardware attribute values
- **Status**: Not found in V2 codebase, needs to be created

### HwCategory
- **Required in**: `src/armodel/v2/models/M2/AUTOSARTemplates/EcuResourceTemplate/__init__.py`
- **Context**: Used in `HwDescriptionEntity` class for `hw_categories` property
- **Type**: Class
- **Date**: 2026-02-14
- **Usage**: Represents hardware categories
- **Status**: Not found in V2 codebase, needs to be created

### HwType
- **Required in**: `src/armodel/v2/models/M2/AUTOSARTemplates/EcuResourceTemplate/__init__.py`
- **Context**: Used in `HwDescriptionEntity` class for `hw_type` property
- **Type**: Class
- **Date**: 2026-02-14
- **Usage**: Represents hardware types
- **Status**: Not found in V2 codebase, needs to be created

## Missing Classes Found During V2 Model Refactor (2026-02-14)

### TraceableTable
- **Required in**: `src/armodel/v2/models/M2/MSR/Documentation/Chapters.py`
- **Context**: Used in `TopicContentOrMsrQuery` class for `traceableTable` property (line 1409, 1413, 1419, 1439, 1469)
- **Type**: Class (likely ARObject)
- **Date**: 2026-02-14
- **Usage**: Represents a traceable table in documentation
- **Status**: ❌ Not found in V2 codebase, needs to be created
- **Note**: Class doesn't exist in V1 either, may be placeholder or needs creation from AUTOSAR spec

## High-Priority Missing Classes (Need Imports)

### TimeValue
- **Frequency**: 679 references
- **Status**: EXISTS in V2 `src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py`
- **Action Required**: Add import to all files that use it
- **Example Files**:
  - `src/armodel/v2/models/M2/AUTOSARTemplates/CommonStructure/InternalBehavior.py`
  - `src/armodel/v2/models/M2/AUTOSARTemplates/SystemTemplate/RteEventToOsTaskMapping.py`
  - Multiple files in Fibex package

### MultidimensionalTime
- **Frequency**: 219 references
- **Status**: EXISTS in V2 `src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/MultidimensionalTime.py`
- **Action Required**: Add import to all files that use it