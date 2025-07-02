from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model="gpt-4o")

prompt1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Summarize the following text \n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

seq_chain = RunnableSequence(prompt1 | model |  parser)

branch_chain = RunnableBranch(
    (lambda x : len(x.split()) > 200, prompt2 |  model | parser),
    RunnablePassthrough()
)

final_chain = seq_chain | branch_chain

result = final_chain.invoke({'topic':'Russia vs Ukraine'})
print(result)


