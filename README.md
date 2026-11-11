# AI Architect Portfolio

Portfolio home for the AI Architect and Agentic Engineer mastery program.
Owner: Primus Vekuh, PhD. Program start: 2026-11-07. Target: 12 production projects in 24 weeks.

## Day 1: Baseline and Lab Setup (this scaffold)

What is here:
- A LangGraph hello agent that calls one tool and runs offline with no API key
- `.env.example` with variable names only, no real keys
- A cost cap note: $50 per month soft cap for API spend, reviewed weekly
- Tests for the tool, and a checklist to close Day 1

New here? Read [ROADMAP.md](ROADMAP.md) first: the whole program in plain English.

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m src.hello_agent "What is 19 plus 23?"
pytest -q
```

Expected output: the agent calls the `calculator` tool and answers 42.

No API key is needed for this demo. The agent is deterministic by design so
Day 1 proves the lab works before any paid model call is made.
To use a live model later, copy `.env.example` to `.env`, add your own key
locally, and never commit `.env`.

## Cost cap

Soft cap: $50 per month across all model APIs for Phases 0 to 2.
Rules: prefer free tiers and small models for drills, log spend weekly in
`docs/cost-log.md`, stop and review if a single project passes $10.

## Project map

1. LangGraph Research Agent with citations and human approval
2. MCP Tool Server plus MCP client agent
3. Customer Support Triage Agent
4. Enterprise Advanced RAG with RAGAS evaluation
5. Agentic RAG and Text2SQL Analyst Agent
6. CrewAI Multi-Agent Research Crew
7. Engineering Team: planner, coder, reviewer, tester
8. Workflow Automation Agent
9. Bedrock AgentCore Production Agent
10. Azure Foundry Agent
11. Secure Enterprise Agent Platform
12. Capstone: a monetizable agent product

Each project gets its own folder under `projects/`, an architecture diagram,
an eval report, a cost report and a 2 to 4 minute demo note.

## Layout

```
src/hello_agent/   Day 1 agent: graph, tool, CLI entry point
tests/             Tool and graph tests
docs/              Day 1 checklist and cost log
projects/          One folder per portfolio project (added as you build)
```
