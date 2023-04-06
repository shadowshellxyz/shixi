#!bin/bash


# 配置git信息

__git_config(){

   __git_config_view

   git config user.name 'shadowshell'
   git config user.email 'shadowshell@foxmail.com'

   __git_config_view

}
register_command "git config" "__git_config"

# 查看配置
__git_config_view(){
    echo  "user.name -> `git config user.name`"
    echo  "user.email -> `git config user.email`"
}
register_command "git config view" "__git_config_view"

__git_edit(){
    read "user_name?Input user name:" 
    git config user.name $user_name
    read "user_email?Input user email:" 
    git config user.email $user_email

    __git_config
}
register_command "git edit" "__git_edit"

# commit feature
__git_commit_feature(){
    
    read "message?Input commit message:" 
    git add *
    git commit -m "feature: $message"
}
register_command "git cmt fat" "__git_commit_feature"

# commit fix
__git_commit_fix(){
    
    read "message?Input commit message:" 
    git add *
    git commit -m "fix: $message"
}
register_command "git cmt fix" "__git_commit_fix"

# commit test
__git_commit_test(){
    
    read "message?Input commit message:" 
    git add *
    git commit -m "test: $message"
}
register_command "git cmt test" "__git_commit_test"

# commit docs
__git_commit_docs(){
    
    read "message?Input commit message:" 
    git add *
    git commit -m "docs: $message"
}
register_command "git cmt docs" "__git_commit_docs"

# auto backup
__git_auto_backup(){
    timestamp=date +'%Y%m%d%H%M%S'
    git add -A
    git commit -m "shixi auto backup,timestamp $timestamp."
    git push origin main   
}
register_command "git backup" "__git_auto_backup"
