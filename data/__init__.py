import requests

API_URL = 'https://opendata.paris.fr/api/records/1.0/search/?'
DATASET = 'dossiers-recents-durbanisme'

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

        print(records)

        if nhits > step: 
            start += step
            print('{}/{}'.format(start, nhits))
        else :
            print('done')
