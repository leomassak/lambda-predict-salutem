from sklearn.neighbors import BallTree
from sklearn.preprocessing import MinMaxScaler

def getUsersByKnn(otherUsers, result):
    temp = []
    for i in range(len(result)):
        x = int(result[i])
        string_id = str(otherUsers[x]['_id'])
        temp.append({
            "id": string_id, 
            "user_name": otherUsers[x]['name'],
            "insurance": otherUsers[x]['insurance'],
            "weight": otherUsers[x]['weight'],
            "height": otherUsers[x]['height'],
        })
    return temp

def transformToKnnArray(data):
    scaler = MinMaxScaler()
    temp = []
    for i in range(len(data)):
        # user_age -> get user age
        user_age = None

        #encode user sex
        encoded_sex = None

        features_array = [data[i]['weight'],data[i]['height'], encoded_sex, user_age].extend(data[i].conditions)
        temp.append(features_array)
    return scaler.fit_transform(temp)

def knn(user, otherUsers):
    tree = BallTree(otherUsers)
    dist, ind = tree.query(user, k=5)
    
    return ind

