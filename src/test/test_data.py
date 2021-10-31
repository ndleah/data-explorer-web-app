import unittest
import pandas as pd
import numpy as np

# change this to the path of your module
import sys
sys.path.append('../')

# import your modules
from data import Dataset

class TestGetName(unittest.TestCase):
    def test_get_name(self):
        data = [['tom', 10], ['nick', 15], ['juli', 14]]
        test_df = pd.DataFrame(data, columns = ['Name', 'Age'])
        test_file_name = "car_accident.csv"
        test_dataset = Dataset(test_df, test_file_name)
        self.assertEqual(test_dataset.get_name(), test_file_name)


class TestNRows(unittest.TestCase):
    def test_get_n_rows(self):
        # create sample dataframe
        data = [['tom', 10], ['nick', 15], ['juli', 14]]
        test_df = pd.DataFrame(data, columns = ['Name', 'Age'])
        test_file_name = "car_accident.csv"
        test_dataset = Dataset(test_df, test_file_name)
        self.assertEqual(test_dataset.get_n_rows(), 3)


class TestNColumns(unittest.TestCase):
    def test_get_n_cols(self):
        # create sample dataframe
        data = [['tom', 10], ['nick', 15], ['juli', 14]]
        test_df = pd.DataFrame(data, columns = ['Name', 'Age'])
        test_file_name = "car_accident.csv"
        test_dataset = Dataset(test_df, test_file_name)
        self.assertEqual(test_dataset.get_n_cols(), 2)


class TestColumnLists(unittest.TestCase):
    def test_get_cols_list(self):
        # create sample dataframe
        data = [['tom', 10], ['nick', 15], ['juli', 14]]
        test_df = pd.DataFrame(data, columns = ['Name', 'Age'])
        test_file_name = "car_accident.csv"
        test_dataset = Dataset(test_df, test_file_name)
        test_cols_list = ['Name', 'Age']
        self.assertEqual(test_dataset.get_cols_list(), test_cols_list)

class TestColumnTypes(unittest.TestCase):
    def test_get_cols_dtype(self):
        # create sample dataframe
        details = [
    {
        "title": "Health Canada",
        "score": 7,
        "comms_num": 0,
        "created": 1614400425,
        "timestamp": "2/27/21 6:33"
    },
    {
        "title": "Canada",
        "score": 2,
        "comms_num": 1,
        "created": 1614316267,
        "timestamp": "2/28/21 6:33"
    },
    {
        "title": "Coronavirus",
        "score": 6,
        "comms_num": 0,
        "created": 1613886608,
        "timestamp": "3/1/21 6:33"
    }]
        test_df = pd.DataFrame(details)
        test_file_name = "car_accident.csv"
        test_dataset = Dataset(test_df, test_file_name)
        test_cols_type = {'comms_num': 'int64',
                        'created': 'int64',
                        'score': 'int64',
                        'timestamp': 'object',
                        'title': 'object'}
        self.assertEqual(test_dataset.get_cols_dtype(), test_cols_type)

class TestNDuplicate(unittest.TestCase):
    def test_get_n_duplicates(self):
        # create sample dataframe
        details = [
    {
        "title": "Health Canada",
        "score": 7,
        "comms_num": 1,
        "created": 1614400425,
        "timestamp": "2/27/21 6:33"
    },
    {
        "title": "Health Canada",
        "score": 7,
        "comms_num": 1,
        "created": 1614400425,
        "timestamp": "2/27/21 6:33"
    },
    {
        "title": "Health Canada",
        "score": 6,
        "comms_num": 1,
        "created": 1613886608,
        "timestamp": "3/1/21 6:33"
    }]
        test_df = pd.DataFrame(details)
        test_file_name = "car_accident.csv"
        test_dataset = Dataset(test_df, test_file_name)
        self.assertEqual(test_dataset.get_n_duplicates(), 1)

class TestNMissing(unittest.TestCase):
    def test_get_n_missing(self):
        # create sample dataframe
        details = [
    {
        "title": np.nan,
        "score": np.nan,
        "comms_num": np.nan,
        "created": np.nan,
        "timestamp": np.nan
    },
    {
        "title": "Health Canada",
        "score": 7,
        "comms_num": 1,
        "created": 1614400425,
        "timestamp": "2/27/21 6:33"
    },
    {
        "title": "Health Canada",
        "score": 6,
        "comms_num": 1,
        "created": 1613886608,
        "timestamp": "3/1/21 6:33"
    }]
        test_df = pd.DataFrame(details)
        test_file_name = "car_accident.csv"
        test_dataset = Dataset(test_df, test_file_name)
        self.assertEqual(test_dataset.get_n_missing(), 1)


# class GetHead(unittest.TestCase):
#     def test_get_head(self):
#         # create sample dataframe
#         data = [['tom', 10], ['nick', 15], ['juli', 14], ['annie', 24], ['julie', 20], ['leah', 18],['patrick', 27]]
#         test_df = pd.DataFrame(data, columns = ['Name', 'Age'])
#         test_file_name = "car_accident.csv"
#         test_dataset = Dataset(test_df, test_file_name)
#         self.assertEqual(test_dataset.get_head(), test_df.head())

# class GetTail(unittest.TestCase):
#     def test_get_tail(self):
#         # create sample dataframe
#         data = [['tom', 10], ['nick', 15], ['juli', 14], ['annie', 24], ['julie', 20], ['leah', 18],['patrick', 27]]
#         test_df = pd.DataFrame(data, columns = ['Name', 'Age'])
#         test_file_name = "car_accident.csv"
#         test_dataset = Dataset(test_df, test_file_name)
#         self.assertEqual(test_dataset.get_tail(2), test_df.tail(2))


# class GetSample(unittest.TestCase):
#     def test_get_sample(self):
#         # create sample dataframe
#         data = [['tom', 10], ['nick', 15], ['juli', 14], ['annie', 24], ['julie', 20], ['leah', 18],['patrick', 27]]
#         test_df = pd.DataFrame(data, columns = ['Name', 'Age'])
#         test_file_name = "car_accident.csv"
#         test_dataset = Dataset(test_df, test_file_name)
#         self.assertEqual(test_df.get_tail(2), test_df.tail(2))


class GetNumericColumns(unittest.TestCase):
    def test_get_numeric_columns(self):
        # create sample dataframe
        data = [['tom', 10], ['nick', 15], ['juli', 14]]
        test_df = pd.DataFrame(data, columns = ['Name', 'Age'])
        test_file_name = "car_accident.csv"
        test_dataset = Dataset(test_df, test_file_name)
        self.assertEqual(test_dataset.get_numeric_columns(), ['Age'])


class GetTextColumns(unittest.TestCase):
    def test_get_numeric_columns(self):
        # create sample dataframe
        data = [['tom', 10], ['nick', 15], ['juli', 14]]
        test_df = pd.DataFrame(data, columns = ['Name', 'Age'])
        test_file_name = "car_accident.csv"
        test_dataset = Dataset(test_df, test_file_name)
        self.assertEqual(test_dataset.get_text_columns(), ['Name'])


class GetDateColumns(unittest.TestCase):
    def test_get_date_columns(self):
        # create sample dataframe
        rng = pd.to_datetime(pd.date_range('2015-02-24', periods=5, freq='T'),errors='ignore')
        test_df = pd.DataFrame({ 'Date': rng, 'Val': np.random.randn(len(rng)) }) 
        test_file_name = "car_accident.csv"
        test_dataset = Dataset(test_df, test_file_name)
        self.assertEqual(test_dataset.get_date_columns(), ['Date'])


if __name__ == '__main__':
    unittest.main()