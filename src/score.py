# pylint: skip-file
import json

import numpy as np
import pandas as pd

def loadModel_v1():
    import pickle
    filename = 'finalized_model.sav'
    model = pickle.load(open(f'models/{filename}', 'rb'))
    return model

def loadModel_v2():
    import joblib
    filename = 'finalized_model.sav'
    model = joblib.load(open(f'models/{filename}', 'rb'))
    return model

def predict(data):
    try:
        data = json.loads(data)
        data = data['data']
        loaded_model = loadModel_v1()
        result = loaded_model.predict(np.array(data))
        return result.tolist()
    except Exception as e:
        error = str(e)
        return error

def main():
    x_test = pd.read_csv('data/x_test.csv')
    y_test = pd.read_csv('data/y_test.csv')
    loaded_model = loadModel_v1()
    result = loaded_model.score(x_test, y_test)
    print(result)

if __name__ == '__main__':
    main()