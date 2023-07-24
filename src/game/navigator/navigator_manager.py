from typing import Self

from src.database.dao.navigator_dao import NavigatorDao
from src.database.database import Database
from src.game.manager.manager import Manager
from src.game.navigator.public_room import PublicRoom


class NavigatorManager(Manager):
    def __init__(self):
        self.public_rooms = []
        self.navigator_dao = None

    @classmethod
    def get_instance(cls) -> Self | None:
        if cls.instance is None:
            cls.instance = NavigatorManager()
            print("NavigatorManager loaded!")
            return None
        else:
            return cls.instance

    def set_dao(self, db: Database) -> None:
        self.navigator_dao = NavigatorDao(db)

    def get_dao(self) -> NavigatorDao:
        return self.navigator_dao

    def load_public_rooms(self) -> None:
        """
        Load all public rooms saved in database
        :return:
        """
        self.public_rooms = self.get_dao().get_public_rooms()

    def get_public_rooms(self) -> list[PublicRoom]:
        """
        Return the set of public rooms
        :return:
        """
        return self.public_rooms

