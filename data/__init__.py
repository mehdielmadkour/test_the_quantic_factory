import requests
import pandas as pd
import sqlalchemy as sa
from sqlalchemy_utils.functions import database_exists

API_URL = 'https://opendata.paris.fr/api/records/1.0/search/?'
DATASET = 'dossiers-recents-durbanisme'
DB_URL = 'sqlite:///dataset.db'

engine = sa.create_engine(DB_URL)

def getDataFromAPI(rows, start=0):

    params = {
        'dataset': DATASET,
        'rows': rows,
        'start': start
    }
    r = requests.get(API_URL, params=params)
    j = r.json()
    return j


def getAllData(step):

    start = 0
    nhits = step

    while start < nhits:
        data = getDataFromAPI(step, start)
        nhits = data['nhits']
        records = data['records']

        df = formatData(records)
        save(df, DATASET)

        if nhits > start+step: 
            start += step
            print('{}/{}'.format(start, nhits))
        else :
            print('done')
            break


def formatData(records):

    data = list(map(lambda record: record['fields'], records))
    df = pd.DataFrame(data)
    df.geo_point_2d = df.geo_point_2d.astype(str)
    df.geo_shape = df.geo_shape.astype(str)
    return df


def save(data, database, append=True):
    if append:
        data.to_sql(database, engine, if_exists='append', index=False)
    else: 
        data.to_sql(database, engine, if_exists='replace', index=False)

def getDataFromDatabase(database=DATASET):

    if not database_exists(DB_URL): getAllData(100)
    return pd.read_sql(database, engine)
