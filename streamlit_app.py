import streamlit as st

st.title('InterPrep Artificial intelligence')

st.info('Your Interview Prepration oF Your Future Job')

with st.expander('Accordian'):
  st.write('This is the text inside the Accordian')

with st.sidebar:
  st.radio('Select your Gander : ',['Male','Female','other'])
  st.slider('Select your Age : ',1,100)
  st.selectbox('Select your Profession : ',["Software Developer","Full Stack Developer","Front-End Developer","Back-End Developer",
    "DevOps Engineer","Mobile App Developer","Data Engineer","Cloud Engineer","Security Engineer","Site Reliability Engineer (SRE)",
    "Machine Learning Engineer","Artificial Intelligence Engineer","Embedded Systems Engineer","Quality Assurance (QA) Engineer",
    "Test Automation Engineer","Software Architect","Product Manager","Scrum Master","Systems Analyst","Release Manager","UI/UX Designer",
    "Database Administrator (DBA)","Network Engineer","Technical Support Engineer","Blockchain Developer"])  

