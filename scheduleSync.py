import os, sys
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
        if len(sys.argv) > 2:
            if sys.argv[2] == "sessions":
                print(self.__f.getSessionsJson())
            elif sys.argv[2] == "tags":
                print(self.__f.getTagsJson())
            elif sys.argv[2] == "themes":
                print(self.__f.getThemesJson())
        else:
            print(self.__f.getSessionsJson())
            print(self.__f.getTagsJson())
            print(self.__f.getThemesJson())
        return self

apiURL = sys.argv[1]
ScheduleSync(requests.get(url=apiURL)).launchParsing().showFactory()
