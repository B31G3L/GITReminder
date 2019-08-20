from threading import Thread
from src.service.NotificationService import NotificationService
from src.service.MainService import MainService
from src.service.GitService import GitService

if __name__ == "__main__":

    notificationService = NotificationService()
    gitService = GitService(notificationService)


    # 1 Start Systray
    mainService = MainService(notificationService, gitService)
    isStarted = mainService.startSystray()

    # 2 Start GitReminder
    mainService.startGitReminder()
       
    




