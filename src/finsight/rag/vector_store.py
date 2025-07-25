"""A tiny cosine-similarity vector store.

Kept intentionally small and dependency-free; chromadb is used in the
packaged tool path, but this store keeps unit tests fast and hermetic.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Tuple

from finsight.rag.embeddings import Embedder, HashingEmbedder


def cosine(a: List[float], b: List[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    return dot  # inputs are pre-normalised


@dataclass
class VectorStore:
    embedder: Embedder = field(default_factory=HashingEmbedder)
    _docs: List[str] = field(default_factory=list)
    _vecs: List[List[float]] = field(default_factory=list)

    def add(self, docs: List[str]) -> None:
        vecs = self.embedder.embed(docs)
        self._docs.extend(docs)
        self._vecs.extend(vecs)

    def search(self, query: str, k: int = 4) -> List[Tuple[str, float]]:
        if not self._docs:
            return []
        qv = self.embedder.embed([query])[0]
        scored = [(doc, cosine(qv, v)) for doc, v in zip(self._docs, self._vecs)]
        scored.sort(key=lambda p: p[1], reverse=True)
        return scored[:k]
