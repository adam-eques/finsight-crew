import pytest

from finsight.rag.chunking import chunk_text


def test_empty():
    assert chunk_text("") == []


def test_chunk_counts():
    text = " ".join(str(i) for i in range(1000))
    chunks = chunk_text(text, size=100, overlap=20)
    assert len(chunks) > 1
    assert all(len(c.split()) <= 100 for c in chunks)


def test_overlap_guard():
    with pytest.raises(ValueError):
        chunk_text("a b c", size=10, overlap=10)
