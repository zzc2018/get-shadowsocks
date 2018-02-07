# coding: utf-8
import commands


def environment():
    need_install = []
    b = commands.getstatusoutput("wget --version")
    if b[0] == 0:
        print("wget 已经安装")
    else:
        print("wget 需要安装")
        need_install.append("wget")
    a = commands.getstatusoutput("pip --version")
    if a[0] == 0:
        print("pip 已经安装")
    else:
        print("pip 需要安装")
        need_install.append("pip")
    h = commands.getstatusoutput("pip --version")
    if h[0] == 0:
        print("requests 已经安装")
    else:
        print("requests 需要安装")
        need_install.append("requests")
    return need_install


def get_pip():
    c = commands.getstatusoutput("wget -P ./.get_shadowsocks http://zzc2018.cn/get-pip.py")
    if c[0] == 0:
        pass
    else:
        print("pip 安装失败")
    d = commands.getstatusoutput("python ./.get_shadowsocks/get-pip.py")
    if d[0] ==0:
        print("pip 安装成功")
    else:
        print("pip 安装失败")


def get_shadowsocks():
    k = commands.getstatusoutput("ssserver --version")
    if k[0] == 0:
        print("shadowsocks 已经安装")
    else:
        commands.getstatusoutput("pip install shadowsocks")
        f = commands.getstatusoutput("ssserver --version")
        if f[0] == 0:
            print("shadowsocks 安装成功")
        else:
            print("shadowsocks 安装失败")


def write_json():
    port = int(input("请输入端口: "))
    passwd = str(input("请输入密码"))
    import requests
    ip = requests.get("http://2017.ip138.com/ic.asp").text
    ip = ip[ip.find("[") + 1 : ip.find("]")]
    text = """
    {
    "server":"%s",
    "server_port":%d,
    "local_address": "127.0.0.1",
    "local_port":1080,
    "password":"%s",
    "timeout":300,
    "method":"aes-256-cfb"
    }
    """ % (ip, port, passwd)
    g = open("/etc/sss.json", "w")
    g.write(text)
    g.close


def get_wget():
    i = commands.getstatusoutput("yum -y install wget")
    if i[0] == 0:
        print("wget 安装成功")
    else:
        print("wget 安装失败")


def get_requests():
    j = commands.getstatusoutput("pip install requests")
    if j[0] == 0:
        print("requests 安装成功")
    else:
        print("requests 安装失败")


def delete_dir():
    commands.getstatusoutput("rm -rf ./.get_shadowsocks")


def main():
    mkdir = commands.getstatusoutput("mkdir ./.get_shadowsocks")
    if mkdir[0] == 0:
        pass
    else:
        print("创建目录失败")
    needs = environment()
    if needs:
        for i in needs:
            if i == "pip":
                get_pip()
            if i == "requests":
                get_requests()
            if i == "wget":
                get_wget()
        needs = environment()
    get_shadowsocks()
    write_json()
    delete_dir()


if __name__ == '__main__':
    main()
