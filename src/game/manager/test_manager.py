from src.database.database import Database
from src.game.manager.manager import Manager


class TestManager(Manager):
    def get_dao(self):
        pass

    def set_dao(self, db: Database):
        pass

    @classmethod
    def get_instance(cls):
        cls.instance = 2


TestManager.get_instance()
test_manager = TestManager()
print(test_manager.instance)
