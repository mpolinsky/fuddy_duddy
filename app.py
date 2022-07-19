import streamlit as st

st.title('Counter Example')

# Streamlit runs from top to bottom on every iteraction so
# we check if `count` has already been initialized in st.session_state.

if 'res' not in st.session_state:
	st.session_state.res = list()

	
option = st.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)
st.session_state.choice=option	
	

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
st.write(st.session_state)

if st.session_state.count > 5:
    st.session_state.res.append('red')

st.write(st.session_state.res)
