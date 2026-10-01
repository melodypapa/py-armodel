"""Mechanical checks for the sync-autosar-class skill static review."""

import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / ".claude" / "skills" / "sync-autosar-class"
RULES_PATH = SKILL_DIR / "rules.md"
SKILL_PATH = SKILL_DIR / "SKILL.md"

RULE_HEADER_RE = re.compile(r"^##\s+Rule\s+(\d{4})", re.MULTILINE)
SUBRULE_HEADER_RE = re.compile(r"^###\s+(\d{4}\.\d+(?:\.\d+)?)\s", re.MULTILINE)
RULE_REF_RE = re.compile(r"\bRule\s+(\d{4}(?:\.\d+)?)\b")


def collect_defined_rules() -> Tuple[List[str], List[str]]:
    rules_text = RULES_PATH.read_text(encoding="utf-8")
    top_level = RULE_HEADER_RE.findall(rules_text)
    sub_level = SUBRULE_HEADER_RE.findall(rules_text)
    return top_level, sub_level


def collect_referenced_rules() -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for path in (RULES_PATH, SKILL_PATH):
        text = path.read_text(encoding="utf-8")
        for match in RULE_REF_RE.finditer(text):
            rid = match.group(1)
            counts[rid] = counts.get(rid, 0) + 1
    return counts


def check_continuity(top_level: List[str]) -> List[str]:
    findings: List[str] = []
    top = max((int(r) for r in top_level), default=0)
    expected = [f"{n:04d}" for n in range(1, top + 1)]
    if top_level != expected:
        findings.append(f"top-level rule list is {top_level}, expected {expected}")
    seen = set()
    duplicates = [r for r in top_level if r in seen or seen.add(r)]
    if duplicates:
        findings.append(f"duplicate top-level rule IDs: {duplicates}")
    return findings


def check_dangling_refs(defined: List[str], referenced: Dict[str, int]) -> List[str]:
    findings: List[str] = []
    defined_set = set(defined)
    for rid in referenced:
        if rid not in defined_set and not any(d == rid.split(".")[0] for d in defined_set):
            findings.append(f"referenced Rule {rid} has no definition")
    return findings


LEGACY_BLOCK_RE = re.compile(r"#\s*(\w+)\s+method parity checklist:")
LEGACY_ROW_RE = re.compile(
    r"^\s*#\s*\[[xX—]\]\s+\S+\s+\[[x—]\]\s+impl\s+\[[x—]\]\s+docstring\s+\[[x—]\]\s+test\s*$"
)
LEGACY_STAMP_RE = re.compile(r"#\s*((?:Spec|XSD) verified:[^\n]*)")


def collect_legacy_checklists() -> List[str]:
    """Checklist blocks whose rows end at the 'test' column — Rule 0023 legacy format."""
    results: List[str] = []
    models_dir = ROOT / "src" / "armodel" / "models"
    for path in sorted(models_dir.rglob("*.py")):
        current: Optional[str] = None
        stamp: Optional[str] = None
        has_legacy = False
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            block = LEGACY_BLOCK_RE.search(line)
            if block:
                if current is not None and has_legacy:
                    results.append(f"{path.relative_to(ROOT)}: {current} — stale stamp: {stamp or 'none'}")
                current, stamp, has_legacy = block.group(1), None, False
            elif current is not None:
                stamp_match = LEGACY_STAMP_RE.search(line)
                if stamp_match and stamp is None:
                    stamp = stamp_match.group(1).strip()
                elif LEGACY_ROW_RE.match(line):
                    has_legacy = True
        if current is not None and has_legacy:
            results.append(f"{path.relative_to(ROOT)}: {current} — stale stamp: {stamp or 'none'}")
    return results


def main() -> int:
    top_level, sub_level = collect_defined_rules()
    referenced = collect_referenced_rules()
    findings: List[str] = []
    findings.extend(check_continuity(top_level))
    findings.extend(check_dangling_refs(top_level, referenced))

    print("=== sync-autosar-class static checks ===")
    print(f"Defined top-level rules ({len(top_level)}): {top_level}")
    print(f"Defined sub-rules ({len(sub_level)}): {sub_level}")
    print(f"Referenced rule IDs ({len(referenced)}): {sorted(referenced)}")
    legacy = collect_legacy_checklists()
    print(f"Legacy-format checklists (Rule 0023 re-sync inventory) ({len(legacy)}):")
    for item in legacy:
        print(f"  - {item}")
    if findings:
        print("\nFINDINGS:")
        for f in findings:
            print(f"  - {f}")
        return 1
    print("\nAll mechanical checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
