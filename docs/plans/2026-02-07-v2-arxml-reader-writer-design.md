# V2 ARXML Reader/Writer Design

**Date:** 2026-02-07
**Status:** Design Approved
**Author:** Design Team

## Executive Summary

This document outlines the design for V2 ARXML reader and writer for py-armodel. The V2 implementation uses a Java-style interface design where model classes are simple data holders (POJOs) and external Reader/Writer classes handle all serialization logic using reflection.

## Key Design Decisions

| Aspect | Decision | Rationale |
|--------|----------|-----------|
| **Architecture** | Model-integrated with external serialization | Java-style POJO pattern, cleaner separation of concerns |
| **Model Classes** | No serialization methods in models | Models are pure data holders |
| **Serialization** | External Reader/Writer using reflection | Like JAXB/Jackson, easier to maintain |
| **XML Library** | ElementTree (cElementTree) | Faster, lightweight, compatible |
| **Schema Mappings** | XSD-based generation | Single source of truth, no manual maintenance |
| **Error Handling** | V1-compatible (exceptions by default, warning mode optional) | Maintain backward compatibility |
| **Scope** | Full V1 parity from day one | Support all AUTOSAR 3.2.3 - R24-11 |
| **Version Handling** | Schema-driven with automatic version detection | Declarative mappings per version |

## Architecture Overview

```
src/armodel/v2/
├── models/                    # V2 models (pure data, no serialization)
│   └── M2/AUTOSARTemplates/...
├── reader/                    # V2 reader infrastructure
│   ├── base_reader.py         # Core reading orchestration
│   ├── element_handler.py     # Element handler registry
│   ├── xsd_generator.py       # XSD mapping generator
│   └── schema_registry.py     # Schema mappings loader
├── writer/                    # V2 writer infrastructure
│   ├── base_writer.py         # Core writing orchestration
│   └── element_formatter.py   # XML formatting utilities
├── utils/                     # Shared utilities
│   ├── errors.py              # Custom error types
│   └── context.py             # Reading/writing context
└── schema_data/               # Generated schema mappings
    ├── AUTOSAR_3.2.3_mappings.json
    ├── AUTOSAR_4.0.3_mappings.json
    ├── AUTOSAR_R23-11_mappings.json
    └── AUTOSAR_R24-11_mappings.json
```

## Model Integration

**Models are Pure Data Holders (Java POJO Pattern)**

```python
class SwComponentType(ARObject):
    """
    Software component type - pure data model.
    NO serialization methods.
    """
    def _validate_abstract(self) -> None:
        pass

    def __init__(self) -> None:
        super().__init__()
        self.short_name: Optional[str] = None
        self.category: Optional[str] = None
        # ... just data fields
```

**External Reader/Writer Handle Serialization**

The Reader and Writer use reflection to inspect model structure and serialize/deserialize.

## Reader Design

**Core Reader Infrastructure:**

```python
class ARXMLReader:
    """Reads ARXML and creates model instances."""

    def __init__(self, options: Optional[Dict] = None):
        self.warning = options.get("warning", False) if options else False

    def load(self, file_path: str, document: AUTOSAR) -> None:
        """Load ARXML file into AUTOSAR document."""
        # Parse XML with ElementTree
        # Detect AUTOSAR version
        # Create DeserializationContext
        # Delegate to model classes via reflection

    def _deserialize_element(self, elem: ET.Element, parent: Any, ctx: Context) -> Any:
        """Deserialize XML element using reflection."""
        # Get model class from ElementHandler registry
        # Create instance
        # Set attributes from XML
        # Deserialize child elements
```

## Writer Design

**Core Writer Infrastructure:**

```python
class ARXMLWriter:
    """Writes model instances to ARXML."""

    def __init__(self, options: Optional[Dict] = None):
        self.format = options.get("format", True) if options else True

    def save(self, file_path: str, document: AUTOSAR) -> None:
        """Save AUTOSAR document to ARXML file."""
        # Get version from document
        # Create SerializationContext
        # Serialize using reflection
        # Pretty print and write

    def _serialize_object(self, obj: Any, ctx: Context) -> ET.Element:
        """Serialize object to XML using reflection."""
        # Get XML tag name from schema mappings
        # Create element
        # Set attributes
        # Serialize children
```

## XSD-Based Schema Generation

**Automatic Mapping Generation from AUTOSAR XSD Files**

The XSD files contain `mmt.qualifiedName` attributes that provide exact mappings:

```xml
<xsd:complexType name="APPLICATION-SOFTWARE-COMPONENT-TYPE">
  <xsd:appinfo source="tags">
    mmt.qualifiedName="ApplicationSoftwareComponentType"
  </xsd:appinfo>
  <xsd:element name="SHORT-NAME">
    <xsd:appinfo source="tags">
      mmt.qualifiedName="Identifiable.shortName"
    </xsd:appinfo>
  </xsd:element>
</xsd:complexType>
```

**Generator extracts:**
- XML element names → Python class names
- XML child elements → Python field names
- XML attributes → Python attributes
- minOccurs/maxOccurs for validation

**Usage:**

