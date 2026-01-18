# Requirement Management

Manage AUTOSAR project requirements with traceability to code, tests, and documentation.

## Actions

When the user runs `/req`, help manage requirements based on `$ARGUMENTS`:

### Add New Requirement
- Add requirement to `docs/requirements/requirements.md`
- Assign stable ID: `SWR_<MODULE>_<NUMBER>` (next available number)
- Include required sections:
  - Title
  - Maturity (draft/accept/invalid)
  - Description
- Link to related code and tests

### Update Requirement Maturity
- Change maturity level (draft → accept → invalid)
- Document why the change was made
- Never change the requirement ID

### Traceability Check
- Search code for requirement ID references in docstrings
- Verify tests reference requirements they validate
- Check CLAUDE.md for requirement listings
- Report any orphaned requirements or missing traceability

### Requirement Formats

**Requirements**: `SWR_<MODULE>_<NUMBER>`
- Example: `SWR_MODEL_00001`, `SWR_PARSER_00003`

**Tests**: `SWUT_<MODULE>_<NUMBER>`
- Example: `SWUT_MODEL_00001`, `SWUT_PARSER_00002`

**Coding Rules**: `CODING_RULE_<CATEGORY>_<NUMBER>`
- Example: `CODING_RULE_IMPORT_00001`, `CODING_RULE_STYLE_00003`

**Maturity Levels**:
- **draft**: Newly created, under review, or not yet implemented
- **accept**: Accepted, implemented, and validated
- **invalid**: Deprecated, superseded, or no longer applicable

## Critical Rules

**STABLE IDs ARE PERMANENT**
- Once assigned, requirement IDs must NEVER be changed
- Even if the requirement is removed or superseded
- Use the next available number for new requirements
- Never reuse a deleted ID

## Usage Examples

```
/req add SWR_WRITER_00007 "Add support for custom markdown templates"
/req update SWR_WRITER_00006 maturity accept
/req check traceability
/req list draft
/req search parser
```

## Requirements by Module

- **Model**: SWR_MODEL_00001 - SWR_MODEL_00013
- **Parser**: SWR_PARSER_00001 - SWR_PARSER_00007
- **Writer**: SWR_WRITER_00001 - SWR_WRITER_00006
- **CLI**: SWR_CLI_00001 - SWR_CLI_00011
- **Package**: SWR_PACKAGE_00001 - SWR_PACKAGE_00003

## References

- Requirements document: `docs/requirement/requirements.md`
- Coding standards: `docs/development/coding_rules.md`
- Project instructions: `CLAUDE.md`
