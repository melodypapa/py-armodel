import json
import re
import sys

MIXIN = "VariationPointCapable"
IMPORT_LINE = "from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable"


def insert_mixin(base_list):
    base_list = base_list.strip()
    parts = [p.strip() for p in base_list.split(",")]
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
        last_import = 0
        for i, line in enumerate(lines[:200]):
            if line.startswith(("from ", "import ")):
                last_import = i
        lines.insert(last_import + 1, IMPORT_LINE)
        content = "\n".join(lines)
    with open(path, "w") as f:
        f.write(content)


def main():
    batches = sys.argv[1].split(",")
    work = json.load(open("/tmp/vp_work.json"))
    count = 0
    for path, entries in sorted(work.items()):
        if any(batch in path for batch in batches):
            anchor_file(path, entries)
            count += len(entries)
    print("anchored classes in batches %r: %d" % (batches, count))
    return 0


if __name__ == "__main__":
    sys.exit(main())
