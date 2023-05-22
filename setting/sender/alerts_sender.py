"""Filling table stations_alerts.station_errors"""
import pandas as pd
import minio


def main(file='alerts.csv', table_name='public.station_errors'):
    """:file: path to prepared csv file
       :table_name: destination table"""
    df = pd.read_csv(file)



if __name__ == '__main__':
    main()
