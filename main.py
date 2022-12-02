import pandas as pd
import numpy as np
import psycopg2
import json



conn = psycopg2.connect(
    host='localhost',
    port='5433',
    database='names',
    user='postgres',
    password='0000')

cur = conn.cursor()
cur.execute("select * from card;")
L = cur.fetchall()




object_list = []
for i in L:

    a = {
        'parcel_no': i[0],
        'registration_section': i[1],
        'registry': i[2],
        'lessor': i[3],
        'lessee': i[4],
        'approximate_area': i[5]
    }
    object_list.append(a)




j = json.dumps(object_list)

with open('card_objects.json', 'w') as f:
    f.write(j)


cur.close()







