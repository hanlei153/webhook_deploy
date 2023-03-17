# webhook_deploy
#### webhook_deploy 是一个自动同步github仓库代码的程序，比如你的仓库出现提交事件时触发webhook，实现同步代码到你的服务器上

### 克隆存储库

    git clone https://github.com/henlei153/webhook_deploy.git
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

### docker启动，-v将宿主机的代码路径映射到容器内，config.ini中path修改为映射到容器内的路径

    docker run -itd --name container_name -p 8000:8000 -v your_dir:your_dir image_name
    进入容器
    cd /opt/webhooks_deploy
    编辑你的config.ini
