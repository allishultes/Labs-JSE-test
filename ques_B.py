import pandas as pd
import numpy as np
from pandas import read_csv

def main():
    df = pd.read_csv('data/article-Regions.csv')
    df_hourly = group_by_hour(df)
    path = './output/b.txt'
    header = get_header(df_hourly)
    output_file(df_hourly, path, header)

def group_by_hour(df):
    table_times = pd.to_datetime(df.Date)
    df['Hour'] = table_times.dt.hour
    df_hourly = df.groupby('Hour')['North America', 'United Kingdom', 'Europe', 'Asia', 'Australia'].mean().reset_index()
    return df_hourly

def get_header(df_hourly):
    column_names = df_hourly.columns.values
    header = "\t|\t".join(column_names)
    return header

def output_file(df_hourly, path, header):
    np.savetxt(path, df_hourly.values, header=header, fmt='%1.0f', delimiter='\t|\t')

main()
