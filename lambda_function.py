import json
from predict_function import PredictFindU

def lambda_handler(event, context):
    # usr_id, lat, long, ts
    req = eval(event['body'])

    predictor = PredictFindU(req["usr_id"])

    response = predictor.run_predict(req["lat"],req["lon"],req["ts"])
    # TODO implement
    return {
        'statusCode': 200,
        #'body': json.dumps({"alert":response}) #0 : no alert, 1 : alert
        'body': json.dumps(response)
    }