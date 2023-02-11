from communication.outgoing.message_composer import MessageComposer
from network.messages.server_message import ServerMessage


class ClientPrivateRoomMessageComposer(MessageComposer):
    def __init__(self, room_id):
        self.response = ServerMessage(166)
        self.room_id = room_id

    def get_response(self) -> ServerMessage:
        return self.response

    def compose(self):
        self.response.append_string_with_break("/client/private/" + str(self.room_id) + "/Id")
