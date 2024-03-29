from src.communication.outgoing.message_composer import MessageComposer
from src.communication.outgoing.notifications.habbo_broadcast_message_composer import HabboBroadcastMessageComposer
from src.game.users.components.club_subscription import ClubSubscription
from src.game.users.components.user_details import UserDetails


class User:
    def __init__(self, socket):
        self.socket = socket

        # TODO: create a RoomUser class! it's better < RoomEntity
        self.room_id = None
        self.pos_x = None
        self.pos_y = None
        self.pos_z = None

        # Components
        self.club_subscription_component = ClubSubscription()
        self.details = UserDetails()

    def send(self, server_message: MessageComposer) -> None:
        """
        Compose and send a pack to the client
        :param server_message:
        :return:
        """
        try:
            server_message.compose()
            self.socket.send(bytearray(server_message.get_response().get_bytes()))
            print(type(server_message).__name__ + " sent!")
        except Exception as e:
            print(e.args)

    def send_alert(self, message: str) -> None:
        self.send(HabboBroadcastMessageComposer(message))

    def login(self):
        print(self.get_details().get_username() + " is connected!")

    def disconnect(self) -> None:
        """
        Disconnect (online/authenticated) user by closing the socket.
        :return:
        """
        print(self.get_details().get_username() + " is disconnected!")
        self.get_socket().close()

    def delete_session_client(self) -> None:
        """
        Disconnect client by closing the socket
        :return:
        """
        print("Client disconnected!")
        self.get_socket().close()

    def get_details(self) -> UserDetails:
        """
        :return: user details
        """
        return self.details

    def get_subscription(self) -> ClubSubscription:
        return self.club_subscription_component

    def get_socket(self):
        """
        :return: socket
        """
        return self.socket
