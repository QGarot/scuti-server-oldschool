from communication.outgoing.message_composer import MessageComposer
from network.messages.server_message import ServerMessage


class GuestRoomSearchResultMessageComposer(MessageComposer):
    def __init__(self):
        self.response = ServerMessage(451)

    def compose(self):
        self.response.append_int32(1)
        self.response.append_string_with_break("")
        self.response.append_int32(1)

        for i in range(1):
            self.response.append_int32(3)
            self.response.append_boolean(True)  # Event?
            self.response.append_string_with_break("jeu du celib " + str(i))  # Room name
            self.response.append_string_with_break("Tig3r")  # Owner name
            self.response.append_int32(0)  # Access: open (0), locked (1), password (2)
            self.response.append_int32(49)  # Number of people in the room
            self.response.append_int32(50)  # Capacity
            self.response.append_string_with_break("Scutiz room :p") # Description
            self.response.append_int32(0)  # idk
            self.response.append_boolean(True)  # Is trading allowed ?
            self.response.append_int32(2)  # Rating
            self.response.append_int32(2)  # Category
            self.response.append_string_with_break("07/02/23")  # Started at (date)

            # Tags
            self.response.append_int32(2)  # Number of tags
            self.response.append_string_with_break("tag1")
            self.response.append_string_with_break("tag2")

            # Thumbnail
            self.response.append_int32(13)  # background image icon
            self.response.append_int32(3)  # foreground image icon
            self.response.append_int32(1)  # item count
            self.response.append_int32(1)  # item position
            self.response.append_int32(3)  # item img id

            self.response.append_boolean(True)  # allow pets
            self.response.append_boolean(False)  # display room entry ad

    def get_response(self):
        return self.response
