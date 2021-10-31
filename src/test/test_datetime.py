import unittest
from collections import Counter
from altair.vegalite.v4.schema.core import CompositeMarkDef
import pandas as pd
import altair as alt
import sys
sys.path.append("../")
from date_time import DateColumn

class Test_datetime_name(unittest.TestCase):
    def setup(self):
        self.strname = "nametest"
        
    def test_name(self):
        strname = "nametest"
        dc = DateColumn()
        result = dc.get_name()
        output = result(strname)
        self.assertEqual(output, self.strname)

    def test_nameempty(self):
        nameempty = ""
        dc = DateColumn()
        with self.assertRaises(Exception):
            dc.get_name(nameempty)

    def test_namenone(self):
        namenone = None
        dc = DateColumn()
        with self.assertRaises(Exception):
            dc.get_name(namenone)
        
    def test_nameint(self):
        numname = 1
        dc = DateColumn()
        with self.assertRaises(Exception):
            dc.get_name(numname)

# class Test_datetime_data(unittest.TestCase):
#     def setup(self):
#         self.series = pd.stack(pd.DataFrame({"col1" : ['2021-02-27T06:33:45','2021-02-26T07:11:07']}))

#     def test_strdata(self):
#         data = "datatest"
#         dc = DateColumn()
#         result = dc.get_data(data)
#         self.assertEqual(result, False)
    
#     def test_multicol_data(self):
#         data = pd.DataFrame({"col1" : ['2021-02-27T06:33:45','2021-02-26T07:11:07'], 
#                             "col2" : ['2021-02-21T07:50:08', '2021-02-26T07:11:07']})
#         dc = DateColumn()
#         result = dc.get_data(data)
#         self.assertEqual(result, False)
    
#     def test_futuredata(self):
#         data = pd.stack(pd.Series(['2021-12-27T06:33:45','2021-02-26T07:11:07', '2021-02-21T07:50:08']))
#         dc = DateColumn()
#         result = dc.get_data(data)
#         self.assertEqual(result, False)
    
#     def test_data(self):
#         data = self.series
#         dc = DateColumn()
#         result = dc.get_data(data)
#         self.assertEqual(result, True)
    
#     def test_none_data(self):
#         data = None
#         dc = DateColumn()
#         result = dc.get_data(data)
#         self.assertEqual(result, None)
    
#     def test_empty_data(self):
#         data = { 
#         }
#         dc = DateColumn()
#         result = dc.get_data(data)
#         self.assertEqual(result, None)

# class Test_datetime_unique(unittest.TestCase):
#     def setup(self):
#         # different date
#         self.series = pd.stack(pd.DataFrame({"col1" : ['2021-02-27T06:33:45','2021-02-26T07:11:07']}))
#         # same date and time
#         self.series1 = pd.stack(pd.DataFrame({"col1" : ['2021-02-27T06:33:45','2021-02-27T06:33:45']}))

#     def test_strdata(self):
#         data = "datatest"
#         dc = DateColumn()
#         result = dc.get_unique(data)
#         self.assertEqual(result, None)
    
#     def test_multicol_data(self):
#         data = pd.DataFrame({"col1" : ['2021-02-27T06:33:45','2021-02-26T07:11:07'], 
#                             "col2" : ['2021-02-21T07:50:08', '2021-02-26T07:11:07']})
#         dc = DateColumn()
#         result = dc.get_unique(data)
#         self.assertEqual(result, None)
    
#     def test_data(self):
#         data = self.series
#         dc = DateColumn()
#         result = dc.get_unique(data)
#         self.assertEqual(result, 2)
    
#     def test_data1(self):
#         data = self.series1
#         dc = DateColumn()
#         result = dc.get_unique(data)
#         self.assertEqual(result, 1)
    
#     def test_none_data(self):
#         data = None
#         dc = DateColumn()
#         result = dc.get_unique(data)
#         self.assertEqual(result, None)
    
