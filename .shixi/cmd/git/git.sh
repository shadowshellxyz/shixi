#!bin/bash
# author:shadow walker

git_gen_sshkeys(){
    
    ssh-keygen -t rsa -C 'shadowshell@foxmail.com' -f ~/.ssh/id_rsa_github
    ssh-keygen -t rsa -C 'shadowshell@foxmail.com' -f ~/.ssh/id_rsa_gitee

    cp ~/.ssh/id_rsa_github.pub $SHIXI_HOME/
    cp ~/.ssh/id_rsa_gitee.pub $SHIXI_HOME/
    
}

git_recfg(){
    cp -rf $SHIXI_CMD_HOME/git/config ~/.ssh/
}

git_cfg_test(){
    ssh -T git@gitee.com
}

git_cfg_view(){
    cat ~/.ssh/config
}

# config

shixi_git_cfg_init(){

   shixi_git_cfg_view
  
   git config user.name 'shadowshell'

   git config user.email 'shadowshell@foxmail.com'

   shixi_git_cfg_view

}

# view config
shixi_git_cfg_view(){
    echo  "user.name -> `git config user.name`"
    echo  "user.email -> `git config user.email`"
}

# pull
shixi_git_pull(){
    git pull
}

# backup
shixi_git_bak(){

    # init git config
    shixi_git_cfg_init

    printf "\n\n"
    printf  "......shixi backup preparing......"
    printf "\n\n"

    timestamp=`date +'%Y%m%d%H%M%S'`
    git add -A
    git commit -m "shixi auto backup,timestamp $timestamp."
    git push  
   
    printf "\n\n"
    printf "......shixi backup ended......"
    printf "\n\n"
}

# edit config
shixi_git_config_edit(){
    read "user_name?Input user name:" 
    git config user.name $user_name
    read "user_email?Input user email:" 
    git config user.email $user_email

    shixi_git_config_view
}

# get branch name
shixi_git_get_branch_name(){
    return `git rev-parse --abbrev-ref HEAD`    
}

# git add & commit & push
__git_acp(){

   # get current branch name
   current_branch_name=`__git_get_branch_name`
   
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
#register_command "git acp" "__git_acp"

