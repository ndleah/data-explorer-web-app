import unittest
from unittest import mock
from unittest.mock import patch
from collections import Counter
from altair.vegalite.v4.schema.core import CompositeMarkDef
import pandas as pd
import altair as alt
import sys

from pandas.core import series
sys.path.append("../")
from date_time import DateColumn

class Test_datetime_name(unittest.TestCase):
    def test_dt(self):
        strname = "nametest"
        dc = DateColumn(strname)
        result = dc.get_name()
        self.assertEqual(result, "Nametest")

class Test_datetime_unique(unittest.TestCase):
    def test_dt(self):
        # 2 different date
        dataframe = pd.DataFrame(['2021-02-27T06:33:45', '2021-02-26T07:11:07']).stack()
        date_timedata = pd.to_datetime(dataframe, errors='ignore')
        test_col = "test_colname"
        dc = DateColumn(test_col, date_timedata)
        self.assertEqual(dc.get_unique(), 2)

class Test_datetime_missing(unittest.TestCase):
    def test_dt(self):
        # 1 missing date
        dataframe = pd.DataFrame(['2021-02-27T06:33:45', "", '2021-02-26T07:11:07']).stack()
        date_timedata = pd.to_datetime(dataframe, errors='ignore')
        test_col = "test_colname"
        dc = DateColumn(test_col, date_timedata)
        self.assertEqual(dc.get_missing(), 1)

class Test_datetime_weekend(unittest.TestCase):
    def test_dt(self):
        # 1 weekend date
        dataframe = pd.DataFrame(['2021-02-27T06:33:45', '2021-02-26T07:11:07']).stack()
        date_timedata = pd.to_datetime(dataframe, errors='ignore')
        test_col = "test_colname"
        dc = DateColumn(test_col, date_timedata)
        self.assertEqual(dc.get_weekend(), 1)

class Test_datetime_weekday(unittest.TestCase):
    def test_dt(self):
        # 1 weekday date
        dataframe = pd.DataFrame(['2021-02-27T06:33:45', '2021-02-26T07:11:07']).stack()
        date_timedata = pd.to_datetime(dataframe, errors='ignore')
        test_col = "test_colname"
        dc = DateColumn(test_col, date_timedata)
        self.assertEqual(dc.get_weekday(), 1)

class Test_datetime_future(unittest.TestCase):
    def test_dt(self):
        # 1 future date
        dataframe = pd.DataFrame(['2021-12-27T06:33:45', '2021-02-26T07:11:07']).stack()
        date_timedata = pd.to_datetime(dataframe, errors='ignore')
        test_col = "test_colname"
        dc = DateColumn(test_col, date_timedata)
        self.assertEqual(dc.get_future(), 1)

class Test_datetime_1900(unittest.TestCase):
    def test_dt(self):
        # 1 1900 date
        dataframe = pd.DataFrame(['1900-01-01T06:33:45', '2021-02-26T07:11:07']).stack()
        date_timedata = pd.to_datetime(dataframe, errors='ignore')
        test_col = "test_colname"
        dc = DateColumn(test_col, date_timedata)
        self.assertEqual(dc.get_empty_1900(), 1)

class Test_datetime_1970(unittest.TestCase):
    def test_dt(self):
        # 1 1970 date
        dataframe = pd.DataFrame(['1970-01-01T06:33:45', '2021-02-26T07:11:07']).stack()
        date_timedata = pd.to_datetime(dataframe, errors='ignore')
        test_col = "test_colname"
        dc = DateColumn(test_col, date_timedata)
        self.assertEqual(dc.get_empty_1970(), 1)

class Test_datetime_min(unittest.TestCase):
    def test_dt(self):
        dataframe = pd.DataFrame(['1970-01-01T06:33:45', '2021-02-26T07:11:07']).stack()
        date_timedata = pd.to_datetime(dataframe, errors='ignore')
        test_col = "test_colname"
        dc = DateColumn(test_col, date_timedata)
        self.assertEqual(dc.get_min(), pd.to_datetime('1970-01-01T06:33:45'))

class Test_datetime_max(unittest.TestCase):
    def test_dt(self):
        dataframe = pd.DataFrame(['1970-01-01T06:33:45', '2021-02-26T07:11:07']).stack()
        date_timedata = pd.to_datetime(dataframe, errors='ignore')
        test_col = "test_colname"
        dc = DateColumn(test_col, date_timedata)
        self.assertEqual(dc.get_max(), pd.to_datetime('2021-02-26T07:11:07'))

class Test_datetime_bar(unittest.TestCase):
    def test_dt(self):
        dataframe = pd.DataFrame(
            [
        '1970-01-01T06:33:45', 
        '1970-01-01T06:33:45', 
        '1970-01-01T06:33:45', 
        '2021-02-26T07:11:07', 
        '2021-02-26T07:11:07', 
        '2021-02-27T07:11:07'
            ]
            ).stack()

        date_timedata = pd.to_datetime(dataframe, errors='ignore')
        test_col = "test_colname"
        dc = DateColumn(test_col, date_timedata)

        # compare class to expected class
        class_str = str(type(dc.get_barchart()))
        chart_class = class_str.split('"')
        chart_str = chart_class[0]
        self.assertEqual(chart_str, "<class 'altair.vegalite.v4.api.Chart'>")
        
class Test_datetime_frequent(unittest.TestCase):
    def test_dt(self):
        dataframe = pd.DataFrame(
            [
        '1970-01-01T06:33:45', 
        '1970-01-01T06:33:45', 
        '1970-01-01T06:33:45', 
        '2021-02-26T07:11:07', 
        '2021-02-26T07:11:07', 
        '2021-02-27T07:11:07'
            ]
            ).stack()

        date_timedata = pd.to_datetime(dataframe, errors='ignore')
        test_col = "test_colname"
        dc = DateColumn(test_col, date_timedata)
        
        # compare class to expected class
        class_str = str(type(dc.get_frequent()))
        table_class = class_str.split('"')
        chart_str = table_class[0]
        self.assertEqual(chart_str, "<class 'pandas.core.frame.DataFrame'>")

if __name__ == '__main__':
    unittest.main()