#!/bin/bash

# routing table
declare -A ROUTING_TABLE
register_command(){
    command=$1
    handler=$2
    ROUTING_TABLE["$command"]=$handler
    # echo "Register command -->> command is '$command', handler is '$handler'."
}

# execute command
execute_command(){
    command=$*
    # echo "command is $command"
    # command is empty
    if [[ -z "$command" ]]
        then 
        command="shixi"
    fi 

    # lookup command handler
    handler=${ROUTING_TABLE["$command"]}
     # log
    # echo "command is '$command', handler is '$handler'."
    # handler is empty
    if [[ -z "$handler" ]]
    then 
        echo "Invalid command: $command"
    else
        # execute command
        $handler
    fi 
}

# alias command
alias shixi=execute_command

