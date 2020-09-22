
# Azure Machine Learning Workshop

## Requirements



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
git checkout azure-ml-ru
```

#### Install dependencies

Run `_init.sh` for checking python and pip versions and install all necessary dependencies:

```
cd azure-ml-service/
./_init.sh 
```

#### References

1. [Azure Machine Learning Overview](https://docs.microsoft.com/en-us/azure/machine-learning/overview-what-is-azure-ml), Micosoft Docs.
1. [Video Instruction]() (in Russian), Youtube.


### Lab 1B: Azure ML SDK

1. Open and run [01B-azure-ml-sdk-intro.ipynb](01B-azure-ml-sdk-intro.ipynb) in JupterLab.

#### References

1. [Azure ML SDK Overview](https://docs.microsoft.com/ru-ru/python/api/overview/azure/ml/?view=azure-ml-py), Microsoft Docs.
2. [Install Azure ML SDK](https://docs.microsoft.com/ru-ru/python/api/overview/azure/ml/install?view=azure-ml-py), Microsoft Docs.
3. [Azure ML SDK Source Code](https://github.com/Azure/azure-sdk-for-python), GitHub.



## Module II: Azure ML Datastores and Datasets

#### Lab 2A: Working with Datastores and Datasets using Azure ML Portal

Go to [Azure ML portal](https://ml.azure.com/) and using UI:

1. Create new Datastore
2. Upload to created Datastore `diabetes_train.csv` dataset from [`data`](../data) dir.

#### References

1. [Video Instruction]() (in Russian), Youtube.


#### Lab 2B: Working with Datastores and Datasets using Azure ML SDK

1. Open and run [02B-datastores-and-datasets](02B-datastores-and-datasets) in JupterLab.


