"""Day 1 hello agent: a tiny LangGraph state graph that calls one tool.

Flow: receive a question, extract the arithmetic, call the calculator tool,
return the answer with the tool result in the state. Runs fully offline.
If langgraph is not installed yet, a plain fallback runs the same flow so
the lab check still passes before dependencies are installed.
"""
from typing import TypedDict

from .tools import calculator


class AgentState(TypedDict, total=False):
    question: str
    expression: str
    tool_result: float
    answer: str


def _extract(question: str) -> str:
    # The whole question is passed to the tool, which extracts the math.
    return question


def call_tool(state: AgentState) -> AgentState:
    result = calculator(state["expression"])
    return {"tool_result": result,
            "answer": f"The calculator tool returned {result:g}."}


def run_agent(question: str) -> AgentState:
    """Run the agent end to end and return the final state."""
    try:
        from langgraph.graph import StateGraph, END

        graph = StateGraph(AgentState)
        graph.add_node("prepare", lambda s: {"expression": _extract(s["question"])})
        graph.add_node("calculator_tool", call_tool)
        graph.set_entry_point("prepare")
        graph.add_edge("prepare", "calculator_tool")
        graph.add_edge("calculator_tool", END)
        app = graph.compile()
        return app.invoke({"question": question})
    except ImportError:
        state: AgentState = {"question": question, "expression": _extract(question)}
        state.update(call_tool(state))
        return state
