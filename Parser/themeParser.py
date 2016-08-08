from Parser.abstractParser import Parser

class ThemeParser(Parser):
    def __init__(self, ul):
        super().__init__(ul)
        self._binding = {"id":["time", "timers", "duration"], "duration":["duration"]}
        self._parse(ul)