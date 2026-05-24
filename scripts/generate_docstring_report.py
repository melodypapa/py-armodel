"""Generate a docstring coverage report for the py-armodel codebase."""

import ast
import os
from pathlib import Path


def get_class_info(filepath):
    """Extract class names and their docstrings from a Python file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            source = f.read()
        tree = ast.parse(source, filename=filepath)
    except (SyntaxError, UnicodeDecodeError):
        return []

    results = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            docstring = ast.get_docstring(node)
            results.append({
                "name": node.name,
                "docstring": docstring,
                "line": node.lineno,
            })
    return results


def scan_directory(base_dir):
    """Scan all Python files and return results grouped by module."""
    modules = {}

    for root, dirs, files in os.walk(base_dir):
        dirs[:] = [d for d in dirs if d not in ("__pycache__", "build", ".git")]

        for fname in sorted(files):
            if not fname.endswith(".py"):
                continue
            if fname == "__init__.py":
                continue

            filepath = os.path.join(root, fname)
            rel_path = os.path.relpath(filepath, base_dir)
            module = os.path.dirname(rel_path)

            classes = get_class_info(filepath)
            if classes:
                if module not in modules:
                    modules[module] = []
                modules[module].append({
                    "file": rel_path,
                    "classes": classes,
                })

    return modules


def format_docstring_summary(docstring):
    """Get first line of docstring, truncated."""
    if not docstring:
        return None
    first_line = docstring.strip().split("\n")[0]
    if len(first_line) > 120:
        return first_line[:117] + "..."
    return first_line


def generate_report(modules):
    """Generate markdown report."""
    lines = []
    lines.append("# Docstring Coverage Report")
    lines.append("")
    lines.append("Generated for manual review. Flag any inaccurate docstrings for correction.")
    lines.append("")

    total_documented = 0
    total_undocumented = 0

    for module in sorted(modules.keys()):
        files = modules[module]
        module_doc = 0
        module_undoc = 0

        lines.append(f"## {module}")
        lines.append("")

        for file_info in files:
            lines.append(f"### {file_info['file']}")
            lines.append("")

            for cls in file_info["classes"]:
                if cls["docstring"]:
                    total_documented += 1
                    module_doc += 1
                    summary = format_docstring_summary(cls["docstring"])
                    lines.append(f"- **{cls['name']}** (L{cls['line']}): {summary}")
                else:
                    total_undocumented += 1
                    module_undoc += 1
                    lines.append(f"- ~~{cls['name']}~~ (L{cls['line']}): *missing*")

            lines.append("")

        coverage = module_doc / (module_doc + module_undoc) * 100 if (module_doc + module_undoc) > 0 else 0
        lines.append(f"> Coverage: {module_doc}/{module_doc + module_undoc} ({coverage:.1f}%)")
        lines.append("")

    total = total_documented + total_undocumented
    overall = total_documented / total * 100 if total > 0 else 0
    lines.insert(3, f"**Overall: {total_documented}/{total} documented ({overall:.1f}%), {total_undocumented} missing**")
    lines.insert(4, "")

    return "\n".join(lines)


if __name__ == "__main__":
    base = Path(__file__).parent.parent / "src" / "armodel"
    modules = scan_directory(str(base))
    report = generate_report(modules)

    output = Path(__file__).parent.parent / "reports" / "docstring_review.md"
    output.write_text(report, encoding="utf-8")
    print(f"Report written to {output}")
    print(f"Modules: {len(modules)}")
