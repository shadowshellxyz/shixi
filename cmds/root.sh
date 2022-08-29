#!/bin/bash

# define commands path
JARVIS_COMMANDS_PATH=$JARVIS_HOME/Shadow/jarvis/cmds

source $JARVIS_COMMANDS_PATH/daily.sh
source $JARVIS_HOME/WorkNotes/.autoscript.sh

jarvis_hello(){
    msg="hello"
    echo $msg
}

jarvis_date(){
    msg=`date "+%Y-%m-%d %A %H:%M:%S"`
    echo $msg
}

jarvis_prepare(){
    pull_note
}

jarvis_done(){
    push_note
    push_jarvis
}

jarvis_work_prepare(){
    pull_worknotes
}

jarvis_work_doneq(){
    push_worknotes
}