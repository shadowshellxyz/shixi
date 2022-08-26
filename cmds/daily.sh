#!/bin/bash

timestamp=`date "+%Y%m%d%H%M%S"`
commit_msg="$timestamp auto backup."

refresh_git_config(){
    git config user.name shadow
    git config user.email shadowdefendernet@qq.com
}

# update notes
pull_note(){
    cd $JARVIS_HOME/Shadow/Note
    git pull origin main
    cd ~
}

# save notes
push_note(){
    cd $JARVIS_HOME/Shadow/Note
    refresh_git_config
    git add -A
    git commit -m $commit_msg
    git push origin main
}

push_jarvis(){
    cd $JARVIS_HOME/Shadow/jarvis
    refresh_git_config
    git add -A
    git commit -m $commit_msg
    git push origin main
}

