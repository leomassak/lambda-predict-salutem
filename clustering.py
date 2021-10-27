from sklearn.neighbors import BallTree
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime
from datetime import date

def getUsersByKnn(otherUsers, result):
    temp = []
    for i in range(len(result)):
        x = int(result[i])
        string_id = str(otherUsers[x]['_id'])
        temp.append({
            "id": string_id, 
            "conditions": otherUsers[x]['conditions'],
        })
    return temp

def transformToKnnArray(data):
    temp = []
    today = date.today()
    for i in range(len(data)):
        birth_date = datetime.strptime(data[i]['birthday'], '%d/%m/%Y')
        age = today.year - birth_date.year
        if today.month < birth_date.month or today.month == birth_date.month and today.day < birth_date.day:
            age -= 1

        encoded_sex = 1 if data[i]['sex'] == 'M' else 0
        features_array = [data[i]['weight'],data[i]['height'], encoded_sex, age]
        features_array.extend(data[i]['conditions'])
        temp.append(features_array)
    return temp

def knn(user, otherUsers):
    tree = BallTree(otherUsers)
    dist, ind = tree.query(user, k=5)
    
    return ind

