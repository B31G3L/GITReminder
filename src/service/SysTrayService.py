import sys

from infi.systray import SysTrayIcon
from conf_reader.reader import ConfReader
from PySide2 import QtWidgets

from src.gui.setStyle import setPalette

from src.service.AboutUIService import AboutUIService



CHECK_ICO = 'assets/img/bell_check.ico'
ERROR_ICO = 'assets/img/bell_x.ico'
CHANGE_ICO = 'assets/img/bell_clock.ico'

STATUS_OK = 'Git-Reminder Status: ok'
STATUS_CHANGE = 'Git-Reminder Status: Commit/Push erforderlich'
STATUS_ERROR = 'Git-Reminder Status: Repo nicht gefunden'
class SysTrayService:

    def __init__(self, mainService, logger):
        pass
        self.logger = logger
        self.app = None
        self.aboutUI = None
        self.settingUI = None
        
        self.mainService = mainService

    
    def start(self):
        # TODO notification anpassen (kein ToolTip)
        self.logger.info('SysTrayService =  Systray: Start')
        menu_options = (("Status", None, self.status),("Restart", None, self.restart),("About", None, self.about),)
        self.systray = SysTrayIcon(CHECK_ICO, STATUS_OK, menu_options,  on_quit=self.on_quit_callback)
        self.systray.start()
        self.logger.info('SysTrayService =  Systray: OK ')

        
    def about(self, systray):
        ConfReader('assets/GITPuRe_ini.ini')
        version = ConfReader.get('MetaInformations', 'Version') 
        self.iniAboutUI()
        aboutText = '<html><head/><body><p>Utility to get a notification to commit and/or push the repository</p><p><br/>Developed by Christian Beigelbeck \
        </p><p>\
        Licensed under the <a href="https://www.gnu.org/licenses/gpl-3.0-standalone.html"><span style=" text-decoration:\
         underline; color:#2980b9;">GPL v3 license</span></a></p><p>Project home: \
         <a href="https://github.com/B31G3L/VCSReminder/"><span style=" text-decoration:\
         underline; color:#2980b9;">https://github.com/B31G3L/VCSReminder/</a></p> \
         Application version: ' + str(version) + '</body></html> '
        
        QtWidgets.QMessageBox.about(self.aboutUI, 'About', aboutText)

    def on_quit_callback(self, systray):
        self.logger.debug('Run: on_quit_callback')
        self.mainService.stop()

    def updateSystrayInfo(self, ico, status):
        self.systray.update(ico, status)

    def restart(self, systray):
        self.logger.debug('Run: restart')
        self.mainService.restart()
    

    def openSettings(self, systray):
        pass
        self.logger.debug('Run: openSettings')
        self.iniSettingUI()
        self.logger.debug('exec settingUI')
        self.settingUI.exec()
        self.app.exec_()

      
        
    def iniAboutUI(self):
        
            if self.app == None:
                self.logger.debug('INI Application')
                self.app = QtWidgets.QApplication(sys.argv)
                self.logger.debug('set Style')
                self.app.setStyle("Fusion")
                self.logger.debug('set Palette')
                self.app.setPalette(setPalette())
            if self.aboutUI == None:
                self.aboutUI = AboutUIService(self.logger)
    
        
    def status(self):
        
           pass
    
    

    