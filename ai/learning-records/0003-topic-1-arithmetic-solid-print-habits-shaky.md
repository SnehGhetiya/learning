# Topic 1: arithmetic understood; output habits still forming

The learner completed Topic 1 and its stretch challenge (`practice/01_study_plan.py`). They correctly used `//` and `%` without help, for example `weeks % 4` for the leftover weeks, so the numeric operators are solid. Two gaps showed up. They computed `total_minutes` but never printed it, meaning "scripts only show what you print" hasn't fully stuck yet. They also put a trailing space inside a `print` label, not knowing that `print` adds separators itself. They also misread "minutes per week" as total minutes, so exercise wording should be precise.

**Evidence**: `practice/01_study_plan.py` on 2026-09-24. Its output is `Weeks to finish:  18.0` (double space), and `total_minutes` is unused.

**Implications**: Topic 2 opens with feedback on both points and uses f-strings as the fix. Keep revisiting "print what you want to see" in the Topic 3 warm-up. The script sets `hours_per_week = 10`, while MISSION.md says under 5 h/week. Ask whether their time budget has changed.
