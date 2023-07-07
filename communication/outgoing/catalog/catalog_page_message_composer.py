from communication.outgoing.message_composer import MessageComposer
from game.catalog.catalog_manager import CatalogManager
from game.catalog.catalog_page import CatalogPage
from network.messages.server_message import ServerMessage


class CatalogPageMessageComposer(MessageComposer):
    def __init__(self, page: CatalogPage):
        self.response = ServerMessage(127)
        self.page = page

    def get_response(self) -> ServerMessage:
        return self.response

    def compose(self) -> None:
        self.response.append_int32(self.page.get_id())
        page_layout = self.page.get_layout()
        match page_layout:
            case "frontpage":
                self.response.append_string_with_break("frontpage3")  # layout
                self.response.append_int32(3)
                self.response.append_string_with_break(self.page.get_layout_headline())
                self.response.append_string_with_break(self.page.get_layout_teaser())
                self.response.append_string_with_break("")  # ?
                self.response.append_int32(9)
                self.response.append_string_with_break(self.page.get_text1())
                self.response.append_string_with_break(self.page.get_text_link_desc())
                self.response.append_string_with_break(self.page.get_text2())
                self.response.append_string_with_break(self.page.get_text_details())
                self.response.append_string_with_break(self.page.get_text_link_page())
                self.response.append_string_with_break("Code crédits/pixels/coquillages")
                self.response.append_string_with_break("")
                self.response.append_string_with_break("Lire plus >> ")
                self.response.append_string_with_break("")  # magic.credits
            case "club_buy":
                self.response.append_string_with_break(page_layout)  # layout
                self.response.append_int32(1)
                self.response.append_string_with_break("habboclub_2")
                self.response.append_int32(1)
            case _:  # default case
                self.response.append_string_with_break(page_layout)
                self.response.append_int32(3)
                self.response.append_string_with_break(self.page.get_layout_headline())
                self.response.append_string_with_break(self.page.get_layout_teaser())
                self.response.append_string_with_break(self.page.get_layout_special())
                self.response.append_int32(3)
                self.response.append_string_with_break(self.page.get_text1())
                self.response.append_string_with_break(self.page.get_text_details())
                self.response.append_string_with_break(self.page.get_text_teaser())

        catalog_items = CatalogManager.get_instance().get_items_of_page(self.page.get_id())
        self.response.append_int32(len(catalog_items))
        for item in catalog_items:
            self.response.append_uint(item.get_id())
            self.response.append_string_with_break(item.get_name())
            self.response.append_int32(item.get_credits_cost())
            # TODO: edit SQL structure for activity point type!!
            self.response.append_int32(0)  # price in activity points
            self.response.append_int32(0)  # activity point type: 0 for pixels, 4 for shells
            self.response.append_int32(1)
            self.response.append_string_with_break(item.get_furni_type())
            self.response.append_int32(item.get_sprite_id())
            self.response.append_string_with_break("")  # Extra data
            self.response.append_int32(item.get_amount())
            self.response.append_int32(-1)
            self.response.append_int32(0)  # vip?
