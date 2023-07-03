from typing import Self

from database.dao.room_model_dao import RoomModelDao
from database.database import Database
from game.rooms.models.room_model import RoomModel


class RoomModelManager:
    instance = None

    def __init__(self):
        self.models = []
        self.room_model_dao = None

    @classmethod
    def get_instance(cls) -> Self | None:
        if cls.instance is None:
            cls.instance = RoomModelManager()
            print("RoomModelManager loaded!")
            return None
        else:
            return cls.instance

    def set_dao(self, db: Database):
        """
        Set DAO instance(s)
        :param db:
        :return:
        """
        self.room_model_dao = RoomModelDao(db)

    def get_room_model_dao(self) -> RoomModelDao:
        """
        :return: room model dao
        """
        return self.room_model_dao

    def get_models(self) -> list[RoomModel]:
        """
        :return: Get all room models loaded
        """
        return self.models

    def add_model(self, model: RoomModel) -> None:
        """
        Add a specific room model to the list of room models
        :param model:
        :return:
        """
        self.models.append(model)

    def load_models(self) -> None:
        """
        Load all room models registered in the database
        :return:
        """
        self.models = self.get_room_model_dao().get_models()

    def get_model_by_name(self, name: str) -> RoomModel | None:
        """
        :param name:
        :return: get a model with its name
        """
        for model in self.get_models():
            if model.name == name:
                return model
        return None
