# quick_note

# 一个基于flask框架的小便签
**********
## 功能介绍：
具有登录认证功能，使用了sqlalchmey数据库，基于flask
根据视频：https://www.youtube.com/watch?v=Z1RJmh_OqeA 修改而来
## 页面外观：
#### 认证界面，输入正确的密码进入功能页面否则跳转error页面
[![ppg0zDO.png](https://s1.ax1x.com/2023/03/30/ppg0zDO.png)](https://imgse.com/i/ppg0zDO)
#### 功能界面
[![ppg0xKK.png](https://s1.ax1x.com/2023/03/30/ppg0xKK.png)](https://imgse.com/i/ppg0xKK)
****

## 使用方法
1. 具备python3环境
2. 运行```pip3 install virtualenv```安装python虚拟环境
3. ```pip3 virtual env```创建一个python虚拟环境
4. 激活python虚拟化境
* 对于windows平台：```env/Scripts/activate```
* 对于Linux平台：```source env/bin/activate ```
5. 安装运行所需要的依赖：```pip3 install requirement.txt```
6. 将原本文件中的/instance/test.db删除
7. 确保处于python虚拟环境中输入如下指令：
```
$ python
>>> from project import app, db
>>> app.app_context().push()
>>> db.create_all()
```
8.完成上述步骤以后修改app.py中的password为自己想要的值，cookies也可以自己设置，但要确保app.py中所有的cookies值一致
9.运行 ```python ./app.py```