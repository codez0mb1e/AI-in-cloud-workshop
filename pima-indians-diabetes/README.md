
# Pima Indians Diabetes Lab

## Objective

Using Machine Learning methods predict whether or not a patient has diabetes, based on certain diagnostic measurements. 

## Content

The datasets consists of several medical predictor variables and one target variable, `Outcome`. Predictor variables includes the number of pregnancies the patient has had, their BMI, insulin level, age, and so on.

Several constraints were placed on the selection of these instances from a larger database. In particular, all patients here are females at least 21 years old of Pima Indian heritage.

## Steps

1. Create [Azure ML Workspace](https://portal.azure.com/#create/Microsoft.MachineLearningServices)
1. Azure ML Compute: create compute cluster
1. Azure ML Datasets: upload [Pima Indians Diabetes Database](https://www.kaggle.com/uciml/pima-indians-diabetes-database)
1. Azure ML Designer: create Pima Indians Diabetes Experiment and train model
1. Azure ML Notebooks: [clone repo](init.sh) and [Pima Indians Diabetes EDA](EDA.ipynb)
1. Tools for Azure ML: install VS Code and Azure Machine Learning Extension.

## Acknowledgements

Smith, J.W., Everhart, J.E., Dickson, W.C., Knowler, W.C., & Johannes, R.S. (1988). [Using the ADAP learning algorithm to forecast the onset of diabetes mellitus](http://rexa.info/paper/04587c10a7c92baa01948f71f2513d5928fe8e81). In Proceedings of the Symposium on Computer Applications and Medical Care (pp. 261--265). IEEE Computer Society Press.
