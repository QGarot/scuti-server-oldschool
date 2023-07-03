from communication.outgoing.message_composer import MessageComposer
from game.catalog.catalog_manager import CatalogManager
from network.messages.server_message import ServerMessage


class CatalogIndexMessageComposer(MessageComposer):
    # TODO: display pages depending on the rank
    def __init__(self):
        self.response = ServerMessage(126)
        self.pages = CatalogManager.get_instance().get_catalog_pages()

    def get_response(self) -> ServerMessage:
        return self.response

    def compose(self) -> None:
        self.response.append_boolean(True)
        self.response.append_int32(0)
        self.response.append_int32(0)
        self.response.append_int32(-1)
        self.response.append_string_with_break("")
        self.response.append_int32(self.get_tree_size(1, -1))
        self.response.append_boolean(True)
        for page in self.pages:
            if page.get_parent_id() == -1:
                # "Serialize" page
                self.response.append_int32(page.get_icon_color())
                self.response.append_int32(page.get_icon_image())
                self.response.append_int32(page.get_id())
                self.response.append_string_with_break(page.get_caption())
                self.response.append_int32(self.get_tree_size(1, page.get_id()))
                self.response.append_boolean(True)  # Visible

                for p in self.pages:
                    if p.get_parent_id() == page.get_id():
                        # "Serialize" page
                        self.response.append_int32(p.get_icon_color())
                        self.response.append_int32(p.get_icon_image())
                        self.response.append_int32(p.get_id())
                        self.response.append_string_with_break(p.get_caption())
                        self.response.append_int32(self.get_tree_size(1, p.get_id()))
                        self.response.append_boolean(True)  # Visible

    def get_tree_size(self, rank: int, tree_id: int):
        num = 0
        for page in self.pages:
            if page.get_parent_id() == tree_id:
                num = num + 1
        return num
