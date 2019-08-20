import configparser
import os



STRING_FILE = 'assets/Strings.ini'

class StringService:


    def getMetaInfos(metaInfo):
        config = configparser.ConfigParser()
        config.read(STRING_FILE)
        meta = config['MetaInformations']
        return meta[metaInfo]

    def getIcons(icon):
        config = configparser.ConfigParser()
        config.read(STRING_FILE)
        icons = config['Icons']
        return icons[icon]
    
    def getMessages(message):
        config = configparser.ConfigParser()
        config.read(STRING_FILE)
        messages = config['Messages']
        return messages[message]
       