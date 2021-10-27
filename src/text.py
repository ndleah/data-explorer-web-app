# To be filled by students
import streamlit as st
from dataclasses import dataclass
import pandas as pd
import altair as alt



@dataclass
class TextColumn:
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

  def get_empty(self):
    """
    Return number of rows with empty string for selected column
    """
    return (self.serie.values == '').sum()

  def get_whitespace(self):
    """
    Return number of rows with only whitespaces for selected column
    """
    return sum(self.serie.str.isspace().fillna(False))

  def get_lowercase(self):
    """
    Return number of rows with only lower case characters for selected column
    """
    return sum(self.serie.str.islower().fillna(False))

  def get_uppercase(self):
    """
    Return number of rows with only upper case characters for selected column
    """
    return sum(self.serie.str.isupper().fillna(False))
  
  def get_alphabet(self):
    """
    Return number of rows with only alphabet characters for selected column
    """
    return sum(self.serie.str.isalpha().fillna(False))

  def get_digit(self):
    """
    Return number of rows with only numbers as characters for selected column
    """
    return sum(self.serie.str.isdigit().fillna(False))

  def get_mode(self):
    """
    Return the mode value for selected column
    """
    return self.serie.mode()


  def get_barchart(self):
    """
    Return the generated bar chart for selected column
    """

    data = {self.col_name:self.serie}
    df_barchart = pd.DataFrame(data)
    chart = alt.Chart(df_barchart).mark_bar().encode(x=self.col_name, y='count()')
    return chart

  def get_frequent(self):
    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    """
    data = {'value':self.serie}
    df = pd.DataFrame(data)
    df_frequent = df.groupby('value').size().reset_index(name = 'occurrence')
    df_frequent['percentage'] = df_frequent['occurrence']/df_frequent['occurrence'].sum()
    
    return df_frequent