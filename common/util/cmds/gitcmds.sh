#!bin/bash


# 配置git信息

jarvis_git_config(){

   jarvis_git_config_view

   git config user.name 'ShadowShell'
   git config user.email 'shadowshell@foxmail.com'

   jarvis_git_config_view

}
register_command "git config" "jarvis_git_config"

# 查看配置
jarvis_git_config_view(){
    echo  "user.name -> `git config user.name`"
    echo  "user.email -> `git config user.email`"
}
register_command "git config view" "jarvis_git_config_view"

jarvis_git_edit(){
    read "user_name?Input user name:" 
    git config user.name $user_name
    read "user_email?Input user email:" 
    git config user.email $user_email

    jarvis_git_config
}
register_command "git edit" "jarvis_git_edit"

# commit feature
jarvis_git_commit_feature(){
    
    read "message?Input commit message:" 
    git add *
    git commit -m "feature: $message"
}
register_command "git cmt fat" "jarvis_git_commit_feature"

# commit fix
jarvis_git_commit_fix(){
    
    read "message?Input commit message:" 
    git add *
    git commit -m "fix: $message"
}
register_command "git cmt fix" "jarvis_git_commit_fix"

# commit test
jarvis_git_commit_test(){
    
    read "message?Input commit message:" 
    git add *
    git commit -m "test: $message"
}
register_command "git cmt test" "jarvis_git_commit_test"

# commit docs
jarvis_git_commit_docs(){
    
    read "message?Input commit message:" 
    git add *
    git commit -m "docs: $message"
}
register_command "git cmt docs" "jarvis_git_commit_docs"