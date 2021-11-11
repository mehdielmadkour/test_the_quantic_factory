from datetime import datetime
from data import getDataFromDatabase, save
import pandas as pd

getDataFromDatabase()

def calculate_approval_time():

    data = data = getDataFromDatabase()

    data = data.loc[:, ['commune', 'date_depot', 'date_decision', 'etat', 'type_dossier', 'circonscription']]
    data = data[data.etat != 'En cours d\'instruction']

    def calculate_time(depot, decision):
        date_depot = datetime.strptime(depot,'%Y-%m-%d')
        date_decision = datetime.strptime(decision,'%Y-%m-%d')
        time = date_decision - date_depot
        return time.days

    time = list(data.apply(lambda row : calculate_time(row['date_depot'], row['date_decision']), axis=1))
    data['time'] = time
    save(data, 'APPROVAL_TIME', append=False)

    
def calculate_approval_time_by_district():

    data = getDataFromDatabase('APPROVAL_TIME')
    data = data.loc[:, ['commune', 'time']]

    results = []
    for commune in range(1, 21):
        data_commune = data[data.commune == commune]
        results.append(data_commune['time'].mean())
    
    district = [i for i in range(1, 21)]

    df = pd.DataFrame({
        'district': district,
        'approval_time': results 
    })

    save(df, 'APPROVAL_TIME_BY_DISTRICT', append=False)


def calculate_approval_time_by_type():

    data = getDataFromDatabase('APPROVAL_TIME')
    data = data.loc[:, ['type_dossier', 'time']]

    dossiers = ['Déclarations préalables', 'Permis d\'aménager', 'Permis de construire', 'Permis de démolir']
    
    results = []
    for type_dossier in dossiers:
        data_type = data[data.type_dossier == type_dossier]
        results.append(data_type['time'].mean())

    df = pd.DataFrame({
        'type_dossier': dossiers,
        'approval_time': results 
    })

    save(df, 'APPROVAL_TIME_BY_TYPE', append=False)


def calculate_approval_proportion_by_district():

    data = getDataFromDatabase('APPROVAL_TIME')
    data = data.loc[:, ['commune', 'etat']]
    data = data[data.etat != 'En cours d\'instruction']

    results = []
    for commune in range(1, 21):
        data_commune = data[data.commune == commune]
        
        accord = data_commune[data_commune.etat == 'Accordé']
        refus = data_commune[data_commune.etat == 'Refusé']

        result_commune = {
            'district': commune,
            'accord': len(accord),
            'refus': len(refus),
            'proportion': len(accord) / (len(accord) + len(refus))
        }

        results.append(result_commune)

    df = pd.DataFrame(results)
    
    save(df, 'APPROVAL_PROPORTION_BY_DISTRICT', append=False)


def calculate_approval_proportion_by_type():

    data = getDataFromDatabase('APPROVAL_TIME')

    data = data.loc[:, ['type_dossier', 'etat']]
    data = data[data.etat != 'En cours d\'instruction']

    dossiers = ['Déclarations préalables', 'Permis d\'aménager', 'Permis de construire', 'Permis de démolir']

    results = []
    for type in dossiers:
        data_dossier = data[data.type_dossier == type]
        
        accord = data_dossier[data_dossier.etat == 'Accordé']
        refus = data_dossier[data_dossier.etat == 'Refusé']

        result_dossier = {
            'type_dossier': type,
            'accord': len(accord),
            'refus': len(refus),
            'proportion': len(accord) / (len(accord) + len(refus))
        }

        results.append(result_dossier)
    
    df = pd.DataFrame(results)
    
    save(df, 'APPROVAL_PROPORTION_BY_TYPE', append=False)


def calculate_approval_time_by_constituency():

    data = getDataFromDatabase('APPROVAL_TIME')
    data = data.loc[:, ['circonscription', 'time']]

    circonscriptions = ['EST', 'NORD', 'OUEST', 'SUD']

    results = []
    for circonscription in circonscriptions:
        data_circonscription = data[data.circonscription == circonscription]
        results.append(data_circonscription['time'].mean())

    df = pd.DataFrame({
        'constituency': circonscriptions,
        'approval_time': results 
    })

    save(df, 'APPROVAL_TIME_BY_CONSTITUENCY', append=False)


def calculate_approval_proportion_by_constituency():

    data = getDataFromDatabase('APPROVAL_TIME')

    data = data.loc[:, ['circonscription', 'etat']]
    data = data[data.etat != 'En cours d\'instruction']

    circonscriptions = ['EST', 'NORD', 'OUEST', 'SUD']

    results = []
    for circonscription in circonscriptions:
        data_circonscription = data[data.circonscription == circonscription]
        
        accord = data_circonscription[data_circonscription.etat == 'Accordé']
        refus = data_circonscription[data_circonscription.etat == 'Refusé']

        result_dossier = {
            'constituency': circonscription,
            'accord': len(accord),
            'refus': len(refus),
            'proportion': len(accord) / (len(accord) + len(refus))
        }

        results.append(result_dossier)
    
    df = pd.DataFrame(results)
    
    save(df, 'APPROVAL_PROPORTION_BY_CONSTITUENCY', append=False)