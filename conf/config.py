import configparser
import os

def get_config():
    config=configparser.ConfigParser()                  #实例化
    config_path=os.path.join(os.path.dirname(__file__),'confi.ini')   #获取配置文件路径 需要绝对路径，以防函数被被调用的时候，因为相对路劲引起报错
    config.read(config_path,encoding='utf-8')           #读取配置文件
    conf={"host":""}                                    #初始值
    conf["host"]=config.get("host",'ip')

    return conf

