# To be filled by students
import streamlit as st
from dataclasses import dataclass
import pandas as pd


@dataclass
class TextColumn:
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

  def get_empty(self):
    """
    Return number of rows with empty string for selected column
    """
    return None

  def get_whitespace(self):
    """
    Return number of rows with only whitespaces for selected column
    """
    return None

  def get_lowercase(self):
    """
    Return number of rows with only lower case characters for selected column
    """
    return None

  def get_uppercase(self):
    """
    Return number of rows with only upper case characters for selected column
    """
    return None
  
  def get_alphabet(self):
    """
    Return number of rows with only alphabet characters for selected column
    """
    return None

  def get_digit(self):
    """
    Return number of rows with only numbers as characters for selected column
    """
    return None

  def get_mode(self):
    """
    Return the mode value for selected column
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