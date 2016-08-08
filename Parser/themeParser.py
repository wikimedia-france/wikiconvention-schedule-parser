from Parser.abstractParser import Parser

class ThemeParser(Parser):
    def __init__(self, ul):
        super().__init__(ul)
        self._binding = {}
        self._parse(ul)
