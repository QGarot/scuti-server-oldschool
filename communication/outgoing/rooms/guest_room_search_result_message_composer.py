from communication.outgoing.message_composer import MessageComposer
from game.rooms.room_manager import RoomManager
from network.messages.server_message import ServerMessage
import communication.outgoing.header


class GuestRoomSearchResultMessageComposer(MessageComposer):
    def __init__(self, username: str):
        self.response = ServerMessage(communication.outgoing.header.GuestRoomSearchResultMessageComposer)
        self.rooms = RoomManager().get_instance().get_rooms_by_owner_username(username)

    def compose(self):
        n = len(self.rooms)
        self.response.append_int32(1)
        self.response.append_string_with_break("")
        self.response.append_int32(n)

        for room in self.rooms:
            self.response.append_int32(room.get_room_data().get_id())
            self.response.append_boolean(True)  # Event?
            self.response.append_string_with_break(room.get_room_data().get_caption())  # Room name
            self.response.append_string_with_break(room.get_room_data().get_owner_name())  # Owner name
            self.response.append_int32(room.get_room_data().get_state())  # Access: open (0), locked (1), password (2)
            self.response.append_int32(49)  # Number of people in the room
            self.response.append_int32(50)  # Capacity
            self.response.append_string_with_break(room.get_room_data().get_description()) # Description
            self.response.append_int32(0)  # idk
            self.response.append_boolean(True)  # Is trading allowed ?
            self.response.append_int32(room.get_room_data().get_score())  # Rating
            self.response.append_int32(room.get_room_data().get_category())  # Category
            self.response.append_string_with_break("07/02/23")  # Started at (date)

            # Tags
            self.response.append_int32(2)  # Number of tags
            self.response.append_string_with_break("tag1")
            self.response.append_string_with_break("tag2")

            # Thumbnail
            self.response.append_int32(room.get_room_data().get_icon_background())  # background image icon
            self.response.append_int32(room.get_room_data().get_icon_foreground())  # foreground image icon
            self.response.append_int32(1)  # item count
            self.response.append_int32(1)  # item position
            self.response.append_int32(3)  # item img id

            self.response.append_boolean(True)  # allow pets
            self.response.append_boolean(False)  # display room entry ad

    def get_response(self):
        return self.response
