FROM python:3.9-alpine3.17
MAINTAINER HANLEI
WORKDIR /opt
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories && \
    apk add openssh git --no-cache && \
	cd /opt && git clone https://github.com/hanlei153/webhook_deploy.git && \
	pip3 install flask
EXPOSE 8000
CMD ["sh", "-c", "/usr/local/bin/python3 /opt/webhook_deploy/webhooks.py"]
