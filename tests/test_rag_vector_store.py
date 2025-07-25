from finsight.rag.vector_store import VectorStore


def test_search_ranks_relevant_first():
    vs = VectorStore()
    vs.add([
        "revenue grew driven by services and wearables",
        "the board declared a quarterly dividend",
        "supply chain risk in the greater china region",
    ])
    hits = vs.search("china supply chain risk", k=1)
    assert hits
    assert "china" in hits[0][0]


def test_empty_store():
    assert VectorStore().search("x") == []
