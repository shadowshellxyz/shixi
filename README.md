

# 环境

1. 安装 pip

``` SHELL
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py  
$ sudo python3 get-pip.py  
```

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

