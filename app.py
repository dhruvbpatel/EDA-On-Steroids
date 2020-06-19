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
    <h2 style="color:white;text-align:center;">EDA-On-Steroids</h2>
    
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

            if st.checkbox("View Multiple Columns",False):
                select_column = st.multiselect("Select Columns",col_list)
                col_df = df[select_column]
                st.dataframe(col_df)
            
            if st.checkbox("Show Dataset Statistics",False):
                st.write("Stats")
                st.write(df.describe())

                st.write("No of Columns:")
                st.write(len(df.columns))

                st.write("Columns")
                st.write(df.columns.to_list())

                st.write("No of Observatios")
                st.write(len(df))

                st.write("Number of Missing Values")
                missing_val = df.isnull().sum()
                missing_val_df = pd.DataFrame(missing_val, columns=["Counts"])
                st.write(missing_val_df)

                st.write("Missing Cells Percentage")
                
                missing_val_sum = missing_val.sum()
                missing_val_percent = 100*(missing_val_sum)/(df.shape[0]*df.shape[1])
                st.write(missing_val_percent,"%")

                st.write("Column Category")
                cat_col = [col for col in df.columns.to_list() if df[col].dtype=='object']

                cat_col_count = len(cat_col)
                num_col_count = len(df.columns)-cat_col_count
                num_cat_df = pd.DataFrame({"Categorical Column Count":[cat_col_count],"Numerical Column Count":[num_col_count]},index=["Counts"])
                st.write(num_cat_df)
            
### individual column summary
            if st.checkbox("Show Individual Column Summary",False):
                col_options = df.columns.to_list()
                selected_col=st.selectbox("Select Column",col_options)

                st.write("Statistics for ",selected_col)
                st.write(df[selected_col].describe())

                st.write("Number of Distinct Values in ",selected_col, ":")
                unique_val = df[selected_col].nunique()
                st.write(unique_val)

                st.write("Unique values percentage :")
                unique_val_percent = 100*unique_val/len(df)
                st.write(unique_val_percent,"%")

                st.write("Missing Values :")
                missing_val_col = df[selected_col].isnull().sum()
                st.write(missing_val_col)

                st.write("Missing Values percentage :")
                missing_val_col_percent = 100*missing_val_col/len(df)
                st.write(missing_val_col_percent,"%")

                
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
        #st.subheader("Build the model")  
        st.subheader("Module will be added soon !!!!")  
    
    footer = """
    


    <footer style="margin-top:280px;">
    Made with 🧡 by <a href="https://github.com/dhruvbpatel">@dhruvhimself</a>
    <br><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <a href="https://www.linkedin.com/in/dhruv-patel-1057/" target="_blank">
    <img src="https://img.icons8.com/metro/24/000000/linkedin.png"/>
    </a>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <a href="https://github.com/dhruvbpatel" target="_blank">
    <img src="https://img.icons8.com/material-sharp/26/000000/github.png"/>
    </a>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <a href="https://twitter.com/dhruvhimself" target="_blank">
    <img src="https://img.icons8.com/metro/26/000000/twitter.png"/>
    </a>
    </footer>

    """
    st.sidebar.markdown(footer, unsafe_allow_html=True)
    
    hide_streamlit_style = """
            <style>
                        #MainMenu {visibility: hidden;}


                        

            </style>

            """


    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    
if __name__ == '__main__':
    main()
