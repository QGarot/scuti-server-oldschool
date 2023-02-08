from abc import ABC, abstractmethod

from network.messages.server_message import ServerMessage


class MessageComposer(ABC):
    @abstractmethod
    def compose(self):
        """
        Compose message to send to the client
        :return:
        """
        pass

    @abstractmethod
    def get_response(self) -> ServerMessage:
        pass
