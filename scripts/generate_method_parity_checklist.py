"""Generate method parity checklist comment blocks for model classes."""

import ast
import re
import argparse
from pathlib import Path


def normalize_token(name):
    result = name.lower()
    if result.startswith("test_"):
        result = result[5:]
    return result.replace("_", "")


def normalize_class_name(name):
    return name.lower().replace("_", "")


def build_test_index(test_root):
    index = {}
    test_root = Path(test_root)
    if not test_root.is_dir():
        return index
    for pyfile in test_root.rglob("*.py"):
        if pyfile.name == "__init__.py":
            continue
        try:
            tree = ast.parse(pyfile.read_text(encoding="utf-8"))
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name.startswith("Test"):
                cls_key = normalize_class_name(node.name[4:])
                tokens = set()
                for item in node.body:
                    if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        tokens.add(normalize_token(item.name))
                if cls_key not in index:
                    index[cls_key] = set()
                index[cls_key].update(tokens)
    return index


def get_direct_methods(class_node):
    methods = []
    for item in class_node.body:
        if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
            methods.append(item)
    return methods


def has_real_body(func_node):
    if not func_node.body:
        return False
    body = func_node.body
    first_is_docstring = (
        isinstance(body[0], ast.Expr)
        and isinstance(body[0].value, ast.Constant)
    )
    remaining = body[1:] if first_is_docstring else body
    if not remaining:
        return False
    if len(remaining) == 1 and isinstance(remaining[0], ast.Pass):
        return False
    return True


def has_docstring(func_node):
    doc = ast.get_docstring(func_node, clean=False)
    return bool(doc)


def is_tested(method_name, class_name, test_index):
    cls_key = normalize_class_name(class_name)
    if cls_key not in test_index:
        return False
    tokens = test_index[cls_key]
    token = normalize_token(method_name)
    if token in tokens:
        return True
    if method_name == "__init__":
        for alt in ("init", "initialization", "constructor"):
            if alt in tokens:
                return True
    return False


def get_class_docstring_span(class_node, lines):
    body = class_node.body
    if not body:
        return None
    first = body[0]
    if not (isinstance(first, ast.Expr) and isinstance(first.value, ast.Constant)):
        return None
    start = first.lineno
    end = first.end_lineno
    return (start, end)


def find_existing_block_span(lines, search_start, search_end, class_name, indent):
    if search_start >= len(lines):
        return None
    header_re = re.compile(
        r"^" + re.escape(indent) + r"# " + re.escape(class_name) + r" method parity checklist:\s*$"
    )
    for i in range(search_start, min(search_end, len(lines))):
        if header_re.match(lines[i]):
            end_idx = i
            while end_idx + 1 < len(lines) and lines[end_idx + 1].startswith(indent + "#"):
                end_idx += 1
            return (i, end_idx)
    return None


def compute_insertion_point(class_node, lines, docstring_span):
    if docstring_span is not None:
        return docstring_span[1]
    first_body = class_node.body
    if first_body:
        return first_body[0].lineno - 1
    return class_node.end_lineno - 1


def format_checklist_block(class_name, methods, test_index, indent):
    lines = []
    lines.append(f"{indent}# {class_name} method parity checklist:")
    if not methods:
        lines.append(f"{indent}# (no methods)")
        return lines
    for func in methods:
        m_name = func.name
        i = has_real_body(func)
        d = has_docstring(func)
        t = is_tested(m_name, class_name, test_index)
        impl_mark = "[x]" if i else "[ ]"
        doc_mark = "[x]" if d else "[ ]"
        test_mark = "[x]" if t else "[ ]"
        row_mark = "[x]" if (i and d and t) else "[ ]"
        line = f"{indent}# {row_mark} {m_name:<28} {impl_mark} impl  {doc_mark} docstring  {test_mark} test"
        lines.append(line)
    return lines


def collect_class_nodes_with_indent(tree, lines):
    result = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            if node.body:
                first_body_line = lines[node.body[0].lineno - 1]
                indent = first_body_line[:len(first_body_line) - len(first_body_line.lstrip())]
            else:
                indent = ""
            result.append((node, indent))
    return result


