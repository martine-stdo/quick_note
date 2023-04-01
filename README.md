# quick_note
# 一个小便签📙
## 功能介绍：
具有登录认证功能，使用了sqlalchmey数据库，基于flask框架
搭建<br>
认证界面由使用CryptoJS对密码进行加密处理，后端使用hashlib进行md5加密增加了数据传输的安全性<br>
根据油管视频：https://www.youtube.com/watch?v=Z1RJmh_OqeA 修改而来
## 页面外观：
### 认证界面
输入正确的密码进入功能页面否则跳转error页面
[![ppWVD9s.png](https://s1.ax1x.com/2023/04/01/ppWVD9s.png)](https://imgse.com/i/ppWVD9s)

### error界面
[![ppWVr3n.png](https://s1.ax1x.com/2023/04/01/ppWVr3n.png)](https://imgse.com/i/ppWVr3n)
### 主功能界面
[![ppWVcuV.png](https://s1.ax1x.com/2023/04/01/ppWVcuV.png)](https://imgse.com/i/ppWVcuV)

### 更新信息页面
[![ppWVyj0.png](https://s1.ax1x.com/2023/04/01/ppWVyj0.png)](https://imgse.com/i/ppWVyj0)
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
8.完成上述步骤以后修改app.py中的配置，如下图所示
***
[![ppWVwNQ.png](https://s1.ax1x.com/2023/04/01/ppWVwNQ.png)](https://imgse.com/i/ppWVwNQ)
9.运行 ```python ./app.py```