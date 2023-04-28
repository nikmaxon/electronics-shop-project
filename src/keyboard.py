from src.item import Item


class MixinLog:
    ENG = "EN"

    def __init__(self):
        self.__language = "EN"

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        elif self.__language == "RU":
            self.__language = "EN"
        return self

    @property
    def language(self):
        return self.__language


class KeyBoard(Item, MixinLog):
    pass
