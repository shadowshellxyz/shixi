#!/bin/bash

# author: shadow walker

shixi(){

  echo 'Hello, now is '`date +'%Y-%m-%d %H:%M:%S'`
}

shixi_clone(){

  # gitee
  # git clone git@gitee.com:shadowshell/shixi.git  
  # git clone git@gitee.com:shadowshell/walker.git
  # git clone git@gitee.com:shadowshell/toolkit.git
  
  # github
  # git clone git@github.com:shadowshellxyz/shixi.git
  
  # git clone git@github.com:shadowshellxyz/walker.git
  
  # git clone git@github.com:shadowshellxyz/toolkit.git

}

shixi_init(){

  git remote set-url github git@github.com:shadowshellxyz/shixi.git

}

shixi_pre(){

  cd $SHIXI_HOME/shixi
  shixi_git_pull

  cd $SHIXI_HOME/walker
  shixi_git_pull  
}

shixi_done(){

  cd $SHIXI_HOME/shixi
  shixi_git_bak

  cd $SHIXI_HOME/walker
  shixi_git_bak
}

