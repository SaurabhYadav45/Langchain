from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path
import os

pdf_path  = Path(__file__).parent/"nodejs.pdf"

loader = PyPDFLoader(pdf_path)

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[0].metadata)
print(docs)