class PublicRoom:
    def __init__(self, banner_id: int, ptype: int, caption: str, description: str, image_type: str, room_id: int, recommended: int, category: bool, id: int):
        self.banner_id = banner_id
        self.type = ptype
        self.caption = caption
        self.description = description
        self.image_type = image_type
        self.room_id = room_id
        self.recommended = recommended
        self.category = category
        self.id = id

    def get_banner_id(self) -> int:
        return self.banner_id

    def get_type(self) -> int:
        return self.type

    def get_caption(self) -> str:
        return self.caption

    def get_description(self) -> str:
        return self.description

    def get_image_type(self) -> str:
        return self.image_type

    def get_room_id(self) -> int:
        return self.room_id

    def get_recommended(self) -> int:
        return self.recommended

    def get_id(self) -> int:
        return self.id
