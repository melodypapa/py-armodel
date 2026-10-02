#!/usr/bin/env python3
"""Regenerate docs/plan/sync-todo/xsd_classes.md — the report of all XSD-only classes.

An "XSD-only class" is a class whose node in docs/plan/sync-todo/hierarchy_tree.md is
tagged `(XSD)`: no Class/Enumeration table in either the R23-11 or R4.3.1 markdown
corpus, so its spec source is the R23-11 XSD (autosar/R23-11/xsd/AUTOSAR_00052.xsd).
Table rows: class name, XML element name (the matching xsd:complexType name; "(X group
only)" = the class exists only as an xsd:element group with no own complexType), and the
sync group id (the Group*.md queue file holding the class's `- [ ]`/`- [x]` row).

atpVariation-generated variation-point containers (`*Content` / `*Conditional` classes
whose XSD documentation reads "This element was generated/modified due to an
atpVariation stereotype") are excluded from the main table and listed in a trailing
appendix — they are variation-decomposition artifacts whose members are owned by the
parent class (mmt.qualifiedName="Parent.attr"), not standalone meta-classes.

Class-name matching is case/hyphen-insensitive (IPsecRule -> IPV-4-RULE). Stdlib only;
run from anywhere inside the repo.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TODO = ROOT / "docs/plan/sync-todo"
XSD = ROOT / "autosar/R23-11/xsd/AUTOSAR_00052.xsd"

tree = (TODO / "hierarchy_tree.md").read_text(encoding="utf-8")


def norm(name):
    return name.lower().replace("-", "").replace("_", "")


# 1. XSD-only class nodes from the hierarchy tree
classes = []
seen = set()
for m in re.finditer(r"^[│\s]*[├└]─ ([A-Za-z_]\w*) \(XSD\)", tree, re.M):
    if m.group(1) not in seen:
        seen.add(m.group(1))
        classes.append(m.group(1))

# 2. XSD complexTypes (=> XML element names), simpleTypes, element groups — with docs
xsd_text = XSD.read_text(encoding="utf-8")
complex_types = {}
for m in re.finditer(r'<xsd:complexType[^>]*\bname="([^"]+)"', xsd_text):
    complex_types.setdefault(norm(m.group(1)), []).append(m.group(1))
simple_types = {}
for m in re.finditer(r'<xsd:simpleType[^>]*\bname="([^"]+)"', xsd_text):
    simple_types.setdefault(norm(m.group(1)), []).append(m.group(1))
gn = {}
for m in re.finditer(r'<xsd:group[^>]*\bname="([^"]+)"', xsd_text):
    gn.setdefault(norm(m.group(1)), []).append(m.group(1))

ct_docs = {}
for m in re.finditer(r'<xsd:complexType[^>]*\bname="([^"]+)">.*?<xsd:documentation>(.*?)</xsd:documentation>', xsd_text, re.S):
    ct_docs.setdefault(norm(m.group(1)), m.group(2))
group_docs = {}
for m in re.finditer(r'<xsd:group name="([^"]+)">.*?<xsd:documentation>(.*?)</xsd:documentation>', xsd_text, re.S):
    group_docs.setdefault(norm(m.group(1)), m.group(2))

# 3. Group id: queue rows `- [ ] \`Name\`` / `- [x] \`Name\`` in Group*.md
group_files = sorted(TODO.glob("Group*.md"), key=lambda p: int(re.search(r"Group(\d+)", p.stem).group(1)))
group_of = {}
for gf in group_files:
    gid = int(re.search(r"Group(\d+)", gf.stem).group(1))
    for line in gf.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\s*- \[[ x]\] `([A-Za-z_]\w*)`", line)
        if m:
            group_of.setdefault(m.group(1), []).append(gid)


def gid_of(cls):
    gids = group_of.get(cls)
    if not gids:
        return "—"
    return ", ".join(f"G{g}" for g in sorted(set(gids)))


rows = []  # (class, element, gid)
variation = []  # (class, element, gid) — atpVariation-generated containers, excluded from table
missing_element = []
for cls in sorted(classes):
    key = norm(cls)
    if key in complex_types:
        elem = "/".join(complex_types[key])
    elif key in gn:
        elem = "(" + "/".join(gn[key]) + " group only)"
    elif key in simple_types:
        elem = "—"
    else:
        elem = "??"
        missing_element.append(cls)
    doc = ct_docs.get(key) or group_docs.get(key) or ""
    if "atpVariation" in doc:
        variation.append((cls, elem, gid_of(cls)))
    else:
        rows.append((cls, elem, gid_of(cls)))

missing_group = [c for c, _, g in rows if g == "—"]

lines = []
lines.append("# XSD-only classes (source: AUTOSAR_00052.xsd)")
lines.append("")
lines.append("Every class whose node in `hierarchy_tree.md` is tagged `(XSD)` — no Class/Enumeration")
lines.append("table in either the R23-11 or R4.3.1 markdown corpus; spec source is the R23-11 XSD")
lines.append("(`autosar/R23-11/xsd/AUTOSAR_00052.xsd`).")
lines.append("")
lines.append("Excluded from the table: the atpVariation-generated variation-point containers")
lines.append('(`*Content` / `*Conditional` classes whose XSD documentation reads "This element was')
lines.append('generated/modified due to an atpVariation stereotype") — see the appendix at the bottom.')
lines.append("")
lines.append("Columns:")
lines.append("")
lines.append("- **Class** — spec class name (hierarchy_tree.md node).")
lines.append("- **XML element** — matching `xsd:complexType` name in `AUTOSAR_00052.xsd`; that name is")
lines.append("  the element name used in instance arxml documents (enumerations are complexTypes")
lines.append("  wrapping a `--SIMPLE` simpleType, so they carry an element name too). `(X group only)`")
lines.append("  = the class exists in the XSD only as an `xsd:element group` named X with no own")
lines.append("  complexType (abstract base composition — no own instance element).")
lines.append("- **Group** — Group*.md sync-queue file(s) holding the class's `- [ ]`/`- [x]` row")
lines.append("  (`G<n>` = Group<n>.md); `—` = no queue row anywhere in Group1–36 (not queued, not")
lines.append("  modeled in src).")
lines.append("")
n_grouponly = sum(1 for _, e, _ in rows if e.endswith("group only)"))
lines.append(
    f"**Total: {len(rows)} XSD-only classes** — {len(rows) - n_grouponly} with an own `xsd:complexType`"
    f" (incl. enumerations, which are complexTypes wrapping a `--SIMPLE` simpleType),"
    f" {n_grouponly} element-group-only, {len(missing_element)} unmatched against the XSD,"
    f" {len(missing_group)} without a Group*.md queue row;"
    f" plus {len(variation)} atpVariation-generated containers excluded (see appendix)."
)
lines.append("")
lines.append("| Class | XML element | Group |")
lines.append("|---|---|---|")
for cls, elem, gid in rows:
    lines.append(f"| `{cls}` | {elem} | {gid} |")
lines.append("")

if missing_group:
    lines.append("## XSD-only classes with no Group*.md queue row")
    lines.append("")
    lines.append(", ".join(f"`{c}`" for c in missing_group))
    lines.append("")

if variation:
    lines.append("## Excluded — atpVariation-generated variation-point containers")
    lines.append("")
    lines.append('XSD documentation of each reads "This element was generated/modified due to an')
    lines.append('atpVariation stereotype." — they are variation-point decomposition artifacts')
    lines.append("(`*Content` attribute holders / `*Conditional` wrappers), not standalone meta-classes;")
    lines.append('their members are owned by the parent class (`mmt.qualifiedName="Parent.attr"`).')
    lines.append("")
    lines.append("| Class | XML element | Group |")
    lines.append("|---|---|---|")
    for cls, elem, gid in variation:
        lines.append(f"| `{cls}` | {elem} | {gid} |")
    lines.append("")

out = TODO / "xsd_classes.md"
out.write_text("\n".join(lines), encoding="utf-8")
print(f"classes={len(classes)} table={len(rows)} variation_excluded={len(variation)}")
print(f"missing_element={missing_element}")
print(f"missing_group={len(missing_group)}")
print(f"variation with queue rows: {[(c, g) for c, _, g in variation if g != '—']}")
print(f"written: {out}")
