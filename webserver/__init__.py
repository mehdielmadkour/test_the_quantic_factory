from flask import Flask, jsonify, render_template
from data import getDataFromDatabase

server = Flask(__name__)

@server.route('/')
def dashboard():
    return render_template('dashboard.html')

@server.route('/api/approval_time_by_district')
def approval_time_by_district():

    data = getDataFromDatabase('APPROVAL_TIME_BY_DISTRICT')

    response =  jsonify({
        'labels': list(data['district']),
        'values': list(data['approval_time']),
        'title': 'Temps d\'approbation des dossier'
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@server.route('/api/approval_time_by_type')
def approval_time_by_type():

    data = getDataFromDatabase('APPROVAL_TIME_BY_TYPE')

    response =  jsonify({
        'labels': list(data['type_dossier']),
        'values': list(data['approval_time']),
        'title': 'Temps d\'approbation des dossier'
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@server.route('/api/approval_proportion_by_district')
def approval_proportion_by_district():

    data = getDataFromDatabase('APPROVAL_PROPORTION_BY_DISTRICT')

    response =  jsonify({
        'labels': list(data['district']),
        'values': list(data['proportion']),
        'title': 'Taux d\'approbation des dossier'
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@server.route('/api/approval_proportion_by_type')
def approval_proportion_by_type():

    data = getDataFromDatabase('APPROVAL_PROPORTION_BY_TYPE')

    response =  jsonify({
        'labels': list(data['type_dossier']),
        'values': list(data['proportion']),
        'title': 'Taux d\'approbation des dossier'
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@server.route('/api/approval_time_by_constituency')
def approval_time_by_constituency():

    data = getDataFromDatabase('APPROVAL_TIME_BY_CONSTITUENCY')

    response =  jsonify({
        'labels': list(data['constituency']),
        'values': list(data['approval_time']),
        'title': 'Temps d\'approbation des dossier'
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@server.route('/api/approval_proportion_by_constituency')
def approval_proportion_by_constituency():

    data = getDataFromDatabase('APPROVAL_PROPORTION_BY_CONSTITUENCY')

    response =  jsonify({
        'labels': list(data['constituency']),
        'values': list(data['proportion']),
        'title': 'Taux d\'approbation des dossier'
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response