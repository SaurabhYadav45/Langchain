from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader
import os
# print("Current working dir:", os.getcwd())
load_dotenv()


model = ChatOpenAI()

prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "abc.txt")

loader = TextLoader(file_path, encoding='utf-8')

docs = loader.load()
# print(docs)
# print(len(docs))

print(docs[0].page_content)
print(docs[0].metadata)
