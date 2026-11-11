"""Project 1 research agent: PLAN, SEARCH, ANSWER as a LangGraph graph.

State flows through three nodes. The answer is built only from the
passages the search tool returned, and each point names its source.
Runs offline; falls back to a plain flow if langgraph is missing.
"""
from typing import TypedDict

from .search_tool import keywords, search


class ResearchState(TypedDict, total=False):
    question: str
    plan: list[str]
    passages: list[dict]
    answer: str


def plan_node(state: ResearchState) -> ResearchState:
    return {"plan": keywords(state["question"])}


def search_node(state: ResearchState) -> ResearchState:
    hits = search(state["question"])
    return {"passages": [{"source": h.source, "text": h.text} for h in hits]}


def answer_node(state: ResearchState) -> ResearchState:
    if not state["passages"]:
        return {"answer": "I found no source for that question in the document set."}
    lines = [f"Question: {state['question']}", ""]
    for p in state["passages"]:
        first = p["text"].split(". ")[0].strip()
        if not first.endswith("."):
            first += "."
        lines.append(f"- {first} [{p['source']}]")
    sources = sorted({p["source"] for p in state["passages"]})
    lines += ["", "Sources: " + ", ".join(sources)]
    return {"answer": "\n".join(lines)}


def run_research(question: str) -> ResearchState:
    """Run PLAN, SEARCH, ANSWER end to end and return the final state."""
    try:
        from langgraph.graph import StateGraph, END

        graph = StateGraph(ResearchState)
        graph.add_node("plan", plan_node)
        graph.add_node("search", search_node)
        graph.add_node("answer", answer_node)
        graph.set_entry_point("plan")
        graph.add_edge("plan", "search")
        graph.add_edge("search", "answer")
        graph.add_edge("answer", END)
        return graph.compile().invoke({"question": question})
    except ImportError:
        state: ResearchState = {"question": question}
        for node in (plan_node, search_node, answer_node):
            state.update(node(state))
        return state
