from src.communication.incoming.message_event import MessageEvent
from src.communication.outgoing.moderator.mod_message_composer import ModMessageComposer
from src.communication.outgoing.notifications.habbo_broadcast_message_composer import HabboBroadcastMessageComposer
from src.communication.outgoing.rooms.chat.chat_message_composer import ChatMessageComposer
from src.game.users.user import User
from src.network.messages.client_message import ClientMessage


class ChatMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage) -> None:
        message = request.pop_fixed_string()
        user.send(ChatMessageComposer(user_id=user.get_details().get_id(), message=message))

        # just for some tests
        if message == "alert1":
            user.send(ModMessageComposer("test dsl", "https://google.com"))

        elif message == "alert2":
            user.send(HabboBroadcastMessageComposer("scuti is here"))
