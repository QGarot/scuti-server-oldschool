from src.communication.incoming.message_event import MessageEvent
from src.communication.outgoing.rooms.engine.furniture_aliases_message_composer import FurnitureAliasesMessageComposer
from src.game.users.user import User
from src.network.messages.client_message import ClientMessage


class GetFurnitureAliasesMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage):
        user.send(FurnitureAliasesMessageComposer())
