Status: active. This is **the** plan record. It replaces the old 10 h/week plan (LR-0005, deleted 2026-10-12; it's in git history).
---

# Current plan: 5–6 h/week for about 5 months, learning from books + Claude + projects

`index.html` holds the session-by-session plan with exact readings. This record explains **why** the plan looks the way it does.

## Decisions (all 2026-10-12, made by the learner)

| Question | Answer |
|---|---|
| Weekly time | **5–6 h, steady** (down from 10 h). A friend advised against spending a month on Python alone. |
| Remaining Python | **Merge and learn on demand**: topics 7–12 become 3 sessions; classes/type hints are taught when Pydantic needs them. |
| Learning sources | **Books + Claude + projects together.** |
| Raschka book vs. timeline | **Extend to ~5 months** and read it in full (other options were replacing the depth module or reading lightly in parallel). |

## The shape

- **Budget**: ~46 sessions of ~2.5 h, 2 a week, finishing **mid-to-late March 2027**.
- **Every session**: **read** (book section, 30–40 min) → **learn with Claude** (lesson, quiz, questions, ~40 min) → **build** (60–70 min).
- **Modules** (sessions): 1 Finish Python (3) · 2 Web & APIs (4, no separate project) · 3 LLM fundamentals (11, with the FastAPI skill-extractor project and evals) · 4 LangChain/LangGraph (4) · 5 **Capstone** (8, ships ~end of January 2027, protected) · 6 **Raschka in order** (13, `my-gpt` repo, LoRA, publish to HF) · buffer (3).
- **Cut order if behind**: buffer → Fluent Python readings become skims → shrink Module 4 → drop Raschka ch. 7. **Never cut evals or the capstone.**
- The "topics first, then a project" rule (LR-0002) still holds; projects are just smaller.

## Why the books are used the way they are (from their own prefaces, read 2026-10-12)

- 📖 ***Fluent Python*, 2nd ed.** (`~/Downloads/fluent-python-2nd.pdf`, 1,011 pages): "If you are just learning Python, this book is going to be hard to follow." After ch. 1, any part can be read in any order. So it's read **selectively (~100 pages)**, each section paired with what's being built (comprehensions, data model, dataclasses, type hints, async/HTTPX, decorators, generators). It was tested on Python 3.10, so lessons flag 3.11–3.14 changes.
- 📗 **Raschka, *Build a Large Language Model (From Scratch)*** (`~/Downloads/build-large-language-model-scratch.pdf`, 370 pages): "designed to be read sequentially", needs "a strong foundation in Python", and runs "on a regular laptop". So ch. 1 + §2.1–2.5 go in Module 3 (tokens/embeddings), and the rest waits until after the capstone, read in order. Code: github.com/rasbt/LLMs-from-scratch. Solutions: appendix C.

## Implications for lessons

- Each lesson names its reading (FP by section name + PDF page; Raschka by § number) and **still stands alone** if the reading was skipped.
- Quizzes may check the reading. When book code conflicts with current docs, teach the current way and explain the difference.
- Plan in sessions, not weeks. A missed week means following the cut order, not redoing the plan.
- Revisit this record if the time budget, deadline or hiring timeline changes.
