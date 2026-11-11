# Project 1: Research Agent

## What this is, in plain words
A small program that answers a question by first searching a set of
documents, then writing an answer that names its sources.
That is the core of every research agent: do not answer from memory,
find evidence first, then answer and show where the evidence came from.

## How it works (3 steps)
1. PLAN: the agent pulls the key words out of your question.
2. SEARCH: a tool searches the documents in `docs/` and returns the
   best matching passages, each tagged with its source file.
3. ANSWER: the agent writes a short answer built only from those
   passages, with the source named after each point, like [rag-explained].

## Run it
From this folder:
```bash
python -m research_agent "What is RAG and why does it matter?"
python -m research_agent "What is an agent?"
pytest tests -q
```
No API key and no cost: this version searches local documents so the
pattern is visible end to end. Later steps swap the local search for
live web search and a real model, the shape stays the same.

## Today's task (Primus)
1. Run the two questions above and read the answers.
2. Add ONE document of your own: a new file in `docs/`, 5 to 10 lines,
   on any topic you know well (for example, cloud migration steps).
3. Ask the agent a question your new document answers.
4. Check the answer names your document as its source.
That check is the whole lesson: an agent is only trustworthy when you
can see where its answer came from.
