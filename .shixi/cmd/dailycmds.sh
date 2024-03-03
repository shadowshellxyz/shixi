#!/bin/bash

timestamp=`date "+%Y%m%d%H%M%S"`
commit_message="shixi auto backup,timestamp $timestamp."

# update notes
__pull_walker(){
    cd $SHADOWSHELL_HOME/walker
    git pull origin main
    cd ~
}

# save notes
__push_walker(){
    cd $SHADOWSHELL_HOME/walker
    refresh_git_config
    git add -A
    git commit -m $commit_message
    git push origin main
}

__pull_shixi(){
    cd $SHADOWSHELL_HOME/shixi
    git pull origin main
    cd ~
}

__push_shixi(){
    cd $SHADOWSHELL_HOME/shixi
    refresh_git_config
    git add -A
    git commit -m $commit_message
    git push origin main
}

refresh_git_config() {
    git config user.name shadowshell
    git config user.email shadowshell@foxmail.com
}

