#!/usr/bin/env python3
"""
Code Generator Module for py-armodel

This module handles generation of Python class code from AUTOSAR requirements.
"""

from pathlib import Path
from typing import Dict, List, Any


def _is_container_class(class_name: str, parent: str, attributes: Dict[str, Any]) -> bool:
    """Check if a class should have container management methods.

    Returns True for classes that:
    - Inherit from CollectableElement, ElementCollection, or ARPackage
    - Have attributes ending with 's' (suggesting collections)

    Args:
        class_name: Name of the class
        parent: Parent class name
        attributes: Dictionary of attributes

    Returns:
        True if class is a container, False otherwise
    """
    # Check parent class
    container_parents = {
        'CollectableElement', 'ElementCollection', 'ARPackage',
        'AtpStructureElement', 'Identifiable', 'ARElement'
    }

    if parent in container_parents:
        return True

    # Check if class name suggests it's a container
    container_suffixes = [
        'Set', 'Group', 'Collection', 'Mapping', 'Definitions',
        'Elements', 'Instances', 'Mappings', 'Sequence'
    ]

    for suffix in container_suffixes:
        if class_name.endswith(suffix):
            return True

    # Check for list-type attributes that suggest container behavior
    for attr_name, attr_info in attributes.items():
        if attr_info.get('multiplicity') == '*':
            return True

    return False


def _should_have_addElement_method(class_name: str, parent: str) -> bool:
    """Check if a class should have addElement-style factory methods.

    Args:
        class_name: Name of the class
        parent: Parent class name

    Returns:
        True if class should have addElement methods, False otherwise
    """
    factory_parents = {
        'ARPackage', 'AtpStructureElement', 'Identifiable', 'ARElement',
        'InternalBehavior', 'SwcInternalBehavior', 'BswInternalBehavior',
    }
    return parent in factory_parents


def _should_have_create_methods(class_name: str, parent: str) -> bool:
    """Check if a class should have createXxxx methods (i.e., inherits from Identifiable).

    Create methods are only for classes that:
    - Inherit from Identifiable (which has elements collection and addElement method)
    - Are container classes that own child objects

    Args:
        class_name: Name of the class
        parent: Parent class name

    Returns:
        True if class should have create methods, False otherwise
    """
    create_method_parents = {
        'Identifiable', 'ARPackage', 'ARElement', 'InternalBehavior',
        'SwcInternalBehavior', 'BswInternalBehavior', 'Implementation',
        'AUTOSAR', 'AtpStructureElement', 'CollectableElement',
    }
    return parent in create_method_parents


def _wrap_docstring_line(line: str, indent: str = '    ', max_width: int = 80) -> List[str]:
    """Wrap a docstring line to stay under max_width characters.

    Args:
        line: The line to wrap
        indent: The indentation to use for wrapped lines
        max_width: Maximum line width (default 80)

    Returns:
        List of wrapped lines
    """
    if len(line) <= max_width:
        return [line]

    lines = []
    words = line.split()
    current_line = indent

    for word in words:
        if len(current_line) + 1 + len(word) <= max_width:
            if current_line == indent:
                current_line += word
            else:
                current_line += ' ' + word
        else:
            if current_line != indent:
                lines.append(current_line)
            current_line = indent + word

    if current_line != indent:
        lines.append(current_line)

    return lines


def _format_attr_comment(note: str) -> str:
    """Format attribute note as multi-line comment based on periods.

    Args:
        note: Attribute note string

    Returns:
        Formatted multi-line comment string
    """
    # Split by '. ' and create multi-line comment
    sentences = [s.strip() for s in note.split('.') if s.strip()]
    # Add period back to each sentence if it doesn't end with one
    sentences = [s if s.endswith('.') else s + '.' for s in sentences]

    if len(sentences) == 1:
        # Wrap the single sentence if it's too long
        wrapped = _wrap_docstring_line(sentences[0], indent='', max_width=77)
        # Add # prefix to each line
        wrapped = ['# ' + line if not line.startswith('#') else line for line in wrapped]
        if len(wrapped) == 1:
            return wrapped[0]
        else:
            # First line is normal, subsequent lines need indent
            return wrapped[0] + '\n        ' + '\n        '.join(wrapped[1:])
    else:
        lines = []
        for sentence in sentences:
            # Wrap each sentence if it's too long
            wrapped = _wrap_docstring_line(sentence, indent='', max_width=77)
            # Add # prefix to each line
            wrapped = ['# ' + line if not line.startswith('#') else line for line in wrapped]
            if len(wrapped) == 1:
                lines.append(wrapped[0])
            else:
                # First line is normal, subsequent lines need indent
                lines.append(wrapped[0])
                lines.extend(['        ' + line for line in wrapped[1:]])
        return '\n        '.join(lines)


