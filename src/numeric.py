# To be filled by students
from _typeshed import Self
import streamlit as st
from dataclasses import dataclass
import pandas as pd
import altair as alt
import statistics as stat
import numpy as numpy



@dataclass
class NumericColumn:
  col_name: str = None #not sure
  serie: pd.Series = None
 
  def get_name(self):
    """
    Return name of selected column
    df 
    """
   return self.name

  def get_unique(self):
    """
    Return number of unique values for selected column
    """
    #return len(self.serie.unique().tolist())

    #
    # return df.get_unique()

        for x in self:
        # check if exists in unique_list or not
        if x not in self:
            self.append(x)


  def get_missing(self):
    """
    Return number of missing values for selected column
    """
   return self.serie.isna().sum()

  def get_zeros(self):
    """
    Return number of occurrence of 0 value for selected column
    """

    return sum(self.serie.str.is0().fillna(True))

  def get_negatives(self):
    """
    Return number of negative values for selected column
    """
    return None

  def get_mean(self):
    """
    Return the average value for selected column
    """
    return stat.mean(Self)

## https://stackabuse.com/calculating-mean-median-and-mode-in-python/


  def get_std(self):
    """
    Return the standard deviation value for selected column
    """
    return numpy.std(self)
  
  def get_min(self):
    """
    Return the minimum value for selected column
    """
    return min(self)

  def get_max(self):
    """
    Return the maximum value for selected column
    """
    return max(self)

  def get_median(self):
    """
    Return the median value for selected column
    """
    import numpy

    x = numpy.median(self)
    return(x)

  def get_histogram(self):
    """
    Return the generated histogram for selected column
    """
    fig = ff.create_distplot(
...         self, group_labels, bin_size=[25])

# https://docs.streamlit.io/library/api-reference/charts/st.plotly_chart

  def get_frequent(self):
    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    """
    data = {'value':self.serie} 
    df = pd.DataFrame(data)
    df_frequent = df.groupby('value').size().reset_index(name = 'occurrence_0')
    df_frequent['percentage'] = df_frequent['occurrence_0']/df_frequent['occurrence_0'].sum()r