```bash
python scripts/generate_schema_mappings.py \
  --xsd docs/xsd/AUTOSAR_STRICT_COMPACT.xsd \
  --version 3.2.3 \
  --output src/armodel/v2/schema_data/AUTOSAR_3.2.3_mappings.json
```

## Error Handling Strategy

**V1-Compatible Two-Mode Design:**

1. **Default (strict mode):** Raise exceptions immediately
2. **Warning mode:** Log errors, continue processing

```python
# Strict mode (default)
reader = ARXMLReader()
reader.load("invalid.arxml", document)  # Raises ReadError

# Warning mode
reader = ARXMLReader(options={"warning": True})
reader.load("invalid.arxml", document)  # Logs warnings, doesn't raise
```

## Usage Examples

**Reading ARXML:**

```python
from armodel.v2.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.v2.reader.base_reader import ARXMLReader

AUTOSAR.setARRelease('R23-11')
document = AUTOSAR.getInstance()

reader = ARXMLReader(options={"warning": False})
reader.load("input.arxml", document)

# Access models
components = document.findSwComponentTypes()
```

**Writing ARXML:**

```python
from armodel.v2.writer.base_writer import ARXMLWriter

writer = ARXMLWriter(options={"format": True})
writer.save("output.arxml", document)
```

## Testing Strategy

**Unit + Integration Testing:**

- **Unit Tests:** Test each model's serialization, reader/writer core
- **Integration Tests:** Round-trip validation (parse → write → parse → compare)
- **Schema Tests:** Validate XSD generation and mappings
- **Version Tests:** Test across all supported AUTOSAR versions

**Test Structure:**

```
tests/test_armodel/
├── reader_v2/              # Reader unit tests
├── writer_v2/              # Writer unit tests
├── models_v2/              # Model serialization tests
└── integration_v2/         # Round-trip integration tests
```

## Implementation Phases

### Phase 1: Core Infrastructure (Foundation)
- [ ] Create `src/armodel/v2/reader/` and `src/armodel/v2/writer/` directories
- [ ] Implement error classes (`ReadError`, `WriteError`)
- [ ] Implement context classes (`DeserializationContext`, `SerializationContext`)
- [ ] Create element handler registry
- [ ] Implement base reader skeleton
- [ ] Implement base writer skeleton

### Phase 2: XSD Schema Generation
- [ ] Implement XSD parser
- [ ] Extract element/attribute mappings from XSD
- [ ] Generate schema mappings for AUTOSAR 3.2.3
- [ ] Generate schema mappings for AUTOSAR 4.0.3
- [ ] Generate schema mappings for AUTOSAR R23-11
- [ ] Generate schema mappings for AUTOSAR R24-11
- [ ] Create schema registry to load mappings

### Phase 3: Reader Implementation
- [ ] Implement XML parsing with ElementTree
- [ ] Implement AUTOSAR version detection
- [ ] Implement element deserialization using reflection
- [ ] Handle attributes and child elements
- [ ] Support warning mode
- [ ] Add proper error messages with context

### Phase 4: Writer Implementation
- [ ] Implement object serialization using reflection
- [ ] Add XML formatting and pretty print
- [ ] Handle namespaces and schema declarations
- [ ] Add proper error handling

### Phase 5: Model Integration
- [ ] Add serialization methods to core models (ARObject, Identifiable, etc.)
- [ ] Add serialization to CommonStructure models
- [ ] Add serialization to SWComponentTemplate models
- [ ] Add serialization to all other M2 models
- [ ] Validate full V1 parity

### Phase 6: Testing
- [ ] Write unit tests for reader
- [ ] Write unit tests for writer
- [ ] Write model serialization tests
- [ ] Write round-trip integration tests
- [ ] Test across all AUTOSAR versions
- [ ] Achieve >80% code coverage

### Phase 7: Documentation and CLI
- [ ] Update V2 migration guide
- [ ] Add reader/writer usage examples
- [ ] Update CLI tools if needed
- [ ] Create release notes

## Benefits of V2 Design

✅ **Clean Architecture:** Java-style POJO pattern with external serialization
✅ **Maintainable:** No 400K-line monolithic files
✅ **Type-Safe:** Uses Python type hints throughout
✅ **XSD-Driven:** Automatic schema mapping generation
✅ **Version-Aware:** Supports all AUTOSAR versions declaratively
✅ **Testable:** Easy unit testing with clear separation
✅ **V1-Compatible:** Same error handling behavior
✅ **Performance:** ElementTree is faster than lxml for reading

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Reflection overhead | Profile and optimize hot paths |
| XSD schema changes | Automate regeneration in CI/CD |
| Missing mappings in V2 | Implement gracefully with clear errors |
| Performance vs V1 | Benchmark and optimize as needed |

## References

- V1 Implementation: `src/armodel/parser/arxml_parser.py`, `src/armodel/writer/arxml_writer.py`
- V2 Models: `src/armodel/v2/models/`
- AUTOSAR XSD: `docs/xsd/AUTOSAR_STRICT_COMPACT.xsd`
- V2 Coding Rules: `docs/development/coding_rules_v2.md`

## Appendix: Key Code Examples

See full examples in the main design sections above.
