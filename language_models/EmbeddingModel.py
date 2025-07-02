# from langchain_openai import OpenAIEmbeddings
# from dotenv import load_dotenv
# load_dotenv()


# embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
# result = embeddings.embed_query("This is a cat and rat in a maze")
# print(str(result))



#                    embed_documnet

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)
documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]
result  = embeddings.embed_documents(documents)
print(str(result))