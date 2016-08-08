from Parser.abstractParser import Parser

class SessionParser(Parser):
    def __init__(self, ul):
        super().__init__(ul)
        self._fingerprint = {"tags":""}
        self._binding = {"facilitator1":["facilitators"], "facilitator2":["facilitators"], "facilitator3":["facilitators"], "facilitator4":["facilitators"], "facilitator5":["facilitators"], "facilitator6":["facilitators"], "facilitator7":["facilitators"], "facilitator8":["facilitators"], "facilitator9":["facilitators"], "tag1":["tags"], "tag2":["tags"], "tag3":["tags"], "tag4":["tags"], "tag5":["tags"], "tag6":["tags"], "tag7":["tags"], "tag8":["tags"], "tag9":["tags"], "tag10":["tags"], "tag11":["tags"], "tag12":["tags"], "tag13":["tags"], "tag14":["tags"], "tag15":["tags"]}
        self._parse(ul)

