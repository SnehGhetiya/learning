# Topic 4: lists, loops and while/break are solid; stretch tasks partly finished

The learner scored 10/10 on Topic 4. `practice/04_study_plan_v4.py` builds the full study plan and correctly uses `for` over a list, `range(len(...))` indexing, a `while True`/`break` input check, `.append()`, `", ".join(...)` and `.split()` for whole-word matching. The whole-word AI check now handles "Head of AI", "AI/ML Engineer" and "AI-Engineer" and rejects "Maintenance Manager". This replaces the case-by-case patching from Topic 3, so the general tool landed.

**Stretch tasks** (tested 2026-09-28 with 6 roles):
- Punctuation: done with chained `.replace()` before `.split()`. The second part (`ml` and `llm` as keywords) was skipped, so "ML Engineer" and "LLM Engineer" are not detected.
- Longest module: finds the largest hours (45) with a "best so far" loop, but doesn't track which module it belongs to, so the name isn't printed. It's also printed after the closing `====` line.
- Collect skills: done. Skills aren't `.strip()`ped (a line of spaces gets added), and when no skills are entered it prints an empty "My skills:" line.

**Evidence**: One loop body is indented 2 spaces while the rest use 4. It works, but it doesn't follow PEP 8.

**Implications**:
- They tend to do the main part of a stretch task and drop the second half, so give review feedback on the missing parts in small pieces.
- Topic 5: tracking "best so far" as two variables (hours + name) sets up tuples and dicts well (`{"name": ..., "hours": ...}`). Topic 7's `enumerate`/`zip`/`max(key=...)` will make these patterns shorter.
- Keep reinforcing 4-space indentation.

**Update (same day)**: At the learner's request, Claude completed the three stretch fixes in `practice/04_study_plan_v4.py` (keyword list + loop with `break`, longest module name and hours, `.strip()` on skills and hiding an empty skills line). The learner didn't write these themselves, so check the "best so far" and keyword-loop patterns again in Topic 5's warm-up and stretch tasks.
