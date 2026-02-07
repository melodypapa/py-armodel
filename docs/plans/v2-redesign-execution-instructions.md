# V2 Redesign Execution Instructions

**For Parallel Session Execution**

## Quick Start

1. **Open a new session** in your worktree (if using git worktrees) or in the current directory

2. **Load the executing-plans skill** at the start:
   ```
   /skill superpowers:executing-plans
   ```

3. **Tell the new session**:
   ```
   I want to execute the implementation plan at docs/plans/2026-02-07-v2-redesign-implementation-plan.md

   Start with Phase 1, Task 1.

   Follow the plan exactly - each step has complete code, commands, and expected outputs.

   Commit after each task as specified in the plan.
   ```

## Plan Location

**Implementation Plan:** `docs/plans/2026-02-07-v2-redesign-implementation-plan.md`
**Design Document:** `docs/plans/2026-02-07-v2-redesign-easier-to-use.md`
**Coding Rules:** `docs/development/coding_rules_v2.md` (CODING_RULE_V2_00016-00019)

## Quality Gates

After each phase, verify:
- ✅ All tests pass: `pytest tests/test_armodel/v2/models/ -v`
- ✅ No new ruff errors: `ruff check src/armodel/v2/models/`
- ✅ MyPy errors not increased: `mypy src/armodel/v2/models/ 2>&1 | wc -l`
- ✅ Commit after each task

## Checkpoints

**After Phase 1 (Task 6):** ARObject core infrastructure complete
**After Phase 2 (Task 10):** Referrable class complete
**After Phase 3 (Task 13):** Identifiable class complete
**After Phase 4 (Task 17):** ApplicationSwComponentType complete
**After Phase 5 (Task 20):** Quality gates and documentation complete

## Troubleshooting

If tests fail:
1. Check the error message carefully
2. Verify code matches plan exactly
3. Run with -vv for more details: `pytest <test_file> -vv`
4. Check file paths are correct

If mypy errors increase:
1. Check type hints are correct
2. Verify string annotations used for forward refs
3. No TYPE_CHECKING blocks needed (use string annotations instead)

If ruff errors increase:
1. Check line length (79 characters)
2. Verify import style (block imports)
3. Check naming conventions

## Progress Tracking

Update this file as you complete phases:

- [ ] Phase 1: ARObject (Tasks 1-6)
- [ ] Phase 2: Referrable (Tasks 7-10)
- [ ] Phase 3: Identifiable (Tasks 11-13)
- [ ] Phase 4: ApplicationSwComponentType (Tasks 14-17)
- [ ] Phase 5: Quality Gates (Tasks 18-20)

## Expected Outcomes

**After completing all phases:**
- ✅ ~35 new tests, all passing
- ✅ MyPy errors < 4,000
- ✅ Ruff errors ≤ 18
- ✅ 100% backward compatible
- ✅ Core infrastructure enhanced
- ✅ Pattern established for remaining classes

## Completion

When all tasks complete, return to original session with:
- Summary of completed work
- Test results
- Quality metrics
- Any issues encountered

---

**Ready to start! Open new session and use:**
```
/skill superpowers:executing-plans
```

**Then reference this plan:**
```
docs/plans/2026-02-07-v2-redesign-implementation-plan.md
```
