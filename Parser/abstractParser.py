from pyquery import PyQuery as pq
import re

class Parser:
    def __init__(self, ul):
        self.__fingerprint = {}
        self._binding = {}

    def __split(self, element):
        return pq(element).html().split('=',1)

    def _bind(self, key, value):
        self.__push(key, key, value)
        try:
            for bind in self._binding[key]:
                self.__push(key, bind, value)
        except:
            pass

    def __push(self, key, bind, value):
        p = '(.*)[0-9]+'
        c = re.compile(p)
        s = re.search(p, key)
        #remove bind number
        bs = re.search(p, bind)
        if bs is not None:
            bind = bs.group(1)
        #test input
        inputString = bool(not c.match(key))
        #test output
        if s == None:
            outputString = True
        else:
            outputString = not (bind == s.group(1))
        #conditions
        if inputString:
            if not bind in self.__fingerprint:
                self.__fingerprint[bind] = value
            elif self.__fingerprint[bind] == "":
                self.__fingerprint[bind] = value
            elif bind == key:
                self.__fingerprint[bind] = value
            else:
                pass
        else:
            if outputString:
                if not bind in self.__fingerprint:
                    self.__fingerprint[bind] = value
                elif self.__fingerprint[bind] == "":
                    self.__fingerprint[bind] = value
                else:
                    self.__fingerprint[bind] += ", " + value
            else:
                if not bind in self.__fingerprint:
                    self.__fingerprint[bind] = [value]
                else:
                    self.__fingerprint[bind].append(value)

    def _parse(self, ul):
        for li in ul:
            try:
                d = self.__split(li)
                self._bind(d[0], d[1])
            except Exception:
                pass

    def getResult(self):
        return self.__fingerprint