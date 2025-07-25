"""Glue: chunk a document, index it, and retrieve context for a query."""

from __future__ import annotations

from typing import List

from finsight.rag.chunking import chunk_text
from finsight.rag.vector_store import VectorStore


class FilingRetriever:
    def __init__(self, chunk_size: int = 800, overlap: int = 120):
        self.store = VectorStore()
        self.chunk_size = chunk_size
        self.overlap = overlap

    def index(self, text: str) -> int:
        chunks = chunk_text(text, self.chunk_size, self.overlap)
        self.store.add(chunks)
        return len(chunks)

    def context_for(self, question: str, k: int = 4) -> str:
        hits = self.store.search(question, k=k)
        return "\n---\n".join(doc for doc, _ in hits)
