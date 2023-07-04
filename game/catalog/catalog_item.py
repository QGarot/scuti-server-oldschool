class CatalogItem:
    def __init__(self, id: int, page_id: int, item_id: int, name: str, credits_cost: int, pixels_cost: int,
                 shells_cost: int, amount: int, vip: int, achievement: int, song_id: int):
        self.id = id
        self.item_id = item_id
        self.name = name
        self.credits_cost = credits_cost
        self.pixels_cost = pixels_cost
        self.shells_cost = shells_cost
        self.amount = amount
        self.page_id = page_id
        self.vip = vip
        self.achievement = achievement
        self.song_id = song_id

    def get_id(self) -> int:
        return self.id

    def get_name(self) -> str:
        return self.name

    def get_credits_cost(self) -> int:
        return self.credits_cost

    def get_pixels_cost(self) -> int:
        return self.pixels_cost

    def get_shells_cost(self) -> int:
        return self.shells_cost

    def get_amount(self) -> int:
        return self.amount

    def get_page_id(self) -> int:
        return self.page_id

    def get_item_id(self) -> int:
        return self.item_id

    def get_vip(self) -> int:
        return self.vip

    def get_achievement(self) -> int:
        return self.achievement

    def get_song_id(self) -> int:
        return self.song_id
