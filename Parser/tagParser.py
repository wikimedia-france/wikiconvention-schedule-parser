from Parser.abstractParser import Parser

class TagParser(Parser):
    def __init__(self, ul):
        super().__init__(ul)
        self._binding = {}
        self._parse(ul)