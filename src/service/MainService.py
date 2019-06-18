
from conf_reader.reader import ConfReader

from src.service.SysTrayService import SysTrayService
class MainService:
        
    def __init__(self, logger):
        self.logger = logger
        self.logger.debug(' INI MainService')

        
        ConfReader('VCSR_INI.ini')
        self.successIcon = ConfReader.get('Icons', 'success') 
        self.warningIcon = ConfReader.get('Icons', 'warning') 
        self.errorIcon = ConfReader.get('Icons', 'error') 

        self.statusOk = ConfReader.get('Messages', 'status_ok') 
        self.statusChanged = ConfReader.get('Messages', 'status_changed') 
        self.statusError = ConfReader.get('Messages', 'status_error') 

        
        self.sysTrayService = SysTrayService(self, logger)
        self.sysTrayService.start()
        self.isRunning = False
        self.threads = [] 