#     def test_empty_data(self):
#         data = { 
#         }
#         dc = DateColumn()
#         result = dc.get_unique(data)
#         self.assertEqual(result, None)

# class Test_datetime_missing(unittest.TestCase):
#     def setup(self):
#         self.series = pd.stack(pd.DataFrame({"col1" : ['2021-02-27T06:33:45','2021-02-26T07:11:07']}))
#         self.series1 = pd.stack(pd.DataFrame({"col1" : [None,'2021-02-26T07:11:07']}))

#     def test_strdata(self):
#         data = "datatest"
#         dc = DateColumn()
#         result = dc.get_missing(data)
#         self.assertEqual(result, None)
    
#     def test_multicol_data(self):
#         data = pd.DataFrame({"col1" : ['2021-02-27T06:33:45','2021-02-26T07:11:07'], 
#                             "col2" : ['2021-02-21T07:50:08', '2021-02-26T07:11:07']})
#         dc = DateColumn()
#         result = dc.get_missing(data)
#         self.assertEqual(result, None)
    
#     def test_data(self):
#         data = self.series
#         dc = DateColumn()
#         result = dc.get_missing(data)
#         self.assertEqual(result, 0)

#     def test_data1(self):
#         data = self.series1
#         dc = DateColumn()
#         result = dc.get_missing(data)
#         self.assertEqual(result, 1)
    
#     def test_none_data(self):
#         data = None
#         dc = DateColumn()
#         result = dc.get_missing(data)
#         self.assertEqual(result, None)
    
#     def test_empty_data(self):
#         data = { 
#         }
#         dc = DateColumn()
#         result = dc.get_missing(data)
#         self.assertEqual(result, None)

# class Test_datetime_weekend(unittest.TestCase):
#     def setup(self):
#         # 26th Friday, 27th Saturday
#         self.series = pd.stack(pd.DataFrame({"col1" : ['2021-02-27T06:33:45','2021-02-26T07:11:07']}))
#         # 28th Sunday, 27th Saturday
#         self.series1 = pd.stack(pd.DataFrame({"col1" : ['2021-02-27T06:33:45','2021-02-28T07:11:07']}))
#         # 26th Friday, 25th Thursday
#         self.series2 = pd.stack(pd.DataFrame({"col1" : ['2021-02-25T06:33:45','2021-02-26T07:11:07']}))

#     def test_strdata(self):
#         data = "datatest"
#         dc = DateColumn()
#         result = dc.get_weekend(data)
#         self.assertEqual(result, None)
    
#     def test_multicol_data(self):
#         data = pd.DataFrame({"col1" : ['2021-02-27T06:33:45','2021-02-26T07:11:07'], 
#                             "col2" : ['2021-02-21T07:50:08', '2021-02-26T07:11:07']})
#         dc = DateColumn()
#         result = dc.get_weekend(data)
#         self.assertEqual(result, None)
    
#     def test_data(self):
#         data = self.series
#         dc = DateColumn()
#         result = dc.get_weekend(data)
#         self.assertEqual(result, 1)
    
#     def test_data1(self):
#         data = self.series1
#         dc = DateColumn()
#         result = dc.get_weekend(data)
#         self.assertEqual(result, 2)
    
#     def test_data2(self):
#         data = self.series2
#         dc = DateColumn()
#         result = dc.get_weekend(data)
#         self.assertEqual(result, 0)
    
#     def test_none_data(self):
#         data = None
#         dc = DateColumn()
#         result = dc.get_weekend(data)
#         self.assertEqual(result, None)
    
#     def test_empty_data(self):
#         data = { 
#         }
#         dc = DateColumn()
#         result = dc.get_weekend(data)
#         self.assertEqual(result, None)

