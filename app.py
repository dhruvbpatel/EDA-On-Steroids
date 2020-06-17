## pckgs
import streamlit as st
import matplotlib.pyplot as plt 
import matplotlib
import numpy as np
import sklearn
import pandas as pd
import seaborn as sns


## main func
def main():
    # st.title("EDA on the GO")
    st.sidebar.title("Select Task")

    html_header="""
    <div style ="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">EDA-ON-Steroids</h2>
    </div>
    """
    st.markdown(html_header,unsafe_allow_html=True)

    option =["EDA","Data Visualization","Train Model"]
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

            # st.selectbox("columns",df.columns.to_list())
            
    if choice == 'Data Visualization':
        df = pd.read_csv(data)
        col_list = df.columns.to_list()
        st.subheader("Data Visualization")
        corr_option = ["Show Correlation between all Features",
                        "Show Correlation between among Selected Features"]

        corr_choice=st.selectbox("Select Correlation Plot",corr_option)        

        if corr_choice == "Show Correlation between all Features":
            st.write(sns.heatmap(df.corr(),annot=True))
            st.pyplot()
        if corr_choice == "Show Correlation between among Selected Features":
            num_col = [col for col in df.columns.to_list() if df[col].dtype != 'object']  ## selecting only numerical cols
            select_col=st.multiselect("Select columns",num_col)
            select_col_df = df[select_col]

            st.write(sns.heatmap(select_col_df.corr(),annot=True))
            st.pyplot()


    if choice=='Train Model':
        st.subheader("Build the model")    

    
if __name__ == '__main__':
    main()
