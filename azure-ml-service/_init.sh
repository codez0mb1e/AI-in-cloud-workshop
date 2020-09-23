#!/bin/sh

# check installed frameworks
python --version
pip --version

# install dependencies
pip install -r requirements.txt

# update installed dependecies (optional)
# pip install --upgrade azureml-sdk --use-feature=2020-resolver