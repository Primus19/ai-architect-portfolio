"""CLI: python -m src.hello_agent "What is 19 plus 23?" """
import sys

from .agent import run_agent


def main() -> None:
    question = " ".join(sys.argv[1:]) or "What is 19 plus 23?"
    state = run_agent(question)
    print(f"Question: {question}")
    print(f"Tool result: {state['tool_result']:g}")
    print(f"Answer: {state['answer']}")


if __name__ == "__main__":
    main()
