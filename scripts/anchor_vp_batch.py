import importlib.util
import json
import re
import sys

MIXIN = "VariationPointCapable"
IMPORT_LINE = "from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable"


def module_for(path):
    rel = re.sub(r"^src/", "", path).replace("/", ".")
    if rel.endswith(".__init__.py"):
        rel = rel[: -len(".__init__.py")]
    else:
        rel = rel[: -len(".py")]
    return importlib.import_module(rel)


def insert_mixin(base_list):
    parts = [p.strip() for p in base_list.strip().split(",")]
    if MIXIN in parts:
        return None
    idx = parts.index("ABC") if "ABC" in parts else len(parts)
    parts.insert(idx, MIXIN)
    return ", ".join(parts)


def anchor_file(path, entries):
    with open(path) as f:
        lines = f.read().split("\n")
    for name, lineno, bases in sorted(entries, key=lambda e: -e[1]):
        line = lines[lineno - 1]
        m = re.match(r"^(\s*class\s+%s\()(.*)\)(:.*)?$" % name, line)
        if not m:
            raise SystemExit("no match: %s:%d: %r" % (path, lineno, line))
        new_bases = insert_mixin(m.group(2))
        if new_bases is not None:
            lines[lineno - 1] = m.group(1) + new_bases + ")" + (m.group(3) or "")
    content = "\n".join(lines)
    if IMPORT_LINE not in content:
        insert_at = None
        for i, line in enumerate(lines[:150]):
            stripped = line.strip()
            if stripped.startswith("from ") and " import (" in line:
                for j in range(i + 1, min(i + 80, len(lines))):
                    if lines[j].rstrip().endswith(")"):
                        break
                continue
            if line.startswith(("from ", "import ")):
                insert_at = i + 1
                break
        if insert_at is None:
            raise SystemExit("no safe import anchor in %s" % path)
        lines.insert(insert_at, IMPORT_LINE)
        content = "\n".join(lines)
    with open(path, "w") as f:
        f.write(content)


def main():
    batches = sys.argv[1].split(",")
    work = json.load(open("/tmp/vp_work.json"))
    anchored, skipped, failed_imports = 0, [], []
    for path, entries in sorted(work.items()):
        if not any(batch in path for batch in batches):
            continue
        try:
            module = module_for(path)
        except Exception as e:
            failed_imports.append((path, str(e)))
            continue
        todo = []
        for name, lineno, bases in entries:
            cls = getattr(module, name, None)
            if cls is None:
                failed_imports.append((path, name))
                continue
            if issubclass(
                cls, __import__("armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable", fromlist=["VariationPointCapable"]).VariationPointCapable
            ):
                skipped.append(name)
            else:
                todo.append((name, lineno, bases))
        if todo:
            anchor_file(path, todo)
            anchored += len(todo)
    print("anchored: %d, skipped (already capable): %d" % (anchored, len(skipped)))
    if skipped:
        print("skipped:", ", ".join(sorted(set(skipped))))
    if failed_imports:
        print("IMPORT FAILURES:")
        for item in failed_imports:
            print("  ", item)
    return 0


if __name__ == "__main__":
    sys.exit(main())
