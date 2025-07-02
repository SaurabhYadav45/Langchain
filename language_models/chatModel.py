#                **************** OpenAi ****************

# from langchain_openai import  ChatOpenAI
# from dotenv import load_dotenv
# load_dotenv()

# model = init_chat_model("gpt-4o-mini", model_provider="openai")
# chat_model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=20)
# result = chat_model.invoke("write a 5 line poem on cricket")
# print(result.content)


#                **************** Anthropic Model : Claude ***********

# from langchain_anthropic import ChatAnthropic
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatAnthropic(model='claude-3-5-sonnet-20241022')

# result = model.invoke('What is the capital of India')

# print(result.content)


#                ******************* Google Gemini ******************

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

chat_model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
result = chat_model.invoke("What is the capital of india")
print(result.content)
