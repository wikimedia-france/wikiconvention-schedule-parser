from pyquery import PyQuery as pq
import requests
from Factory.factory import *
from Parser.allParser import *

class ScheduleSync:
    def __init__(self, rq):
        self.__f = Factory()
        self.__uls = pq(rq.json()['parse']['text']['*'])

    def launchParsing(self):
        for ul in self.__uls(".session"):
            p = SessionParser(ul)
            self.__f.addSession(p.getResult())
        for ul in self.__uls(".timeblock"):
            p = TimeblockParser(ul)
            self.__f.addTimeblock(p.getResult())
        for ul in self.__uls(".tag"):
            p = TagParser(ul)
            self.__f.addTag(p.getResult())
        for ul in self.__uls(".theme"):
            p = ThemeParser(ul)
            self.__f.addTheme(p.getResult())
        self.__f.linkSessionToDay()
        return self

    def showFactory(self):
        print(self.__f.getSessionJson())
        print(self.__f.getTagsJson())
        print(self.__f.getThemeJson())
        return self

apiURL = "https://meta.wikimedia.org/w/api.php?action=parse&format=json&text=%7B%7BUser%3AJitrixis%2FWikiConvention%2FProgramme%7Cshow%3DSimple%7D%7D&prop=text"

ScheduleSync(requests.get(url=apiURL)).launchParsing().showFactory()