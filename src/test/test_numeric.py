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
         numeric_column = "Column name"
         test_example = pd.DataFrame(numeric_column)
         test_numeric = NumericColumn()
         test_both = Dataset(test_example, test_numeric)
         self.assertEqual(test_both.get_name, test_numeric)

#Test: Create class and get unique values:

class TestUniqueValues(unittest.TestCase):
    def test_get_unique(self):
        data = [0,1,2,3,4.4]
        test_example = pd.DataFrame(data)
        test_numeric = NumericColumn()
        test_both = Dataset(test_example, test_numeric)
        self.assertEqual(test_both.get_unique(), 5)

#Test: Create class and get missing values

class TestMissingValues(unittest.TestCase):
     def test_get_missing(self:)
        data = [0,1,2,3,4.4,NaN]
        test_example = pd.DataFrame(data)
        test_numeric = NumericColumn()
        test_both = Dataset(test_example, test_numeric)
        self.assertEqual(test_both.get_missing(), 1)

#Test: Create class and get zero values

class TestGetZeros(unittest.TestCase):
     def test_get_zeros(self:)
        data = [0,1,2,3,4.4]
        test_example = pd.DataFrame(data)
        test_numeric = NumericColumn()
        test_both = Dataset(test_example, test_numeric)
        self.assertEqual(test_both.get_zeros(), 1)

#Test: Create class and get negative values
class TestGetNegatives(unittest.TestCase):
    def test_get_negatives(self:)
        data = [0,1,2,3,4.4,-5]
        test_example = pd.DataFrame(data)
        test_numeric = NumericColumn()
        test_both = Dataset(test_example, test_numeric)
        self.assertEqual(test_both.get_negatives(), 1) 

#Test: Create class and display average value
class TestGetAverage(unittest.TestCase):
    def test_get_mean(self:)
        data = [0,1,2,3,4.4]
        mean(data)
        test_example = pd.DataFrame(data)
        test_numeric = NumericColumn()
        test_both = Dataset(test_example, test_numeric)
        self.assertEqual(test_both.get_mean(), 2.08) 

#Test: Create class and display stamdard deviation value
class TestGetStandardDeviation(unittest.TestCase):
    def test_get_std(self:)
        data = [0,1,2,3,4.4]
        test_example = pd.DataFrame(data)
        test_numeric = NumericColumn()
        test_both = Dataset(test_example, test_numeric)
        self.assertEqual(test_both.get_std(), 1.5315351775261319) 
        #np.std

#Test: Create class and display stamdard deviation value
class TestGetMinimumValue(unittest.TestCase):
    def test_get_min(self:)
    data = [0,1,2,3,4.4]
    test_example = pd.DataFrame(data)
    test_numeric = NumericColumn()
    test_both = Dataset(test_example, test_numeric)
    self.assertEqual(test_both.get_min(), 0) 

#Test: Create class and display maximum value
class TestGetMaximumValue(unittest.TestCase):
    def test_get_max(self:)
    data = [0,1,2,3,4.4]
    test_example = pd.DataFrame(data)
    test_numeric = NumericColumn()
    test_both = Dataset(test_example, test_numeric)
    self.assertEqual(test_both.get_max(), 4.4) 

#Test: Create class and display median value
class TestGetMedianValue(unittest.TestCase):
    def test_get_median(self:)
    data = [0,1,2,3,4.4]
    test_example = pd.DataFrame(data)
    test_numeric = NumericColumn()
    test_both = Dataset(test_example, test_numeric)
    self.assertEqual(test_both.get_median(),2) 

# Create a dataFrame for displaying in the Web App
value = {'value': pd.Series([unique_values,missing_values,occurence_0,negative_value,avg_value,std_value,min_value,max_value,median_value], 
index = ['Number of Unique Values:','Number of Missing Values:','Number of Rows with 0:','Number of Rows with Negative Values:',
'Average Values:','Standard Deviation Values:','Minimum Value', 'Maximum Value','Median Value'])}
df_value = pd.DataFrame(value)
st.write(df_value)

    
# Plot bar chat and display in Web App
st.markdown('**Histogram**')
st.altair_chart(numeric.get_histogram())

# Create a frequent table and display in WebA[[]]
st.markdown('**Most Frequent Values**')
frequent = numeric.get_frequent()
st.write(frequent)

if __name__ == '__main__':
    unittest.main()
