# To be filled by students
import streamlit as st
from dataclasses import dataclass
import pandas as pd


@dataclass
class DateColumn:
  col_name: str
  serie: pd.Series

  def get_name(self):
    """
    Return name of selected column
    """
    return None

  def get_unique(self):
    """
    Return number of unique values for selected column
    """
    return None

  def get_missing(self):
    """
    Return number of missing values for selected column
    """
    return None

  def get_weekend(self):
    """
    Return number of occurrence of days falling during weekend (Saturday and Sunday)
    """
    return None

  def get_weekday(self):
    """
    Return number of weekday days (not Saturday or Sunday)
    """
    return None
  
  def get_future(self):
    """
    Return number of cases with future dates (after today)
    """
    return None

  def get_empty_1900(self):
    """
    Return number of occurrence of 1900-01-01 value
    """
    return None

  def get_empty_1970(self):
    """
    Return number of occurrence of 1970-01-01 value
    """
    return None

  def get_min(self):
    """
    Return the minimum date
    """
    return None

  def get_max(self):
    """
    Return the maximum date 
    """
    return None

  def get_barchart(self):
    """
    Return the generated bar chart for selected column
    """
    return None

  def get_frequent(self):
    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    """
    return None