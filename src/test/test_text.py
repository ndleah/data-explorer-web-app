# To be filled by students

import unittest
import pandas as pd
import numpy as np

# change this to the path of your module
import sys
sys.path.append('../')

# import text.py modul
from text import TextColumn

# test class text name function (5 tests)
class Test_Text_Name(unittest.TestCase):
    def test_name_normal(self):
        # create sample dataframe
        self.strname = {'test': ['A','b']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_name()
            self.assertEqual(result, 'Test')

    def test_name_empty(self):
        # create sample dataframe
        self.strname = {'': ['A','b']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_name()
            self.assertEqual(result, '')
        
    def test_name_space(self):
        # create sample dataframe
        self.strname = {' ': ['A','b']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_name()
            self.assertEqual(result, ' ')
        
    def test_name_number(self):
        # create sample dataframe
        self.strname = {'123': ['A','b']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_name()
            self.assertEqual(result, '123')    
    
    def test_name_special(self):
        # create sample dataframe
        self.strname = {'*#-': ['A','b']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_name()
            self.assertEqual(result, '*#-')


# test Class Unique function (7 tests)
class Test_Text_Unique(unittest.TestCase):
    def test_value_letter(self):
        # create sample dataframe
        self.strname = {'test': ['A','b','abcd', 'A', 'A_B', 'A B', ' A', 'B ']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_unique()
            self.assertEqual(result, 7)

    def test_value_empty(self):
        # create sample dataframe
        self.strname = {'test': ['A','b','abcd','','']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_unique()
            self.assertEqual(result, 4)
        
    def test_value_space(self):
        # create sample dataframe
        self.strname = {'test': ['A','b','abcd', ' ', ' ']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_unique()
            self.assertEqual(result, 4)
        
    def test_value_number(self):
        # create sample dataframe
        self.strname = {'test': ['A','b','abcd', 123, 123]}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_unique()
            self.assertEqual(result, 4)    
    
    def test_value_special(self):
        # create sample dataframe
        self.strname = {'test': ['A','b','abcd', '*', '_', '*']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_unique()
            self.assertEqual(result, 5)

    def test_value_missing(self):
        # create sample dataframe
        self.strname = {'test': ['A','b','abcd',np.NaN, np.NaN]}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_unique()
            self.assertEqual(result, 4)   
   
    def test_value_mix(self):
        # create sample dataframe
        self.strname = {'test': ['A','b', ' ','', np.NaN, 'abcd', '1234', 'ab12', 'A', 'A ',' B',' C ', '1 2','-']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_unique()
            self.assertEqual(result, 13) 


# test Class Missing function (2 tests)
class Test_Text_Missing(unittest.TestCase):
    def test_value_missing_NA(self):
        # create sample dataframe
        self.strname = {'test': ['A','b',np.NaN, 'A',np.NaN]}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_missing()
            self.assertEqual(result, 2)
    
    def test_value_missing_empty(self):
        # create sample dataframe
        self.strname = {'test': ['A','b','','A']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_missing()
            self.assertEqual(result, 0)


# test Class Empty function (2 tests)
class Test_Text_Empty(unittest.TestCase):
    def test_value_empty(self):
        # create sample dataframe
        self.strname = {'test': ['A','b','', 'A','']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_empty()
            self.assertEqual(result, 2)

    def test_value_empty_NA(self):
        # create sample dataframe
        self.strname = {'test': ['A','b','', 'A','','',np.NaN]}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_empty()
            self.assertEqual(result, 3)

# test Class Whitespace function (2 test)
class Test_Text_Whitespace(unittest.TestCase):
    def test_value_whitespace(self):
        # create sample dataframe
        self.strname = {'test': ['A','b',' ', 'A',' ','    ']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_whitespace()
            self.assertEqual(result, 3)

    def test_value_whitespace_in_text(self):
        self.strname = {'test': [' A ',' b', 'A ']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_whitespace()
            self.assertEqual(result, 0)


# test Class with only lower case characters (10 tests)
class Test_Text_Lower_Case(unittest.TestCase):
    def test_value_lowercase_letter(self):
        # create sample dataframe
        self.strname = {'test': ['A','b','b', 'ab']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_lowercase()
            self.assertEqual(result, 3)

    def test_value_lowercase_mix_upper(self):
        # create sample dataframe
        self.strname = {'test': ['A','b','b', 'ab','Ab','bA']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_lowercase()
            self.assertEqual(result, 3)

    def test_value_lowercase_letter_number(self):
        # create sample dataframe
        self.strname = {'test': ['A','b','b', 'ab','2b','b2']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_lowercase()
            self.assertEqual(result, 3)

    def test_value_lowercase_mix_space(self):
        # create sample dataframe
        self.strname = {'test': ['A','b','b', 'a b',' b','b ']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_lowercase()
            self.assertEqual(result, 2)

    def test_value_lowercase_mix_empty(self):
        # create sample dataframe
        self.strname = {'test': ['A','b','b', '']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_lowercase()
            self.assertEqual(result, 2)

    def test_value_lowercase_mix_missing(self):
        # create sample dataframe
        self.strname = {'test': ['A','b','b', np.NaN]}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_lowercase()
            self.assertEqual(result, 2)

    def test_value_lowercase_mix_special(self):
        # create sample dataframe
        self.strname = {'test': ['A','b','b', '*b','b_','*b_']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_lowercase()
            self.assertEqual(result, 2)

    def test_value_lowercase_mix_number(self):
        # create sample dataframe
        self.strname = {'test': ['1','2','3', '*b','b_','b']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_lowercase()
            self.assertEqual(result, 1)

    def test_value_lowercase_number(self):
        # create sample dataframe
        self.strname = {'test': ['1','2','3']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_lowercase()
            self.assertEqual(result, 0)

    def test_value_lowercase_date(self):
        # create sample dataframe
        self.strname = {'test': ['1970-01-01T06:33:45', '2021-02-26T07:11:07']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_lowercase()
            self.assertEqual(result, 0)


# test Class with only upper case characters (10 tests)
class Test_Text_upper_Case(unittest.TestCase):
    def test_value_uppercase_letter(self):
        # create sample dataframe
        self.strname = {'test': ['A','b','b', 'ab']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_uppercase()
            self.assertEqual(result, 1)

    def test_value_uppercase_mix_lower(self):
        # create sample dataframe
        self.strname = {'test': ['A','AB','b', 'ab','Ab','bA']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_uppercase()
            self.assertEqual(result, 2)

    def test_value_uppercase_letter_number(self):
        # create sample dataframe
        self.strname = {'test': ['A','C','ABC', 'ab','2A','A2']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_uppercase()
            self.assertEqual(result, 3)

    def test_value_uppercase_mix_space(self):
        # create sample dataframe
        self.strname = {'test': ['A','B','AB', 'A b',' A','B ']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_uppercase()
            self.assertEqual(result, 3)

    def test_value_uppercase_mix_empty(self):
        # create sample dataframe
        self.strname = {'test': ['A','B','AB', '']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_uppercase()
            self.assertEqual(result, 3)

    def test_value_uppercase_mix_missing(self):
        # create sample dataframe
        self.strname = {'test': ['A','B','AB', np.NaN]}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_uppercase()
            self.assertEqual(result, 3)

    def test_value_uppercase_mix_special(self):
        # create sample dataframe
        self.strname = {'test': ['A','B','AB', '*A','B_','*B_']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_uppercase()
            self.assertEqual(result, 3)

    def test_value_uppercase_number(self):
        # create sample dataframe
        self.strname = {'test': ['1','2','3']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_uppercase()
            self.assertEqual(result, 0)

    def test_value_uppercase_date(self):
        # create sample dataframe
        self.strname = {'test': ['1970-01-01T06:33:45', '2021-02-26T07:11:07']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_uppercase()
            self.assertEqual(result, 0)

    def test_value_uppercase_mix_number(self):
        # create sample dataframe
        self.strname = {'test': ['1','2','3', 'B','b_','b']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_uppercase()
            self.assertEqual(result, 1)


# test Class with only alphabet case characters (7 tests)
class Test_Text_alphabet_Case(unittest.TestCase):
    def test_value_letter(self):
        # create sample dataframe
        self.strname = {'test': ['A','b','b', 'ab']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_alphabet()
            self.assertEqual(result, 4)

    def test_value_alphabet_mix_upper_lower(self):
        # create sample dataframe
        self.strname = {'test': ['A','AB','b', 'ab','Ab','bA']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_alphabet()
            self.assertEqual(result, 6)

    def test_value_lowercase_mix_number(self):
        # create sample dataframe
        self.strname = {'test': ['A','C','ABC', 'ab','2A','b2']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_alphabet()
            self.assertEqual(result, 4)

    def test_value_lowercase_mix_space(self):
        # create sample dataframe
        self.strname = {'test': ['A','B','AB', 'A b',' A','B ',' b','a ']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_alphabet()
            self.assertEqual(result, 3)

    def test_value_lowercase_mix_empty(self):
        # create sample dataframe
        self.strname = {'test': ['A','B','AB', '']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_alphabet()
            self.assertEqual(result, 3)

    def test_value_lowercase_mix_missing(self):
        # create sample dataframe
        self.strname = {'test': ['A','B','AB', np.NaN]}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_alphabet()
            self.assertEqual(result, 3)

    def test_value_lowercase_mix_special(self):
        # create sample dataframe
        self.strname = {'test': ['A','BBBB','AB', '*A','b_','*B_']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_alphabet()
            self.assertEqual(result, 3)

# test Class with only number case characters (5 tests)
class Test_Text_number(unittest.TestCase):
    def test_value_number(self):
        # create sample dataframe
        self.strname = {'test': ['1','3','12', '1234']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_digit()
            self.assertEqual(result, 4)

    def test_value_number_mix_letter(self):
        # create sample dataframe
        self.strname = {'test': ['1','3A','1b2', '12c34A']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_digit()
            self.assertEqual(result, 1)

    def test_value_number_space(self):
        # create sample dataframe
        self.strname = {'test': ['1',' 3','1 2', '12 ']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_digit()
            self.assertEqual(result, 1)

    def test_value_number_empty(self):
        # create sample dataframe
        self.strname = {'test': ['1','','12']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_digit()
            self.assertEqual(result, 2)

    def test_value_number_missing(self):
        # create sample dataframe
        self.strname = {'test': ['1',np.NaN,'12']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_digit()
            self.assertEqual(result, 2)

# test Class with mode value case characters (5 tests)
class Test_Text_mode(unittest.TestCase):
    def test_value_mode_mix(self):
        # create sample dataframe
        self.strname = {'test': ['A','A','b', '1234']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_mode()
            self.assertEqual(result[0], 'A')

    def test_value_mode_number(self):
        # create sample dataframe
        self.strname = {'test': ['1','2','1', '1234']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_mode()
            self.assertEqual(result[0], '1')

    def test_value_mode_letter(self):
        # create sample dataframe
        self.strname = {'test': ['A','A','ab', 'ab']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_mode()
            self.assertEqual(result[0], 'A')

    def test_value_mode_space(self):
        # create sample dataframe
        self.strname = {'test': [' ',' ','ab', 'ab']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_mode()
            self.assertEqual(result[0], ' ')

    def test_value_mode_empty(self):
        # create sample dataframe
        self.strname = {'test': ['','','ab', 'ab']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_mode()
            self.assertEqual(result[0], '')

    def test_value_mode_missing(self):
        # create sample dataframe
        self.strname = {'test': [np.NaN,np.NaN,'ab', 'ab']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_mode()
            self.assertEqual(result[0], 'ab')

    def test_value_mode_special(self):
        # create sample dataframe
        self.strname = {'test': ['*','*','ab', 'ab']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            result = test.get_mode()
            self.assertEqual(result[0], '*')

# test bar chart (1 test)
class Test_Text_bar(unittest.TestCase):
    def test_bar_chart(self):
        self.strname = {'test': ['A','A','ac', 'ab', 'Ab']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
           # compare class to expected class
            class_str = str(type(test.get_barchart()))
            chart_class = class_str.split('"')
            chart_str = chart_class[0]
            self.assertEqual(chart_str, "<class 'altair.vegalite.v4.api.Chart'>")

# test text frequest tabel (1 test)
class Test_Text_frequent(unittest.TestCase):
    def test_frequest(self):    
        self.strname = {'test': ['A','A','ac', 'ab', 'Ab']}
        test_df = pd.DataFrame(self.strname)
        test = TextColumn()
        for (columnName, columnData) in test_df.iteritems():
            test.get_data(columnName, columnData)
            # compare class to expected class
            class_str = str(type(test.get_frequent()))
            table_class = class_str.split('"')
            chart_str = table_class[0]
            self.assertEqual(chart_str, "<class 'pandas.core.frame.DataFrame'>")


if __name__ == '__main__':
    unittest.main()
