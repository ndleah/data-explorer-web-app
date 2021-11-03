# Import modules and packages
import unittest
from unittest.case import TestCase
from numpy import NaN, zeros 
import pandas as pd
import altair as alt
import sys

sys.path.append("../")
from numeric import NumericColumn

#Test: Create class and get name:

class TestNameColumn(unittest.TestCase):
    def test_get_name(self): 
        numericname = "nametest"
        test_numeric = NumericColumn(numericname)
        self.assertEqual(test_numeric.get_name(), "Nametest")

#Test: Create class and get unique values:

class TestUniqueValues(unittest.TestCase):
    def test_get_unique(self):
       # create sample dataframe
        self.strname = {'test_colname': [0,1,2,3,4.4]}
        test_df = pd.DataFrame(self.strname)
        numeric = NumericColumn()
        for (columnName, columnData) in test_df.iteritems():
            numeric.get_data(columnName, columnData)
            result = numeric.get_unique()
            self.assertEqual(result, 5)

#Test: Create class and get missing values

class TestMissingValues(unittest.TestCase):
     def test_get_missing(self):
       # create sample dataframe
        self.strname = {'test_colname': [0,1,NaN,3,4.4]}
        test_df = pd.DataFrame(self.strname)
        numeric = NumericColumn()
        for (columnName, columnData) in test_df.iteritems():
            numeric.get_data(columnName, columnData)
            result = numeric.get_missing()
            self.assertEqual(result, 1)

#Test: Create class and get zero values

class TestGetZeros(unittest.TestCase):
    def test_get_zeros(self):
       # create sample dataframe
        self.strname = {'test_colname': [0,1,2,3,4.4]}
        test_df = pd.DataFrame(self.strname)
        numeric = NumericColumn()
        for (columnName, columnData) in test_df.iteritems():
            numeric.get_data(columnName, columnData)
            result = numeric.get_zeros()
            self.assertEqual(result, 1)

#Test: Create class and get negative values
class TestGetNegatives(unittest.TestCase):
    def test_get_negatives(self):
       # create sample dataframe
        self.strname = {'test_colname': [0,1,2,3,4.4,-5]}
        test_df = pd.DataFrame(self.strname)
        numeric = NumericColumn()
        for (columnName, columnData) in test_df.iteritems():
            numeric.get_data(columnName, columnData)
            result = numeric.get_negatives()
            self.assertEqual(result, 1)

#Test: Create class and display average value
class TestGetAverage(unittest.TestCase):
    def test_get_negatives(self):
       # create sample dataframe
        self.strname = {'test_colname': [0,1,2,3,4.4]}
        test_df = pd.DataFrame(self.strname)
        numeric = NumericColumn()
        for (columnName, columnData) in test_df.iteritems():
            numeric.get_data(columnName, columnData)
            result = numeric.get_mean()
            self.assertEqual(result, 2.08)

#Test: Create class and display stamdard deviation value
class TestGetStandardDeviation(unittest.TestCase):
    def test_get_std(self):
       # create sample dataframe
        self.strname = {'test_colname': [0,1,2,3,4.4]}
        test_df = pd.DataFrame(self.strname)
        numeric = NumericColumn()
        for (columnName, columnData) in test_df.iteritems():
            numeric.get_data(columnName, columnData)
            result = numeric.get_std()
            self.assertEqual(result, 1.7123083834403194) 

#Test: Create class and display stamdard deviation value
class TestGetMinimumValue(unittest.TestCase):
    def test_get_min(self):
       # create sample dataframe
        self.strname = {'test_colname': [0,1,2,3,4.4]}
        test_df = pd.DataFrame(self.strname)
        numeric = NumericColumn()
        for (columnName, columnData) in test_df.iteritems():
            numeric.get_data(columnName, columnData)
            result = numeric.get_min()
            self.assertEqual(result, 0) 

#Test: Create class and display maximum value
class TestGetMaximumValue(unittest.TestCase):
    def test_get_max(self):
       # create sample dataframe
        self.strname = {'test_colname': [0,1,2,3,4.4]}
        test_df = pd.DataFrame(self.strname)
        numeric = NumericColumn()
        for (columnName, columnData) in test_df.iteritems():
            numeric.get_data(columnName, columnData)
            result = numeric.get_max()
            self.assertEqual(result, 4.4) 

#Test: Create class and display median value
class TestGetMedianValue(unittest.TestCase):
    def test_get_median(self):
      # create sample dataframe
        self.strname = {'test_colname': [0,1,2,2,3,4.4]}
        test_df = pd.DataFrame(self.strname)
        numeric = NumericColumn()
        for (columnName, columnData) in test_df.iteritems():
            numeric.get_data(columnName, columnData)
            result = numeric.get_median()
            self.assertEqual(result, 2) 

if __name__ == '__main__':
    unittest.main()
