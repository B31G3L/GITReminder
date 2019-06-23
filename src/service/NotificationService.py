from win10toast import ToastNotifier

class NotificationService:

    def __init__(self, logger):
        pass
        self.logger = logger
        self.logger.debug('Run : ini')


    def showToastNotification(mainText, subText, iconPath):
        toaster = ToastNotifier()
        toaster.show_toast(mainText, subText,
                        icon_path=iconPath,
                        duration=5,
                        threaded=True)