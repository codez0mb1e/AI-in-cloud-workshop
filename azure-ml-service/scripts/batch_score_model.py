
#%% Imprort dependencies
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


def run(mini_batch):
    # This runs for each batch
    results = []

    # process each file in the batch
    for f in mini_batch:
        # Read the comma-delimited data into an array
        data = np.genfromtxt(f, delimiter=',')
        # Reshape into a 2-dimensional array for prediction (model expects multiple items)
        prediction = model.predict(data.reshape(1, -1))
        # Append prediction to results
        results.append("{}: {}".format(os.path.basename(f), prediction[0]))
    
    return results
