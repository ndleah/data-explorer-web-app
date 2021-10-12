# To be filled by students
import streamlit as st
from dataclasses import dataclass
import pandas as pd



@dataclass
class NumericColumn:
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

  def get_zeros(self):
    """
    Return number of occurrence of 0 value for selected column
    """
    return None

  def get_negatives(self):
    """
    Return number of negative values for selected column
    """
    return None

  def get_mean(self):
    """
    Return the average value for selected column
    """
    return None

  def get_std(self):
    """
    Return the standard deviation value for selected column
    """
    return None
  
  def get_min(self):
    """
    Return the minimum value for selected column
    """
    return None

  def get_max(self):
    """
    Return the maximum value for selected column
    """
    return None

  def get_median(self):
    """
    Return the median value for selected column
    """
    return None

  def get_histogram(self):
    """
    Return the generated histogram for selected column
    """
    return None

  def get_frequent(self):
    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    """
    return None
