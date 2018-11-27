import unittest
import pandas as pd
from pandas import read_csv
import numpy as np
from ques_B import *

class TestQuesB(unittest.TestCase):

    def test_group_by_hour(self):

        # Checks that "Hour" is a column in the dataframe
        df = pd.read_csv('./tests/test-b.csv')
        df_hourly = group_by_hour(df)
        self.assertIn("Hour", df_hourly.columns.values)

        # Checks that hours are whole numbers
        hours = [13, 14, 15]
        df_hours = df_hourly.Hour.values.flatten()
        df_hours.tolist()
        self.assertTrue((hours == df_hours).all())

    def test_output_file(self):

        # Tests that output file matches input dataframe
        hourly_data = [{'Hour': 13, 'Mobile': 100},
                        {'Hour': 14, 'Mobile': 150},
                        {'Hour': 15, 'Mobile': 200}]

        # Sets parameters to padd to function output_file()
        df_hourly = pd.DataFrame(hourly_data)
        path = './tests/b.txt'
        header = 'Hour\t|\tMobile'

        output_file(df_hourly, path, header)

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
