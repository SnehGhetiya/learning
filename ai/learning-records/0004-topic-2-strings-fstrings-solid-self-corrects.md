# Topic 2: strings, f-strings and input conversion are solid; acts on feedback

The learner scored 8/8 on Topic 2 (including the two Topic 1 warm-up questions) and finished all three stretch tasks in `practice/02_study_plan._v2.py`. They chained `.strip().upper()` on a second `input()` of their own, converted with `float(input(...))`, formatted with `:.0f`/`:.1f`, and used `"=" * 30` for dividers. Without being asked, they also went back and fixed `01_study_plan.py` using the Topic 1 feedback (removed the double space and now print the minutes value). So "scripts only show what you print" from LR-0003 has now stuck.

**Evidence**: Both scripts were run on 2026-09-24 and their output is correct (for example, 45.0 % 4 gives "Leftover weeks: 1").

**Implications**:
- Topic-sized lessons at this depth work well. Keep the format, and consider slightly richer stretch challenges.
- The filename contains a stray dot (`02_study_plan._v2.py`). Point out file naming now, because dots in names will break `import` in Topic 10 (modules).
- Still unanswered: `hours_per_week = 10` in their script vs "<5 h/week" in MISSION.md. Ask again before changing the pace.
