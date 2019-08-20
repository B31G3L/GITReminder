from git import Repo
from git import InvalidGitRepositoryError
from git import NoSuchPathError

CHECK_ICO = 'assets/img/bell_check.ico'
ERROR_ICO = 'assets/img/bell_x.ico'
CHANGE_ICO = 'assets/img/bell_clock.ico'
class GitService:


    def __init__(self, notificationService):
        self.notificationService = notificationService

    def isListGitRepos(self, gitRepos):
        for  repo in gitRepos:
            self.isGitRepo(repo)


    def isGitRepo(self, profile):
        try:
            path = profile.projectPath
            repo = Repo(path)
            if not repo.bare:
                return True
            else:
                self.notificationService.showToastNotification("GitReminder",'Could not load repository \nPfad: '+  path, ERROR_ICO)
                return False
        except InvalidGitRepositoryError:
            self.notificationService.showToastNotification("GitReminder",'{} is not a Git Repo \nPfad: {}'.format(profile.name, path), ERROR_ICO)
            return False

        except NoSuchPathError:
            self.notificationService.showToastNotification("GitReminder",'{} not found \nPfad: {}'.format(profile.name, path), ERROR_ICO)
            return False

    def isRepoDirty(self, profile):
        repo = Repo(profile.projectPath)
        if repo.is_dirty():
            self.notificationService.showToastNotification('Please Commit and Push', 'Project {} has been changed'.format(profile.name), CHANGE_ICO)
            return True
        else:
            return False
    