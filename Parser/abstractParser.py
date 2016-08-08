from pyquery import PyQuery as pq

class Parser:
    def __init__(self, ul):
        self.__fingerprint = {}
        self._binding = {}

    def __split(self, element):
        return pq(element).html().split('=',1)

    def _bind(self, key, value):
        for bind in self._binding[key]:
            if not hasattr(self.__fingerprint, bind):
                self.__fingerprint[bind] = value
            elif self.__fingerprint[bind] == "":
                self.__fingerprint[bind] = value
            elif bind == key:
                self.__fingerprint[bind] = value

    def _parse(self, ul):
        for li in ul:
            try:
                d = self.__split(li)
                self._bind(d[0], d[1])
            except Exception:
                pass

    def getResult(self):
        return self.__fingerprint