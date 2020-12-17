

#%% Import libraries
import os
import json
import joblib
import numpy as np

from azureml.core.model import Model


def init():
    global model
    # AZUREML_MODEL_DIR is an environment variable created during deployment. Join this path with the filename of the model file.
    # It holds the path to the directory that contains the deployed model (./azureml-models/$MODEL_NAME/$VERSION).
    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'model.pkl')
    model = joblib.load(model_path)


def run(new_data):
    # Get the input data as a numpy array
    data = np.array(json.loads(new_data)['data'])
    
    # Get a prediction from the model
    pred = model.predict(data)
    
    # Get the corresponding classname for each prediction (0 or 1)
    classnames = ['not-diabetic', 'diabetic']
    
    predicted_classes = []
    for p in pred:
        predicted_classes.append(classnames[p])
        
    # Return the predictions as JSON
    return json.dumps(predicted_classes)
