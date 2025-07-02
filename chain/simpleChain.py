from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template="genearte 5 interesting facts about a {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

chain = prompt | model | parser
result = chain.invoke({'topic': 'Indian Constitution'})
print(result)

# chain.get_graph().print_ascii()