def _generate_init_code(
    class_name: str,
    docstring: str,
    is_abstract: bool,
    has_short_name_init: bool,
    is_arobject_child: bool
) -> str:
    """Generate __init__ method code.

    Args:
        class_name: Name of the class
        docstring: Class docstring
        is_abstract: Whether the class is abstract
        has_short_name_init: Whether __init__ should have (parent, short_name) signature
        is_arobject_child: Whether the class directly inherits from ARObject

    Returns:
        __init__ method code
    """
    if is_abstract:
        if has_short_name_init and not is_arobject_child:
            return f'''{docstring}
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is {class_name}:
            raise TypeError("{class_name} is an abstract class.")
        super().__init__(parent, short_name)'''
        elif is_arobject_child:
            return f'''{docstring}
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is {class_name}:
            raise TypeError("{class_name} is an abstract class.")
        super().__init__()
        self.parent = parent
        self.short_name = short_name'''
        else:
            return f'''{docstring}
    def __init__(self):
        if type(self) is {class_name}:
            raise TypeError("{class_name} is an abstract class.")
        super().__init__()'''
    else:
        if has_short_name_init and not is_arobject_child:
            return f'''{docstring}
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)'''
        elif is_arobject_child:
            return f'''{docstring}
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__()
        self.parent = parent
        self.short_name = short_name'''
        else:
            return f'''{docstring}
    def __init__(self):
        super().__init__()'''


def _generate_docstring(class_info: Dict[str, Any]) -> str:
    """Generate class docstring from requirements.

    Args:
        class_info: Class information dictionary from requirements

    Returns:
        Formatted docstring
    """
    note = class_info.get('note', '')
    sources = class_info.get('sources', [])

    docstring_lines = []
    docstring_lines.append('    """')

    if note:
        # Wrap the note line if it's too long
        wrapped_note = _wrap_docstring_line(f'    {note}')
        docstring_lines.extend(wrapped_note)

    if sources:
        docstring_lines.append('    ')
        docstring_lines.append('    Sources:')
        for source in sources:
            source_line = (
                f'      - {source.get("pdf_file", "")} '
                f'(Page {source.get("page_number", "")}, '
                f'{source.get("autosar_standard", "")} {source.get("standard_release", "")})'
            )
            # Wrap the source line if it's too long
            wrapped_source = _wrap_docstring_line(source_line, indent='      ', max_width=80)
            docstring_lines.extend(wrapped_source)

    docstring_lines.append('    """')
    return '\n'.join(docstring_lines)


def _generate_attribute_initialization(
    class_name: str,
    attributes: Dict[str, Any]
) -> List[str]:
    """Generate attribute initialization code.

    Args:
        class_name: Name of the class
        attributes: Dictionary of attributes

    Returns:
        List of code lines for attribute initialization
    """
    attr_code = []

    for attr_name, attr_info in attributes.items():
        attr_type = attr_info.get('type', 'Any')
        multiplicity = attr_info.get('multiplicity', '1')
        is_ref = attr_info.get('is_ref', False)
        attr_note = attr_info.get('note', '')
        original_type = attr_info.get('original_type')

        # Use string annotation (forward reference) for self-referencing types
        is_self_reference = (attr_type == class_name)

        # Map is_ref to RefType for references
        if is_ref and attr_type == 'Any':
            attr_type = 'RefType'
        elif is_ref and multiplicity in ['*', '0..1']:
            pass  # Keep the original type

        # Add comment with original type if it was changed to Any
        if original_type and original_type != 'Any':
            if attr_note:
                attr_note = f"Type: {original_type}. {attr_note}"
            else:
                attr_note = f"Type: {original_type}"

        # Determine Python attribute name (plural for lists)
        py_attr_name = (
            attr_name + 's' if not attr_name.endswith('s') else attr_name
            if multiplicity == '*'
            else attr_name
        )

        if multiplicity == '*':
            if is_ref:
                py_type = 'List[RefType]'
            else:
                py_type = f'List["{class_name}"]' if is_self_reference else f'List[{attr_type}]'

            if attr_note:
                attr_code.append(f'        {_format_attr_comment(attr_note)}')
            attr_code.append(f'        self.{py_attr_name}: {py_type} = []')

        elif multiplicity == '0..1':
            if is_ref:
                py_type = 'RefType'
            else:
                py_type = f'Optional["{class_name}"]' if is_self_reference else f'Optional[{attr_type}]'

            if attr_note:
                attr_code.append(f'        {_format_attr_comment(attr_note)}')
            attr_code.append(f'        self.{py_attr_name}: {py_type} = None')

        else:
            if is_ref:
                py_type = 'RefType'
            else:
                py_type = f'"{class_name}"' if is_self_reference else attr_type

            if attr_note:
                attr_code.append(f'        {_format_attr_comment(attr_note)}')
            attr_code.append(f'        self.{py_attr_name}: {py_type} = None')

    return attr_code


