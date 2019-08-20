import configparser
import os

from src.object.profil import Profil

CONFFILE = 'assets/profilConf.ini'

config = None

PROJECTPATH = 'projectpath'
REMINDERTIMEHOUR = 'remindertimehour'
REMINDERTIMEMIN = 'remindertimemin'
SLEEPTIME = 'sleeptime'

class ConfigService:
    
    

    def __init__(self, notificationService):
        self.config = configparser.ConfigParser()
        self.notificationService = notificationService
        if os.path.isfile('./' + CONFFILE):
            pass
            #self.logger.info('ConfigFile: {} exist.'.format(CONFFILE))
        else:
            #self.logger.info('ConfigFile: {} dont exist.'.format(CONFFILE))
            self.notificationService.showToastNotification("GitReminder","ConfigFile: dont exist. Will be created","assets/img/bell_check.ico")
            self.createDefaultConf()

    def reloadConfig(self):
        self.config = configparser.ConfigParser()



    def getSelections(self):
        self.config.read(CONFFILE)
        return self.config.sections()

    def getProfileBySelection(self, selection):
        self.config.read(CONFFILE)
        pp = ''
        rmh = 0
        rmm = 0
        st = 0
        for (each_key, each_val) in self.config.items(selection):
            if(each_key == PROJECTPATH):
                    pp = each_val
            if(each_key == REMINDERTIMEHOUR):
                    rmh = each_val
            if(each_key == REMINDERTIMEMIN):
                    rmm = each_val
            if(each_key == SLEEPTIME):
                    st = each_val
        return Profil(selection, rmh, rmm, pp, st)

    def readConf(self):
        self.config.read(CONFFILE)
        profilList = []
        for each_section in self.config.sections():
            
            pp = ''
            rmh = 0
            rmm = 0
            st = 0
            for (each_key, each_val) in self.config.items(each_section):
                if(each_key == PROJECTPATH):
                    pp = each_val
                if(each_key == REMINDERTIMEHOUR):
                    rmh = each_val
                if(each_key == REMINDERTIMEMIN):
                    rmm = each_val
                if(each_key == SLEEPTIME):
                    st = each_val
            profilList.append( Profil(each_section, rmh, rmm, pp, st))
        return profilList
        
    def createDefaultConf(self):
        #self.logger.info('ConfigFile = createDefaultConf: Start')
        self.config['DefaultProject'] = {PROJECTPATH: 'C:\\', REMINDERTIMEHOUR: 0, REMINDERTIMEMIN: 0, SLEEPTIME: 5}
        self.config.write(open(CONFFILE, 'w'))
        #self.logger.info('ConfigFile = createDefaultConf: OK')

    def createNewProfile(self, profileName):
        
        self.config.read(CONFFILE)
        self.config[profileName] = {PROJECTPATH: 'C:\\', REMINDERTIMEHOUR: 0, REMINDERTIMEMIN: 0, SLEEPTIME: 5}
        self.config.write(open(CONFFILE, 'w'))

    def deleteProfile(self, profileName):
        self.config.read(CONFFILE)
        self.config.remove_section(profileName)
        self.config.write(open(CONFFILE, 'w'))

    def saveProfile(self, profil):
        
        self.config.read(CONFFILE)
        self.config[profil.name] = {PROJECTPATH: profil.projectPath, REMINDERTIMEHOUR: profil.reminderTimeHour, REMINDERTIMEMIN: profil.reminderTimeMin, SLEEPTIME: profil.sleeptime}
        self.config.write(open(CONFFILE, 'w'))
        return self.readConf()