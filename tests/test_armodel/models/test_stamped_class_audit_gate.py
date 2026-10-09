"""Repo-wide gate: a stamped model class must pass the sync-autosar-class mechanical audit.

`# Spec verified:` / `# XSD verified:` is the skill's review gate (Rule 0012.1), but it
was a claim nothing checked: classes were stamped under an older bar and the drift only
surfaced at a 9b that may never have looked. These tests make the claim mechanically
true — a stamped class must have a current-format checklist, rows that match its
methods, and a reader/writer that calls a base helper (Rules 0002 / 0024 / 0025).

Only *stamped* classes are gated. A class with no marker is legitimately mid-queue
(Steps 1-8 done, awaiting 9b), so failing it would punish correct behaviour.

The tree carries a large pre-existing backlog, so by default this is a REGRESSION gate:
it fails only for stamped classes absent from `stamped_audit_baseline.txt`. New drift
is blocked today; draining the baseline is the ratchet. Set `SYNC_AUDIT_STRICT=1` to
require a clean sweep (the end state).

Companion CLI: `python .agents/skills/sync-autosar-class/audit_stamped_classes.py [--baseline <file>]`.
"""

import importlib.util
import os
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[3]
BASELINE = Path(__file__).with_name("stamped_audit_baseline.txt")
STRICT = os.environ.get("SYNC_AUDIT_STRICT") == "1"


def _load_gate():
    path = ROOT / ".agents" / "skills" / "sync-autosar-class" / "audit_stamped_classes.py"
    spec = importlib.util.spec_from_file_location("audit_stamped_classes", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _baseline() -> set:
    if not BASELINE.exists():
        return set()
    return {ln.strip() for ln in BASELINE.read_text(encoding="utf-8").splitlines() if ln.strip() and not ln.startswith("#")}


def _blocks(audit, text):
    """(class name, collect_block result) for every class carrying a checklist block."""
    import ast as _ast

    try:
        tree = _ast.parse(text)
    except SyntaxError:
        return
    for node in tree.body:
        if isinstance(node, _ast.ClassDef):
            blk = audit.collect_block(text.splitlines(), node.name)
            if blk:
                yield node.name, blk


@pytest.fixture(scope="module")
def failures():
    """{class: [failing messages]} for every stamped class that fails the audit."""
    gate = _load_gate()
    return gate.audit_stamped(gate.load_audit_class())


@pytest.fixture(scope="module")
def targets():
    gate = _load_gate()
    return gate.stamped_targets(gate.load_audit_class())


class TestStampedClassAuditGate:
    def test_gate_selects_stamped_classes_only(self, targets):
        """The gate must key off the provenance marker, nothing else.

        Derived rather than hard-coded: which classes are unstamped changes as sync
        work lands (a class loses its marker when it is re-opened for drift), so
        naming one here would make this test fail on a branch that has not had
        that sync applied yet.
        """
        names = {cls for cls, _path, _marker in targets}
        assert "ARList" in names, "a known stamped class must be selected"
        for _cls, _path, marker in targets:
            assert marker.startswith(("# Spec verified:", "# XSD verified:"))

        gate = _load_gate()
        audit = gate.load_audit_class()
        unstamped = None
        for path in sorted(gate.MODELS_DIR.rglob("*.py")):
            text = audit.read(path)
            for block_cls, blk in _blocks(audit, text):
                if not any(ln.startswith(("# Spec verified:", "# XSD verified:")) for ln in blk[2]):
                    unstamped = block_cls
                    break
            if unstamped:
                break
        assert unstamped is not None, "expected at least one checklist without a marker in the tree"
        assert unstamped not in names, f"{unstamped} carries no marker and must not be gated"

    def test_no_new_stamped_class_violations(self, failures):
        """A stamped class that fails the audit is a defect — unless it is known debt."""
        if STRICT:
            assert not failures, f"{len(failures)} stamped classes fail the mechanical audit (strict mode): " + ", ".join(sorted(failures)[:15])
            return
        new = sorted(set(failures) - _baseline())
        assert not new, (
            f"{len(new)} newly-stamped-or-regressed class(es) fail the mechanical audit. "
            f"Fix the class (checklist format / rows / base reader+writer call) or, if it is a "
            f"true false-positive of audit_class.py, record it as an accepted deviation. "
            f"Offenders: {', '.join(new)}"
        )

    @pytest.mark.skipif(STRICT, reason="baseline is not consulted in strict mode")
    def test_baseline_has_no_already_resolved_entries(self, failures):
        """Ratchet: once a class passes, it must leave the baseline.

        This is what makes the backlog shrink instead of becoming a permanent shield —
        a fix should cost one line of bookkeeping, not be invisible.
        """
        resolved = sorted(_baseline() - set(failures))
        assert not resolved, (
            f"{len(resolved)} baseline entries now pass the audit. Re-run "
            f"python .agents/skills/sync-autosar-class/audit_stamped_classes.py --write-baseline {BASELINE.relative_to(ROOT)} to shrink it. "
            f"Resolved: {', '.join(resolved[:15])}"
        )
