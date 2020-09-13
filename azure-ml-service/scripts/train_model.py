#%% Import libraries
import os
import argparse

import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt

from azureml.core import Run


#%% Set regularization hyperparameter (passed as an argument to the script)
parser = argparse.ArgumentParser()
parser.add_argument('--reg_rate', type=float, dest='reg_rate', default=0.01, help='Set regularization rate')
parser.add_argument('--output_dir', type=str, dest='output_dir', default='outputs', help='Set output folder')
args = parser.parse_args()

reg = args.reg_rate
output_dir = args.output_dir


#%% Get the experiment run context
run = Run.get_context()


#%% load the diabetes data (passed as an input dataset)
print('Loading Data...')
diabetes = run.input_datasets['data'].to_pandas_dataframe()


#%% Separate features and labels
X, y = diabetes[['Pregnancies','PlasmaGlucose','DiastolicBloodPressure','TricepsThickness','SerumInsulin','BMI','DiabetesPedigree','Age']].values, diabetes['Diabetic'].values


#%% Split data into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=314)


#%% Train a logistic regression model
print(f'Training a logistic regression model with regularization rate of {reg}')
run.log('Regularization Rate',  np.float(reg))
model = LogisticRegression(C=1/reg, solver='liblinear').fit(X_train, y_train)


#%% calculate accuracy
y_hat = model.predict(X_test)
acc = np.average(y_hat == y_test)
print(f'Accuracy: {acc}')
run.log('Accuracy', np.float(acc))


#%% calculate AUC
y_scores = model.predict_proba(X_test)
auc = roc_auc_score(y_test,y_scores[:,1])
print(f'AUC: {str(auc)}')
run.log('AUC', np.float(auc))


#%% plot ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_scores[:,1])
fig = plt.figure(figsize=(6, 4))


#%% Plot the diagonal 50% line
plt.plot([0, 1], [0, 1], 'k--')


#%% Plot the FPR and TPR achieved by our model
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
run.log_image(name='ROC', plot = fig)
plt.show()


#%% Save the trained model
# note file saved in the outputs folder is automatically uploaded into experiment record
os.makedirs(output_dir, exist_ok=True)
joblib.dump(value=model, filename=f'{output_dir}/model.pkl')

run.complete()
