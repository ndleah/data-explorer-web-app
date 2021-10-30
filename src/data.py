from pandas.core.frame import DataFrame
import streamlit as st
from dataclasses import dataclass
import pandas as pd


@dataclass
class Dataset:
  df: pd.DataFrame = None
  name: str = None

  def get_name(self):
    """
    Return filename of loaded dataset
    """
    return self.name

  def get_n_rows(self):
    """
      Return number of rows of loaded dataset
    """
    self.df_rows = self.df.shape[0]
    return self.df_rows

  def get_n_cols(self):
    """
      Return number of columns of loaded dataset
    """    
    self.df_col = self.df.shape[1]
    return self.df_col

  def get_cols_list(self):
    """
      Return list column names of loaded dataset
    """
    self.df_col_list = list(self.df.columns)
    return self.df_col_list

  def get_cols_dtype(self):
    """
      Return dictionary with column name as keys and data type as values
    """
    self.df_dict = self.df.dtypes.apply(lambda x: x.name).to_dict()
    return self.df_dict

  def get_n_duplicates(self):
    """
      Return number of duplicated rows of loaded dataset
    """
    self.df_dup_rows = len(self.df)-len(self.df.drop_duplicates())
    return self.df_dup_rows

  def get_n_missing(self):
    """
      Return number of rows with missing values of loaded dataset
    """
    self.df_missing_rows = len(self.df) - len(self.df.dropna())
    return self.df_missing_rows

  def get_head(self, n=5):
    """
      Return Pandas Dataframe with top rows of loaded dataset
    """
    return self.df.iloc[:n]

  def get_tail(self, n=5):
    """
      Return Pandas Dataframe with bottom rows of loaded dataset
    """
    return self.df.iloc[-n:]

  def get_sample(self, n=5):
    """
      Return Pandas Dataframe with random sampled rows of loaded dataset
    """
    return self.df.sample(n=n)

  def get_numeric_columns(self):
    """
      Return list column names of numeric type from loaded dataset
    """
    self.numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    self.df_numeric = self.df.select_dtypes(include=self.numerics).columns.tolist()
    return self.df_numeric

  def get_text_columns(self):
    """
      Return list column names of text type from loaded dataset
    """
    self.df_text = self.df.select_dtypes(include="object").columns
    return self.df_text

  def get_date_columns(self):
    """
      Return list column names of datetime type from loaded dataset
    """
    self.date = ['date', 'time', 'datetime']
    self.df_date = self.df.select_dtypes(include=self.date).columns
    return self.df_date

