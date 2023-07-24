from abc import ABC, abstractmethod


class Scuti(ABC):
    @abstractmethod
    def run_server(self) -> None:
        """
        Start the server
        :return:
        """
        pass
