from Parser.abstractParser import Parser


class SessionParser(Parser):
    def __init__(self, ul):
        super().__init__(ul)
        self._fingerprint = {"id":"","facilitator_array":[],"facilitators":"","tags":"","description":""}
        self._binding = {"id": [{"bind": "id", "type": "string", "primary": True}],
                         "title": [{"bind": "title", "type": "string", "primary": True}],
                         "timeblock": [{"bind": "timeblock", "type": "string", "primary": True}],
                         "start": [{"bind": "start", "type": "string", "primary": True}],
                         "duration": [{"bind": "duration", "type": "string", "primary": True}],
                         "description": [{"bind": "description", "type": "string", "primary": True}],
                         "facilitators": [{"bind": "facilitators", "type": "arraystring", "primary": True}],
                         "facilitator": [{"bind": "facilitator_array", "type": "array", "primary": True},
                                         {"bind": "facilitators", "type": "arraystring", "primary": False}],
                         "link": [{"bind": "link", "type": "url", "primary": True}],
                         "location": [{"bind": "location", "type": "string", "primary": True}],
                         "theme": [{"bind": "category", "type": "string", "primary": True}],
                         "tags": [{"bind": "tags", "type": "arraystring", "primary": True}],
                         "tag": [{"bind": "tagArray", "type": "array", "primary": True},
                                  {"bind": "tags", "type": "arraystring", "primary": False}],
                         "next_session_id": [{"bind": "nextSessionID", "type": "string", "primary": True}],
                         "next_session_title": [{"bind": "nextSessionTitle", "type": "string", "primary": True}]}
        self._parse(ul)
