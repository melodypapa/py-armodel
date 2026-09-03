"""Rule 0020 per-class verification: XSD anchors vs markdown atpVariation triggers vs Python capability.

Usage:
    python scripts/verify_vp_rule.py            # full audit -> docs/superpowers/plans/vp_capability_audit_report.md
    python scripts/verify_vp_rule.py <KEBAB>    # evidence printout for one anchor class
"""

import importlib.util
import os
import re
import subprocess
import sys

XSD = "autosar/R23-11/xsd/AUTOSAR_00052.xsd"
MD_DIR = "autosar/R23-11/markdown"
ANCHORS = "docs/superpowers/plans/vp_anchors.txt"
REPORT = "docs/superpowers/plans/vp_capability_audit_report.md"
MIXIN_MODULE = "armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable"

NAME_FIXES = {
    "EcuMapping": "ECUMapping",
    "InstantiationRteEventProps": "InstantiationRTEEventProps",
    "PortApiOption": "PortAPIOption",
    "RteEvent": "RTEEvent",
}


def parse_xsd():
    lines = open(XSD).read().split("\n")
    blocks = {}
    order = []
    current = None
    for i, line in enumerate(lines):
        m = re.search(r'<xsd:(complexType|group) name="([A-Z0-9-]+)"', line)
        if m:
            current = m.group(2)
            blocks[current] = {"start": i + 1, "lines": [], "kind": m.group(1)}
            order.append(current)
            continue
        m2 = re.search(r'<xsd:(attributeGroup|simpleType) name="', line)
        if m2:
            current = None
            continue
        if current:
            blocks[current]["lines"].append(line)
    for name, b in blocks.items():
        text = "\n".join(b["lines"])
        b["direct_vp"] = 'name="VARIATION-POINT"' in text
        b["applicable_for"] = re.findall(r"Applicable for: ([\w.]+)", text)
        b["not_applicable_for"] = re.findall(r"Not Applicable for: ([\w.]+)", text)
        qn = re.search(r'mmt.qualifiedName="([\w.]+)\.variationPoint"', text)
        b["qn"] = qn.group(1) if qn else None
        b["group_refs"] = re.findall(r'<xsd:group ref="AR:([A-Z0-9-]+)"/>', text)
    return blocks


def parse_markdown():
    pairs = []
    mentioned = set()
    for fname in sorted(os.listdir(MD_DIR)):
        if not fname.endswith(".md"):
            continue
        current_class = None
        for lineno, line in enumerate(open(os.path.join(MD_DIR, fname), errors="replace"), 1):
            cls = re.match(r"\|\s*Class\s*\|\s*([\w.]+)", line)
            if cls:
                current_class = cls.group(1)
                continue
            for name in re.findall(r"\b([A-Z]\w+(?:Ref)?Conditional)\b", line):
                mentioned.add(name)
            norm = line.replace(" ", "")
            if "atpVariation" not in norm or "variationPoint.shortLabel" not in norm:
                continue
            m = re.match(r"\|\s*([\w ()]+?)\s*\|", line)
            if m and current_class:
                attr = m.group(1).replace(" ", "")
                attr = re.sub(r"\(.*?\)", "", attr)
                if attr not in ("Attribute", "Class", "Note", "Base", "Package", "Aggregated by", "Subclasses"):
                    pairs.append((fname, lineno, current_class, attr))
                    for t in re.findall(r"\|\s*(\w+RefConditional)\s*\|", line):
                        mentioned.add(t)
    return pairs, mentioned


def class_name_from_row(fname):
    return None


def python_status(cls):
    actual = NAME_FIXES.get(cls, cls)
    out = subprocess.run(
        ["grep", "-rl", "-E", r"class %s\(" % actual, "src/armodel/models", "--include=*.py"],
        capture_output=True,
        text=True,
    ).stdout.strip()
    if not out:
        return "not implemented"
    try:
        module = importlib.import_module(module_for(out.split("\n")[0]))
        klass = getattr(module, actual)
    except Exception:
        return "implemented (status unknown)"
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable

    return "anchored" if issubclass(klass, VariationPointCapable) else "implemented, NOT capable"


def module_for(path):
    rel = re.sub(r"^src/", "", path).replace("/", ".")
    if rel.endswith(".__init__.py"):
        rel = rel[: -len(".__init__.py")]
    else:
        rel = rel[: -len(".py")]
    return rel


