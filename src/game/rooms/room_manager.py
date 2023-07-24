from typing import Self

from src.database.dao.room_dao import RoomDao
from src.database.database import Database
from src.game.manager.manager import Manager
from src.game.rooms.room import Room


class RoomManager(Manager):
    def __init__(self):
        self.rooms = []
        self.room_dao = None

    @classmethod
    def get_instance(cls) -> Self | None:
        if cls.instance is None:
            cls.instance = RoomManager()
            print("RoomManager loaded!")
            return None
        else:
            return cls.instance

    def set_dao(self, db: Database):
        """
        Set DAO instance(s)
        :param db:
        :return:
        """
        self.room_dao = RoomDao(db)

    def get_dao(self) -> RoomDao:
        """
        :return: room dao instance
        """
        return self.room_dao

    def load_rooms(self) -> None:
        """
        Load all rooms registered in the database
        :return:
        """
        self.rooms = self.get_dao().get_rooms()

    def get_rooms_map(self) -> list[Room]:
        """
        :return: entire rooms map
        """
        return self.rooms

    def get_rooms_by_owner_username(self, username: str) -> list[Room]:
        """
        :param username:
        :return: rooms of 'username'
        """
        rooms_selected = []
        for room in self.get_rooms_map():
            if room.get_room_data().get_owner_name() == username:
                rooms_selected.append(room)

        return rooms_selected

    def get_room_by_id(self, id: int) -> Room | None:
        for room in self.get_rooms_map():
            if room.get_room_data().get_id() == id:
                return room
        return None

    def update_current_visitors_in_a_room(self, room_id: int) -> None:
        room = self.get_room_by_id(room_id)
        visitors_now = room.get_users_now()

        self.get_dao().update_visitor(room_id, visitors_now)
        room.get_room_data().set_visitors_now(visitors_now)

