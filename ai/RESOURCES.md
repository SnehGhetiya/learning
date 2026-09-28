# AI Engineering Resources

All entries were checked on 2026-09-23. Re-verify versions and free-tier limits at lesson time, because they change often.

## Knowledge

### Python & tooling
- [The Python Tutorial (official, for Python 3.14.7)](https://docs.python.org/3/tutorial/index.html)
  The canonical introduction, written by the Python team. Use for: any core language feature (data structures, control flow, modules, classes, errors).
- [What's New in Python 3.14](https://docs.python.org/3/whatsnew/3.14.html)
  Use for: making sure lessons use current features. Python 3.15 is due October 2026; check [python.org/downloads](https://www.python.org/downloads/) and [endoflife.date/python](https://endoflife.date/python).
- [uv documentation (Astral)](https://docs.astral.sh/uv/)
  The current standard Python project and package manager (it replaces pip, venv and pyenv). Use for: project setup, dependencies, running scripts. Note: since uv 0.12, `uv init` creates a `src/` layout by default ([init docs](https://docs.astral.sh/uv/concepts/projects/init/)).

### Building LLM applications (core of the job)
- [Book: _AI Engineering_ by Chip Huyen (O'Reilly, 2025)](https://www.oreilly.com/library/view/ai-engineering/9781098166298/)
  The most-read book on O'Reilly in 2025. It explains how AI engineering differs from ML engineering and covers evals, RAG, agents and fine-tuning trade-offs. Use for: the "why" and system-design thinking. There's a free companion repo at [chiphuyen/aie-book](https://github.com/chiphuyen/aie-book).
- [Claude Academy (Anthropic, free)](https://academy.claude.com/)
  Free courses with certificates, including "Building with the Claude API", tool use and MCP. Use for: API patterns, tool use, agents, MCP. (A certificate is a nice resume line.)
- [Ollama](https://ollama.com/) and its [model library](https://ollama.com/library)
  Runs open models locally for free, with an OpenAI-compatible API. Use for: free, private LLM calls on this machine (30 GB RAM is enough for 7–8B quantized models).
- [Google AI Studio / Gemini API](https://ai.google.dev/gemini-api/docs)
  Has a free tier with no credit card. Limits change often (they were cut in Dec 2025), so check the [live rate-limit page](https://ai.google.dev/gemini-api/docs/rate-limits). Free-tier data may be used for training, so never send private data.
- [LangChain & LangGraph docs (v1.x)](https://docs.langchain.com/oss/python/langchain/agents)
  Both have reached 1.0 ([announcement](https://www.langchain.com/blog/langchain-langgraph-1dot0)), with no breaking changes until 2.0. Agents are now built with `create_agent`, which runs on LangGraph. The old `AgentExecutor`/`create_react_agent` tutorials are outdated. Use for: Module 4.

### Machine learning & deep learning
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
  Official docs for classic ML. Use for: regression, classification, train/test split and metrics.
- [fast.ai: Practical Deep Learning for Coders](https://course.fast.ai/)
  A free, top-down course by Jeremy Howard in which you build working models first and learn theory later. It fits a web developer and needs no special hardware. Use for: deep learning intuition and deploying models as web apps.
- [PyTorch Tutorials (official)](https://docs.pytorch.org/tutorials/)
  Use for: tensors, autograd and training loops.
- [Andrej Karpathy: Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html)
  Builds backprop, then MLPs, then a GPT from scratch, along with a tokenizer. Widely regarded as the best intuition-builder. Use for: the "train a small model" milestone.

### Fine-tuning
- [Hugging Face LLM Course (free)](https://huggingface.co/learn/llm-course/en/chapter1/1)
  Covers Transformers, Datasets, Tokenizers, the Hub, chat templates, SFT, LoRA and evaluation. It's developed in the open and was updated July 2026. Use for: the Hugging Face ecosystem and fine-tuning.
- [Unsloth notebooks](https://unsloth.ai/docs/get-started/unsloth-notebooks)
  Free Colab/Kaggle notebooks for LoRA fine-tuning. 4-bit quantization fits small models on the free T4 GPU. Use for: the fine-tuning milestone.

## Wisdom (Communities)
- [Python Discord](https://www.pythondiscord.com/)
  A large, well-moderated community with help channels. Use for: "why doesn't my Python work?" questions.
- [r/learnpython](https://www.reddit.com/r/learnpython/)
  Beginner-friendly. Use for: Python learning questions and code review.
- [Hugging Face Discord](https://hf.co/join/discord) and [HF Forums](https://discuss.huggingface.co/)
  Use for: fine-tuning, model and dataset questions, sharing your published models.
- [fast.ai forums](https://forums.fast.ai/)
  A long-running, high-signal community tied to the course. Use for: deep learning study groups.
- [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/)
  The main community for running and fine-tuning open models locally. Use for: Ollama and quantization questions, and "which model fits my RAM" advice.

## Gaps
- A high-trust, **current** source on hiring expectations for AI engineers (most "2026 roadmap" posts are SEO blogs). Candidates: real job postings (collect them during the course), Chip Huyen's book, and practitioner communities.
- A free, high-trust course on **evals** specifically. Search when we reach that phase.
