from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model="gpt-4o")

prompt1 = PromptTemplate(
    template="generate a tweet on a {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="generate a linkedin post on a {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet':RunnableSequence(prompt1, model, parser),
    'post': RunnableSequence(prompt2, model, parser)
})

result = parallel_chain.invoke({'topic': 'Job offer letter'})
print("Tweet: ")
print(result['tweet'])
print("\n")

print("Linkedin Post: ")
print(result['post'])