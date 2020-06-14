
# AI in Microsoft Azure Workshop

## Syllabus

#### Introduction

[Opening speech](https://youtu.be/aew5exB5Xxg).

Requirements to the students:

1. Modern web browser
2. [Microsoft Azure Account](https://azure.microsoft.com/en-us/)
3. [Basic knowledge in R](https://codez0mb1e.github.io/StarRter/) or Python.

#### Module I: Basics of Machine Learning

##### Introduction to Machine Learning

Topics:

- ML terminology, scope and relevance
- ML tasks: supervised learning, unsupervised learning, and reinforcement learning
- ML algorithms: regression, classification, clustering
- Intuitive understanding of algorithms: from linear regression to neural networks.

Materials:

- [Slides](https://1drv.ms/p/s!Aq3CCEvm580vjLkCLr7vKvADYpWZgA?e=mKuzCn).

Advanced materials:

- [Introduction to Machine Learning course](https://coursera.org/learn/machine-learning), Stanford University
- [Introduction to Machine Learning course](https://coursera.org/learn/vvedenie-mashinnoe-obuchenie), HSE and Yandex.

##### Azure AI Platform

Topics:

- Data Science tools in Azure: basic programming languages, ML frameworks, and cloud services.
- Selecting an ML service for a specific task.

Materials:

- [Slides](https://1drv.ms/p/s!Aq3CCEvm580vjLkDGRcDRPR4GwXG-A?e=6jjCJw)
- [Introduction to Azure AI Platform](https://youtu.be/G-37PWkftGg) video lesson.

Advanced materials:

- [Azure.com/AI](https://www.azure.com/ai)
- [Microsoft AI Blog](https://blogs.microsoft.com/ai/).

##### Azure Machine Learning

Topics:

- Overview of the Azure Machine Learning
- Azure ML Datasets: upload, getting and transforming data
- Azure ML Designer: supported ML algorithms, train and evaluation model
- Azure ML Notebooks: an interactive application for analyzing and developing ML models
- AutoML in Azure ML
- Tools Azure ML: VS Code and Azure Machine Learning Extension for interaction with Azure ML.

Materials:

- [Getting started in Azure ML Studio](https://youtu.be/TXBV2Nnrpfc) video lesson.

Advanced materials:

- [Azure Machine Learning documentation](https://docs.microsoft.com/en-us/azure/machine-learning/)
- [Machine Learning Algorithm Cheat Sheet](https://docs.microsoft.com/en-us/azure/machine-learning/algorithm-cheat-sheet)
- [Lecture at HSE/MAMI on Azure Machine Learning](https://www.codeinstinct.pro/2015/10/azureml-lecture-at-hse.html)
- [Machine learning hackathon: How to win!](https://www.codeinstinct.pro/2015/11/azure-ml-hackathon.html).

##### Practice

1. Create [Azure ML Workspace](https://portal.azure.com/#create/Microsoft.MachineLearningServices) 
1. Azure ML Compute: сreate compute cluster
1. Azure ML Datasets: upload [Pima Indians Diabetes Database](https://www.kaggle.com/uciml/pima-indians-diabetes-database)
1. Azure ML Designer: create Pima Indians Diabetes Experiment and train model
1. Azure ML Notebooks: visualization using Jupyter Lab
1. Tools for Azure ML: install VS Code and Azure Machine Learning Extension.

#### Module II: Basics of Deep Learning

##### Introduction to Deep Learning

Topics:

- The current stage of neural network development
- Types of neural networks:
  - Fully connected neural networks (FNN)
  - Convolutional neural networks (CNN)
  - Recurrent neural networks (RNN)
  - Generative adversarial network ([GAN](https://github.com/codez0mb1e/evangelism/tree/master/AI-Workshop/samples/generative_models)).

Materials:

- [Slides](https://1drv.ms/p/s!Aq3CCEvm580vjLkEnIm-_G37lRIkZg?e=Jtcp8T).

Advanced materials:

- [Deep Learning Specialization](https://www.deeplearning.ai/deep-learning-specialization/) courses, Andrew Ng, et al.
- [Deep Learning Book](http://www.deeplearningbook.org/), Ian Goodfellow, et al.

##### Deep Learning in Azure AI Platform

##### Azure Data Science VM

Topics:

- Virtual machines for Data Science
- Data Science VM images types.

Materials:

- [Slides](https://1drv.ms/p/s!Aq3CCEvm580vjLkDGRcDRPR4GwXG-A?e=6jjCJw)
- [Neural Networks in Azure ML Studio](https://youtu.be/Pa5DmvvcwLI) video lecture.

Advanced materials:

- [Azure Data Science VM documentation](https://docs.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/)

##### Practice

- Deployment of Azure Deep Learning VM
- Handwriting recognition of digits (MNIST database)
  - [Azure ML](https://github.com/codez0mb1e/evangelism/tree/master/AI-in-Azure/demos/mnist-cnn-model--azure-ml)
  - [keras CNN](https://github.com/codez0mb1e/evangelism/tree/master/AI-in-Azure/demos/mnist-cnn-model--keras)
  - [keras autoencoder](https://github.com/codez0mb1e/evangelism/blob/master/AI-Workshop/samples/generative_models/simple_autoencoder.R)
- [Bitcoin price prediction](https://github.com/codez0mb1e/evangelism/tree/master/AI-Workshop/samples/LSTM)

#### Module III. Large Scalable Machine Learning

##### Big Data Concepts

[Slides]()

##### Big Data Ecosystem in Azure

[Practice](https://github.com/codez0mb1e/evangelism/tree/master/big-data-workshop/apache-spark-on-azure-vm)

##### Azure HDInsight

[Practice](https://github.com/codez0mb1e/evangelism/tree/master/big-data-workshop/apache-spark-on-azure-hdinsight)

##### Azure Databricks

[Practice](https://github.com/codez0mb1e/evangelism/tree/master/big-data-workshop/apache-spark-on-azure-databricks)

#### Module IV. _Optional Topics_

##### Auto ML

Materials:

- [Slides](http://0xcode.in/auto-ml-intro)
- [Azure Automated ML documentation](https://docs.microsoft.com/en-us/azure/machine-learning/service/concept-automated-ml)

Practice:

- [Prediction of the Dow Jones index on Donald Trump's tweets](http://0xcode.in/auto-ml-intro)

##### MLOps

- [Slides](https://www.codeinstinct.pro/2018/11/data-science-in-cloud.html)

#### Final Project

- Datasets hubs
  - [Azure Open Datasets](https://azure.microsoft.com/en-in/services/open-datasets/)
  - [Kaggle Datasets](https://www.kaggle.com/datasets)
  - [github.com/awesomedata](https://github.com/awesomedata/awesome-public-datasets)
- Research papers hubs
  - AI list on [arxiv.org](https://arxiv.org/list/cs.AI/recent)
- Communities
  - [datascience.stackexchange.com](https://datascience.stackexchange.com/)
  - [Github.com](https://github.com/)
  - [Kaggle](https://www.kaggle.com/)
  - [ML trainings](https://mltrainings.ru/)
  - ODS.ai.
