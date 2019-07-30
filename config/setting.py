import configparser
import os




# def getConfig(section, key):
conf = configparser.ConfigParser()
conf.read(os.path.split(os.path.realpath(__file__))[0] + '/setting.ini')
g_dingTalkHttpApi = conf.get('dingtalk', 'api')
g_flaskPort = conf.get('flask', 'port')