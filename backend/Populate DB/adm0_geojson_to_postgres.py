#!/usr/bin/python

from __future__ import print_function, unicode_literals
import operator
import psycopg2
import psycopg2.extras
import io
import json
import sys
import logging

from config import config



INSERT_STATEMENT = 'INSERT INTO valhko_app_adm0 (adm_name ,adm_type, adm_geom)  \
                    VALUES (%s,%s, ST_SetSRID(ST_GeomFromGeoJSON(%s), 4326));'

def import_feature(cur,feature_data):
    
        geojson = json.dumps(feature_data['features'][0]['geometry'])
        adm0_name = feature_data['features'][0]['properties']['COUNTRY']
       
        print(adm0_name)


        cur.execute(INSERT_STATEMENT, (adm0_name,"Country", geojson))


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
    files = [io.open(a,'r') for a in sys.argv[1:]]

    for file in files:
        feature_data = json.load(file)
        import_feature(cur, feature_data)
        
    # commit changes
    conn.commit()
	# close the communication with the PostgreSQL
    cur.close()
    print('Database connection closed.')
    
    

    