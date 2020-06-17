## pckgs
import streamlit as st
import matplotlib.pyplot as plt 
import matplotlib
import numpy as np
import sklearn
import pandas as pd


## main func
def main():
    # st.title("EDA on the GO")
    st.sidebar.title("Task")

    html_header="""
    <div style ="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">EDA-ON-Steroids</h2>
    </div>
    """
    st.markdown(html_header,unsafe_allow_html=True)

    option =["EDA","Plots","Train"]
    choice=st.sidebar.selectbox("Select Task",option)

    ## EDA 
    if choice=='EDA':
        st.subheader("Exploratory Data Analysis")

        data = st.file_uploader("Upload Data here (CSV file only)",type=['csv'])

        if data is not None:
            df=pd.read_csv(data)

            if st.checkbox("Show raw data", False):
                
                if data is not None:
                    st.subheader("RAW DATA")    
                    st.write(df)
            
            if st.checkbox("Show info",False):
                data_info=pd.DataFrame(df.info())
                st.write(data_info)
    if choice=='Plots':
        st.subheader("Data Visualization")
    if choice=='Train':
        st.subheader("Build the model")

    
if __name__ == '__main__':
    main()
