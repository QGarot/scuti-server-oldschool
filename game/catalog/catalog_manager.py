from typing import Self

from database.dao.catalog_dao import CatalogDao
from database.database import Database
from game.catalog.catalog_page import CatalogPage


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

    def get_catalog_pages(self) -> list[CatalogPage]:
        """
        Get pages loaded
        :return:
        """
        return self.catalog_pages_list

    def load_pages(self) -> None:
        """
        Load all catalog pages registered in the database
        :return:
        """
        self.catalog_pages_list = self.get_dao().get_catalog_pages()

    def get_catalog_page_by_id(self, page_id: int) -> CatalogPage | None:
        """

        :param page_id:
        :return:
        """
        for catalog_page in self.get_catalog_pages():
            if catalog_page.get_id() == page_id:
                return catalog_page
        return None
        