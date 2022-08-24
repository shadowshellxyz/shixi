#!/bin/bash
# author: Shadow

printf "\n>>>>>>>>>>>>...setup begining...\n"

# source files
source $JARVIS_HOME/Shadow/jarvis/cmds/define.sh

# install python dependencies
pip3 freeze > requirements.txt
pip3 install -r requirements.txt

printf ">>>>>>>>>>>>>....setup ended...\n"
