
# Azure Machine Learning Workshop


## Module I: Introduction to Azure Machine Learning

### Lab 1A: Preparation

#### Create Azure Machine Learning Workspace

1. Go to [Azure Portal](https://portal.azure.com/#home) and switch to English UI
1. Find [Machine Learning service](https://portal.azure.com/#create/Microsoft.MachineLearningServices) and create Azure ML `Workspace`
1. Go to [Azure ML Portal](https://ml.azure.com/) and create `Compute instance` (Compute > Compute instance tab)
1. Click to JupiterLab link after creating the `Compute instance`.


#### Clone repository

Clone repo and switch to necessary branch:

```
cd Users/<your_user_name> # WARN: replace on your user name'

git clone https://github.com/codez0mb1e/AI-in-cloud-workshop.git

cd AI-in-cloud-workshop/
git checkout winter-school-2020
```

#### Install dependencies

Run `_init.sh` for checking python and pip versions and install all necessary dependencies:

```
cd azure-ml-service/
./_init.sh 
```

References:

1. [Azure Machine Learning Overview](https://docs.microsoft.com/en-us/azure/machine-learning/overview-what-is-azure-ml), Micosoft Docs.
1. [Video Instruction](https://youtu.be/Kkyrk-1fT7k) (in Russian), Youtube.


### Lab 1B: Azure ML SDK

Steps: 

1. Open and run [01B-azure-ml-sdk-intro.ipynb](01B-azure-ml-sdk-intro.ipynb) in JupterLab.

References:

1. [Azure ML SDK Overview](https://docs.microsoft.com/ru-ru/python/api/overview/azure/ml/?view=azure-ml-py), Microsoft Docs.
2. [Install Azure ML SDK](https://docs.microsoft.com/ru-ru/python/api/overview/azure/ml/install?view=azure-ml-py), Microsoft Docs.
3. [Azure ML SDK Source Code](https://github.com/Azure/azure-sdk-for-python), GitHub.



## Module II: Azure ML Datastores and Datasets

### Lab 2A: Working with Datastores and Datasets using Azure ML Portal

Go to [Azure ML portal](https://ml.azure.com/) and using UI:

Steps: 

1. Create new Datastore
  - _Hint:_ use [Azure Storage Explorer](https://azure.microsoft.com/en-us/features/storage-explorer/) for manually upload data to created Datastore
  
2. Upload to created Datastore `diabetes_train.csv` dataset from [`data`](../data) dir.
  - _Hint:_ use https://raw.githubusercontent.com/codez0mb1e/AI-in-cloud-workshop/azure-ml-ru/data/diabetes_train.csv as link to origin csv file.

References:

1. [Video Instruction](https://youtu.be/ls6CwSUti_o) (in Russian), Youtube.
2. [About Diabetes dataset](datasets.md).


### Lab 2B: Working with Datastores and Datasets using Azure ML SDK

Steps: 

1. Open and run [02B-datastores-and-datasets.ipynb](02B-datastores-and-datasets.ipynb) in JupterLab.

References:

1. [Dataset module](https://docs.microsoft.com/ru-ru/python/api/azureml-core/azureml.core.dataset?view=azure-ml-py), Azure ML SDK Docs.
1. [Datastore module](https://docs.microsoft.com/ru-ru/python/api/azureml-core/azureml.core.datastore?view=azure-ml-py), Azure ML SDK Docs.



## Module III: Azure ML Designer

### Lab 3A: Train and deploy model using Azure ML Designer

Steps: 

1. Create and deploy model using Azure ML Designer (see [1])

References:

1. [Video Instruction](https://youtu.be/oaZHALjlwVM) (in Russian), Youtube.
1. [Azure ML Designer Overview](https://docs.microsoft.com/ru-ru/azure/machine-learning/concept-designer), Microsoft Docs.
1. Tutorial: [Deploy a machine learning model with the designer](https://docs.microsoft.com/ru-ru/azure/machine-learning/tutorial-designer-automobile-price-deploy), Microsoft Docs.


### Lab 3B: Inference deployed ML model

Steps: 

1. Get `Endpoint URI` and `API Key` for deployed ML model
1. Update `endpoint_uri` and `api_key` in [config.yml](config.yml)
1. Open and run [03B-model-inference.ipynb](03B-model-inference.ipynb) in JupterLab.



## Module IV: Azure ML Experiments

### Lab 4A: Create and run Azure ML Experiments

Steps: 

1. Open and run [04A-experiments.ipynb](04A-experiments.ipynb) in JupterLab.

References:

1. [Experiment module](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.experiment.experiment?view=azure-ml-py), Azure ML SDK Docs.

### Lab 4B: Train model using Azure ML Experiments

Steps: 

1. Open and run [04B-training-model.ipynb](04B-training-model.ipynb) in JupterLab.

References:

1. [Estimator for training with Scikit-Learn](https://docs.microsoft.com/en-us/python/api/azureml-train-core/azureml.train.sklearn?view=azure-ml-py), Azure ML SDK Docs.


## Extra

### Development tools for Azure ML

1. Install VS Code and Azure Machine Learning Extension.


## Final Project

Steps: 

#### 1. Define project's topic

- Select and download the data set (see [1])
- Formulate the problem to be solved in terms of Machine learning.


#### 2. Find the solution by using Azure Machine Learning service Using the Azure ML developer or the Azure ML SDK:

- Download and register the downloaded dataset as an Azure ML Datasets
- Create an Experiment for Project
- Train a machine learning model using hyperparameter tuning or/and Auto ML 
- Publish the trained model as a web service
- Using the Azure ML SDK, connect to a published web service and send a request to it with new data to make a forecast for.

#### 3. Share your Solution with the world

- The way - up to you!

References:

1. [Open Data Hubs List](references.md)