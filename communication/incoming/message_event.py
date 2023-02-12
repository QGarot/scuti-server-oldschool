from game.users.user import User
from network.messages.client_message import ClientMessage
from abc import ABC, abstractmethod


class MessageEvent(ABC):
    @staticmethod
    @abstractmethod
    def handle(user: User, request: ClientMessage) -> None:
        """
        Handle the event received
        :param user:
        :param request: client message
        :return:
        """
        pass
