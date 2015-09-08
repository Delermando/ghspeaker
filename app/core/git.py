
class Git(object):

    def __init__(self, Github):
        self.Github = Github

    def getGithubUser(self, userName, password):
        github = self.Github(userName, password)
        return github.get_user()    

    def getRepository(self, user, repositoryName):
        return user.get_repo( repositoryName )

    def getDirContentFromRepository(self,repository, dirName):
        return repository.get_dir_contents( dirName )