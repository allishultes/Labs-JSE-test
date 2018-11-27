import unittest
import pandas as pd
import numpy as np

from pandas import read_csv
from ques_E import *

class TestQuesE(unittest.TestCase):

    def test_group_by_hour(self):

        # Checks that "Hour" is a column in the dataframe
        df = pd.read_csv('./tests/test-e.csv')
        df_hourly = group_by_hour(df)
        self.assertIn("Hour", df_hourly.columns.values)

        # Checks that hours are whole numbers
        hours = [17, 18, 19]
        df_hours = df_hourly.Hour.values.flatten()
        df_hours.tolist()
        self.assertTrue((hours == df_hours).all())

    def test_slice_mobile_data(self):

        hourly_data = [{'Hour': 13, 'Mobile': 100},
                        {'Hour': 14, 'Mobile': 150},
                        {'Hour': 15, 'Mobile': 200}]

        df_hourly = pd.DataFrame(hourly_data)
        test_data = slice_mobile_data(df_hourly)
        check_hour = test_data.values.flatten()
        check_hour.tolist()

        # Checks that only the final row is returned
        self.assertTrue(([15, 200] == check_hour).all())

    def test_output_file(self):

        # Tests that output file matches input dataframe
        hourly_data = [{'Hour': 13, 'Mobile': 100},
                        {'Hour': 14, 'Mobile': 150},
                        {'Hour': 15, 'Mobile': 200}]

        # Sets parameters to padd to function output_file()
        mobile_slice = pd.DataFrame(hourly_data)
        path = './tests/e.txt'
        header = 'Hour\t|\tMobile'

        output_file(mobile_slice, path, header)

        # Reads in just-generated .txt file
        file = open(path, "r")
        written_data = []

        # Iterates through lines of file, removes formatting and adds to written_data list
        for line in file.readlines():
            values = line.split('\t|\t')
            hour = values[0]
            mobile = values[1].replace('\n', '')
            row = {'Hour': hour, 'Mobile': mobile}

            written_data.append(row)

        written_data.pop(0) # Removes the first row, which is the header

        # Converts strings to floats
        for element in written_data:
            element['Mobile'] = float(element['Mobile'])
            element['Hour'] = float(element['Hour'])

        file.close()

        # Checks that data written by function is equal to data passed into the function
        self.assertTrue(hourly_data == written_data)

if __name__ == '__main__':
    unittest.main()
