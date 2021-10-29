from collections import Counter
from datetime import datetime as dt, timedelta
from pandas.core.frame import DataFrame
import streamlit as st
from dataclasses import dataclass
import pandas as pd
import altair as alt


@dataclass
class DateColumn:
  col_name: str = None
  serie: pd.Series = None

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
    day_endweek = self.serie.dt.dayofweek
    weekend_count = len([day_num for day_num in day_endweek if day_num > 4])
    return weekend_count


  def get_weekday(self):
    """
    Return number of weekday days (not Saturday or Sunday)
    """
    day_weekday = self.serie.dt.dayofweek
    weekday_count = len([day_num for day_num in day_weekday if day_num < 5])
    return weekday_count

  
  def get_future(self):
    """
    Return number of cases with future dates (after today)
    """
    today_date = pd.Timestamp.today()
    futuredate = 0
    for dates in self.serie:
      if dates > today_date:
        futuredate = futuredate +1
    return futuredate

  def get_empty_1900(self):
    """
    Return number of occurrence of 1900-01-01 value
    """
    number_of_dates_1900 = len([dates for dates in self.serie if dates == "1900-01-01"])
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
    print(max_date)
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
    ).properties(
      width = 400,
      height = 400
    )
    return bar_chart

  def get_frequent(self):
    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    """
    count_most_freq = Counter(self.serie)
    most_freq_20 = count_most_freq.most_common(20)
    df_most_freq_20 = pd.DataFrame(most_freq_20, columns=["value", "occurrence"])
    df_most_freq_20["percentage"] = df_most_freq_20["occurrence"]/df_most_freq_20["occurrence"].sum() * 100
    return df_most_freq_20