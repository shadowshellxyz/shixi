#!/bin/bash

timestamp=`date "+%Y-%m-%d %H:%M:%S"`
# update notes
pull_note(){
    cd $JARVIS_HOME/Shadow/Note
    git pull origin main
    cd ~
}

# save notes
push_note(){
    cd $JARVIS_HOME/Shadow/Note
    git add -A
    git commit -m 'auto backup -> $timestamp'
    git push origin main
}

push_jarvis(){
    cd $JARVIS_HOME/Shadow/jarvis
    git add -A
    git commit -m 'auto backup -> $timestamp'
    git push origin main
}

