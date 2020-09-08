#!/bin/sh


# check that is not your VM
sudo apt install htop
htop


# check installed frameworks
python --version
pip --version


# clone this repo
git clone https://github.com/codez0mb1e/AI-in-cloud-workshop.git

# and switch to nessesary branch
cd AI-in-cloud-workshop/
git checkout azure-ml-ru
