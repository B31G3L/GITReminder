from win10toast import ToastNotifier
import time

class NotificationService:

    def __init__(self):
        pass


    def showToastNotification(self, mainText, subText, iconPath):
        toaster = ToastNotifier()
        toaster.show_toast(mainText, subText,
                        icon_path=iconPath,
                        duration=5,
                        threaded=True)
                        
        # Wait for threaded notification to finish
        while toaster.notification_active(): time.sleep(0.3)