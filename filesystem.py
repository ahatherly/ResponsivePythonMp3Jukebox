from os import listdir
from os.path import isfile, isdir, join
from shutil import copyfile

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

    def getArtistAlbum(self):
        result = {}
        # Artist
        parent = self.getParent()
        if parent != "":
            n = parent.rfind("/")
            if n<1:
                result['artist']=''
            else:
                result['artist']=parent[n+1:]
        # Album
        if self.path != "":
            n = self.path.rfind("/")
            if n<1:
                result['album']=''
            else:
                result['album']=self.path[n+1:]
        return result

    def getFiles(self):
        fullPath = self.homePath+"/"+self.path
        fileList = listdir(fullPath)
        files = []
        for f in fileList:
            if isfile(join(fullPath, f)) and f.endswith(".mp3"):
                fileEntry = {}
                fileEntry['name'] = f
                files.append(fileEntry)
                # See if we have a track number in the name we can sort on
                parts = f.split(" ")
                if parts[0].isnumeric():
                    fileEntry['sortKey'] = (str(int(parts[0]))).zfill(3)
                else:
                    parts = f.split(".")
                    if parts[0].isnumeric():
                        fileEntry['sortKey'] = (str(int(parts[0]))).zfill(3)
                    else:
                        parts = f.split("-")
                        if parts[0].isnumeric():
                            fileEntry['sortKey'] = (str(int(parts[0]))).zfill(3)
                        else:
                            fileEntry['sortKey'] = f

        return sorted(files, key=lambda k: k['sortKey'])

    def findThumbnail(self, path):
        fullPath = self.homePath+"/"+self.path+"/"+path
        fileList = listdir(fullPath)
        for f in fileList:
            if isfile(join(fullPath, f)):
                if f.endswith(".jpg") or f.endswith(".JPG"):
                    return f
        return ""

    def getCurrentDirThumb(self):
        return self.findThumbnail("")
    
    def getDirectories(self):
        fullPath = self.homePath+"/"+self.path
        files = []
        #files = [f for f in listdir(fullPath) if isdir(join(fullPath, f))]
        fileList = listdir(fullPath)
        for f in fileList:
            if isdir(join(fullPath, f)):
                dirEntry = {}
                dirEntry['name'] = f
                dirEntry['thumb'] = self.findThumbnail(f)
                files.append(dirEntry)

        return sorted(files, key=lambda k: k['name'])

    def copyCover(self):
        fullPath = self.homePath+"/"+self.path
        print(fullPath+"/cover.jpg")
        copyfile("/tmp/cover.jpg", fullPath+"/cover.jpg")
