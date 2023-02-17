from communication.outgoing.message_composer import MessageComposer
from database.database import Database
from game.users.user import User
from database.dao.user_dao import UserDao
from game.users.user_details import UserDetails
from typing import Self


class UserManager:
    instance = None

    def __init__(self):
        # list of users online
        self.users = []
        # DAO
        self.user_dao = None

    @classmethod
    def get_instance(cls) -> Self | None:
        if cls.instance is None:
            cls.instance = UserManager()
            print("UserManager loaded!")
            return None
        else:
            return cls.instance

    def set_dao(self, db: Database) -> None:
        """
        Set DAO instance(s)
        :param db:
        :return:
        """
        self.user_dao = UserDao(db)

    def get_dao(self) -> UserDao:
        """
        :return: return dao instance
        """
        return self.user_dao

    def get_users(self) -> list[User]:
        """
        :return: list of users registered
        """
        return self.users

    def get_user_by_id(self, user_id: int) -> User | None:
        """
        :param user_id:
        :return: user corresponding to this id
        """
        for user in self.get_users():
            if user.get_details().get_id() == user_id:
                return user

        return None

    def get_user_by_username(self, name: str) -> User | None:
        """
        :param name:
        :return: user corresponding to this name
        """
        for user in self.get_users():
            if user.get_details().get_username() == name:
                return user

        return None

    # TODO: use dao structure here to return only data thanks to a SQL query instead of 'return None'
    def get_user_data(self, user_id: int) -> UserDetails | None:
        """
        :param user_id:
        :return: data corresponding to user with this user_id
        """
        user = self.get_user_by_id(user_id)
        if user is not None:
            return user.get_details()
        else:
            return None

    def connect_user(self, user: User) -> None:
        """
        Add user to the list of users connected
        :param user:
        :return:
        """
        if user is not None:
            self.users.append(user)
            user.login()

    def send_all(self, server_message: MessageComposer) -> None:
        """
        Send a composer to all users connected
        :param server_message:
        :return:
        """
        for user in self.get_users():
            user.send(server_message)
