import json

class Factory:
    def __init__(self):
        self.__session_json = {"sessions":[],"timeblocks":[]}
        self.__tags_json = []
        self.__themes_json = []

    def linkSessionToDay(self):
        for i, v in enumerate(self.__session_json["sessions"]):
            for tb in self.__session_json["timeblocks"]:
                if v["timeblock"] == tb["key"]:
                    self.__session_json["sessions"][i]["day"] = tb["day"]

    def addSession(self, session):
        self.__session_json["sessions"].append(session)

    def addTimeblock(self, timeblock):
        self.__session_json["timeblocks"].append(timeblock)

    def addTag(self, tag):
        self.__tags_json.append(tag)

    def addTheme(self, theme):
        self.__themes_json.append(theme)

    def getSessionsJson(self):
        return json.dumps(self.__session_json, sort_keys=True)

    def getTagsJson(self):
        return json.dumps(self.__tags_json, sort_keys=True)

    def getThemesJson(self):
        return json.dumps(self.__themes_json, sort_keys=True)