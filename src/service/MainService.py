import sys
import os
import webbrowser
import time

from threading import Thread

from src.service.ConfigService import ConfigService
from src.service.StringService import StringService
from infi.systray import SysTrayIcon

APP_NAME = 'GitReminder'



STATUS_OK = 'Git-Reminder Status: ok'
STATUS_NOT_RUNNING = 'Git-Reminder Status: not running'
STATUS_RUNNING = 'Git-Reminder Status: running'
STATUS_CHANGE = 'Git-Reminder Status: Commit/Push erforderlich'
STATUS_ERROR = 'Git-Reminder Status: {} Repos fehlerhaft'

class MainService:

    
    def __init__(self, notificationService, gitService):
        self.CHECK_ICO = StringService.getIcons('success')
        self.ERROR_ICO = StringService.getIcons('error')
        self.CHANGE_ICO = StringService.getIcons('warning')

        self.notificationService = notificationService
        self.gitService = gitService
        self.isGitReminderStarted = False
        self.threads = [] 

        self.countStatusDirty = 0
        self.countStatusError = 0
        self.countStatusOk = 0

        

    
    def startSystray(self):
        a = StringService.getIcons('success')
        
        try:
            menu_options = (
                            (APP_NAME, self.CHECK_ICO, (
                                ('Start', None, self.startGitReminderFromSystray),
                                ('Stop', None, self.stopGitReminderFromSystray),
                                ('Restart', None,  self.restartGitReminderFromSystray),
                            )),
                            ("Status", None, self.status),
                            ("About", None, self.about),          
                            )
            self.systray = SysTrayIcon( self.CHECK_ICO, STATUS_OK, menu_options,  on_quit=self.on_quit_callback)
            self.systray.start()
        except:
            self.notificationService.showToastNotification(APP_NAME, "Start: FAILED", self.ERROR_ICO)
            sys.exit()
    
    def startGitReminderFromSystray(self, systray):
        self.startGitReminder()

    def startGitReminder(self):
        if self.isGitReminderStarted:
            self.notificationService.showToastNotification(APP_NAME, "is already started", self.CHECK_ICO)
        else:
            configService = ConfigService(self.notificationService)
            self.noGitRepos = False
            self.dirtyGitRepos = False

            self.countStatusDirty = 0
            self.countStatusError = 0
            self.countStatusOk = 0

            for repo in configService.readConf():
                if self.gitService.isGitRepo(repo):
                    if self.gitService.isRepoDirty(repo):
                       self.countStatusDirty += 1
                       self.updateSystrayInfo()
                       self.startThreadwithRepo(repo)
                    else:
                        self.countStatusOk += 1
                        self.startThreadwithRepo(repo)
                        self.updateSystrayInfo()
                else:
                    self.countStatusError += 1
                    self.updateSystrayInfo()

            self.notificationService.showToastNotification(APP_NAME, "is started", self.CHECK_ICO)

            self.isGitReminderStarted = True

            
            
    def startThreadwithRepo(self, repo):
        thread = Thread(target=self.profileThreads, args=(repo,))
        self.threads += [thread]
        thread.start()

    def profileThreads(self, repo):
        mins = int(repo.sleeptime) * 60
        currentTime = 0
        while self.isGitReminderStarted:
            if currentTime == mins:
                nowTime = datetime.now()
                targetTime = datetime(nowTime.year, nowTime.month, nowTime.day, int(profile.reminderTimeHour), int(profile.reminderTimeMin))
                if targetTime < nowTime:
                    self.startCheckProfile(profile)
                currentTime = 0

            time.sleep(1)
            currentTime += 1
        
    
    def stopGitReminderFromSystray(self, systray):
        self.stopGitReminder()

    def stopGitReminder(self):
        if not self.isGitReminderStarted:
            self.notificationService.showToastNotification(APP_NAME, "is already stopped", self.CHECK_ICO)
        else:
            self.isGitReminderStarted = False
            for x in  self.threads: 
                x.join()
            self.threads = []
            self.notificationService.showToastNotification(APP_NAME, "is stopped", self.CHECK_ICO)
            self.systrayUpdate(CHECK_ICO, STATUS_NOT_RUNNING)
    
    def restartGitReminder(self):
        self.stopGitReminder()
        self.startGitReminder()
    
    def restartGitReminderFromSystray(self, systray):
        self.restartGitReminder()
        
    def status(self, systray):
        if self.isGitReminderStarted:
            self.notificationService.showToastNotification(APP_NAME, "is started", self.CHECK_ICO)
        else:
            self.notificationService.showToastNotification(APP_NAME, "is stopped", self.CHECK_ICO)
      

    def updateSystrayInfo(self):
        if self.countStatusError > 0:
            self.systrayUpdate(self.ERROR_ICO, StringService.getMessages('systray_status_error').format(self.countStatusError))
        elif self.countStatusDirty > 0:
            self.systrayUpdate(self.CHANGE_ICO, StringService.getMessages('systray_status_dirty').format(self.countStatusDirty))
        else:
            self.systrayUpdate(self.CHECK_ICO, StringService.getMessages('systray_status_ok').format(self.countStatusOk))

    def systrayUpdate(self, ico, status):
        self.systray._create_window
        self.systray.update(ico, status)

    def about(self, systray):
        webbrowser.open(StringService.getMetaInfos('about'))
 
    def on_quit_callback(self, systray):
        pass
    
    
       
    
    

    