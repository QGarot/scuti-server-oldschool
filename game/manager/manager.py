from abc import abstractmethod, ABC

from database.database import Database


class Manager(ABC):
    instance = None

    @classmethod
    @abstractmethod
    def get_instance(cls):
        pass

    @abstractmethod
    def set_dao(self, db: Database):
        pass

    @abstractmethod
    def get_dao(self):
        pass
