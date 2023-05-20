from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

from barfi import st_barfi, barfi_schemas, Block
import streamlit as st

from barfi import Block

query = st.text_input('query')

LLM = Block(name='LLM')
LLM.add_output()
def get_llm(self):
    llm = OpenAI(temperature=0.9)
    self.set_interface(name='llm', value=4)
LLM.add_compute(get_llm)

Prompt = Block(name='Prompt')
Prompt.add_output()
def get_prompt(self):
    prompt = PromptTemplate(
        input_variables=["product"],
        template="What is a good name for a company that makes {product}?",
    )
Prompt.add_compute(get_prompt)

Memory = Block(name='Memory')
Memory.add_output()
def feed_func(self):
    self.set_interface(name='Output 1', value=4)
Memory.add_compute(feed_func)

VectorStore = Block(name='VectorStore')
VectorStore.add_output()
def feed_func(self):
    self.set_interface(name='Output 1', value=4)
VectorStore.add_compute(feed_func)

Chain = Block(name='Chain')
Chain.add_input()
Chain.add_input()
Chain.add_output()
def mixer_func(self):
    llm = self.get_interface(name='llm')
    prompt = self.get_interface(name='prompt')
    chain = LLMChain(llm=llm, prompt=prompt)
    self.set_interface(name='Chain Output', value=chain.run({product:query}))
Chain.add_compute(mixer_func)

Agent = Block(name='Agent')
Agent.add_input()
Agent.add_input()
Agent.add_output()
def mixer_func(self):
    in_1 = self.get_interface(name='Input 1')
    in_2 = self.get_interface(name='Input 2')
    value = (in_1 + in_2)
    self.set_interface(name='Output 1', value=value)
Agent.add_compute(mixer_func)

result = Block(name='Result')
result.add_input()
def result_func(self):
    result = self.get_interface(name='Input 1')
    st.markdown(result)
result.add_compute(result_func)

load_schema = st.selectbox('Select a saved schema:', barfi_schemas())

compute_engine = st.checkbox('Activate barfi compute engine', value=False)

barfi_result = st_barfi(base_blocks=[LLM, Prompt, Memory, VectorStore, Chain, Agent, result],
                    compute_engine=compute_engine, load_schema=load_schema)

if barfi_result:
    st.write(barfi_result)
