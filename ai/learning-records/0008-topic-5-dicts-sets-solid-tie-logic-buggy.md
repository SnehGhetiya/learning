# Topic 5: dicts, sets and tuples are solid; the tie stretch has a logic bug

The learner scored 8/10 on Topic 5. `practice/05_study_plan_v5.py` uses a list of dicts, `progress.get(..., "not started")`, a `(name, hours)` tuple as "best so far", tuple unpacking and `ai_keywords & set(words)` correctly.

**Stretch tasks** (tested 2026-10-02):
- Skill levels: done. `my_skills` is a dict, loop with `.items()` prints skills below 3. Small issues: typo "pracitce", printed after the closing `====` line.
- Word counter: done exactly right with `counts.get(word, 0) + 1`.
- Ties: not done as asked. Instead of a second loop that collects every module with `longest_hours` into a list, they added a `longest_2` tuple updated in the same loop. Because `longest_1` updates first, `longest_2` copies it, and the output is "LLM fundamentals and LLM fundamentals". The tie line also always prints, even with no tie.

**Regression**: Turning `my_skills` into a dict broke the AI-skills block. "Skills you have" now prints *all* skills (including "sql") instead of `ai_skills & set(my_skills)`, and "Skills to learn" is commented out. The lesson's hint (`set(my_skills)`) was not used.

**Implications**:
- Same pattern as LR-0007: the main part of a change is done, the follow-on part is dropped. Review the knock-on effects of a change explicitly.
- They didn't run the output against the expected result (the duplicate name is visible on screen). Encourage "run and read the output" as a habit.
- The "collect all matches into a list" pattern (loop + `if` + `.append()`) needs another rep: reuse it in Topic 6 (a function that returns a list).
- Uses nested same-type quotes in f-strings (`{" and ".join(...)}`), which works on 3.14 but the lesson recommends mixing quotes.

**Update (same day)**: At the learner's request, Claude fixed the tie logic (second loop + `.append()` into `tied`, printed only if `len(tied) > 1`), restored the AI-skills lines with `set(my_skills)`, fixed the typo, moved the practise loop inside the `====` lines, and switched to mixed f-string quotes. The learner didn't write these, so give them a fresh "collect all matches" task in Topic 6's warm-up.
