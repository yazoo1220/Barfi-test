from barfi import st_barfi, barfi_schemas, Block
import streamlit as st

from barfi import Block

LLM = Block(name='LLM')
LLM.add_input()
LLM.add_input()
LLM.add_output()
def feed_func(self):
    self.set_interface(name='Output 1', value=4)
LLM.add_compute(feed_func)

Prompt = Block(name='Prompt')
Prompt.add_output()
def feed_func(self):
    self.set_interface(name='Output 1', value=4)
Prompt.add_compute(feed_func)

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
    in_1 = self.get_interface(name='Input 1')
    in_2 = self.get_interface(name='Input 2')
    value = (in_1 + in_2)
    self.set_interface(name='Output 1', value=value)
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
    in_1 = self.get_interface(name='Input 1')
result.add_compute(result_func)

load_schema = st.selectbox('Select a saved schema:', barfi_schemas())

compute_engine = st.checkbox('Activate barfi compute engine', value=False)

barfi_result = st_barfi(base_blocks=[LLM, Prompt, Memory, VectorStore, Agent, Result],
                    compute_engine=compute_engine, load_schema=load_schema)

if barfi_result:
    st.write(barfi_result)
