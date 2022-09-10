#!/bin/bash

timestamp=`date "+%Y%m%d%H%M%S"`
commit_msg="$timestamp auto backup."

# update notes
pull_note(){
    cd $SHADOW_SHIELDS_HOME/Note
    git pull origin main
    cd ~
}

# save notes
push_note(){
    cd $SHADOW_SHIELDS_HOME/Note
    refresh_git_config
    git add -A
    git commit -m $commit_msg
    git push origin main
}

push_jarvis(){
    cd $SHADOW_SHIELDS_HOME/jarvis
    refresh_git_config
    git add -A
    git commit -m $commit_msg
    git push origin main
}

refresh_git_config(){
    git config user.name shadow
    git config user.email shadowwalkerxyz@qq.com
}

