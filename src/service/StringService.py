import configparser
import os



STRING_FILE = 'assets/Strings.ini'

class StringService:


    def getMetaInfos():
        config = configparser.ConfigParser()
        config.read(STRING_FILE)
        return config['MetaInformations']

    def getIcons(icon):
        config = configparser.ConfigParser()
        config.read(STRING_FILE)
        icons = config['Icons']
        return icons[icon]
    
    def getMessages():
        config = configparser.ConfigParser()
        config.read(STRING_FILE)
        return config['Messages']
       