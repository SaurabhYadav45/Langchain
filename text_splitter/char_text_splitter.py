from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path
import os

# path = Path(__file__).parent.parent/"dl-curriculum.pdf"
loader = PyPDFLoader('dl-curriculum.pdf')
docs = loader.load()

text_splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20,
    separator=''
)

result = text_splitter.split_documents(docs)
print(result)
