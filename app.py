from data import getDataFromDatabase
from analyse import get_approval_time_by_district

if __name__ == '__main__':
    
    data = getDataFromDatabase()
    get_approval_time_by_district(data)