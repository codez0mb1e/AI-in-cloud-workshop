# Azure Machine Learning Workshop

## Steps

### Preparation

#### Create Azure Machine Learning Workspace

1. Go to [Azure Portal](https://portal.azure.com/#home) and switch to English UI
1. Find [Machine Learning service](https://portal.azure.com/#create/Microsoft.MachineLearningServices) and create Azure ML `Workspace`
1. Go to (Azure ML Portal)[https://ml.azure.com/] and create `Compute instance` (Compute > Compute instance tab)
1. Click to JupiterLab link after creating the `Compute instance`.

#### Clone repository

Clone repo and switch to nessesary branch:

```
git clone https://github.com/codez0mb1e/AI-in-cloud-workshop.git

cd AI-in-cloud-workshop/
git checkout azure-ml-ru
```

#### Install dependencies

Run `_init.sh` for checking python and pip versions and install all necessary  dependencies

```
cd azure-ml-service/
./_init.sh 
```
