from src.hello_agent.agent import run_agent
from src.hello_agent.tools import calculator


def test_calculator_words():
    assert calculator("19 plus 23") == 42


def test_calculator_symbols():
    assert calculator("7 * 6") == 42


def test_agent_calls_tool():
    state = run_agent("What is 19 plus 23?")
    assert state["tool_result"] == 42
    assert "42" in state["answer"]
