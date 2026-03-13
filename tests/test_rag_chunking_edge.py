from finsight.rag.chunking import chunk_text


def test_single_word():
    assert chunk_text("hello", size=10, overlap=2) == ["hello"]
