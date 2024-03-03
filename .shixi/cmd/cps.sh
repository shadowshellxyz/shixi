#!/bin/bash

# author: ShadowShell

jarvis_startup_chatbot(){
    $SHADOWSHELL_HOME/Code/chatbot/startup.sh
}
register_command "startup chatbot" "jarvis_startup_chatbot"

jarvis_startup_cps(){
    $SHADOWSHELL_HOME/Code/cps/startup.sh
}
register_command "startup cps" "jarvis_startup_cps"



