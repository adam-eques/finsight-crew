"""Split long documents into overlapping, word-bounded chunks."""

from __future__ import annotations

from typing import List


def chunk_text(text: str, size: int = 800, overlap: int = 120) -> List[str]:
    if size <= 0:
        raise ValueError("size must be positive")
    if overlap >= size:
        raise ValueError("overlap must be smaller than size")
    words = text.split()
    if not words:
        return []
    chunks = []
    start = 0
    step_size = size - overlap
    while start < len(words):
        chunk = words[start:start + size]
        chunks.append(" ".join(chunk))
        start += step_size
    return chunks
