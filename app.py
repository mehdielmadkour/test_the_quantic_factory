from data import getDataFromDatabase
from analyse import *
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/approval_time_by_district')
def approval_time_by_district():

    data = getDataFromDatabase('APPROVAL_TIME_BY_DISTRICT')

    response =  jsonify({
        'labels': list(data['district']),
        'values': list(data['approval_time']),
        'title': 'Temps d\'approbation des dossier'
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/api/approval_time_by_type')
def approval_time_by_type():

    data = getDataFromDatabase('APPROVAL_TIME_BY_TYPE')

    response =  jsonify({
        'labels': list(data['type_dossier']),
        'values': list(data['approval_time']),
        'title': 'Temps d\'approbation des dossier'
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/api/approval_proportion_by_district')
def approval_proportion_by_district():

    data = getDataFromDatabase('APPROVAL_PROPORTION_BY_DISTRICT')

    response =  jsonify({
        'labels': list(data['district']),
        'values': list(data['proportion']),
        'title': 'Taux d\'approbation des dossier'
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/api/approval_proportion_by_type')
def approval_proportion_by_type():

    data = getDataFromDatabase('APPROVAL_PROPORTION_BY_TYPE')

    response =  jsonify({
        'labels': list(data['type_dossier']),
        'values': list(data['proportion']),
        'title': 'Taux d\'approbation des dossier'
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/api/approval_time_by_constituency')
def approval_time_by_constituency():

    data = getDataFromDatabase('APPROVAL_TIME_BY_CONSTITUENCY')

    response =  jsonify({
        'labels': list(data['constituency']),
        'values': list(data['approval_time']),
        'title': 'Temps d\'approbation des dossier'
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/api/approval_proportion_by_constituency')
def approval_proportion_by_constituency():

    data = getDataFromDatabase('APPROVAL_PROPORTION_BY_CONSTITUENCY')

    response =  jsonify({
        'labels': list(data['constituency']),
        'values': list(data['proportion']),
        'title': 'Taux d\'approbation des dossier'
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == '__main__':
    
    getDataFromDatabase()
    calculate_approval_time()
    calculate_approval_time_by_district()
    calculate_approval_time_by_type()
    calculate_approval_proportion_by_district()
    calculate_approval_proportion_by_type()
    calculate_approval_time_by_constituency()
    calculate_approval_proportion_by_constituency()

    app.run(debug=True, port=8080)