# class Test_datetime_weekday(unittest.TestCase):
#     def setup(self):
#         # 26th Friday, 27th Saturday
#         self.series = pd.stack(pd.DataFrame({"col1" : ['2021-02-27T06:33:45','2021-02-26T07:11:07']}))
#         # 28th Sunday, 27th Saturday
#         self.series1 = pd.stack(pd.DataFrame({"col1" : ['2021-02-27T06:33:45','2021-02-28T07:11:07']}))
#         # 26th Friday, 25th Thursday
#         self.series2 = pd.stack(pd.DataFrame({"col1" : ['2021-02-25T06:33:45','2021-02-26T07:11:07']}))


#     def test_strdata(self):
#         data = "datatest"
#         dc = DateColumn()
#         result = dc.get_weekday(data)
#         self.assertEqual(result, None)
    
#     def test_multicol_data(self):
#         data = pd.DataFrame({"col1" : ['2021-02-27T06:33:45','2021-02-26T07:11:07'], 
#                             "col2" : ['2021-02-21T07:50:08', '2021-02-26T07:11:07']})
#         dc = DateColumn()
#         result = dc.get_weekday(data)
#         self.assertEqual(result, None)
    
#     def test_data(self):
#         data = self.series
#         dc = DateColumn()
#         result = dc.get_weekday(data)
#         self.assertEqual(result, 1)
    
#     def test_data1(self):
#         data = self.series1
#         dc = DateColumn()
#         result = dc.get_weekday(data)
#         self.assertEqual(result, 0)
    
#     def test_data2(self):
#         data = self.series2
#         dc = DateColumn()
#         result = dc.get_weekday(data)
#         self.assertEqual(result, 2)
    
#     def test_none_data(self):
#         data = None
#         dc = DateColumn()
#         result = dc.get_weekday(data)
#         self.assertEqual(result, None)
    
#     def test_empty_data(self):
#         data = { 
#         }
#         dc = DateColumn()
#         result = dc.get_weekday(data)
#         self.assertEqual(result, None)

# class Test_datetime_future(unittest.TestCase):
#     def setup(self):
#         # 26th Friday, 27th Saturday (February 2021)
#         self.series = pd.stack(pd.DataFrame({"col1" : ['2021-02-27T06:33:45','2021-02-26T07:11:07']}))
#         # 28th Sunday February 2021 , 27th Monday December 2021
#         self.series1 = pd.stack(pd.DataFrame({"col1" : ['2021-12-27T06:33:45','2021-02-28T07:11:07']}))
#         # 26th Sunday, 25th Saturday December 2021
#         self.series2 = pd.stack(pd.DataFrame({"col1" : ['2021-12-25T06:33:45','2021-12-26T07:11:07']}))


#     def test_strdata(self):
#         data = "datatest"
#         dc = DateColumn()
#         result = dc.get_future(data)
#         self.assertEqual(result, None)
    
#     def test_multicol_data(self):
#         data = pd.DataFrame({"col1" : ['2021-02-27T06:33:45','2021-02-26T07:11:07'], 
#                             "col2" : ['2021-02-21T07:50:08', '2021-02-26T07:11:07']})
#         dc = DateColumn()
#         result = dc.get_future(data)
#         self.assertEqual(result, None)
    
#     def test_data(self):
#         data = self.series
#         dc = DateColumn()
#         result = dc.get_future(data)
#         self.assertEqual(result, 0)
    
#     def test_data1(self):
#         data = self.series1
#         dc = DateColumn()
#         result = dc.get_future(data)
#         self.assertEqual(result, 1)
    
#     def test_data2(self):
#         data = self.series2
#         dc = DateColumn()
#         result = dc.get_future(data)
#         self.assertEqual(result, 2)
    
#     def test_none_data(self):
#         data = None
#         dc = DateColumn()
#         result = dc.get_future(data)
#         self.assertEqual(result, None)
    
#     def test_empty_data(self):
#         data = { 
#         }
#         dc = DateColumn()
#         result = dc.get_future(data)
#         self.assertEqual(result, None)

