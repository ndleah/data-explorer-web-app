import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from pandas.core.frame import DataFrame
import altair as alt
from numeric import NumericColumn

#title of the app
st.title("Data Explorer Web App")

#df = pd.read_csv("reddit_vm.csv")

#st.subheader("File Uploader")
#file_uploaded = st.file_uploader("CSV File Uploader", type = ["csv"])

# Display header title
#st.title('Data Explorer Tool')
# Upload CSV data
#dataset = st.file_uploader("Choose a CSV file",type=["csv"]) 

#if dataset is not None:
  # read csv file
  #df = pd.read_csv(dataset)
  #df.columns = df.columns.str.replace(' ','_') # replace the column has space with '_'

st.markdown('We develop an interactive web application using Streamlit that will read a provided CSV file by the user and perform some exploratory data analysis on it. ')

uploaded_file = st.file_uploader("Please choose a CSV file:")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df_numeric  = df.select_dtypes(include=['float64', 'int64'])
    df_numeric.columns = df_numeric.columns.str.replace(' ','_') # replace the column has space with '_'
    st.write(df_numeric)
    numeric = NumericColumn()
    column_num = 0
    st.header('2. Numeric Column Information')

  ######################################################
  # 1. Overall Information
  ######################################################
  # Display header called “Overall Information”
 ## st.header('2. Numeric Columns')
  # instantiate class object
 ## gen_info = Dataset(df, dataset.name)

#functions

# Display name of column as subtitle
column_name = numeric.get_name()
st.markdown(f'**2.{column_num} Field Name:** **_{column_name}_**')
column_num = column_num + 1

# Display number of unique values
unique_values = numeric.get_unique()

# Display number of missing values
missing_values = numeric.get_missing()

# Display number of ocurrence of 0 value
occurence_0 = numeric.get_zeros()

# Display number of negative values
negative_values = numeric.get_negatives()

# Display the average value
avg_value = numeric.get_mean()

# Display the standard deviation value
std_value = numeric.get_std()

# Display the minimum value
min_value = numeric.get_min()

# Display the maximum value
max_value = numeric.get_max()

# Display the median value
median_value = numeric.get_median()


 # Create a dataFrame for displaying in the Web App
  value = {'value':pd.Series([unique_values,missing_values,occurence_0,negative_value,avg_value,std_value,min_value,max_value,median_value], 
  index = ['Number of Unique Values:','Number of Missing Values:','Number of Rows with 0:','Number of Rows with Negative Values:',
  'Average Values:','Standard Deviation Values:','Minimum Value', 'Maximum Value','Median Value'])}
  df_value = pd.DataFrame(value)
  st.write(df_value)

    
  # Plot bar chat and display in Web App
  st.markdown('**Histogram**')
  st.altair_chart(numeric.get_histogram())


  # Create a frequent table and display in WebA[[]]
  st.markdown('**Most Frequent Values**')
  frequent = numeric.get_frequent()
  st.write(frequent)
