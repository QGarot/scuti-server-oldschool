from typing import Self

from database.dao.furniture_dao import FurnitureDao
from database.database import Database
from game.furnitures.furniture import Furniture
from game.manager.manager import Manager


class FurnitureManager(Manager):
    def __init__(self):
        self.furnitures = []
        self.furnitures_dao = None

    @classmethod
    def get_instance(cls) -> Self | None:
        if cls.instance is None:
            cls.instance = FurnitureManager()
            print("UserManager loaded!")
            return None
        else:
            return cls.instance

    def set_dao(self, db: Database) -> None:
        self.furnitures_dao = FurnitureDao(db)

    def get_dao(self) -> FurnitureDao:
        return self.furnitures_dao

    def load_furnitures(self) -> None:
        self.furnitures = self.get_dao().get_furnitures()

    def get_furnitures(self) -> list[Furniture]:
        return self.furnitures

    def get_furniture_by_id(self, furniture_id: int) -> Furniture | None:
        for furniture in self.get_furnitures():
            if furniture.get_id() == furniture_id:
                return furniture
        return None