# class Test_datetime_1900(unittest.TestCase):
#     def setup(self):
#         # 26th Friday, 27th Saturday (February 2021)
#         self.series = pd.stack(pd.DataFrame({"col1" : ['2021-02-27T06:33:45','2021-02-26T07:11:07']}))
#         # 1 January 1900 , 27th Monday December 2021
#         self.series1 = pd.stack(pd.DataFrame({"col1" : ['2021-12-27T06:33:45','1900-01-01T07:11:07']}))
#         # 1 January 1900, 1 January 1900
#         self.series2 = pd.stack(pd.DataFrame({"col1" : ['1900-01-01T06:33:45','1900-01-01T07:11:07']}))

#     def test_strdata(self):
#         data = "datatest"
#         dc = DateColumn()
#         result = dc.get_empty_1900(data)
#         self.assertEqual(result, None)
    
#     def test_multicol_data(self):
#         data = pd.DataFrame({"col1" : ['2021-02-27T06:33:45','2021-02-26T07:11:07'], 
#                             "col2" : ['2021-02-21T07:50:08', '2021-02-26T07:11:07']})
#         dc = DateColumn()
#         result = dc.get_empty_1900(data)
#         self.assertEqual(result, None)
    
#     def test_data(self):
#         data = self.series
#         dc = DateColumn()
#         result = dc.get_empty_1900(data)
#         self.assertEqual(result, 0)
    
#     def test_data1(self):
#         data = self.series1
#         dc = DateColumn()
#         result = dc.get_empty_1900(data)
#         self.assertEqual(result, 1)
    
#     def test_data2(self):
#         data = self.series2
#         dc = DateColumn()
#         result = dc.get_empty_1900(data)
#         self.assertEqual(result, 2)
    
#     def test_none_data(self):
#         data = None
#         dc = DateColumn()
#         result = dc.get_empty_1900(data)
#         self.assertEqual(result, None)
    
#     def test_empty_data(self):
#         data = { 
#         }
#         dc = DateColumn()
#         result = dc.get_empty_1900(data)
#         self.assertEqual(result, None)

# class Test_datetime_1970(unittest.TestCase):
#     def setup(self):
#         # 26th Friday, 27th Saturday (February 2021)
#         self.series = pd.stack(pd.DataFrame({"col1" : ['2021-02-27T06:33:45','2021-02-26T07:11:07']}))
#         # 1 January 1970 , 27th Monday December 2021
#         self.series1 = pd.stack(pd.DataFrame({"col1" : ['2021-12-27T06:33:45','1970-01-01T07:11:07']}))
#         # 1 January 1970, 1 January 1970
#         self.series2 = pd.stack(pd.DataFrame({"col1" : ['1970-01-01T06:33:45','1970-01-01T07:11:07']}))

#     def test_strdata(self):
#         data = "datatest"
#         dc = DateColumn()
#         result = dc.get_empty_1970(data)
#         self.assertEqual(result, None)
    
#     def test_multicol_data(self):
#         data = pd.DataFrame({"col1" : ['2021-02-27T06:33:45','2021-02-26T07:11:07'], 
#                             "col2" : ['2021-02-21T07:50:08', '2021-02-26T07:11:07']})
#         dc = DateColumn()
#         result = dc.get_empty_1970(data)
#         self.assertEqual(result, None)
    
#     def test_data(self):
#         data = self.series
#         dc = DateColumn()
#         result = dc.get_empty_1970(data)
#         self.assertEqual(result, 0)
    
#     def test_data1(self):
#         data = self.series1
#         dc = DateColumn()
#         result = dc.get_empty_1970(data)
#         self.assertEqual(result, 1)
    
#     def test_data2(self):
#         data = self.series2
#         dc = DateColumn()
#         result = dc.get_empty_1970(data)
#         self.assertEqual(result, 2)
    
#     def test_none_data(self):
#         data = None
#         dc = DateColumn()
#         result = dc.get_empty_1970(data)
#         self.assertEqual(result, None)
    