def apply_edits_to_file(filepath, test_index, dry_run, verbose):
    filepath = Path(filepath)
    try:
        raw = filepath.read_bytes()
    except OSError as e:
        print(f"  [SKIP] {filepath.name}: {e}", flush=True)
        return (False, None)

    if b"\r\n" in raw:
        newline = "\r\n"
    elif b"\r" in raw:
        newline = "\r"
    else:
        newline = "\n"

    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as e:
        print(f"  [SKIP] {filepath.name}: encoding error: {e}", flush=True)
        return (False, None)

    if not text.strip():
        return (False, None)

    try:
        tree = ast.parse(text, filename=str(filepath))
    except SyntaxError as e:
        print(f"  [SKIP] {filepath.name}: syntax error: {e}", flush=True)
        return (False, None)

    lines = text.split(newline)
    if lines and not lines[-1]:
        lines.pop()
    classes = collect_class_nodes_with_indent(tree, lines)

    edits = []
    stats = {"impl": 0, "docstring": 0, "test": 0, "total": 0, "classes": 0}

    for class_node, indent in classes:
        cls_name = class_node.name
        doc_span = get_class_docstring_span(class_node, lines)
        insert_pt = compute_insertion_point(class_node, lines, doc_span)
        search_start = max(0, class_node.lineno - 1)
        search_end = min(insert_pt + 20, len(lines))
        existing = find_existing_block_span(lines, search_start, search_end, cls_name, indent)

        methods = get_direct_methods(class_node)
        block = format_checklist_block(cls_name, methods, test_index, indent)

        stats["classes"] += 1
        for func in methods:
            stats["total"] += 1
            if has_real_body(func):
                stats["impl"] += 1
            if has_docstring(func):
                stats["docstring"] += 1
            if is_tested(func.name, cls_name, test_index):
                stats["test"] += 1

        block.append("")

        if existing is not None:
            start_idx, end_idx = existing
            edits.append((start_idx, end_idx + 2, block))
        else:
            edits.append((insert_pt, insert_pt, block))

        if verbose:
            m_count = len(methods)
            i_count = sum(1 for m in methods if has_real_body(m))
            d_count = sum(1 for m in methods if has_docstring(m))
            t_count = sum(1 for m in methods if is_tested(m.name, cls_name, test_index))
            print(f"    {cls_name}: {m_count} methods, {i_count} impl, {d_count} docstring, {t_count} test", flush=True)

    if not edits:
        return (False, stats)

    edits.sort(key=lambda x: x[0], reverse=True)

    for start, end, block_lines in edits:
        lines[start:end] = block_lines

    new_text = newline.join(lines)
    if new_text != text:
        new_text += newline

    if new_text == text:
        return (False, stats)

    if not dry_run:
        filepath.write_bytes(new_text.encode("utf-8"))
        print(f"  [MODIFIED] {filepath.name}", flush=True)

    return (True, stats)


