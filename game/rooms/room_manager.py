from typing import Self

from database.dao.room_dao import RoomDao
from database.database import Database
from game.rooms.room import Room


class RoomManager:
    instance = None

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

    def get_room_dao(self) -> RoomDao:
        """
        :return: room dao instance
        """
        return self.room_dao

    def load_rooms(self) -> None:
        """
        Load all rooms registered in the database
        :return:
        """
        for room in self.get_room_dao().get_rooms():
            self.rooms.append(room)

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
