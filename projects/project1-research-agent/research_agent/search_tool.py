"""The search tool: keyword search over the local document set.

Scores each passage by how many of the question's key words it contains.
Deliberately simple and transparent: this is the tool the agent calls,
and later steps swap it for vector search and live web search.
"""
import re
from dataclasses import dataclass
from pathlib import Path

DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"
STOP = {"what", "is", "a", "an", "the", "and", "why", "does", "it",
        "how", "do", "of", "to", "in", "for", "on", "are", "can"}


@dataclass
class Passage:
    source: str
    text: str
    score: int


def keywords(question: str) -> list[str]:
    words = re.findall(r"[a-z0-9]+", question.lower())
    return [w for w in words if w not in STOP and len(w) > 2]


def load_passages(docs_dir: Path = DOCS_DIR) -> list[Passage]:
    passages = []
    for path in sorted(docs_dir.glob("*.md")):
        body = path.read_text()
        body = re.sub(r"^#.*$", "", body, flags=re.M)  # drop headings
        for chunk in body.split("\n\n"):
            chunk = " ".join(chunk.split())
            if len(chunk) > 40:
                passages.append(Passage(source=path.stem, text=chunk, score=0))
    return passages


def search(question: str, top_k: int = 3, docs_dir: Path = DOCS_DIR) -> list[Passage]:
    keys = keywords(question)
    hits = []
    for p in load_passages(docs_dir):
        text = p.text.lower()
        score = sum(len(re.findall(rf"\b{re.escape(k)}\b", text)) for k in keys)
        # bonus when a key word appears in the source name itself
        score += 3 * sum(1 for k in keys if k in p.source.replace("-", " "))
        if score > 0:
            hits.append(Passage(source=p.source, text=p.text, score=score))
    hits.sort(key=lambda h: (-h.score, h.source))
    return hits[:top_k]
