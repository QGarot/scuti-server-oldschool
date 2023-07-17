from communication.incoming.message_event import MessageEvent
from communication.outgoing.rooms.engine.furniture_aliases_message_composer import FurnitureAliasesMessageComposer
from game.users.user import User
from network.messages.client_message import ClientMessage


class GetFurnitureAliasesMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage):
        user.send(FurnitureAliasesMessageComposer())
