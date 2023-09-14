#!/usr/bin/env bash

sudo apt-get -y install python3-venv # Install pip package
sudo rm -rf ~/env     # remove existing venv
python3 -m venv env # Creates virtual environment
