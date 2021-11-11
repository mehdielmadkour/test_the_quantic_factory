from analyse import *
from webserver import server

if __name__ == '__main__':
    
    calculate_approval_time()
    calculate_approval_time_by_district()
    calculate_approval_time_by_type()
    calculate_approval_proportion_by_district()
    calculate_approval_proportion_by_type()
    calculate_approval_time_by_constituency()
    calculate_approval_proportion_by_constituency()

    server.run(debug=True, port=8080)