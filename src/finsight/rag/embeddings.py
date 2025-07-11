"""Embeddings abstraction.

A real deployment plugs in a provider embedder; for offline tests and
cheap local runs we ship a deterministic hashing embedder so the rest of
the pipeline is exercisable without network access.
"""

from __future__ import annotations

import hashlib
import math
from typing import List, Protocol


class Embedder(Protocol):
    def embed(self, texts: List[str]) -> List[List[float]]:
        ...


class HashingEmbedder:
    """Deterministic bag-of-hashes embedder. Not semantic, but stable and
    dependency-free — useful for tests and offline smoke runs."""

    def __init__(self, dim: int = 256):
        self.dim = dim

    def embed(self, texts: List[str]) -> List[List[float]]:
        return [self._one(t) for t in texts]

    def _one(self, text: str) -> List[float]:
        vec = [0.0] * self.dim
        for token in text.lower().split():
            h = int(hashlib.md5(token.encode()).hexdigest(), 16)
            vec[h % self.dim] += 1.0
        norm = math.sqrt(sum(v * v for v in vec)) or 1.0
        return [v / norm for v in vec]
