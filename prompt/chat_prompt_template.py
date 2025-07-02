from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model="gpt-4o")
prompt = ChatPromptTemplate([
    ("system", "You're helpful AI assistant"),
    ("user", "Tell me about {topic}")
])

formatted_prompt = prompt.format_messages(topic="black holes")
result = llm.invoke(formatted_prompt)
print(result.content)