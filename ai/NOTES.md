# Teaching Notes

## Learner preferences
- Wants **current versions and current changes**. Verify every tool, command and API against official docs before each lesson. Never teach from memory.
  - Example of why: uv ≥0.12 changed `uv init` to a `src/` layout. Most online tutorials still show `main.py`.
- **Structure: topics first, then a project, then move on** (LR-0002). Each module = topic lessons → one module project → next module. Never open a module with a project.
- Wants learning to lead to a resume-ready capstone.
- Coming from **web development**. JS/Node analogies help, but **never skip explaining the Python concept itself**. Complete beginner in Python/AI.
- One new tool at a time: plain `python3` scripts first, uv when packages are introduced (Module 1, Topic 10).
- **~5–6 h/week, ~5 months** (2026-10-12, LR-0010) and free-only. A friend pushed for speed, so don't linger on Python.
- **Wants to learn from books + AI + projects together** (LR-0010). Each ~2.5 h session = **read** (book section, 30–40 min) → **learn with Claude** (lesson + quiz + questions, ~40 min) → **build** (60–70 min). Every lesson names its reading and must still stand alone if it was skipped.
  - 📖 *Fluent Python* 2nd ed.: `~/Downloads/fluent-python-2nd.pdf`. **Selected sections only** (preface: hard for beginners). Tested on 3.10, so flag 3.11–3.14 differences. Cite by section name + PDF page.
  - 📗 Raschka, *Build a LLM (From Scratch)*: `~/Downloads/build-large-language-model-scratch.pdf`. **Read in order**; needs solid Python; runs on a laptop. Code is at github.com/rasbt/LLMs-from-scratch; solutions in appendix C. Cite by § number.
  - Reading the PDFs: no poppler; `pypdf` is installed for `/Library/Developer/CommandLineTools/usr/bin/python3` (add `site.getusersitepackages()` to `sys.path` when run with `-I`).

## Environment (checked 2026-09-23)
- Now on macOS (Darwin), zsh, Python 3.14.7 installed (was Linux at first), Node installed, Homebrew (linuxbrew) available.
- `uv` not installed yet (it's introduced in Module 1, Topic 10). Editor: **Sublime Text** (`subl`) at first, now **Zed** (with a linter, likely ruff; seen 2026-10-06). Also has **LM Studio** installed (useful for local models in Module 2, alongside or instead of Ollama).
- Practice files live in `~/Documents/learning/ai/practice/NN_name.py`; module projects in `~/Documents/learning/ai/projects/`.
- No NVIDIA GPU, 30 GB RAM, 8 cores → local Ollama with 7–8B quantized models is OK; use free Colab/Kaggle for training/fine-tuning.

## Course structure (fast track + books, rendered in `index.html`, which holds the exact reading per session)
About 46 sessions (~2.5 h, 2 a week). Sessions per module are in brackets.
1. **Finish Python** [3]: Topics 1–6 ✅ · S1 built-ins/comprehensions/errors (FP ch. 2 listcomps) · S2 files/JSON + uv (FP ch. 4 text files) · S3 small `job-radar` CLI (reuse `drafts/phase1-project-job-radar-draft.html`)
2. **Web & APIs** [4]: classes/dataclasses (FP ch. 1, 5) · type hints + Pydantic (FP ch. 8) · httpx + async (FP ch. 21) · FastAPI (FP ch. 9 decorators). No separate project.
3. **LLM fundamentals** [11]: Raschka ch. 1 + §2.1–2.5 · local + free API call · prompting/structured output · streaming (FP ch. 17) · tool calling · embeddings · RAG · evals ×2 → **Project**: FastAPI skill extractor + Q&A with an eval report
4. **LangChain & LangGraph** [4] (v1.x, `create_agent`; verify at lesson time) → agent added to the Module 3 service
5. **Capstone** [8], protected, ships ~end of Jan 2027: AI job-search copilot (confirm at the end of Module 3)
6. **Raschka in order** [13]: appendix A · §2.6–2.8 · ch. 3 ×2 · ch. 4 ×2 · ch. 5 ×2 · ch. 6 ×2 · ch. 7 ×2 · appendix E + HF publish → `my-gpt` repo
Buffer [3]: scikit-learn or appendix D if unused.
Cut order: buffer → FP becomes skim → Module 4 → Raschka ch. 7. Never cut evals or the capstone.

## Glossary
Not created yet. Create `GLOSSARY.md` once the learner can *use* terms correctly (per the glossary rules), not before.
