from abc import ABC, abstractmethod

from network.messages.server_message import ServerMessage


class MessageComposer(ABC):
    @abstractmethod
    def compose(self) -> None:
        """
        Compose message to send to the client
        :return:
        """
        pass

    @abstractmethod
    def get_response(self) -> ServerMessage:
        """
        :return: Server message. Ready to be sent to the client
        """
        pass
