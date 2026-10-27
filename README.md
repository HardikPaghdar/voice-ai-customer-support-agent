# Voice AI Customer Support Agent

A support-agent backend accepting speech transcripts, matching a small FAQ set, and escalating potentially sensitive account/security issues. This is the conversation core; speech recognition and synthesis are not bundled yet.

## Features
- Transcript endpoint with conversation ID passthrough
- FAQ matching baseline
- Escalation rules for sensitive issues
- Safe fallback when intent is unclear
- API docs, tests, and CI

## Run
```bash
pip install -r requirements.txt
uvicorn app:app --reload
```
Docs: http://127.0.0.1:8000/docs.

## Limitations / next steps
This version does not capture audio, perform speech-to-text, or synthesize speech. FAQ matching is simple token overlap, not an LLM. Add local STT/TTS adapters, consent-aware audio handling, and a human handoff integration as separate modules.

## Stack
Python, FastAPI, Pydantic, pytest. Core demo requires no paid API.

## Explore more

- [AI Customer Support Assistant](https://github.com/HardikPaghdar/ai-customer-support-assistant) — FAQ-based message triage.
- [RAG Knowledge Base Assistant](https://github.com/HardikPaghdar/rag-knowledge-base-assistant) — document Q&A with references.
- [AI Agent Workflow Automation](https://github.com/HardikPaghdar/ai-agent-workflow-automation) — approved tool-call workflows.
- [More projects on my portfolio](https://hardikpaghdar.netlify.app/).