def _generate_getter_method(
    class_name: str,
    attr_name: str,
    py_attr_name: str,
    multiplicity: str,
    is_ref: bool,
    is_self_reference: bool,
    actual_type: str
) -> str:
    """Generate a getter method for an attribute.

    Args:
        class_name: Name of the class
        attr_name: Original attribute name
        py_attr_name: Python attribute name (may be pluralized)
        multiplicity: Attribute multiplicity
        is_ref: Whether this is a reference attribute
        is_self_reference: Whether this is a self-referencing type
        actual_type: The actual type for the attribute

    Returns:
        Getter method code
    """
    if multiplicity == '*':
        if is_ref:
            return_type = 'List[RefType]'
        else:
            return_type = f'List["{class_name}"]' if is_self_reference else f'List[{actual_type}]'
    else:
        if is_ref:
            return_type = 'RefType'
        else:
            return_type = f'"{class_name}"' if is_self_reference else actual_type

    return f'''    def get{py_attr_name[0].upper()}{py_attr_name[1:]}(self) -> {return_type}:
        return self.{py_attr_name}

'''


def _generate_setter_method(
    class_name: str,
    py_attr_name: str,
    multiplicity: str,
    is_ref: bool,
    is_self_reference: bool,
    actual_type: str
) -> str:
    """Generate a setter method for an attribute.

    Args:
        class_name: Name of the class
        py_attr_name: Python attribute name (may be pluralized)
        multiplicity: Attribute multiplicity
        is_ref: Whether this is a reference attribute
        is_self_reference: Whether this is a self-referencing type
        actual_type: The actual type for the attribute

    Returns:
        Setter method code
    """
    if multiplicity == '*':
        if is_ref:
            param_type = 'List[RefType]'
        else:
            param_type = f'List["{class_name}"]' if is_self_reference else f'List[{actual_type}]'
    else:
        if is_ref:
            param_type = 'RefType'
        else:
            param_type = f'"{class_name}"' if is_self_reference else actual_type

    return f'''    def set{py_attr_name[0].upper()}{py_attr_name[1:]}(self, value: {param_type}) -> "{class_name}":
        self.{py_attr_name} = value
        return self

'''


def _generate_add_create_method(
    class_name: str,
    attr_name: str,
    py_attr_name: str,
    attr_kind: str,
    is_ref: bool,
    actual_type: str,
    should_use_create: bool
) -> str:
    """Generate an add or create method for a list attribute.

    Args:
        class_name: Name of the class
        attr_name: Original attribute name
        py_attr_name: Python attribute name (may be pluralized)
        attr_kind: Kind of attribute ('attribute' or 'reference')
        is_ref: Whether this is a reference attribute
        actual_type: The actual type for the attribute
        should_use_create: Whether to use create method (vs add method)

    Returns:
        Add or create method code
    """
    if should_use_create:
        # Generate createXxxx method for owned child objects
        singular_attr_name = attr_name if not attr_name.endswith('s') else attr_name[:-1]
        child_type = actual_type if '[' not in actual_type else actual_type.split('[')[0].strip('"')

        return f'''    def create{singular_attr_name[0].upper()}{singular_attr_name[1:]}(self, short_name: str) -> {child_type}:
        """Creates and adds a {singular_attr_name} to this {class_name}."""
        if (short_name not in self.elements):
            new_element = {child_type}(self, short_name)
            # Only call addElement if child has getShortName method (Referrable subclasses)
            if hasattr(new_element, 'getShortName'):
                self.addElement(new_element)
            self.{py_attr_name}.append(new_element)
        return new_element

'''
    else:
        # Generate addXxxx method for references or existing objects
        singular_attr_name = attr_name if not attr_name.endswith('s') else attr_name[:-1]

        if is_ref:
            value_type = 'RefType'
        else:
            value_type = f'"{class_name}"' if actual_type == f'List["{class_name}"]' else actual_type
            if value_type.startswith('List['):
                value_type = value_type[5:-1]  # Remove List[ and ]

        return f'''    def add{singular_attr_name[0].upper()}{singular_attr_name[1:]}(self, value: {value_type}) -> "{class_name}":
        """Adds a value to the {py_attr_name} list."""
        self.{py_attr_name}.append(value)
        return self

'''


