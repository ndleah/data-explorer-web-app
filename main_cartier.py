from datetime import datetime
from altair.vegalite.v4.schema.core import Datasets
import pandas as pd
from pandas.core.frame import DataFrame
import streamlit as st
from src import DateColumn

st.title("Data Explorer Web App")

st.subheader("File Uploader")
file_uploaded = st.file_uploader("CSV File Uploader", type = ["csv"])

if  file_uploaded is not None:
    csv_file = pd.read_csv(file_uploaded, parse_dates = True)
    st.dataframe(csv_file)
    csv_file["timestamp"] = pd.to_datetime(csv_file["timestamp"], errors = "ignore")
    datetime_col = csv_file.select_dtypes(include = ["datetime64"])
    datetime_col.columns = datetime_col.columns.str.replace(' ','_') # replace the column has space with '_'
    
    datecol_object = DateColumn(col_name = datetime_col.columns, serie = datetime_col.stack())
    #for (columnname, columndata) in datetime_col.iteritems():
    st.markdown(f"**4.0 Field Name: _{datetime_col.columns}_**")
    # datecol_object.get_data(columnname, columndata)
    

    uniquedate = datecol_object.get_unique()
    missingdate = datecol_object.get_missing()
    weekenddate = datecol_object.get_weekend()
    weekdaydate =datecol_object.get_weekday()
    futuredate = datecol_object.get_future()
    empty1900date = datecol_object.get_empty_1900()
    empty1970date = datecol_object.get_empty_1970()
    mindate = datecol_object.get_min()
    maxdate = datecol_object.get_max()


    data1 = { "" : ["Number of Unique Values", 
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
    
    display_sumdate = pd.DataFrame(data1)
    st.markdown("**DateTime Bar Chart**")
    st.write(display_sumdate)

    # bar chart
    st.markdown("**DateTime Bar Chart**")
    st.altair_chart(datecol_object.get_barchart())

    # create frequency table
    st.markdown('**Most Frequent DateTime Values**')
    frequencies = datecol_object.dt_freq_percent()
    st.write(frequencies)

    # goal to link with leah datetime transformed and parse it through my script to see if table and graph works

    #data = {
    #     "Value" : pd.Series(
    #         [uniquedate, 
    #         missingdate, 
    #         weekenddate, 
    #         weekdaydate, 
    #         futuredate, 
    #         empty1900date, 
    #         empty1970date, 
    #         mindate, 
    #         maxdate
    #         ],
    #     index = [
    #         "Number of Unique Values", 
    #         "Number of Rows with Missing Values", 
    #         "Number of Weekend Dates", 
    #         "Number of Weekday Dates", 
    #         "Number of Dates in Future", 
    #         "Number of Rows with 1900-01-01", 
    #         "Number of Rows with 1970-01-01", 
    #         "Minimum Value", 
    #         "Maximum Value"
    #         ]
    #         )
    #         }