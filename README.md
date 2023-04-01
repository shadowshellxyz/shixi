

# INSTALL

``` shell
$ vi  ~/.bash_profile
$ source ~/.bash_profile

export JARVIS_HOME=/Users/shadow/Workbench
source $JARVIS_HOME/ShadowShellDotXyz/jarvis/setup.sh

```

# 环境

1. 安装 pip

``` SHELL
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py  
$ sudo python3 get-pip.py  
```

- 替换pip源

``` shell
~ mkdir ~/.pip
~ vi ~/.pip/pip.conf
```
复制下面的代码
``` shell
[global]
index-url = https://mirrors.aliyun.com/pypi/simple
```

国内其他pip源，清华的５分钟同步一次官网，建议使用

清华：https://pypi.tuna.tsinghua.edu.cn/simple
中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
华中理工大学：http://pypi.hustunique.com/
山东理工大学：http://pypi.sdutlinux.org/
豆瓣：http://pypi.douban.com/simple/
————————————————

2. 安装 python3

```
https://www.python.org/downloads/mac-osx/
```

# 依赖管理

> python3使用pip3进行依赖管理

1. 创建依赖管理文件

- 在工程根目录下创建文件（requirements.txt）用于管理依赖

2. 生成依赖
``` SHELL
pip3 freeze > requirements.txt
```

3. 安装依赖
``` SHELL
pip3 install -r requirements.txt
```

