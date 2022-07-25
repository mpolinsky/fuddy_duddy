import streamlit as st

with st.expander("Hi Charly"):
    if st.checkbox("Fake expand"):
        st.write("Hello world")

st.session_state
