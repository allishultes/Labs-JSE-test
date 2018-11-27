import pandas as pd
import numpy as np
from pandas import read_csv

def main():
    df = pd.read_csv('./data/article-Devices.csv')
    df_hourly = group_by_hour(df)
    mobile_slice = slice_mobile_data(df_hourly)
    header = get_header(mobile_slice)
    path = './output/e.txt'
    output_file(mobile_slice, path, header)

def group_by_hour(df):
    table_times = pd.to_datetime(df.Date)
    df['Hour'] = table_times.dt.hour
    df_hourly = df.groupby('Hour')['Mobile'].mean().reset_index()
    return df_hourly

def slice_mobile_data(df_hourly):
    avg_mobile = df_hourly['Mobile'].mean()
    mobile_slice = df_hourly[(df_hourly['Mobile'] > avg_mobile)]
    return mobile_slice

def get_header(mobile_slice):
    column_names = mobile_slice.columns.values
    header = "\t|\t".join(column_names)
    return header

def output_file(mobile_slice, path, header):
    np.savetxt(path, mobile_slice, header= header, fmt='%1.0f', delimiter='\t|\t')

main()
