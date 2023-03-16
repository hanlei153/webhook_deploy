# webhook_deploy
#### webhook_deploy 是一个自动同步github仓库代码的程序，比如你的仓库出现提交事件时触发webhook，实现同步代码到你的服务器上

### 克隆存储库

    git clone git@github.com:henlei153/webhook_deploy.git  
    cd webhook_deploy

### 定义你的config.ini

    cat config.ini  
    [git@github:hanlei153/webhook_deploy.git]  
    ;path为代码部署目录  
    path=/home/www

### 部署

    pip3 install flask   
    python3 webhooks.py

### 之后在你的仓库中添加webhook

    webhook地址：
    server:8000/webhooks/github
