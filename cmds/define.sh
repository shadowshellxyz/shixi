#!/bin/bash

# execute command
execute_command(){
    command=$*
    # command is empty
    if [[ -z "$command" ]]
        then 
        command="jarvis"
    fi 
    # lookup command handler
    handler=${routing_table["$command"]}
    # log
    echo "command is '$command', handler is '$handler'."
    # execute command
    $handler
}

# alias command
alias jarvis=execute_command

# source files
source $JARVIS_COMMANDS_PATH/root.sh

# define commands
declare -A routing_table
routing_table["jarvis"]="jarvis_hello"
routing_table["morning"]="jarvis_prepare"
routing_table["prepare"]="jarvis_prepare"
routing_table["evening"]="jarvis_done"
routing_table["done"]="jarvis_done"
routing_table["date"]="jarvis_date"
routing_table["work pre"]="jarvis_work_prepare"
routing_table["work prepare"]="jarvis_work_prepare"
routing_table["work done"]="jarvis_work_done"
routing_table["read excel"]="python3 $JARVIS_COMMANDS_PATH/readexcel.py"
routing_table["write excel"]="python3 $JARVIS_COMMANDS_PATH/writeexcel.py"

