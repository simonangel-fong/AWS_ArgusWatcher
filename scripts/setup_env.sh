#!/bin/bash

# sudo apt-get -y install python3-venv # Install pip package
# echo "install env" > ~/log
sudo rm -rf ~/env     # remove existing venv
echo "remove env" > ~/log
python3 -m venv env # Creates virtual environment
echo "create env" > ~/log
