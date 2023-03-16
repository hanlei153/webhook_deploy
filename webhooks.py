import flask,json,os,configparser,subprocess
server = flask.Flask(__name__)

file = 'config.ini'
#创建配置文件对象
con = configparser.ConfigParser()

#读取配置文件
con.read(file, encoding='utf-8')

#获取所有section
sections = con.sections()

@server.route('/webhooks/github',methods=['post'])
def github_hooks():

    #获取json
    data = flask.request.get_json()

    #获取存储库url
    git_url = data['repository']['git_url']
    http_url = data['repository']['clone_url']

    #获取分支
    branch = data['ref']
    branch = branch.split('/')

    #通过获取到的url匹配config.ini中定义的section中的path
    for i in sections:
        if git_url == i or http_url == i:

            #获取到path
            path = con.items(i)
            path = path[0][1]

            #切换到path目录
            os.chdir(path)

            #获取远程仓库名称
            git_remote = "git remote -v | grep 'push' | awk '{print $1}'"
            p1 = subprocess.Popen(git_remote, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            p1_output, p1_error = p1.communicate()


            #git pull远程仓库
            git_pull = "sudo git pull {} {}".format(p1_output.decode().strip(), branch[2])
            p2 = subprocess.Popen(git_pull, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            p2_output, p2_error = p2.communicate()

            #返回命令执行状态
            res = {'git_remote':p1_output.decode().strip(),'git_pull':p2_output.decode().strip()}
            return res
        else:
            res = {'msg': '未匹配到定义的存储库'}
            return json.dumps(res, ensure_ascii=False)


if __name__ == '__main__':
    server.run(
        host='0.0.0.0',
        port=8000,
        debug=True
    )