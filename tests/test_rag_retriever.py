from finsight.rag.retriever import FilingRetriever


def test_index_and_retrieve():
    r = FilingRetriever(chunk_size=8, overlap=2)
    n = r.index(
        "Apple reported record services revenue. "
        "Risks include foreign exchange exposure and regulatory scrutiny "
        "in the european union over the app store."
    )
    assert n >= 1
    ctx = r.context_for("what regulatory risk in europe?", k=1)
    assert "european" in ctx or "regulatory" in ctx
