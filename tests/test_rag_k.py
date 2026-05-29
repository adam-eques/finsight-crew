from finsight.rag.vector_store import VectorStore


def test_k_exceeds_docs():
    vs = VectorStore()
    vs.add(["one doc only"])
    assert len(vs.search("one", k=5)) == 1
