#!/usr/bin/env python3
"""Repo-wide gate: every stamped model class must pass the sync-autosar-class audit.

`# Spec verified:` / `# XSD verified:` is the skill's review gate (Rule 0012.1).
This script makes that claim mechanically true instead of aspirational: a class
that *claims* to have been reviewed, but whose checklist is in a stale format, has
rows that disagree with its methods, or has a reader/writer that never calls a base
helper, is a defect the moment it is stamped. CI should say so instead of waiting
for a human 9b that may never audit it.

Only stamped classes are gated. A class with no marker is legitimately mid-queue
(Steps 1-8 done, awaiting 9b), so failing it would punish correct behaviour.

Usage:
    python scripts/audit_stamped_classes.py                 # human report, exit 1 on any failure
    python scripts/audit_stamped_classes.py --json
    python scripts/audit_stamped_classes.py --baseline tests/test_armodel/models/stamped_audit_baseline.txt
    python scripts/audit_stamped_classes.py --write-baseline tests/test_armodel/models/stamped_audit_baseline.txt
"""

from __future__ import annotations

import argparse
import ast
import importlib.util
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

ROOT = Path(__file__).resolve().parent.parent
MODELS_DIR = ROOT / "src" / "armodel" / "models"
SKILL_SCRIPT = ROOT / ".claude" / "skills" / "sync-autosar-class" / "audit_class.py"

MARKERS = ("# Spec verified:", "# XSD verified:")


def load_audit_class():
    """Import the skill's audit module (its directory name is not importable).

    The audit resolves `src/` and the parser/writer relative to the CWD. Rather than
    chdir (which would leak into whatever process called us — pytest runs this
    in-process), pin those module globals to absolute paths.
    """
    spec = importlib.util.spec_from_file_location("sync_audit_class", SKILL_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SKILL_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.MODELS_DIR = MODELS_DIR
    module.PARSER = ROOT / "src" / "armodel" / "parser" / "arxml_parser.py"
    module.ABSTRACT_PARSER = ROOT / "src" / "armodel" / "parser" / "abstract_arxml_parser.py"
    module.WRITER = ROOT / "src" / "armodel" / "writer" / "arxml_writer.py"
    module.ABSTRACT_WRITER = ROOT / "src" / "armodel" / "writer" / "abstract_arxml_writer.py"
    return module


def stamped_targets(audit) -> List[Tuple[str, Path, str]]:
    """(class, file, marker) for every model class carrying a provenance marker."""
    out: List[Tuple[str, Path, str]] = []
    for path in sorted(MODELS_DIR.rglob("*.py")):
        text = audit.read(path)
        if not any(m in text for m in MARKERS):
            continue
        try:
            tree = ast.parse(text)
        except SyntaxError:
            continue
        for node in tree.body:
            if not isinstance(node, ast.ClassDef):
                continue
            blk = audit.collect_block(text.splitlines(), node.name)
            if not blk:
                continue
            marker = next((line for line in blk[2] if line.startswith(MARKERS)), "")
            if marker:
                out.append((node.name, path, marker))
    return out


def audit_stamped(audit) -> Dict[str, List[str]]:
    """{class: [failing messages]} for stamped classes that fail the audit."""
    failures: Dict[str, List[str]] = {}
    for cls, path, _marker in stamped_targets(audit):
        report = audit.audit_one(cls, path)
        if report.failed:
            failures[cls] = [f"{code}: {msg}" for lvl, code, msg in report.rows if lvl == "FAIL"]
    return failures


def read_baseline(path: Path) -> Set[str]:
    if not path.exists():
        return set()
    return {line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip() and not line.startswith("#")}


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--baseline", type=Path, help="fail only on violations NOT already in this baseline file")
    ap.add_argument("--write-baseline", type=Path, help="write the current failing set to this file and exit 0")
    args = ap.parse_args(argv)

    audit = load_audit_class()
    targets = stamped_targets(audit)
    failures = audit_stamped(audit)

    if args.write_baseline:
        args.write_baseline.parent.mkdir(parents=True, exist_ok=True)
        args.write_baseline.write_text("\n".join(sorted(failures)) + "\n", encoding="utf-8")
        print(f"wrote {len(failures)} known-failing stamped classes to {args.write_baseline}")
        return 0

    if args.json:
        print(json.dumps({"stamped": len(targets), "failing": failures}, indent=2))
        return 1 if failures else 0

    print(f"stamped model classes: {len(targets)}")
    print(f"stamped classes FAILING the mechanical audit: {len(failures)}")
    for cls in sorted(failures):
        rel = next((str(p.relative_to(ROOT)) for c, p, _ in targets if c == cls), "?")
        print(f"  - {cls}  ({rel})")
        for msg in failures[cls]:
            print(f"      {msg}")

    if args.baseline:
        known = read_baseline(args.baseline)
        new = sorted(set(failures) - known)
        fixed = sorted(known - set(failures))
        print(f"\nbaseline: {args.baseline} ({len(known)} known)")
        if fixed:
            print(f"  resolved since baseline (drop them from the file): {', '.join(fixed)}")
        if new:
            print(f"  NEW violations not in baseline ({len(new)}): {', '.join(new)}")
            return 1
        print("  no new violations")
        return 0

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
