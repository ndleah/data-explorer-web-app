from numpy import empty
from src import Dataset, DateColumn, TextColumn, NumericColumn
import streamlit as st
import pandas as pd
from pandas.core.frame import DataFrame
import altair as alt
from datetime import datetime

######################################################
# Upload csv file
######################################################

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
  st.header('1. Overall Information')
  # instantiate class object
  gen_info = Dataset(df, dataset.name)

  # applying method
  df_name = gen_info.get_name() # get name
  df_rows = gen_info.get_n_rows() # get number of rows
  df_col = gen_info.get_n_cols() # get number of columns
  df_duplicate_rows = gen_info.get_n_duplicates() # get number of duplicated rows
  df_missing_rows = gen_info.get_n_missing() # get number of missing rows
  df_col_list = str(gen_info.get_cols_list()).replace('[','').replace(']','').replace("'","") # get list of column names
  df_col_type = pd.DataFrame([gen_info.get_cols_dtype()]).transpose() # get columns data types

  # Display filename
  st.markdown(f'**Name of Table:** {df_name}')

  # Display number of rows 
  st.markdown(f'**Number of Rows:** {df_rows}')

  # Display number of columns
  st.markdown(f'**Number of Columns:** {df_col}')

  # Display number of duplicated rows
  st.markdown(f'**Number of Duplicated Rows:** {df_duplicate_rows}')

  # Display number of rows with missing values
  st.markdown(f'**Number of Rows with Missing Values:** {df_missing_rows}')

  # Display list of columns and their data type (text, numeric, date)
  st.markdown(f'**List of Columns:**')
  st.write(df_col_list)
  st.markdown(f'**Type of Columns:**')
  st.dataframe(df_col_type)

  # Display slider for selecting the number of rows to be displayed 
  df_slider = st.slider("Select the number of rows to be displayed",5,50,5)

  # Display top N rows (default 5 rows) of dataset
  st.markdown('**Top Rows of Table**')
  st.dataframe(gen_info.get_head(df_slider))

  # Display bottom N rows (default 5 rows) of dataset
  st.markdown('**Bottom Rows of Table**')
  st.dataframe(gen_info.get_tail(df_slider))

  # Display N randomly sampled rows (default 5 rows) of dataset
  st.markdown('**Random Sample Rows of Table**')
  st.dataframe(gen_info.get_sample(df_slider))

  # Display a multi select box for choosing which text columns will be converted to datetime
  df_selectbox = st.multiselect("Which columns do you want to convert to dates", gen_info.get_text_columns())
  df[df_selectbox] = df[df_selectbox].apply(lambda col: pd.to_datetime(col, errors='ignore'))

  ######################################################
  # 2. Information on numeric columns
  ######################################################
  
  # ######################################################
  # 3. Information on text columns
  ######################################################
  # Display header called “Information on text columns”
  st.header('3. Information on text columns')

  # create dataframe with only text data only 
  df_text  = df.select_dtypes(include=['object']) # create text columns dataset
  st.write(df_text)
  text = TextColumn()
  column_num = 0

  for (columnName, columnData) in df_text.iteritems():
    text.get_data(columnName, columnData)
    column_name = text.get_name()

    # Display name of column as subtitle
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

  ######################################################
  # 4. Information on datetime columns
  ######################################################
  
  # Display header called “Information on datetime columns”
  st.header('4. Information on datetime columns')
  empty_list = []
  if df_selectbox[0] is not None:
    if df.select_dtypes(include = ["datetime64"]) is not None:
    
      # create dataframe with only datetime data only 
      datetime_col = df.select_dtypes(include = ["datetime64"])
      
      # instantiate class object
      datecol_object = DateColumn(datetime_col.columns, datetime_col.stack())
      
      # extract column name
      raw_name = datecol_object.col_name
      name_dt_col = raw_name[0]

      # Display name of column as subtitle
      st.markdown(f"**4.0 Field Name: _{name_dt_col}_**")    

      # Applying methods
      uniquedate = datecol_object.get_unique()
      missingdate = datecol_object.get_missing()
      weekenddate = datecol_object.get_weekend()
      weekdaydate =datecol_object.get_weekday()
      futuredate = datecol_object.get_future()
      empty1900date = datecol_object.get_empty_1900()
      empty1970date = datecol_object.get_empty_1970()
      mindate = datecol_object.get_min()
      maxdate = datecol_object.get_max()

      datetime_sum = { "" : ["Number of Unique Values", 
                  "Number of Rows with Missing Values", 
                  "Number of Weekend Dates", 
                  "Number of Weekday Dates", 
                  "Number of Dates in Future", 
                  "Number of Rows with 1900-01-01", 
                  "Number of Rows with 1970-01-01", 
                  "Minimum Value", 
                  "Maximum Value"], 
                  "Value" : [uniquedate, 
                  missingdate, 
                  weekenddate, 
                  weekdaydate, 
                  futuredate, 
                  empty1900date, 
                  empty1970date, 
                  mindate, 
                  maxdate
                  ]
                  }
          
      display_sumdate = pd.DataFrame(datetime_sum)
      #st.dataframe(display_sumdate)

      # bar chart
      st.markdown("**DateTime Bar Chart Frequencies**")
      st.altair_chart(datecol_object.get_barchart())

      # create frequency table
      st.markdown('**Most Frequent DateTime Values**')
      frequencies = datecol_object.get_frequent()
      st.write(frequencies)
    else: 
      st.markdown('**No Datetime found in data.**')
  else:
    st.markdown('**No selection for Datetime conversion found.**')