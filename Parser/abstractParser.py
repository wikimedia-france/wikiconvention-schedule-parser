from pyquery import PyQuery as pq
import re

class Parser:
    urlPrefix = "https://meta.wikimedia.org"

    def __init__(self, ul):
        self._fingerprint = {}
        self._binding = {}

    def __split(self, element):
        return pq(element).html().split('=',1)

    def _bind(self, t, elem):
        key, value = t
        #pull off finals digit
        ks = re.search('(.*)[0-9]+', t[0])
        if ks is not None:
            key = ks.group(1)
        #browse binding
        if key in self._binding:
            for link in self._binding[key]:
                self.__push(link, elem, value)

    def __push(self, link, elem, value):
        value = value.replace("href=\"/wiki/","href=\"" + Parser.urlPrefix + "/wiki/")
        bind, type, primary = link['bind'], link['type'], link['primary']
        if type == "string":
            try:
                if not primary and self._fingerprint[bind] != "":
                    return
            except:
                pass
            self._fingerprint[bind] = value
        elif type == "url":
            value = pq(elem)("a")[0].attrib['href'] if pq(elem)("a").length else value
            if re.compile('^\/wiki\/').match(value):
                value = Parser.urlPrefix + value
            try:
                if not primary and self._fingerprint[bind] != "":
                    return
            except:
                pass
            self._fingerprint[bind] = value
        elif type == "array":
            if not bind in self._fingerprint:
                self._fingerprint[bind] = []
            self._fingerprint[bind].append(value)
        elif type == "arraystring":
            if not bind in self._fingerprint:
                self._fingerprint[bind] = value
            elif self._fingerprint[bind] == "":
                self._fingerprint[bind] = value
            else:
                self._fingerprint[bind] += ", " + value

    def _parse(self, ul):
        for li in ul:
            try:
                d = self.__split(li)
                self._bind(tuple(d), li)
            except Exception:
                pass

    def getResult(self):
        return self._fingerprint