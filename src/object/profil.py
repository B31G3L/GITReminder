
class Profil:

    def __init__(self, name):
        self.name = name
    
    def __init__(self, name, reminderTimeHour, reminderTimeMin, projectPath, sleeptime):
         self.name = name
         self.reminderTimeHour = reminderTimeHour
         self.reminderTimeMin = reminderTimeMin
         self.projectPath = projectPath
         self.sleeptime = sleeptime

    def setReminderTimeHour(self, reminderTimeHour):
        self.reminderTimeHour = reminderTimeHour

    def setReminderTimeMin(self, reminderTimeMin):
        self.reminderTimeMin = reminderTimeMin

    def setProjectPath(self, projectPath):
        self.projectPath = projectPath

    def setSleeptime(self, sleeptime):
        self.sleeptime = sleeptime