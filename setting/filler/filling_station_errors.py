"""Filling table stations_alerts.station_errors"""
import pandas as pd
import psycopg2


def main(file='init_data.csv', table_name='public.station_errors'):
    """:file: path to prepared csv file
       :table_name: destination table"""
    df = pd.read_csv(file)

    columns = df.columns
    data = list(df.itertuples(index=False, name=None))

    conn = psycopg2.connect(
        host="postgres_db",
        port="5433",
        database="stations_alerts",
        user="postgres",
        password="postgres")

    cursor = conn.cursor()

    cursor.executemany(
        f"insert into {table_name} ({','.join(columns)}) values ({','.join(['%s'] * len(columns))})",
        data
    )
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
