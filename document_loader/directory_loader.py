from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

from pathlib import Path
import os

dir  = Path(__file__).parent


loader = DirectoryLoader(
    path=dir,
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

documents = loader.lazy_load()

# for document in docs:
#     print(document)

print(f"Loaded {len(documents)} pages from PDFs")
print(documents[0].page_content[:300])  # print preview
print(documents[0].metadata)