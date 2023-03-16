# webhook_deploy

### 克隆存储库
> 例：
git clone git@github.com:henlei153/webhook_deploy.git  
cd webhook_deploy

### 定义你的config.ini
> 例：  
cat config.ini  
[git@github:hanlei153/webhook_deploy.git]  
;path为代码部署目录  
path=/home/www  

### 部署
pip3 install flask  
python3 webhooks.py
