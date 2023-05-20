from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

from barfi import st_barfi, barfi_schemas, Block
import streamlit as st

from barfi import Block

feed = Block(name='Feed')
feed.add_output()
def feed_func(self):
    self.set_interface(name='Output 1', value=4)
feed.add_compute(feed_func)

splitter = Block(name='Splitter')
splitter.add_input()
splitter.add_output()
splitter.add_output()
def splitter_func(self):
    in_1 = self.get_interface(name='Input 1')
    value = (in_1/2)
    self.set_interface(name='Output 1', value=value)
    self.set_interface(name='Output 2', value=value)
splitter.add_compute(splitter_func)

mixer = Block(name='Mixer')
mixer.add_input()
mixer.add_input()
mixer.add_output()
def mixer_func(self):
    in_1 = self.get_interface(name='Input 1')
    in_2 = self.get_interface(name='Input 2')
    value = (in_1 + in_2)
    self.set_interface(name='Output 1', value=value)
mixer.add_compute(mixer_func)

result = Block(name='Result')
result.add_input()
def result_func(self):
    in_1 = self.get_interface(name='Input 1')
result.add_compute(result_func)

process_blocks = [feed, result, mixer, splitter]

number_10 = Block(name='Number')
number_10.add_output()
def number_10_func(self):
    self.set_interface(name='Output 1', value=10)
number_10.add_compute(number_10_func)

number_5 = Block(name='Number')
number_5.add_output()
def number_5_func(self):
    self.set_interface(name='Output 1', value=5)
number_5.add_compute(number_5_func)

subtraction = Block(name='Subtraction')
subtraction.add_input()
subtraction.add_input()
subtraction.add_output()
def subtraction_func(self):
    in_1 = self.get_interface(name='Input 1')
    in_2 = self.get_interface(name='Input 2')
    value = in_1 - in_2
    self.set_interface(name='Output 1', value=value)    
subtraction.add_compute(subtraction_func)

addition = Block(name='Addition')
addition.add_input()
addition.add_input()
addition.add_output()
def addition_func(self):
    in_1 = self.get_interface(name='Input 1')
    in_2 = self.get_interface(name='Input 2')
    value = in_1 + in_2
    self.set_interface(name='Output 1', value=value)    
addition.add_compute(addition_func)

multiplication = Block(name='Multiplication')
multiplication.add_input()
multiplication.add_input()
multiplication.add_output()
def multiplication_func(self):
    in_1 = self.get_interface(name='Input 1')
    in_2 = self.get_interface(name='Input 2')
    value = in_1 * in_2
    self.set_interface(name='Output 1', value=value)    
multiplication.add_compute(multiplication_func)

division = Block(name='Addition')
division.add_input()
division.add_input()
division.add_output()
def division_func(self):
    in_1 = self.get_interface(name='Input 1')
    in_2 = self.get_interface(name='Input 2')
    value = in_1 / in_2
    self.set_interface(name='Output 1', value=value)    
division.add_compute(division_func)

result = Block(name='Result')
result.add_input()
def result_func(self):
    in_1 = self.get_interface(name='Input 1')
    print(in_1)
result.add_compute(result_func)

math_blocks = [number_10, number_5, result, addition, subtraction, multiplication, division]

# query = st.text_input('query')

# LLM = Block(name='LLM')
# LLM.add_output()
# def get_llm(self):
#     llm = OpenAI(temperature=0.9)
#     self.set_interface(name='Output 1', value=llm)
# LLM.add_compute(get_llm)

# Prompt = Block(name='Prompt')
# Prompt.add_output()
# def get_prompt(self):
#     prompt = PromptTemplate(
#         input_variables=["product"],
#         template="What is a good name for a company that makes {product}?",
#     )
#     self.set_interface(name='Output 1', value=prompt)
# Prompt.add_compute(get_prompt)

# Memory = Block(name='Memory')
# Memory.add_output()
# def feed_func(self):
#     self.set_interface(name='Output 1', value=4)
# Memory.add_compute(feed_func)

# VectorStore = Block(name='VectorStore')
# VectorStore.add_output()
# def feed_func(self):
#     self.set_interface(name='Output 1', value=4)
# VectorStore.add_compute(feed_func)

# Chain = Block(name='Chain')
# Chain.add_input()
# Chain.add_input()
# Chain.add_output()
# def chain_run(self):
#     llm = self.get_interface(name='Input 1')
#     prompt = self.get_interface(name='Input 2')
#     chain = LLMChain(llm=llm, prompt=prompt)
#     answer = chain.run(query)
#     self.set_interface(name='Output 1', value=4) #answer)
#     return answer
# Chain.add_compute(chain_run)

# Agent = Block(name='Agent')
# Agent.add_input()
# Agent.add_input()
# Agent.add_output()
# def mixer_func(self):
#     in_1 = self.get_interface(name='Input 1')
#     in_2 = self.get_interface(name='Input 2')
#     value = (in_1 + in_2)
#     self.set_interface(name='Output 1', value=value)
# Agent.add_compute(mixer_func)

# result = Block(name='Result')
# result.add_input()
# result.add_output()
# def result_func(self):
#     result = self.get_interface(name='Input 1')
#     self.set_interface(name='result', value=4)
#     output_area = st.empty()
#     output_area.markdown(result)
# result.add_compute(result_func)

load_schema = st.selectbox('Select a saved schema:', barfi_schemas())

compute_engine = st.checkbox('Activate barfi compute engine', value=False)

# barfi_result = st_barfi(base_blocks=[LLM, Prompt, Memory, VectorStore, Chain, Agent, result],
#                     compute_engine=compute_engine, load_schema=load_schema)

barfi_result = st_barfi(
    base_blocks=math_blocks, compute_engine=compute_engine, load_schema=barfi_schema_name)

if barfi_result:
    st.write(barfi_result['Result-id-524173']['block'].get_interface(name='Input 1'))
    st.write(barfi_result)

if barfi_result:
    st.write(barfi_result)
    st.write(barfi_result)['Result-1']['block'].get_interface(name='Input 1')
