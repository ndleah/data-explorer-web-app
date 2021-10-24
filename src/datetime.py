from collections import Counter
from datetime import datetime as dt
from pandas.core.frame import DataFrame
import streamlit as st
from dataclasses import dataclass
import pandas as pd
import altair as alt


@dataclass
class DateColumn:
  col_name: str
  serie: pd.Series

  def get_data(self, name, dfdata):
    self.col_name = name
    self.serie = dfdata

  def get_name(self):
    """
    Return name of selected column
    """
    return self.col_name

  def get_unique(self):
    """
    Return number of unique values for selected column
    """
    set_date = set(self.serie)
    number_of_unique_values = len(set_date)
    return number_of_unique_values
  
  def get_missing(self):
    """
    Return number of missing values for selected column
    """
    missing_values = self.serie.isnull().sum()
    return missing_values


  def get_weekend(self):
    """
    Return number of occurrence of days falling during weekend (Saturday and Sunday)
    """
    date_weekday = self.serie.weekday()
    weekend_count = len([day_num for day_num in date_weekday if day_num > 4])
    return weekend_count


  def get_weekday(self):
    """
    Return number of weekday days (not Saturday or Sunday)
    """
    date_weekday = self.serie.weekday()
    weekday_count = len([day_num for day_num in date_weekday if day_num < 5])
    return weekday_count

  
  def get_future(self):
    """
    Return number of cases with future dates (after today)
    """
    today = dt.today()
    future_dates = [dates for dates in self.serie if dates > today]
    number_of_dates_after_today = len(future_dates)
    return number_of_dates_after_today

  def get_empty_1900(self):
    """
    Return number of occurrence of 1900-01-01 value
    """
    dates_1900 = [dates for dates in self.serie if dates == "1900-01-01"]
    number_of_dates_1900 = len(dates_1900)
    return number_of_dates_1900

  def get_empty_1970(self):
    """
    Return number of occurrence of 1970-01-01 value
    """
    dates_1970 = [dates for dates in self.serie if dates == "1970-01-01"]
    number_of_dates_1970 = len(dates_1970)
    return number_of_dates_1970

  def get_min(self):
    """
    Return the minimum date
    """
    min_date = min(self.serie)
    return min_date

  def get_max(self):
    """
    Return the maximum date 
    """
    max_date = max(self.serie)
    return max_date

  def get_barchart(self):
    """
    Return the generated bar chart for selected column
    """
    count_freq = Counter(self.serie)
    dt_freq = count_freq.most_common()
    dates_freq = pd.DataFrame(dt_freq, columns=["Datetime_col", "Frequency"])
    bar_chart = alt.Chart(dates_freq).mark_bar().encode(
      x = "Datetime_col",
      y = "Frequency"
    )
    return bar_chart

  def get_frequent(self):
    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    """
    count_most_freq = Counter(self.serie)
    most_freq_20 = count_most_freq.most_common(20)
    df_most_freq_20 = pd.DataFrame(most_freq_20, columns=["value", "occurrence"])
    percent_of_total = df_most_freq_20[1]/len(self.serie)
    df_most_freq_20["percentage"] = percent_of_total
    df_most_20_freq_percent = pd.dataframe(df_most_freq_20)
    return df_most_20_freq_percent

def dt_freq_percent():
    """
    Return streamlit table containing number of occurrence and percentage for each value
    """
    most_freq = DateColumn.df_most_20_freq_percent
    st_table_dt_freq_percent = st.table(most_freq)
    return st_table_dt_freq_percent