def _generate_methods(
    class_name: str,
    parent: str,
    attributes: Dict[str, Any]
) -> List[str]:
    """Generate getter, setter, and add/create methods for attributes.

    Args:
        class_name: Name of the class
        parent: Parent class name
        attributes: Dictionary of attributes

    Returns:
        List of method code strings
    """
    methods_code = []

    for attr_name, attr_info in attributes.items():
        attr_type = attr_info.get('type', 'Any')
        multiplicity = attr_info.get('multiplicity', '1')
        is_ref = attr_info.get('is_ref', False)

        # Use string annotation (forward reference) for self-referencing types
        is_self_reference = (attr_type == class_name)

        # Determine Python attribute name (plural for lists)
        py_attr_name = (
            attr_name + 's' if not attr_name.endswith('s') else attr_name
            if multiplicity == '*'
            else attr_name
        )

        # Map is_ref to RefType
        if is_ref:
            actual_type = 'RefType'
        else:
            actual_type = attr_type

        # Generate getter
        methods_code.append(_generate_getter_method(
            class_name, attr_name, py_attr_name, multiplicity, is_ref, is_self_reference, actual_type
        ))

        # Generate setter
        methods_code.append(_generate_setter_method(
            class_name, py_attr_name, multiplicity, is_ref, is_self_reference, actual_type
        ))

        # Add add or create method for list attributes based on kind
        if multiplicity == '*':
            attr_kind = attr_info.get('kind', 'attribute')
            should_use_create = (
                attr_kind == 'attribute' and
                not is_ref and
                _should_have_create_methods(class_name, parent)
            )

            methods_code.append(_generate_add_create_method(
                class_name, attr_name, py_attr_name, attr_kind, is_ref, actual_type, should_use_create
            ))

    return methods_code


def generate_class_code(
    class_info: Dict[str, Any],
    package_path: str,
    project_root: Path,
    requirements_dir: Path
) -> str:
    """Generate Python class code from requirements JSON.

    Args:
        class_info: Class information dictionary from requirements
        package_path: Full package path (e.g., 'M2::AUTOSARTemplates::...')
        project_root: Root directory of the project
        requirements_dir: Path to requirements directory

    Returns:
        Generated Python class code
    """
    from . import type_resolver

    class_name = class_info['name']
    is_abstract = class_info.get('is_abstract', False)
    parent = class_info.get('parent') or 'ARObject'
    attributes = class_info.get('attributes', {})

    imports = type_resolver.generate_imports(class_info, package_path, project_root, requirements_dir, class_name)

    # Generate docstring
    docstring = _generate_docstring(class_info)

    # Class declaration
    bases = [parent]
    if is_abstract:
        bases.append('ABC')

    class_decl = f"class {class_name}({', '.join(bases)}):"

    # Check if any base class has __init__(parent, short_name) signature
    has_short_name_init = type_resolver._has_short_name_in_init(class_info, requirements_dir)
    is_arobject_child = (parent == 'ARObject')

    # Generate __init__ code
    init_code = _generate_init_code(
        class_name, docstring, is_abstract, has_short_name_init, is_arobject_child
    )

    # Generate attribute initialization
    attr_code = _generate_attribute_initialization(class_name, attributes)

    # Generate methods
    methods_code = _generate_methods(class_name, parent, attributes)

    # Combine all parts
    code_parts = imports + [''] + [class_decl, init_code, ''] + attr_code + [''] + methods_code

    return '\n'.join(code_parts)
