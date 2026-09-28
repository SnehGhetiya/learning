# Topic 3: conditionals and truthiness are solid; first encounter with false positives and false negatives

The learner scored 10/10 on Topic 3 and did all three stretch tasks in `practice/03_study_plan_v3.py`. They used truthiness (`if not name:`) for the default name. For the range check, they chose a separate `elif` with its own message instead of one chained comparison, which is a sensible design choice. For the "Maintenance Manager" bug, they switched the check to `.startswith("ai")`. That fixes the false positive, but it introduces a false negative ("Senior AI Engineer" is no longer detected) and still has a false positive ("Airline Pilot" matches). They also renamed the Topic 2 file as advised, so they act on feedback reliably.

**Evidence**: The script was tested with 9 inputs on 2026-09-24. The explanatory comment asked for in stretch 3 was left out.

**Implications**:
- Topic 4 motivation: `.split()` into words, then `"ai" in words`, fixes both errors. This is the first natural hook into the precision/recall idea used later for evals.
- Small style notes to reinforce gently: spaces around operators (PEP 8) and trailing whitespace.

**Update (same day)**: The learner revised the check to `" ai " in role or role.startswith("ai ") or role == "ai"` and added a clear bug-explanation comment. This fixes "Senior AI Engineer" and "Airline Pilot", but still misses a trailing "AI" ("Head of AI") and punctuation ("AI/ML Engineer"). They patch each case with another condition, so they haven't yet reached for a more general tool. Topic 4 uses this to motivate `.split()` and a whole-word `in`.
