#!bin/bash
# author:shadowshell

# config

__git_config_init(){

   __git_config_view

   git config user.name 'shadowshell'
   git config user.email 'shadowshell@foxmail.com'

   __git_config_view

}
register_command "git cfg init" "__git_config_init"

# view config
__git_config_view(){
    echo  "user.name -> `git config user.name`"
    echo  "user.email -> `git config user.email`"
}
register_command "git cfg view" "__git_config_view"

# edit config
__git_config_edit(){
    read "user_name?Input user name:" 
    git config user.name $user_name
    read "user_email?Input user email:" 
    git config user.email $user_email

    __git_config
}
register_command "git cfg edit" "__git_config_edit"

# git add & commit & push
__git_acp(){

   # get current branch name
   current_branch_name=`git rev-parse --abbrev-ref HEAD`
   
   # pull latest
   git pull origin $current_branch_name

   # read commit message
   read -a commit_type -p "Input your commit type : "
   read -a commit_message -p "Input your commit message : " 
   pre_commit_message="[$commit_type]:$commit_message"

   # prompt
   echo "Your prepare commit message is : $pre_commit_message."

   # git add & commit & push
   git add -A
   git commit -m $pre_commit_message
   git push origin $current_branch_name

}
register_command "git acp" "__git_acp"

# backup
__git_backup(){

    printf "\n\n"
    printf  "......shixi backup preparing......"
    printf "\n\n"

    current_branch_name=`git rev-parse --abbrev-ref HEAD`
    timestamp=`date +'%Y%m%d%H%M%S'`
    git add -A
    git commit -m "shixi auto backup,timestamp $timestamp."
    git push origin $current_branch_name  
   
    printf "\n\n"
    printf "......shixi backup ended......"
    printf "\n\n"
}
register_command "git bak" "__git_backup"
register_command "git backup" "__git_backup"


