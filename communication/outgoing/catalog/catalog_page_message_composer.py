from communication.outgoing.message_composer import MessageComposer
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
        if page_layout == "frontpage":
            self.response.append_string_with_break("frontpage3")  # layout
            self.response.append_int32(3)  # ? idk :c
            self.response.append_string_with_break(self.page.get_layout_headline())
            self.response.append_string_with_break(self.page.get_layout_teaser())
            self.response.append_string_with_break("")  # ?
            self.response.append_int32(11)  # ?
            self.response.append_string_with_break(self.page.get_text1())
            self.response.append_string_with_break(self.page.get_text_link_desc())
            self.response.append_string_with_break(self.page.get_text2())
            self.response.append_string_with_break(self.page.get_text_details())
            self.response.append_string_with_break(self.page.get_text_link_page())
            self.response.append_string_with_break("Code crédits/pixels/coquillages")
            self.response.append_string_with_break("")
            self.response.append_string_with_break("Lire plus >> ")
            self.response.append_string_with_break("")  # magic.credits
        elif page_layout == "club_buy":
            self.response.append_string_with_break("club_buy")  # layout
            self.response.append_int32(1)
            self.response.append_string_with_break("habboclub_2")
            self.response.append_int32(1)
