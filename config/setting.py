import configparser
import os




# def getConfig(section, key):
conf = configparser.ConfigParser()
conf.read(os.path.split(os.path.realpath(__file__))[0] + '/setting.ini')
    # return conf.get(section, key)