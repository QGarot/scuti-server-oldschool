from src.database.database import Database
from src.game.furnitures.furniture import Furniture


class FurnitureDao:
    def __init__(self, db: Database):
        self.db = db

    def get_furnitures(self) -> list[Furniture]:
        req = self.db.get("SELECT * FROM furnitures")
        res = []
        for furniture in req:
            id = furniture[0]
            public_name = furniture[1]
            item_name = furniture[2]
            type = furniture[3]
            width = furniture[4]
            length = furniture[5]
            stack_height = furniture[6]
            can_stack = furniture[7] == 1
            can_sit = furniture[8] == 1
            is_walkable = furniture[9] == 1
            sprite_id = furniture[10]
            allow_recycle = furniture[11] == 1
            allow_trade = furniture[12] == 1
            allow_marketplace_sell = furniture[13] == 1
            allow_gift = furniture[14] == 1
            allow_inventory_stack = furniture[15] == 1
            interaction_type = furniture[16]
            interaction_modes_count = furniture[17]
            vending_ids = furniture[18]
            is_arrow = furniture[19] == 1
            height_adjustable = furniture[20] == 1
            effect_m = furniture[21]
            effect_f = furniture[22]
            res.append(Furniture(id, public_name, item_name, type, width, length, stack_height, can_stack, can_sit, is_walkable, sprite_id, allow_recycle, allow_trade, allow_marketplace_sell, allow_gift, allow_inventory_stack, interaction_type, interaction_modes_count, vending_ids, is_arrow, height_adjustable, effect_m, effect_f))

        return res
