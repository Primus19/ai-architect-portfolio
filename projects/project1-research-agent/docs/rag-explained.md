# RAG explained
RAG stands for retrieval augmented generation. Instead of answering
from memory, the system first retrieves relevant passages from a set
of documents, then writes an answer grounded in those passages.
RAG matters because company knowledge lives in documents the model
never saw in training, and because grounded answers can cite sources
and are far less likely to invent facts.
A basic RAG system has three parts: a document store, a search step
that finds the right passages, and a writing step that answers using
only those passages.
