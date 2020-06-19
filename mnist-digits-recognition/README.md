
# MNIST Digits Recognition

The MNIST database of handwritten digits.

## Steps

1. Create Ubuntu Server GPU-instance in Azure
    - [Azure Data Science VM](https://portal.azure.com/#create/microsoft-dsvm.ubuntu-18041804) (NC family)
    - [Compute Instance](https://docs.microsoft.com/en-us/azure/machine-learning/concept-compute-instance) (NC family) in Azure Machine Learning service ([issue 1](https://github.com/codez0mb1e/AI-in-cloud-workshop/issues/1))
1. In terminal:
    - Check Ubuntu version: `lsb_release -a`
    - Check in terminal GPU device: `watch nvidia-smi`
    - Check RStudio Server status: `rstudio-server status`
    - Install htop: `sudo apt install htop`
1. Clone repo: `git clone https://github.com/codez0mb1e/AI-in-cloud-workshop.git`
1. Open [MNIST Digits Recognition with Keras](mnist-cnn.Rmd) in RStudio Server.
