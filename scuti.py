from database.database import Database
from game.catalog.catalog_manager import CatalogManager
from game.furnitures.furniture_manager import FurnitureManager
from game.navigator.navigator_manager import NavigatorManager
from game.rooms.models.room_model_manager import RoomModelManager
from game.rooms.room_manager import RoomManager
from game.users.user_manager import UserManager
from network.server import Server


class Scuti:
    def __init__(self):
        self.db = None
        self.server = None

    def run(self):
        self.connect_database("localhost", "root", "", "scuti")
        self.set_managers()
        self.load_managers()
        self.run_server("127.0.0.1", 35000)

    def connect_database(self, host: str, user: str, password: str, name: str) -> None:
        try:
            self.db = Database("localhost", "root", "", "scuti")
        except Exception as error:
            print(error)
            print(error.args)

    def set_managers(self) -> None:
        """
        Initialize managers and set their DAO
        :return:
        """
        # Users
        UserManager.get_instance()
        UserManager.get_instance().set_dao(self.db)

        # Rooms
        RoomModelManager.get_instance()
        RoomModelManager.get_instance().set_dao(self.db)
        RoomManager.get_instance()
        RoomManager.get_instance().set_dao(self.db)

        # Navigator
        NavigatorManager.get_instance()
        NavigatorManager.get_instance().set_dao(self.db)

        # Catalog
        CatalogManager.get_instance()
        CatalogManager.get_instance().set_dao(self.db)

        # Items
        FurnitureManager.get_instance()
        FurnitureManager.get_instance().set_dao(self.db)

    def load_managers(self):
        # Rooms
        RoomModelManager.get_instance().load_models()
        RoomManager.get_instance().load_rooms()

        # Navigator
        # NavigatorManager.get_instance().load_public_rooms()

        # Catalog
        CatalogManager.get_instance().load_pages()
        CatalogManager.get_instance().load_catalog_items()

        # Items
        FurnitureManager.get_instance().load_furnitures()

    def run_server(self, ip: str, port: int):
        self.server = Server(ip, port)
        print(">> Server on!")
        print("-----------------------------------")
