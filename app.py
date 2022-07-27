import streamlit as st
from datetime import datetime as dt
import english_words as ew

def assign(arg):
  st.session_state.hello = arg

if 'word_pool' not in st.session_state:
    st.session_state.word_pool = [i for i in ew.english_words_lower_alpha_set if len(i) > 3][:200]
  
if 'hello' not in st.session_state:
  st.session_state.hello = 55555
  st.session_state.count = 0
  
if 'accumulator' not in st.session_state:
  st.session_state.accumulator = list()
  
if st.session_state.count < 2:
  st.session_state.word_pool.insert(0,None) 
  #with st.form(key=str(dt.now())):
  selection= st.selectbox("Select:", options=st.session_state.word_pool)
    #st.subheader(selection)
    #submit = st.form_submit_button("Submit", on_click=assign, args=(selection,))
    #if submit:
      #st.header("HELLO WORLD")
      #st.session_state.hello = 99999
  if selection is not None:
    st.session_state.hello = selection
  st.session_state.accumulator.append(st.session_state.hello)
  st.session_state.count += 1
    
st.header(st.session_state.hello)

st.session_state.word_pool = st.session_state.word_pool[:-10]


st.session_state
