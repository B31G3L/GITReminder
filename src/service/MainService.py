
from conf_reader.reader import ConfReader
from src.service.SysTrayService import SysTrayService
from src.service.NotificationService import NotificationService
from src.service.ConfigService import ConfigService
from threading import Thread

class MainService:
        
    def __init__(self, logger):
        self.logger = logger
        self.sysTrayService = SysTrayService(self, logger)
        self.sysTrayService.start()
        self.configService = ConfigService(self.logger)
        self.isRunning = False
        self.threads = [] 



    def start(self):
        self.logger.info('MainService:  start')
        NotificationService.showToastNotification('GIT Push Reminder', 'Started', "assets/img/bell_check.ico")
        self.logger.info('MainService:  load Config File == Start')
        self.configService.reloadConfig()
        self.logger.info('MainService:  load Config File == OK')
        self.isRunning = True
        self.logger.info('MainService:  getSelections == START')
        selections = self.configService.getSelections()
        self.logger.info('MainService:  getSelections == {} Selections found'.format(len(selections)))
        self.logger.debug(' {} Threads found'.format(len(self.threads)))
        for selection in selections:
            thread = Thread(target=self.profileThreads, args=(selection,))
            self.threads += [thread]
            thread.start()


    def stop(self):
        self.logger.debug('Stop is called')
        self.isRunning = False
        self.logger.debug(' {} Threads found to stop '.format(len(self.threads)))
        for x in  self.threads: 
            x.join()
        self.threads = []
        NotificationService.showToastNotification('GIT Push Reminder', 'Stopped', "assets/img/bell_check.ico")


    def restart(self):
        self.logger.debug('Restart is called')
        self.stop()
        self.start()
