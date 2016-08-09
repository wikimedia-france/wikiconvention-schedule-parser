from Parser.abstractParser import Parser


class ThemeParser(Parser):
    def __init__(self, ul):
        super().__init__(ul)
        self._fingerprint = {"name":"","description":[]}
        self._binding = {"name": [{"bind": "name", "type": "string", "primary": True}],
                         "description": [{"bind": "description", "type": "array", "primary": True}],
                         "icon_src": [{"bind": "iconSrc", "type": "url", "primary": True}]}
        self._parse(ul)
