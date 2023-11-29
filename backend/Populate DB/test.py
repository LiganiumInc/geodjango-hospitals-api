import sys
import io
import json
import pandas as pd

# INSERT_STATEMENT = 'INSERT INTO ADM1 (adm0_id, adm1_name , adm1_type, adm1_geom)  \
#                     VALUES (%s, %s, %s,  ST_SetSRID(ST_GeomFromGeoJSON(%s), 4326));'

def import_feature(feature_data):

    print(feature_data.head())

    feature_data['date_index'] = pd.to_datetime(feature_data.date_index).dt.date

    for index, row in feature_data.iterrows():
         date_index = row['date_index']
         name_index = row['name_index']
         price = row['price']
         benchmark_price = row['benchmark_price']

         print(date_index,name_index, price, benchmark_price)

        #  cur.execute(INSERT_STATEMENT, (adm0_id,adm1_name, adm1_type, adm1_geom))
        
        
    


    

if __name__ == '__main__':
    if len(sys.argv) == 1:
            handles = [sys.stdin]
    else:
        feature_data = pd.read_excel(sys.argv[1])
        import_feature(feature_data)


        # with con:
        #     with con.cursor() as cur:
        #         import_feature(cur, feature_data)
        #     con.commit()