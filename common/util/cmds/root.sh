#!/bin/bash

# alias jarvis.restart=source ~/.bash_profile

source $SHIXI_COMMANDS_PATH/dailycmds.sh
# source $WORK_NOTES_HOME/.jarvis/.jarvis.sh

__shixi(){
    __hello
    __date
}
register_command "shixi" "__shixi"

__hello(){
    msg="hello"
    echo $msg
}
register_command "hello" "__hello"

__date(){
    msg=`date "+%Y-%m-%d %A %H:%M:%S"`
    echo $msg
}
register_command "date" "__date"

__prepare(){
    pull_note
    # jarvis_work_prepare
}
register_command "prepare" "__prepare"
register_command "morning" "__prepare"
register_command "pre" "__prepare"

__done(){
    push_note
    push_jarvis
    # jarvis_work_done
}
register_command "done" "__done"
register_command "evening" "__done"
