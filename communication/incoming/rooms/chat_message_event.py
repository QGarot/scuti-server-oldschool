from communication.incoming.message_event import MessageEvent
from communication.outgoing.rooms.chat_message_composer import ChatMessageComposer
from game.users.user import User
from network.messages.client_message import ClientMessage


class ChatMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage) -> None:
        message = request.pop_fixed_string()
        user.send(ChatMessageComposer(user_id=1, message=message))
