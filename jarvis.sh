#!/bin/bash

################
# author: Shadow 
################

# setup
source ./setup.sh

communicate(){
    read -p "Input your command > " command
    until [ "$command" = "bye" ]
    do  
        printf "Received one command > $command\n"
        read -p "Input your command > " command
    done 
}
executeCommand(){
    result=`python3 -c 'from core.office.excel_util import ExcelUtil;excel_util = ExcelUtil();excel_util.read("/Users/shadow/Desktop/test.xlsx");'`
    printf "$result"
}

# executeCommand
communicate

echo ">>> bye bye"
