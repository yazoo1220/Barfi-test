from barfi import st_barfi, barfi_schemas, Block
import streamlit as st

from barfi import Block

theme = Block(name='テーマ')
llm.add_output()
def feed_func(self):
    self.set_interface(name='テーマ', value=4)
feed.add_compute(feed_func)

outlilne = Block(name='アウトライン')
outlilne.add_input()
outlilne.add_output()
outlilne.add_output()
def splitter_func(self):
    in_1 = self.get_interface(name='テーマ')
    value = (in_1/2)
    self.set_interface(name='序文', value=value)
    self.set_interface(name='段落１', value=value)
    self.set_interface(name='段落２', value=value)
    self.set_interface(name='段落３', value=value)
    self.set_interface(name='まとめ', value=value)
outlilne.add_compute(splitter_func)

writing = Block(name='ドラフト')
writing.add_output()
def feed_func(self):
    self.set_interface(name='ドラフト', value=4)
writing.add_compute(feed_func)

validation = Block(name='検証')
validation.add_input()
validation.add_output()
validation.add_output()
def splitter_func(self):
    in_1 = self.get_interface(name='Input 1')
    value = (in_1/2)
    self.set_interface(name='差し戻し', value=value)
    self.set_interface(name='通過', value=value)
splitter.add_compute(splitter_func)

mixer = Block(name='統合')
mixer.add_input()
mixer.add_input()
mixer.add_input()
mixer.add_input()
mixer.add_input()
mixer.add_output()
def mixer_func(self):
    in_1 = self.get_interface(name='序文', value=value)
    in_1 = self.get_interface(name='段落１', value=value)
    in_1 = self.get_interface(name='段落２', value=value)
    in_1 = self.get_interface(name='段落３', value=value)
    in_1 = self.get_interface(name='まとめ', value=value)
    value = (in_1 + in_2)
    self.set_interface(name='原稿', value=value)
mixer.add_compute(mixer_func)

result = Block(name='Wordpress')
result.add_input()
def result_func(self):
    in_1 = self.get_interface(name='原稿')
result.add_compute(result_func)

load_schema = st.selectbox('Select a saved schema:', barfi_schemas())

compute_engine = st.checkbox('Activate barfi compute engine', value=False)

barfi_result = st_barfi(base_blocks=[feed, result, mixer, splitter],
                    compute_engine=compute_engine, load_schema=load_schema)

if barfi_result:
    st.write(barfi_result)