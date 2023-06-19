import streamlit as st
import pandas as pd

# Create a dictionary of data
prohibited_phrases = ['sexuality','neighborhood descriptors', 'disability', 'marital status', 'age demographics', 'race', 'ethnicity', 'religion']
result = {
    'neighborhood descriptors' : 3,
    'sexuality' : 2,
    'marital status': 5,
    'race': 3,
    'religion': 2
}
response = {}
for p in prohibited_phrases:
    if p in result:
        val = result[p]
        response.update({p: val})
    else:
        response.update({p: 0})


st.dataframe(response, use_container_width = True)
st.bar_chart(response)
