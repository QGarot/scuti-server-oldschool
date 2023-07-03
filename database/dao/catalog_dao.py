from database.database import Database
from game.catalog.catalog_page import CatalogPage


class CatalogDao:
    def __init__(self, db: Database):
        self.db = db

    def get_catalog_pages(self) -> list[CatalogPage]:
        req = self.db.get("SELECT * FROM catalog_pages ORDER BY order_num")
        res = []
        for catalog_page in req:
            id = catalog_page[0]
            parent_id = catalog_page[1]
            caption = catalog_page[2]
            icon_color = catalog_page[3]
            icon_image = catalog_page[4]
            visible = catalog_page[5]
            enabled = catalog_page[6]
            min_rank = catalog_page[7]
            club_only = catalog_page[8]
            order_num = catalog_page[9]
            page_layout = catalog_page[10]
            page_headline = catalog_page[11]
            page_teaser = catalog_page[12]
            page_special = catalog_page[13]
            page_text1 = catalog_page[14]
            page_text2 = catalog_page[15]
            page_text_details = catalog_page[16]
            page_text_teaser = catalog_page[17]
            vip_only = catalog_page[18]
            page_link_description = catalog_page[19]
            page_link_page_name = catalog_page[20]

            res.append(CatalogPage(id, parent_id, caption, visible, enabled, min_rank, club_only, icon_color,
                                   icon_image, page_layout, page_headline, page_teaser, page_special, page_text1,
                                   page_text2, page_text_details, page_text_teaser, page_link_description,
                                   page_link_page_name))
        return res




