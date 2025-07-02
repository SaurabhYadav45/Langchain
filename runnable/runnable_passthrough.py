from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model="gpt-4o")

prompt1 = PromptTemplate(
    template="Generate trolled tweet on a given sport player just for fun - {name}",
    input_variables=['name']
)

parser = StrOutputParser()

seq_chain = RunnableSequence(prompt1, model, parser)

prompt2 = PromptTemplate(
    template="Explain this joke in short - {text}",
    input_variables=['text']
)

parallel_chain = RunnableParallel({
    'troll': RunnablePassthrough(),
    'explanation':RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(seq_chain, parallel_chain)

result = final_chain.invoke({'name':'Virat kohli'})

print("Troll: ")
print(result['troll'])
print("\n")

print("Explanation: ")
print(result['explanation'])