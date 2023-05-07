class RoomData:
    def __init__(self):
        self.id = 0
        self.room_type = ""
        self.caption = ""
        self.owner_name = ""
        self.description = ""
        self.category = 0
        self.state = "open"
        self.users_now = 0
        self.users_max = 0
        self.model_name = "model_a"
        self.score = 0
        self.tags = ""
        self.icon_bg = 0
        self.icon_fg = 0
        self.icon_items = ""
        self.password = ""
        self.wallpaper = ""
        self.floor = ""
        self.landscape = ""

    def fill(self, id: int, room_type: str, caption: str, owner_name: str, description: str, category: int,
             state: str, users_now: int, users_max: int, model_name: str, score: int, tags: str, icon_bg: int, icon_fg: int, icon_items: str,
             password: str, wallpaper: str, floor: str, landscape: str) -> None:
        self.id = id
        self.room_type = room_type
        self.caption = caption
        self.owner_name = owner_name
        self.description = description
        self.category = category
        self.state = state
        self.users_now = users_now
        self.users_max = users_max
        self.model_name = model_name
        self.score = score
        self.tags = tags
        self.icon_bg = icon_bg
        self.icon_fg = icon_fg
        self.icon_items = icon_items
        self.password = password
        self.wallpaper = wallpaper
        self.floor = floor
        self.landscape = landscape

    def get_id(self) -> int:
        """
        :return: room id
        """
        return self.id

    def get_room_type(self) -> str:
        """
        :return: private or public
        """
        return self.room_type

    def is_private(self) -> bool:
        """
        :return: True if the room is private, false else.
        """
        return self.get_room_type() == "private"

    def get_caption(self) -> str:
        """
        :return: room caption
        """
        return self.caption

    def get_owner_name(self) -> str:
        """
        :return: owner name
        """
        return self.owner_name

    def get_description(self) -> str:
        """
        :return: room description
        """
        return self.description

    def get_category(self) -> int:
        """
        :return: room category id
        """
        return self.category

    def get_state(self) -> int:
        """
        :return: 0 if the room is open, 1 if the room is locked and 2 if there is a password (default value)
        """
        if self.state == "open":
            return 0
        elif self.state == "locked":
            return 1
        else:
            return 2

    def get_users_now(self) -> int:
        """
        :return: current number of users in this room
        """
        return self.users_now

    def get_users_max(self) -> int:
        """
        :return: capacity of users in this room
        """
        return self.users_max

    def get_model(self) -> str:
        """
        :return: model name
        """
        return self.model_name

    def get_score(self) -> int:
        """
        :return: current score
        """
        return self.score

    def get_tags(self) -> str:
        """
        :return: tags
        """
        return self.tags

    def get_icon_background(self) -> int:
        """
        :return: icon background id
        """
        return self.icon_bg

    def get_icon_foreground(self) -> int:
        """
        :return: icon foreground id
        """
        return self.icon_fg

    def get_icon_items(self) -> str:
        """
        :return: icon items
        """
        return self.icon_items

    def get_password(self) -> str:
        """
        :return: room password
        """
        return self.password

    def get_wallpaper(self) -> str:
        """
        :return: custom wallpaper
        """
        return self.wallpaper

    def get_floor(self):
        """
        :return: custom floor
        """
        return self.floor

    def get_landscape(self) -> str:
        """
        :return: landscape
        """
        return self.landscape
