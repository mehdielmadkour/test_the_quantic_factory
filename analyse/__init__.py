from datetime import datetime
from data import getDataFromDatabase, save
import pandas as pd

def calculate_approval_time(data):

    data = data.loc[:, ['commune', 'date_depot', 'date_decision', 'etat']]
    time_data = data[data.etat != 'En cours d\'instruction']

    def calculate_time(depot, decision):
        date_depot = datetime.strptime(depot,'%Y-%m-%d')
        date_decision = datetime.strptime(decision,'%Y-%m-%d')
        time = date_decision - date_depot
        return time.days

    time = list(time_data.apply(lambda row : calculate_time(row['date_depot'], row['date_decision']), axis=1))
    time_data['time'] = time
    save(time_data, 'APPROVAL_TIME', append=False)

    
def get_approval_time_by_district(data):

    calculate_approval_time(data)

    data = getDataFromDatabase('APPROVAL_TIME')

    results = []
    for commune in range(1, 21):
        data_commune = data[data.commune == commune]
        results.append(data_commune['time'].mean())
    
    district = [i for i in range(1, 21)]

    df = pd.DataFrame({
        'district': district,
        'approval_time': results 
    })

    save(df, 'APPROVAL_TIME_PER_DISTRICT', append=False)
    print(df)
