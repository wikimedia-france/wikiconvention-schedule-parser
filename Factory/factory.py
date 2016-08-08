class Factory:
    def __init__(self):
        self.__session_json = {"sessions":[],"timeblocks":[]}
        self.__tags_json = []
        self.__themes_json = []

    def addSession(self, session):
        self.__session_json["sessions"].append(session)

    def addTimeblock(self, timeblock):
        self.__session_json["timeblocks"].append(timeblock)

    def addTag(self, tag):
        self.__tags_json.append(tag)

    def addTheme(self, theme):
        self.__themes_json.append(theme)

    def getSessionJson(self):
        return self.__session_json

    def getTagsJson(self):
        return self.__tags_json

    def getThemeJson(self):
        return self.__themes_json