def generate_markdown_report(all_stats):
    lines = []
    lines.append("# Method Parity Coverage Report")
    lines.append("")
    lines.append("*Auto-generated by scripts/generate_method_parity_checklist.py*")
    lines.append("")
    total_impl = sum(s["impl"] for s in all_stats.values())
    total_doc = sum(s["docstring"] for s in all_stats.values())
    total_test = sum(s["test"] for s in all_stats.values())
    total_all = sum(s["total"] for s in all_stats.values())
    total_cls = sum(s["classes"] for s in all_stats.values())

    def pct(v, t):
        return f"{v/t*100:.1f}%" if t > 0 else "N/A"

    lines.append(f"**Overall:** {total_all} methods across {total_cls} classes")
    lines.append(f"- **Impl:** {total_impl}/{total_all} ({pct(total_impl, total_all)})")
    lines.append(f"- **Docstring:** {total_doc}/{total_all} ({pct(total_doc, total_all)})")
    lines.append(f"- **Test:** {total_test}/{total_all} ({pct(total_test, total_all)})")
    lines.append("")

    grouped = {}
    for relpath, stats in sorted(all_stats.items()):
        parts = Path(relpath).parts
        group = str(Path(*parts[:2])) if len(parts) >= 2 else "root"
        if group not in grouped:
            grouped[group] = []
        grouped[group].append((relpath, stats))

    for group in sorted(grouped.keys()):
        lines.append(f"## {group}")
        lines.append("")
        g_impl = sum(s["impl"] for _, s in grouped[group])
        g_doc = sum(s["docstring"] for _, s in grouped[group])
        g_test = sum(s["test"] for _, s in grouped[group])
        g_all = sum(s["total"] for _, s in grouped[group])
        g_cls = sum(s["classes"] for _, s in grouped[group])
        lines.append(f"**Group total:** {g_all} methods, {g_cls} classes — "
                      f"Impl {g_impl}/{g_all} ({pct(g_impl, g_all)}), "
                      f"Docstring {g_doc}/{g_all} ({pct(g_doc, g_all)}), "
                      f"Test {g_test}/{g_all} ({pct(g_test, g_all)})")
        lines.append("")
        for relpath, stats in grouped[group]:
            r_impl, r_doc, r_test, r_total, r_cls = (
                stats["impl"], stats["docstring"], stats["test"],
                stats["total"], stats["classes"]
            )
            lines.append(f"- **{relpath}**: {r_cls} classes, {r_total} methods — "
                          f"Impl {r_impl}/{r_total} ({pct(r_impl, r_total)}), "
                          f"Docstring {r_doc}/{r_total} ({pct(r_doc, r_total)}), "
                          f"Test {r_test}/{r_total} ({pct(r_test, r_total)})")
        lines.append("")

    return "\n".join(lines)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate method parity checklists for model classes"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Print what would be changed without modifying files"
    )
    parser.add_argument(
        "--module", type=str, default=None,
        help="Substring filter for file paths (forward-slash normalized)"
    )
    parser.add_argument(
        "--verbose", action="store_true",
        help="Log per-class method counts"
    )
    return parser.parse_args()


def main():
    args = parse_args()

    root = Path(__file__).parent.parent
    models_dir = root / "src" / "armodel" / "models"
    test_dir = root / "tests" / "test_armodel"
    report_dir = root / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)

    print(f"Scanning {models_dir} for model files...", flush=True)
    model_files = sorted(models_dir.rglob("*.py"))
    if args.module:
        model_files = [
            f for f in model_files
            if args.module in f.relative_to(models_dir).as_posix()
        ]

    print(f"Building test index from {test_dir}...", flush=True)
    test_index = build_test_index(test_dir)
    print(f"  Found {len(test_index)} test classes in index.", flush=True)

    changed_count = 0
    processed_count = 0
    all_stats = {}

    for filepath in model_files:
        rel = filepath.relative_to(models_dir).as_posix()
        if rel == "__init__.py":
            continue
        processed_count += 1
        if args.verbose:
            print(f"Processing: {rel}", flush=True)
        changed, stats = apply_edits_to_file(filepath, test_index, args.dry_run, args.verbose)
        if stats is not None:
            all_stats[rel] = stats
        if changed:
            changed_count += 1

    print(f"\nProcessed {processed_count} files; modified {changed_count} files.", flush=True)

    total_all = sum(s["total"] for s in all_stats.values())
    total_impl = sum(s["impl"] for s in all_stats.values())
    total_doc = sum(s["docstring"] for s in all_stats.values())
    total_test = sum(s["test"] for s in all_stats.values())

    def pct(v, t):
        return f"{v/t*100:.1f}%" if t > 0 else "N/A"

    print(f"Overall: {total_impl}/{total_all} impl ({pct(total_impl, total_all)}), "
          f"{total_doc}/{total_all} docstring ({pct(total_doc, total_all)}), "
          f"{total_test}/{total_all} test ({pct(total_test, total_all)})", flush=True)

    report_path = report_dir / "method_parity_review.md"
    report_md = generate_markdown_report(all_stats)
    if not args.dry_run:
        report_path.write_text(report_md, encoding="utf-8")
        print(f"Report written to {report_path}", flush=True)
    else:
        print(f"(Dry-run: report not written)", flush=True)


if __name__ == "__main__":
    main()
