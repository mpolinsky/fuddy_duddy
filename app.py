import streamlit as st
import english_words as ew
from datetime import datetime as dt

st.title('Counter Example')

# Streamlit runs from top to bottom on every iteraction so
# we check if `count` has already been initialized in st.session_state.

if 'word_pool' not in st.session_state:
    st.session_state.word_pool = [i for i in ew.english_words_lower_alpha_set if len(i) > 3][::5]

if 'res' not in st.session_state:
    st.session_state.res = list()

if 'choice' not in st.session_state:
    st.session_state.choice = ''

# If no, then initialize count to 0
# If count is already initialized, don't do anything
if 'count' not in st.session_state:
    st.session_state.count = 0
    st.write("ONE TIME")
    
st.write(st.session_state.choice)
st.session_state.name = st.text_input('nameo: ')
# Create a button which will increment the counter
increment = st.button('Increment')
if increment:
    st.session_state.count += 1

# A button to decrement the counter
decrement = st.button('Decrement')
if decrement:
    st.session_state.count -= 1

st.write('Count = ', st.session_state.count)

if st.session_state.count > 5:
    st.session_state.res.append('red')

with st.form(key=str(dt.now())):	
	option = st.selectbox(
	'Select:',
	st.session_state.word_pool)
	submit = st.form_submit_button("submit")
	if submit:
		st.write('You selected:', option)
st.session_state.choice = option	
st.session_state.res.append(st.session_state.choice)

st.write(st.session_state)

