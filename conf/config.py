import configparser
import os

#@property装饰器就是负责把一个方法变成属性调用的：
def get_config():
    config=configparser.ConfigParser()                  #实例化
    config_path=os.path.join(os.path.dirname(__file__),'confi.ini')   #获取配置文件路径 需要绝对路径，以防函数被被调用的时候，因为相对路劲引起报错
    config.read(config_path,encoding='utf-8')           #读取配置文件
    conf={"host":"","user":"","password":"","sender":"","email_host":"","email_port":""}                                    #初始值
    conf["host"]=config.get("host",'host')
    conf['user']=config.get("emial_conf","user")
    conf["password"]=config.get("emial_conf","password")
    conf["sender"]=config.get("emial_conf","sender")
    conf["email_host"]=config.get("emial_conf","email_host")
    conf["email_port"]=config.get("emial_conf","email_port")

    return conf

#print(get_config())