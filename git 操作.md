git 操作
git init 初始化一个仓库s
![alt text](截图文件\image-27.png)
![alt text](截图文件\image-28.png)
创建仓库之后需要设置个人信息
git config --global user.name "用户名"
git config --global user.email "邮箱"
![alt text](截图文件\image-29.png)
git status 查看仓库状态
![alt text](截图文件\image-30.png)
git add 文件名 添加文件到暂存区
![alt text](截图文件\image-31.png)
git commit -m "提交说明" 提交文件到仓库
![alt text](截图文件\image-32.png)
git log 查看提交历史  上述操作用于
![alt text](截图文件\image-33.png)
git reset --hard HEAD^ 回退到上一个版本
git reset --hard HEAD^^ 回退到上上一个版本
git reflog 查看命令历史
git reset --hard 版本号 回退到指定版本
![alt text](截图文件\image-35.png)
![alt text](截图文件\image-34.png)
git reset HEAD 文件名 取消暂存区文件 由绿色变红色
![alt text](截图文件\image-36.png)
git checkout -- 文件名 丢弃工作区文件 变成未暂存区文件
![alt text](截图文件\image-37.png)
git clone 仓库地址 克隆一个仓库
![alt text](截图文件\image-38.png)
git status 查看仓库状态
git add 文件名 添加文件到暂存区
git commit -m "提交说明" 提交文件到仓库
git push 推送到远程仓库
![alt text](截图文件\image-39.png)
![alt text](截图文件\image-40.png)
1、基本步骤,vim 修改(i插入，esc退出插入,:wq保存并退出)
2、git status 查看仓库状态
3、git add 文件名 添加文件到暂存区
4、git commit -m "提交说明" 提交文件到仓库
5、git push 推送到远程仓库

密钥问题
检查本地主机是否已经存在ssh key
cd ~/.ssh
ls
![alt text](截图文件/image-60.png)
生成ssh key
ssh-keygen -t rsa -C "zhouh2209@gmail.com"
//执行后一直回车即可
获取ssh key公钥内容
cd ~/.ssh
cat id_rsa.pub
复制公钥内容
![alt text](截图文件/image-61.png)
Github账号上添加公钥
![alt text](截图文件/image-62.png)
验证是否设置成功
ssh -T git@github.com
![alt text](截图文件/image-63.png)

配置连接问题
配置远程仓库地址
git remote add origin git@github.com:ivea76-create/py3_django.git
验证远程仓库配置
git remote -v
![alt text](截图文件/image-64.png)
执行推送操作
git push 
推送到master分支
git push origin master
![alt text](截图文件/image-65.png)
111