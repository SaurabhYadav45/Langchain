from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI()
messages = [
    SystemMessage(content="You're a helpful AI  assistant"),
    HumanMessage(content="What is Generative AI")
]

response = model.invoke(messages)
messages.append(AIMessage(content=response.content))
print(response.content)



# Chat models also accept OpenAI's format as inputs to chat models:

# chat_model.invoke([
#     {
#         "role": "user",
#         "content": "Hello, how are you?",
#     },
#     {
#         "role": "assistant",
#         "content": "I'm doing well, thank you for asking.",
#     },
#     {
#         "role": "user",
#         "content": "Can you tell me a joke?",
#     }
# ])