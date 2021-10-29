import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from pandas.core.frame import DataFrame
import altair as alt
from numeric import numeric

#title of the app
st.title("Data Explorer Web App")

df = pd.read_csv("reddit_vm.csv")

st.subheader("File Uploader")
file_uploaded = st.file_uploader("CSV File Uploader", type = ["csv"])

# Display header title
st.title('Data Explorer Tool')
# Upload CSV data
dataset = st.file_uploader("Choose a CSV file",type=["csv"]) 

if dataset is not None:
  # read csv file
  df = pd.read_csv(dataset)
  df.columns = df.columns.str.replace(' ','_') # replace the column has space with '_'

  ######################################################
  # 1. Overall Information
  ######################################################
  # Display header called “Overall Information”
  st.header('2. Numeric Columns')
  # instantiate class object
  gen_info = Dataset(df, dataset.name)

#functions

# Display name of column as subtitle
#PENDING

# Display number of unique values
unique_values = numeric.get_unique_values()

# Display number of missing values
missing_values = numeric.get_missing_values()

# Display number of ocurrence of 0 value
occurence_0 = numeric.get_occurence_0_value()

# Display number of negative values
negative_values = numeric.get_negative_values()

# Display the average value
avg_value = numeric.get_avg_value()

# Display the standard deviation value
std_value = numeric.get_std_value()

# #Display the minimum value
min_value = numeric.get_min_value()

# Display the maximum value
max_value = numeric.get_max_value()

# Display the median value
median_value = numeric.get_median_value()


# Create a dataFrame for displaying in the Web App
    value = {'value':pd.Series([unique_values,
            missing_values,
            occurence_0,
            negative_values,
            avg_value,
            std_value,
            min_value, 
            max_value,
            median_value], 
            index = ['Number of Unique Values:'
            , 'Number of Missing Values:'
            , 'Number of Occurence with Value 0:'
            , 'Number of Negative Values:'
            , 'Average Value:'
            , 'Standard Deviation Value:'
            , 'Minimum Value:'
            , 'Maximum Value:'
            , 'Median Value'])}
    df_value = pd.DataFrame(value)
    st.write(df_value)
    
    # Plot bar chat and display in Web App
    st.markdown('#### Histogram')
    st.altair_histogram(numeric.get_histogram())

    # Create a frequent table and display in WebA[[]]
    st.markdown('#### Most Frequent Values')
    frequent = numeric.get_frequent_values()
    st.write(frequent)