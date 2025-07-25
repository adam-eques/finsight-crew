"""A tool that answers questions grounded in supplied filing text."""

from __future__ import annotations

from typing import Type

from pydantic import BaseModel, Field

from finsight.rag.retriever import FilingRetriever


class RagInput(BaseModel):
    document: str = Field(..., description="Raw filing / long-form text")
    question: str = Field(..., description="Question to answer from the text")
    k: int = Field(4, ge=1, le=10)


def make_filings_rag_tool():
    from crewai.tools import BaseTool

    class FilingsRagTool(BaseTool):
        name: str = "filings_rag"
        description: str = (
            "Retrieve the most relevant passages from a filing to ground an answer."
        )
        args_schema: Type[BaseModel] = RagInput

        def _run(self, document: str, question: str, k: int = 4) -> str:
            retriever = FilingRetriever()
            retriever.index(document)
            return retriever.context_for(question, k=k)

    return FilingsRagTool()
