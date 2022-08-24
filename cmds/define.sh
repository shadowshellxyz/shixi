#!/bin/bash

# source files
source $JARVIS_COMMANDS_PATH/root.sh

# define commands
alias jarvis=execute_command

execute_command(){
    #echo $*
    if [ "$*" = "ready" ]
    then
        jarvis_ready
    elif [ "$*" = "bye" ]
    then
        jarvis_bye
    elif [ "$*" = "date" ]
    then
        echo "Hello shadow, now is `date "+%Y-%m-%d %A %H:%M:%S".`"
    elif [ "$*" = "start work" ]
    then
        jarvis_start_work
    elif [ "$*" = "complete work" ]
    then
        jarvis_complete_work
    elif [ "$*" = "read excel" ]
    then
        python3 $JARVIS_COMMANDS_PATH/readexcel.py
    elif [ "$*" = "write excel" ]
    then
        python3 $JARVIS_COMMANDS_PATH/writeexcel.py
    else 
        echo "Invalid command : $*."
    fi
}