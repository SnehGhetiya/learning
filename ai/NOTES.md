# Teaching Notes

## Learner preferences
- Wants **current versions and current changes**. Verify every tool, command and API against official docs before each lesson. Never teach from memory.
  - Example of why: uv ≥0.12 changed `uv init` to a `src/` layout. Most online tutorials still show `main.py`.
- **Structure: topics first, then a project, then move on** (LR-0002). Each module = topic lessons → one module project → next module. Never open a module with a project.
- Wants learning to lead to a resume-ready capstone.
- Coming from **web development**. JS/Node analogies help, but **never skip explaining the Python concept itself**. Complete beginner in Python/AI.
- One new tool at a time: plain `python3` scripts first, uv when packages are introduced (Module 1, Topic 10).
- **~10 h/week** (confirmed 2026-09-24, LR-0005) and free-only. Topics can be fuller (30–40 min) and richer in practice.

## Environment (checked 2026-09-23)
- Linux, zsh, Python 3.14.7 installed, Node installed, Homebrew (linuxbrew) available.
- `uv` not installed yet (it's introduced in Module 1, Topic 10). Editor: **Sublime Text** (`subl`). Also has **LM Studio** installed (useful for local models in Module 2, alongside or instead of Ollama).
- Practice files live in `~/Music/learning/ai/practice/NN_name.py`; module projects in `~/Music/learning/ai/projects/`.
- No NVIDIA GPU, 30 GB RAM, 8 cores → local Ollama with 7–8B quantized models is OK; use free Colab/Kaggle for training/fine-tuning.

## Course structure (tentative; rendered in `index.html`)
Modules, each = topic lessons → module project. About 6 months at ~10 h/week.
1. **Python basics**: 1 running Python & numbers ✅ done · 2 variables & strings ✅ done (8/8) · 3 booleans & if/else ✅ done (10/10) · 4 lists & loops (written 2026-09-24) · 5 dicts, tuples, sets · 6 functions · 7 built-ins & comprehensions · 8 errors & exceptions · 9 files & JSON · 10 modules, packages & uv · 11 classes & dataclasses · 12 type hints → **Project: `job-radar` CLI** (reuse `drafts/phase1-project-job-radar-draft.html`)
2. **Python for web & APIs**: HTTP with httpx · async/await · Pydantic · FastAPI → **Project: job-radar API**
3. **LLM fundamentals**: what LLMs are & tokens · first local call (Ollama/LM Studio) · first free API call · prompting · structured output · tool calling · embeddings · RAG · evals → **Project: skill extractor + Q&A over postings**
4. **LangChain & LangGraph** (v1.x: `create_agent`, middleware, LangGraph runtime; verify at lesson time) → **Project: agent version of job-radar**
5. **Classic ML**: NumPy · pandas · scikit-learn · metrics → **Project: seniority classifier**
6. **Deep learning**: PyTorch · training loops · tiny GPT (Karpathy) → **Project: train a small LM on free GPU**
7. **Fine-tuning**: HF ecosystem · LoRA with Unsloth · compare with RAG/prompting → **Project: fine-tuned model on the Hub**
8. **Capstone**: tentative AI job-search copilot (confirm near the end of Module 3).

## Glossary
Not created yet. Create `GLOSSARY.md` once the learner can *use* terms correctly (per the glossary rules), not before.
