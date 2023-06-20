import streamlit as st
import pandas as pd

def plot_chart(prohibited_phrases, result):
    response = {}
    for p in prohibited_phrases:
        if p in result:
            val = result[p]
            response.update({p: val})
        else:
            response.update({p: 0})
    st.dataframe(response, use_container_width = True)
    st.bar_chart(response)
    st.markdown("This is a ***test***.")

prohibited_phrases = ['sexuality','neighborhood', 'disability', 'marital status', 'age', 'race', 'ethnicity', 'religion', 'gender']
options = st.sidebar.multiselect('Bias to Detect', prohibited_phrases, prohibited_phrases )

def main():
    response_content = {
        "disability": 1,
        "gender": 3,
        "age": 2,
        "race": 1
    }
    plot_chart(prohibited_phrases=options, result=response_content)

if __name__ == '__main__':
    main()    
