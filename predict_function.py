from smart_open import open
from sklearn.neighbors import KNeighborsClassifier
import pickle
import os

class PredictFindU:
    def __init__(self, user_id):
        self.user_id = user_id
        self.S3_PATH = os.environ['s3_path_model']
        self.algorithms = [
            'BIRCH',
            'DBSCAN',
            'OPTICS'
        ]

    def run_predict(self, latitude, longitude, ts):
        predictions = {}
        for e_alg in self.algorithms:
            # TODO model not present, user follows a pattern :)
            with open(f'{self.S3_PATH}knn_model_{e_alg}_{self.user_id}', 'rb') as in_data:
                loaded_model = pickle.load(in_data)
            predictions[e_alg] = loaded_model.predict([[longitude,latitude,ts]])
        print(predictions)
        return 'Predicted!'