#     def test_empty_data(self):
#         data = { 
#         }
#         dc = DateColumn()
#         result = dc.get_empty_1970(data)
#         self.assertEqual(result, None)

# class Test_datetime_min(unittest.TestCase):
#     def setup(self):
#         # 26th Friday, 27th Saturday (February 2021)
#         self.series = pd.stack(pd.DataFrame({"col1" : ['2021-02-27T06:33:45','2021-02-26T07:11:07']}))
#         # 1 January 1970, 1 January 1970
#         self.series1 = pd.stack(pd.DataFrame({"col1" : ['1970-01-01T06:33:45','1970-01-01T06:33:45']}))
#         # 1 January 1970, 1 January 1970 (different times)
#         self.series2 = pd.stack(pd.DataFrame({"col1" : ['1970-01-01T07:33:45','1970-01-01T06:33:45']}))

#     def test_strdata(self):
#         data = "datatest"
#         dc = DateColumn()
#         result = dc.get_min(data)
#         self.assertEqual(result, None)
    
#     def test_multicol_data(self):
#         data = pd.DataFrame({"col1" : ['2021-02-27T06:33:45','2021-02-26T07:11:07'], 
#                             "col2" : ['2021-02-21T07:50:08', '2021-02-26T07:11:07']})
#         dc = DateColumn()
#         result = dc.get_min(data)
#         self.assertEqual(result, None)
    
#     def test_data(self):
#         data = self.series
#         dc = DateColumn()
#         result = dc.get_min(data)
#         self.assertEqual(result, '2021-02-26T07:11:07')
    
#     def test_data1(self):
#         data = self.series1
#         dc = DateColumn()
#         result = dc.get_min(data)
#         self.assertEqual(result, '1970-01-01T06:33:45')
    
#     def test_data2(self):
#         data = self.series2
#         dc = DateColumn()
#         result = dc.get_min(data)
#         self.assertEqual(result, '1970-01-01T06:33:45')
    
#     def test_none_data(self):
#         data = None
#         dc = DateColumn()
#         result = dc.get_min(data)
#         self.assertEqual(result, None)
    
#     def test_empty_data(self):
#         data = { 
#         }
#         dc = DateColumn()
#         result = dc.get_min(data)
#         self.assertEqual(result, None)

# class Test_datetime_max(unittest.TestCase):
#     def setup(self):
#         # 26th Friday, 27th Saturday (February 2021)
#         self.series = pd.stack(pd.DataFrame({"col1" : ['2021-02-27T06:33:45','2021-02-26T07:11:07']}))
#         # 1 January 1970, 1 January 1970 (same times)
#         self.series1 = pd.stack(pd.DataFrame({"col1" : ['1970-01-01T06:33:45','1970-01-01T06:33:45']}))
#         # 1 January 1970, 1 January 1970 (different times)
#         self.series2 = pd.stack(pd.DataFrame({"col1" : ['1970-01-01T07:33:45','1970-01-01T06:33:45']}))

#     def test_strdata(self):
#         data = "datatest"
#         dc = DateColumn()
#         result = dc.get_max(data)
#         self.assertEqual(result, None)
    
#     def test_multicol_data(self):
#         data = pd.DataFrame({"col1" : ['2021-02-27T06:33:45','2021-02-26T07:11:07'], 
#                             "col2" : ['2021-02-21T07:50:08', '2021-02-26T07:11:07']})
#         dc = DateColumn()
#         result = dc.get_max(data)
#         self.assertEqual(result, None)
    
#     def test_data(self):
#         data = self.series
#         dc = DateColumn()
#         result = dc.get_max(data)
#         self.assertEqual(result, '2021-02-27T06:33:45')
    
#     def test_data1(self):
#         data = self.series1
#         dc = DateColumn()
#         result = dc.get_max(data)
#         self.assertEqual(result, '1970-01-01T06:33:45')

