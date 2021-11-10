from data import getDataFromDatabase
from analyse import calculate_approval_time_by_district
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/approval_time_by_district')
def approval_time_by_district():

    calculate_approval_time_by_district()

    data = getDataFromDatabase('APPROVAL_TIME_BY_DISTRICT')

    response =  jsonify({
        'district': list(data['district']),
        'approval_time': list(data['approval_time'])
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == '__main__':
    
    getDataFromDatabase()
    app.run(debug=True, port=8080)