from typing import Self

from database.dao.catalog_dao import CatalogDao
from database.database import Database


class CatalogManager:
    instance = None

    def __init__(self):
        self.catalog_pages_list = []
        self.catalog_items_list = []
        self.catalog_dao = None

    @classmethod
    def get_instance(cls) -> Self | None:
        if cls.instance is None:
            cls.instance = CatalogManager()
            print("CatalogManager loaded!")
            return None
        else:
            return cls.instance

    def set_dao(self, db: Database):
        """
        Set DAO instance(s)
        :param db:
        :return:
        """
        self.catalog_dao = CatalogDao(db)

    def get_dao(self) -> CatalogDao:
        """
        Get DAO instance
        :return:
        """
        return self.catalog_dao

    def load_pages(self) -> None:
        """
        Load all catalog pages registered in the database
        :return:
        """
        self.catalog_pages_list = self.get_dao().get_catalog_pages()



