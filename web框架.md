web框架
请求，相应，业务逻辑
业务逻辑
![alt text](截图文件\image-41.png)
mvt模式
![alt text](截图文件\image-42.png)
m model 用于数据库交互，数据库增删改查
t template 负责封装js,html ,css
v view  负责业务逻辑层 接收请求，返回结果
##虚拟环境创建
mkdir ~/.virtualenvs
设置环境变量
sudo vim ~/.bashrc
![alt text](截图文件/image-43.png)
配置环境变量
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
![alt text](截图文件/image-44.png)
保存后运行
wq
source ~/.bashrc
创建虚拟环境
mkvirtualenv -p python3 myenv
![alt text](截图文件/image-45.png)
列出虚拟环境
lsvirtualenv
![alt text](截图文件/image-46.png)
激活虚拟环境
workon myenv
![alt text](截图文件/image-47.png)
退出虚拟环境
deactivate
![alt text](截图文件/image-48.png)
进入虚拟环境之后安装虚拟环境库
pip install requests
![alt text](截图文件/image-49.png)
创建py3_zzx虚拟环境
![alt text](截图文件/image-50.png)
列出虚拟环境
lsvirtualenv
![alt text](截图文件/image-51.png)
切换虚拟环境
workon py3_zzx
![alt text](截图文件/image-52.png)
删除虚拟环境
rmvirtualenv myenv
![alt text](截图文件/image-53.png)
虚拟环境下列出安装的库
pip list
创建第一个django项目
django-admin startproject bookmanager
进入项目目录
cd bookmanager
tree
![alt text](截图文件/image-55.png)
配置文件详解
![alt text](截图文件/image-56.png)
运行manage.py
python manage.py runserver
![alt text](截图文件/image-57.png)
success!
![alt text](截图文件/image-58.png)
注意事项
![alt text](截图文件/image-59.png)
创建子应用
![alt text](截图文件/image-66.png)
![alt text](截图文件/image-67.png)
层级关系
![alt text](截图文件/image-68.png)
主要用view 和 model 
![alt text](截图文件/image-69.png)
ORM模型可以操作各种关系型数据库，可以转换为特定数据库的insert、update、delete语句，当数据库返回数据集时，再转换为python中的列表
![alt text](截图文件/image-71.png)
MVT设计模式中的model内嵌了orm模型（面向对象）所以需要定义模型类，完成数据库增删改查关系对应
![alt text](截图文件/image-72.png)
类对应数据表，对象对应数据行，属性对应字段
1
