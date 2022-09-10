#!/bin/bash

source $JARVIS_COMMANDS_PATH/dailycmds.sh
source $JARVIS_HOME/WorkNotes/.autoscript.sh

_jarvis(){
    jarvis_hello
    jarvis_date
}
register_command "jarvis" "_jarvis"

jarvis_hello(){
    msg="hello"
    echo $msg
}
register_command "hello" "jarvis_hello"

jarvis_date(){
    msg=`date "+%Y-%m-%d %A %H:%M:%S"`
    echo $msg
}
register_command "date" "jarvis_date"

jarvis_prepare(){
    pull_note
    # jarvis_work_prepare
}
register_command "prepare" "jarvis_prepare"
register_command "morning" "jarvis_prepare"
register_command "pre" "jarvis_prepare"

jarvis_done(){
    push_note
    push_jarvis
    # jarvis_work_done
}
register_command "done" "jarvis_done"
register_command "evening" "jarvis_done"

jarvis_work_prepare(){
    pull_worknotes
}
register_command "work prepare" "jarvis_work_prepare"

jarvis_work_done(){
    push_worknotes
}
register_command "work done" "jarvis_work_done"