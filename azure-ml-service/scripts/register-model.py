
#%% Import libraries
import argparse
import joblib
from azureml.core import Workspace, Model, Run


#%% Get parameters
parser = argparse.ArgumentParser()
parser.add_argument('--model_dir', type=str, dest='model_dir', default='outputs', help='Define ML model directory')
args = parser.parse_args()


#%% Set model directory
model_dir = args.model_dir


#%% Get the experiment run context
run = Run.get_context()


#%% Load the model
model_path = f'{model_dir}/model.pkl'

print(f'Loading {model_path}...')
model = joblib.load(model_path)


#%% Register model
Model.register(workspace=run.experiment.workspace,
               model_path=model_path,
               model_name='diabetes_predict_model',
               tags={'Demo': 'ML Pipeline'})

#%% Finish Experiment
run.complete()
