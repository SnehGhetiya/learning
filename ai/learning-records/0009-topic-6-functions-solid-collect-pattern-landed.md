# Topic 6: functions are solid; the "collect all matches" pattern landed on its own

The learner scored 9/10 on Topic 6. `practice/06_study_plan_v6.py` turns the study plan into functions with `def`, `return`, default parameters, a keyword argument (`limit=5`) and tuple unpacking (`total, top_hours = summarise(modules)`). Tested 2026-10-06 with Head of AI, 100 → 10 hours, Python 7 → 2, RAG 4. The output matches the lesson, including `Longest: LLM fundamentals and Capstone (45 h)`.

**Main task**: `modules_with_hours` uses loop + `if` + `.append()`, and `return` comes after the loop. This is the pattern Claude had to fix for them in LR-0008, and this time they wrote it without help.

**Stretch tasks**:
- `ask_number(prompt, low, high)`: done, and **both parts** were done (hours 1–80 and each skill level 1–5, wrapped in `int(...)`). This is the first time a two-part stretch was finished in full (compare LR-0007 and LR-0008). Small issues: named `ask_numebr` (typo, used consistently so it runs), no docstring, and the old `ask_hours` wasn't deleted.
- `skills_below(skills, limit=3)`: correct. Only called once (`limit=5`); the default call with `limit=3` is missing, and the label "Skills below limit" doesn't say which limit. There's a stray `;` after `[]` (JS habit).
- `count_words(text)`: correct and uses no outside variables. Called on one posting, not two.

**Style**: Indentation is mixed (2, 3 and 4 spaces across functions). There's a nested same-type quote in an f-string again (`{", ".join(...)}`). There's a `# noqa: PLR1730` comment, so a linter (likely ruff in Zed) is running. PLR1730 suggests `max()`, which Topic 7 covers.

**Implications**:
- "Drops the second half" is getting better: ask_number was finished in full, but two "call it again" parts (limit=3, second posting) were still skipped. Keep pointing these out briefly.
- Indentation needs a tooling fix, not more reminders: set up format-on-save (ruff format) in Zed.
- Topic 7: rewrite `summarise` with `sum()`/`max()` and `modules_with_hours` as a list comprehension. This connects to the PLR1730 hint.
- Topic 8: `float(input())` still crashes on "abc". Use `ask_number` as the motivating example for `try`/`except ValueError`.

**Update (same day)**: At the learner's request, Claude fixed the review issues in `practice/06_study_plan_v6.py`. The learner's original code is kept above each fix in `# YOUR VERSION` comments so they can compare. The fixes: 4-space indentation everywhere, `ask_numebr` renamed to `ask_number` with a docstring, `ask_hours` commented out, the `;` removed, `skills_below` called with both the default and `limit=5` with labelled output, and `count_words` run on two postings. The learner didn't write these, so check indentation and the "call it twice" parts again in Topic 7.