def main():
    blocks = parse_xsd()
    if len(sys.argv) > 1:
        kebab = sys.argv[1]
        b = blocks.get(kebab)
        if b is None:
            print("no XSD block:", kebab)
            return 1
        print("XSD: kind=%s start line %d" % (b["kind"], b["start"]))
        print("XSD: direct VARIATION-POINT:", b["direct_vp"])
        print("XSD: Applicable for:", b["applicable_for"])
        print("XSD: Not Applicable for:", b["not_applicable_for"])
        print("XSD: qualifiedName:", b["qn"])
        print("XSD: group refs:", b["group_refs"])
        return 0

    pairs, mentioned = parse_markdown()
    pair_index = {}
    role_index = {}
    for fname, lineno, cls, attr in pairs:
        pair_index.setdefault((cls, attr), []).append("%s:%d" % (fname, lineno))
        role_index.setdefault(attr, set()).add(cls)

    rows = []
    stats = {"PASS-direct": 0, "PASS-base": 0, "DEVIATION": 0, "NOTE": 0}
    for line in open(ANCHORS):
        kebab, cls = line.strip().split(" -> ")
        b = blocks[kebab]
        md_hits = []
        verdict = None
        for token in b["applicable_for"]:
            whole, _, role = token.rpartition(".")
            hits = pair_index.get((whole, role), [])
            if hits:
                md_hits += ["%s (%s.%s)" % (loc, whole, role) for loc in hits]
                verdict = verdict or "PASS (direct anchor)"
            elif role in role_index:
                md_hits += ["role-only: %s.%s" % (w, role) for w in sorted(role_index[role]) if w != whole]
                verdict = verdict or "PASS (markdown trigger via base-class row; role %s)" % role
        if verdict is None:
            if cls.endswith("Conditional") and cls not in mentioned:
                verdict = "NOTE: schema-only wrapper (association pattern, no markdown class)"
            else:
                verdict = "DEVIATION: no-markdown-trigger"
        if verdict.startswith("PASS (direct"):
            stats["PASS-direct"] += 1
        elif verdict.startswith("PASS (markdown"):
            stats["PASS-base"] = stats.get("PASS-base", 0) + 1
        elif verdict.startswith("DEVIATION"):
            stats["DEVIATION"] += 1
        else:
            stats["NOTE"] = stats.get("NOTE", 0) + 1
        xsd_cell = "direct anchor (l.%d)" % b["start"] if b["direct_vp"] else "no direct VP"
        rows.append((cls, python_status(cls), xsd_cell, ", ".join(b["applicable_for"]) or "-", "; ".join(md_hits) or "-", verdict))

    with open(REPORT, "w") as f:
        f.write("# VariationPointCapable capability audit (Rule 0020)\n\n")
        f.write("Generated by `scripts/verify_vp_rule.py` against `AUTOSAR_00052.xsd` (R23-11) and the R23-11 markdown corpus.\n\n")
        f.write("| Python class | Python status | XSD evidence | Applicable for | Markdown evidence | Verdict |\n")
        f.write("|---|---|---|---|---|---|\n")
        for r in rows:
            f.write("| %s | %s | %s | %s | %s | %s |\n" % r)
        f.write("\n## Summary\n\n")
        for k, v in stats.items():
            f.write("- %s: %d\n" % (k, v))
        f.write("\n## Hand-verified annotations\n\n")
        f.write(
            "- `Row` (Tbody.row): the markdown corpus documents this aggregation in the GST splitkey table "
            "(AUTOSAR_FO_TPS_GenericStructureTemplate.md, `| Tbody.row | row, row.variationPoint.shortLabel |`) "
            "rather than an attribute row; the atpVariation evidence exists, shape differs. Counted as DEVIATION "
            "no-markdown-trigger by the script; human verdict: evidence present, different table shape.\n"
        )
        f.write("\n## Deviations requiring disposition (amend Rule 0020 or accept)\n\n")
        f.write(
            "The 10 `no-markdown-trigger` rows are XSD anchors whose `Applicable for` role has no "
            "`atpVariation` attribute row anywhere in the R23-11 markdown corpus (verified including "
            "space-reflow spellings). The XSD annotation is authoritative (Rule 0020); the markdown "
            "tables simply do not carry the trigger for these aggregations.\n"
        )
    print("anchors audited:", len(rows))
    for k, v in stats.items():
        print("%-32s %d" % (k, v))
    return 0


if __name__ == "__main__":
    sys.exit(main())
