#!bin/bash

jarvis_git_config(){
    git config user.name
    git config user.email
}
register_command "git config" "jarvis_git_config"

jarvis_git_edit(){
    read "user_name?Input user name:" 
    git config user.name $user_name
    read "user_email?Input user email:" 
    git config user.email $user_email

    jarvis_git_config
}
register_command "git edit" "jarvis_git_edit"