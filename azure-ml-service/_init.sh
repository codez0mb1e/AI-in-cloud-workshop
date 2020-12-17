#!/bin/sh

# check installed frameworks
python --version
pip --version

# update pip (optional)
pip install --upgrade pip

# install dependencies
pip install -r requirements.txt