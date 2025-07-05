from langchain_community.retrievers import WikipediaRetriever


# WikiPedia Retriever

retriever = WikipediaRetriever(top_k_results=1, lang="en")
query = "Who is Rohit Sharma"
result = retriever.invoke(query)
# print(result)

for i, doc in enumerate(result):
    print(f"--- Result {i+1} ---")
    print("\n")
    print(f"Content: {doc.page_content}")
