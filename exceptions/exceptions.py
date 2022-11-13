class PicturiExceptions(Exception):
    pass

class RepositoryExceptions(PicturiExceptions):
    def __init__(self,msg):
        self.__error=msg

    def get_msg(self):
        return self.__error

    def __str__(self):
        return 'Repository Exception:'+str(self.get_msg())

class CorruptedFileException(RepositoryExceptions):
    def __init__(self):
        RepositoryExceptions.__init__(self,"Fisierul nu poate fi deschis")