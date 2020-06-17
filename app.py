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
    st.subheader("Exploratory Data Analysis")

    data = st.file_uploader("Upload Data here (CSV file only)",type=['csv'])
    ## EDA 
    if choice=='EDA':
        

        if data is not None:
            df=pd.read_csv(data)
            col_list = df.columns.to_list()
            if st.checkbox("Show raw data", False):
                
                if data is not None:
                    st.subheader("RAW DATA")    
                    st.write(df)

            if st.checkbox("Select Columns",False):
                select_column = st.multiselect("Select Columns",col_list)
                col_df = df[select_column]
                st.dataframe(col_df)



            st.write("Stats")
            st.write(df.describe())

            st.write("No of Columns:")
            st.write(len(df.columns))

            st.write("Columns")
            st.write(df.columns.to_list())

            st.selectbox("columns",df.columns.to_list())
            
            
    if choice=='Plots':
        st.subheader("Data Visualization")
    if choice=='Train':
        st.subheader("Build the model")

    
if __name__ == '__main__':
    main()
