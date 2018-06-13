from os import listdir
from os.path import isfile, isdir, join

class FSBrowser:

    homePath = ""
    path = "/"

    def __init__(self, path):
        self.homePath = path

    def setPath(self, path):
        self.path = path

    def getPath(self):
        return self.path

    def getFullPath(self):
        return self.homePath+"/"+self.path

    def getParent(self):
        if self.path != "":
            n = self.path.rfind("/")
            if n<1:
                return "/"
            else:
                return self.path[:n]
    
    def getFiles(self):
        fullPath = self.homePath+"/"+self.path
        files = [f for f in listdir(fullPath) if isfile(join(fullPath, f))]
        return sorted(files)
    
    def getDirectories(self):
        fullPath = self.homePath+"/"+self.path
        files = [f for f in listdir(fullPath) if isdir(join(fullPath, f))]
        return sorted(files)
