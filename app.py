import streamlit as st
import english_words as ew
from datetime import datetime as dt
from collections import Counter as Co


optio = st.selectbox("Select:", options=[1,2,3,4,5])
st.subheader(optio)
