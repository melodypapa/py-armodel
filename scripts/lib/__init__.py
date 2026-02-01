"""
py-armodel Script Library

This package contains modular components for the fix-package-implementation script
and other related tools.
"""

from .package_loader import (
    get_all_packages,
    find_class_in_requirements,
    find_enum_in_requirements,
    load_requirements_index,
    load_package_json,
)
from .type_resolver import (
    build_type_index,
    find_type_in_codebase_cached,
    find_type_in_codebase,
    generate_imports,
    get_generation_report,
    reset_generation_report,
    get_missing_types_to_generate,
    clear_missing_types_to_generate,
    update_cache_for_new_class,
)
from .code_generator import (
    generate_class_code,
    _is_container_class,
    _should_have_create_methods,
)
from .test_generator import (
    generate_test_case,
    print_generation_report,
)
from .code_utils import (
    validate_code,
    format_code_with_ruff,
    parse_existing_class,
    merge_class_with_existing,
    run_tests,
    run_flake8_check,
)

__all__ = [
    # package_loader
    'get_all_packages',
    'find_class_in_requirements',
    'find_enum_in_requirements',
    'load_requirements_index',
    'load_package_json',
    # type_resolver
    'build_type_index',
    'find_type_in_codebase_cached',
    'find_type_in_codebase',
    'generate_imports',
    'get_generation_report',
    'reset_generation_report',
    'get_missing_types_to_generate',
    'clear_missing_types_to_generate',
    'update_cache_for_new_class',
    # code_generator
    'generate_class_code',
    '_is_container_class',
    '_should_have_create_methods',
    # test_generator
    'generate_test_case',
    'print_generation_report',
    # code_utils
    'validate_code',
    'format_code_with_ruff',
    'parse_existing_class',
    'merge_class_with_existing',
    'run_tests',
    'run_flake8_check',
]
