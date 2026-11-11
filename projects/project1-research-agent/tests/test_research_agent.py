import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from research_agent.agent import run_research
from research_agent.search_tool import keywords, search


def test_keywords_drop_stopwords():
    assert keywords("What is an agent?") == ["agent"]


def test_search_finds_rag_doc():
    hits = search("What is RAG and why does it matter?")
    assert hits and hits[0].source == "rag-explained"


def test_answer_cites_sources():
    state = run_research("What is MCP?")
    assert "[mcp-explained]" in state["answer"]
    assert "Sources:" in state["answer"]
