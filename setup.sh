#!/bin/bash
# author: Shadow

printf "\n>>>>>>>>>>>>...setup begining...\n"

pip3 freeze > requirements.txt
pip3 install -r requirements.txt

printf ">>>>>>>>>>>>>....setup ended...\n"
