#!/bin/bash

# execute command
execute_command(){
    handler=${routing_table["$*"]}
    echo "command is '$*', handler is '$handler'."
    `$handler`
}

# alias command
alias jarvis=execute_command

# source files
source $JARVIS_COMMANDS_PATH/root.sh

# define commands
declare -A routing_table
routing_table["morning"]="jarvis_ready"
routing_table["evening"]="jarvis_bye"
routing_table["date"]="Hello shadow, now is `date "+%Y-%m-%d %A %H:%M:%S".`"
routing_table["start work"]="jarvis_start_work"
routing_table["complete work"]="jarvis_complete_work"
routing_table["read excel"]="python3 $JARVIS_COMMANDS_PATH/readexcel.py"
routing_table["write excel"]="python3 $JARVIS_COMMANDS_PATH/writeexcel.py"