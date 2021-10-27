import pandas as pd
from pandas.core.frame import DataFrame
import streamlit as st
from text import TextColumn


st.title('Data Explorer Web App')
st.markdown('We develop an interactive web application using Streamlit that will read a provided CSV file by the user and perform some exploratory data analysis on it. ')

uploaded_file = st.file_uploader("Please choose a CSV file:")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df_text  = df.select_dtypes(include=['object'])
    df_text.columns = df_text.columns.str.replace(' ','_') # replace the column has space with '_'
    st.write(df_text)
    text = TextColumn()
    column_num = 0
    st.header('3. Text Column Information')

for (columnName, columnData) in df_text.iteritems():
    
    text.get_data(columnName, columnData)

    column_name = text.get_name()
    st.markdown(f'**3.{column_num} Field Name:** **_{column_name}_**')
    column_num = column_num + 1

    # Display number of unique value
    unique = text.get_unique()
    
    # Display number of missing values
    missing = text.get_missing()
    
    # Display number of rows with empty string
    empty = text.get_empty()
    
    # Display number of only whitespaces
    whitespaces = text.get_whitespace()
        
    # Display number of only lower case characters
    lower = text.get_lowercase()
    
    # Display number of only upper case characters
    upper = text.get_uppercase()
    
    # Display number of only alphabet characters
    alp = text.get_alphabet()
    
    # Display number of only digital characters
    digital = text.get_digit()
    
    # Display the mode value
    mode_value = text.get_mode()
    
    # Create a dataFrame for displaying in the Web App
    value = {'value':pd.Series([unique,missing,empty, whitespaces, lower, upper, alp, digital,mode_value[0]], index = ['Number of Unique Values:', 'Number of Rows with Missing Values:',
    'Number of Empty Rows:', 'Number of Rows with Only Whitespace:', 'Number of Rows with Only Lowercases:', 'Number of Rows with Only Uppercases:', 'Number of Rows with Only Alphabet:','Number of Rows with Only Digits:','Mode Value'])}
    df_value = pd.DataFrame(value)
    st.write(df_value)
    
    # Plot bar chat and display in Web App
    st.markdown('**Bar Chat**')
    st.altair_chart(text.get_barchart())

    # Create a frequent table and display in WebA[[]]
    st.markdown('**Most Frequent Values**')
    frequent = text.get_frequent()
    st.write(frequent)


