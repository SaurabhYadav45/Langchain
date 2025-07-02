from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model="gpt-4o")
prompt = PromptTemplate(
    input_variables=['topic'],
    template="Write a short and informative paragraph about {topic}."
)

formatted_prompt = prompt.format(topic="Quantum Computing")
response = llm.invoke(formatted_prompt)
print(response.content)