from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model="gpt-4o")

def count_word(text):
    return len(text.split())

prompt = PromptTemplate(
    template="generate a joke on a {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

seq_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count':RunnableLambda(count_word)
})

final_chain = RunnableSequence(seq_chain, parallel_chain)

result = final_chain.invoke({'topic':'AI'})

print(result['joke'])
print(result['word_count'])