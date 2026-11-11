"""CLI: python -m research_agent "What is RAG and why does it matter?" """
import sys

from .agent import run_research


def main() -> None:
    question = " ".join(sys.argv[1:]) or "What is RAG and why does it matter?"
    state = run_research(question)
    print(state["answer"])


if __name__ == "__main__":
    main()
