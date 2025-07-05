from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

# Your source documents
documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models."),
]

# Initialize the embedding model
embedding_model = OpenAIEmbeddings()

# Create Chroma vector store in memory
vector_store = Chroma.from_documents(
    embedding=embedding_model,
    documents=documents,
    collection_name="my_collection"
)

# Convert vectorstore into a retriever
retriever = vector_store.as_retriever(search_kwargs={"k":2})

query = "What is the use of embedding models?"
result = retriever.invoke(query)

for i, doc in enumerate(result):
    print(f"-- Result {i+1}--")
    print(f"Content: {doc.page_content}")
    print("\n")
