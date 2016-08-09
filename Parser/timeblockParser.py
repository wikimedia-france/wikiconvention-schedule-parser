from Parser.abstractParser import Parser


class TimeblockParser(Parser):
    def __init__(self, ul):
        super().__init__(ul)
        self._fingerprint = {"key":""}
        self._binding = {"key": [{"bind": "key", "type": "string", "primary": True}],
                         "order": [{"bind": "order", "type": "string", "primary": True}],
                         "timeblock_name": [{"bind": "timeblock name", "type": "string", "primary": True}],
                         "day": [{"bind": "day", "type": "string", "primary": True}],
                         "start_time": [{"bind": "start time", "type": "string", "primary": True}],
                         "reserved_for_everyone": [
                             {"bind": "reserved for everyone", "type": "string", "primary": True}]}
        self._parse(ul)
