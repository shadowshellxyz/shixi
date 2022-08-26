#!/bin/bash

source $JARVIS_COMMANDS_PATH/daily.sh
source $JARVIS_HOME/WorkNotes/.autoscript.sh

# define commands path
JARVIS_COMMANDS_PATH=$JARVIS_HOME/Shadow/jarvis/cmds

jarvis_hello(){
    msg="hello"
    echo $msg
}

jarvis_ready(){
    pull_note
}

jarvis_bye(){
    push_note
    push_jarvis
}

jarvis_start_work(){
    pull_worknotes
}

jarvis_complete_work(){
    push_worknotes
}