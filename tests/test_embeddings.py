from finsight.rag.embeddings import HashingEmbedder
from finsight.rag.vector_store import is_normalised


def test_unit_vectors():
    vec = HashingEmbedder(dim=64).embed(["apple services growth"])[0]
    assert is_normalised(vec)
