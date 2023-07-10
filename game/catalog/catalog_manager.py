from typing import Self

from database.dao.catalog_dao import CatalogDao
from database.database import Database
from game.catalog.catalog_item import CatalogItem
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

    def load_catalog_items(self) -> None:
        """
        Load all catalog items registered in the database
        :return:
        """
        self.catalog_items_list = self.get_dao().get_catalog_items()

    def get_catalog_page_by_id(self, page_id: int) -> CatalogPage | None:
        """

        :param page_id:
        :return:
        """
        for catalog_page in self.get_catalog_pages():
            if catalog_page.get_id() == page_id:
                return catalog_page
        return None

    def get_catalog_items(self) -> list[CatalogItem]:
        return self.catalog_items_list

    def get_items_of_page(self, page_id: int) -> list[CatalogItem]:
        res = []
        for catalog_item in self.get_catalog_items():
            if catalog_item.get_page_id() == page_id:
                res.append(catalog_item)
        return res

    def get_catalog_item_by_id(self, catalog_item_id: int) -> CatalogItem | None:
        for catalog_item in self.get_catalog_items():
            if catalog_item.get_id() == catalog_item_id:
                return catalog_item
        return None
