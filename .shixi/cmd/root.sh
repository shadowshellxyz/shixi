#!/bin/bash

# alias shixirestart=source ~/.bash_profile

# alias ll=`ls -la -h`

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
    __pull_walker
    __pull_shixi
}
register_command "prepare" "__prepare"
register_command "morning" "__prepare"
register_command "pre" "__prepare"

__done(){

    # backup walker
    cd $SHADOWSHELL_HOME/walker
    shixi git backup

    # backup shixi
    cd $SHADOWSHELL_HOME/shixi
    shixi git backup

     # backup toolkit
    cd $SHADOWSHELL_LOCAL_HOME/shadowshell/toolkit
    shixi git backup
}
register_command "done" "__done"
register_command "evening" "__done"
