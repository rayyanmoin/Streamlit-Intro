import streamlit as st

st.title('InterPrep Artificial intelligence')

st.info('Your Interview Prepration oF Your Future Job')

with st.expander('Accordian'):
  st.write('This is the text inside the Accordian')

with st.sidebar:
  st.radio('Select your Gander : ',['Male','Female','other'])
  
