import datetime
x = datetime.datetime.now()
Date = x.strftime("%Y-%m-%d")

class Document:
    def __init__(self, authorlist=[], date=Date):
        self.__authors = authorlist
        self.__date = Date

    def getAuthors(self):
        return self.__authors

    def addAuthor(self, authName):
        self.__authors.append(authName)

    def getDate(self):
        return self.__date


class Book (Document):
    def __init(self, title):
        self.__title = title

    def getTitle(self):
        return self.__title

class Email (Document):
    def __init__(self, subj, to = []):
        self.__subj = subj
        self.__to = to

    def getSubject(self):
        return self.__subj

    def getTo(self):
        return self.__to





