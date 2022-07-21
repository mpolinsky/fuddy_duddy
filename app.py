import streamlit as st
from datetime import datetime as dt


def assign(arg):
  st.session_state.hello = arg

if 'hello' not in st.session_state:
  st.session_state.hello = 55555
  
with st.form(key=str(dt.now())):
  selection = st.selectbox("Select:", options=[1,2,3,4,5])
  st.subheader(selection)
  submit = st.form_submit_button("Submit", on_click=assign, args=(selection,))
  if submit:
    st.header("HELLO WORLD")
    st.session_state.hello = 99999
    
st.header(st.session_state.hello)

st.session_state
