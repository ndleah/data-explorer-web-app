from datetime import datetime
import pandas as pd
from pandas.core.frame import DataFrame
import streamlit as st
from src.date_time import DateColumn

st.title("Data Explorer Web App")

st.subheader("File Uploader")
file_uploaded = st.file_uploader("CSV File Uploader", type = ["csv"])

if  file_uploaded is not None:
    csv_file = pd.read_csv(file_uploaded, parse_dates = True)
    st.dataframe(csv_file)
    datetime_col = csv_file.select_dtypes(include = ["datetime64"])
    datetime_col.columns = datetime_col.columns.str.replace(' ','_') # replace the column has space with '_'

for (columnname, columndata) in datetime_col.iteritems():
    DateColumn.get_data(columnname)
    
    column_name = DateColumn.get_name()
    col_num = 0
    st.markdown(f"**. {col_num} Field Name:** **_{column_name}_**")
    col_num = col_num + 1

    uniquedate = DateColumn.get_unique()
    missingdate = DateColumn.get_missing()
    weekenddate = DateColumn.get_weekend()
    weekdaydate =DateColumn.get_weekday()
    futuredate = DateColumn.get_future
    empty1900date = DateColumn.get_empty_1900()
    empty1970date = DateColumn.get_empty_1970()
    mindate = DateColumn.get_min()
    maxdate = DateColumn.get_max()

    data = {"Summary Information" : ["Number of Unique Values", "Number of Rows with Missing Values", "Number of Weekend Dates", "Number of Weekday Dates", "Number of Dates in Future", "Number of Rows with 1900-01-01", "Number of Rows with 1970-01-01", "Minimum Value", "Maximum Value"], 
    "Value" : [uniquedate, missingdate, weekenddate, weekdaydate, futuredate, empty1900date, empty1970date, mindate, maxdate]}
    display_sumdate = pd.DataFrame(data)
    st.write(display_sumdate)