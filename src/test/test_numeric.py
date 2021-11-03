# To be filled by students
import unittest
from collections import Counter
from altair.vegalite.v4.schema.core import X
from numeric import NumericColumn
import pandas as pd
import altair as alt
import numpy as np

# change this to the path of your module
import sys
sys.path.append('../')

# To be filled by students
#from _typeshed import Self
from altair.vegalite.v4.schema.channels import X
import streamlit as st
from dataclasses import dataclass
import pandas as pd
import altair as alt
import statistics as stat
import numpy as numpy


@dataclass
class NumericColumn:
  col_name: str = None
  serie: pd.Series = None

  def get_data(self, name, dfdata):
    self.col_name = name
    self.serie = dfdata
 
  def get_name(self):
    """
    Return name of selected column
    """
    return self.col_name.capitalize()

  def get_unique(self):
    """
    Return number of unique values for selected column
    """
    return len(self.serie.unique().tolist())


  def get_missing(self):
    """
    Return number of missing values for selected column
    """
    return self.serie.isna().sum()

  def get_zeros(self):
    """
    Return number of occurrence of 0 value for selected column
    """

    ##return sum(self.serie.str.is0().fillna(True))

    return (self.serie == 0).sum()


  def get_negatives(self):
    """
    Return number of negative values for selected column
    """
    return (self.serie < 0).sum()

  def get_mean(self):
    """
    Return the average value for selected column
    """
    return self.serie.mean()


  def get_std(self):
    """
    Return the standard deviation value for selected column
    """
    return self.serie.std()
  
  def get_min(self):
    """
    Return the minimum value for selected column
    """
    return self.serie.min()

  def get_max(self):
    """
    Return the maximum value for selected column
    """
    return self.serie.max()

  def get_median(self):
    """
    Return the median value for selected column
    """
    return self.serie.median()

  def get_histogram(self):
    """
    Return the generated histogram for selected column
    """
    data = {self.col_name:self.serie}
    df_barchart = pd.DataFrame(data)
    chart = alt.Chart(df_barchart).mark_bar().encode(alt.X(self.col_name, bin = alt.Bin(step = 50)), y='count()')
    return chart

  def get_frequent(self):
    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    """
    data = {'value':self.serie}
    df = pd.DataFrame(data)
    df = df.head(20)
    df_frequent = df.groupby('value').size().reset_index(name = 'occurrence')
    df_frequent['percentage'] = df_frequent['occurrence']/df_frequent['occurrence'].sum()
    
    return df_frequent