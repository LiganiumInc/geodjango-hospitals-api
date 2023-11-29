#!/usr/bin/python

from __future__ import print_function, unicode_literals
import operator
import psycopg2
import psycopg2.extras
import io
import json
import sys
import logging
import pandas as pd

from config import config



INSERT_STATEMENT = 'INSERT INTO indice_values (date_index,name_index, price, benchmark_price)  \
                    VALUES (%s,%s,%s,%s);'

def import_feature(cur, feature_data):

    print(feature_data.head())

    feature_data['date_index'] = pd.to_datetime(feature_data.date_index).dt.date

    for index, row in feature_data.iterrows():
         date_index = row['date_index']
         name_index = row['name_index']
         price = row['price']
         benchmark_price = row['benchmark_price']

         print(date_index,name_index, price, benchmark_price)

         cur.execute(INSERT_STATEMENT, (date_index,name_index, price, benchmark_price))

if __name__ == '__main__':
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    # execute the main statements
    # read command lines arguments to get input files names
    feature_data = pd.read_excel(sys.argv[1])
    import_feature(cur,feature_data)
        
    # commit changes
    conn.commit()
	# close the communication with the PostgreSQL
    cur.close()
    print('Database connection closed.')
    
    

    