from Parser.abstractParser import Parser

class SessionParser(Parser):
    def __init__(self, ul):
        super().__init__(ul)
        self._binding = {"id":["time", "timers", "duration"], "duration":["duration"]}
        self._parse(ul)