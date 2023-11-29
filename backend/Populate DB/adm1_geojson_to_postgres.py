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



INSERT_STATEMENT = 'INSERT INTO valhko_app_adm1 (adm0_id, adm_name , adm_type, adm_geom)  \
                    VALUES (%s, %s, %s,  ST_SetSRID(ST_GeomFromGeoJSON(%s), 4326));'

def import_feature(cur,feature_data):

    for elem in feature_data['features']:

        adm_name = elem['properties']['NAME_1']
        adm_type = elem['properties']['ENGTYPE_1']
        adm_geom = json.dumps(elem['geometry'])

        # let's get the foreign key
        adm0_name = elem['properties']['COUNTRY']
        print(adm0_name)
        cur.execute("SELECT id from valhko_app_adm0 where adm_name = (%s)",(adm0_name,))
        adm0_id = cur.fetchone()
        print(adm0_id)

        print("Foreign Key : ",adm0_id, "Parent : ", adm0_name, "Type : ", adm_type,"Name : ", adm_name,)

        cur.execute(INSERT_STATEMENT, (adm0_id,adm_name, adm_type, adm_geom))


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
    
    

    