#     def test_data2(self):
#         data = self.series2
#         dc = DateColumn()
#         result = dc.get_max(data)
#         self.assertEqual(result, '1970-01-01T07:33:45')
    
#     def test_none_data(self):
#         data = None
#         dc = DateColumn()
#         result = dc.get_max(data)
#         self.assertEqual(result, None)
    
#     def test_empty_data(self):
#         data = { 
#         }
#         dc = DateColumn()
#         result = dc.get_max(data)
#         self.assertEqual(result, None)

# class Test_datetime_bar(unittest.TestCase):
#     def setup(self):
#         # 26th Friday, 27th Saturday (February 2021)
#         self.series = pd.stack(pd.DataFrame({"col1" : ['2021-02-27T06:33:45','2021-02-26T07:11:07']}))
#         count_freq = Counter(self.series)
#         dt_freq = count_freq.most_common()
#         dates_freq = pd.DataFrame(dt_freq, columns=["Datetime_col", "Frequency"])
       
#        # barchart for self series
#         self.bar_chart = alt.Chart(dates_freq).mark_bar().encode(
#         x = "Datetime_col",
#         y = "Frequency"
#         ).properties(
#         width = 400,
#         height = 400
#         )

#     def test_strdata(self):
#         data = "datatest"
#         dc = DateColumn()
#         result = dc.get_barchart(data)
#         self.assertEqual(result, None)
    
#     def test_multicol_data(self):
#         data = pd.DataFrame({"col1" : ['2021-02-27T06:33:45','2021-02-26T07:11:07'], 
#                             "col2" : ['2021-02-21T07:50:08', '2021-02-26T07:11:07']})
#         dc = DateColumn()
#         result = dc.get_barchart(data)
#         self.assertEqual(result, None)
    
#     def test_data(self):
#         data = self.series
#         dc = DateColumn()
#         result = dc.get_barchart(data)
#         self.assertEqual(result, self.bar_chart)
    
#     def test_none_data(self):
#         data = None
#         dc = DateColumn()
#         result = dc.get_barchart(data)
#         self.assertEqual(result, None)
    
#     def test_empty_data(self):
#         data = { 
#         }
#         dc = DateColumn()
#         result = dc.get_barchart(data)
#         self.assertEqual(result, None)

# class Test_datetime_frequent(unittest.TestCase):
#     def setup(self):
#         # 26th Friday, 27th Saturday (February 2021)
#         self.series = pd.stack(pd.DataFrame({"col1" : ['2021-02-27T06:33:45','2021-02-26T07:11:07']}))

#         # frequency table for self series
#         count_most_freq = Counter(self.serie)
#         most_freq_20 = count_most_freq.most_common(20)
#         df_most_freq_20 = pd.DataFrame(most_freq_20, columns=["value", "occurrence"])
#         df_most_freq_20["percentage"] = df_most_freq_20["occurrence"]/df_most_freq_20["occurrence"].sum() * 100
#         self.df_most_freq_20 = df_most_freq_20

#     def test_strdata(self):
#         data = "datatest"
#         dc = DateColumn()
#         result = dc.get_frequent(data)
#         self.assertEqual(result, None)
    
#     def test_multicol_data(self):
#         data = pd.DataFrame({"col1" : ['2021-02-27T06:33:45','2021-02-26T07:11:07'], 
#                             "col2" : ['2021-02-21T07:50:08', '2021-02-26T07:11:07']})
#         dc = DateColumn()
#         result = dc.get_frequent(data)
#         self.assertEqual(result, None)
    
#     def test_data(self):
#         data = self.series
#         dc = DateColumn()
#         result = dc.get_frequent(data)
#         self.assertEqual(result, self.df_most_freq_20)
    
#     def test_none_data(self):
#         data = None
#         dc = DateColumn()
#         result = dc.get_frequent(data)
#         self.assertEqual(result, None)
    
#     def test_empty_data(self):
#         data = { 
#         }
#         dc = DateColumn()
#         result = dc.get_frequent(data)
#         self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()