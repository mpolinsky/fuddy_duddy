import streamlit as st
import english_words as ew
from datetime import datetime as dt
from collections import Counter as Co

with st.form(key=str(dt.now())):
  optio = st.selectbox("Select:", options=[1,2,3,4,5])
  st.subheader(optio)
  submit = st.form_submit_button("Submit")
  if submit:
    st.header("HGELOOOO")
    st.session_state.hello = 99
    
st.header(st.session_state.hello)
