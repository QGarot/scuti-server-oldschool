class Furniture:
    def __init__(self, id: int, public_name: str, item_name: str, type: str, width: int, length: int, stack_height: int,
                 can_stack: bool, can_sit: bool, is_walkable: bool, sprite_id: int, allow_recycle: bool,
                 allow_trade: bool, allow_marketplace_sell: bool, allow_gift: bool, allow_inventory_stack: bool,
                 interaction_type: str, interaction_modes_count: int, vending_ids: int, is_arrow: bool,
                 height_adjustable: bool, effect_m: int, effect_f: int):

        self.id = id
        self.public_name = public_name
        self.item_name = item_name
        self.type = type
        self.width = width
        self.length = length
        self.stack_height = stack_height
        self.can_stack = can_stack
        self.can_sit = can_sit
        self.is_walkable = is_walkable
        self.sprite_id = sprite_id
        self.allow_recycle = allow_recycle
        self.allow_trade = allow_trade
        self.allow_marketplace_sell = allow_marketplace_sell
        self.allow_gift = allow_gift
        self.allow_inventory_stack = allow_inventory_stack
        self.interaction_type = interaction_type
        self.interaction_modes_count = interaction_modes_count
        self.vending_ids = vending_ids
        self.is_arrow = is_arrow
        self.height_adjustable = height_adjustable
        self.effect_m = effect_m
        self.effect_f = effect_f

    def get_id(self) -> int:
        return self.id

    def get_public_name(self) -> str:
        return self.public_name

    def get_item_name(self) -> str:
        return self.item_name

    def get_type(self) -> str:
        return self.type

    def get_width(self) -> int:
        return self.width

    def get_length(self) -> int:
        return self.length

    def get_stack_height(self) -> int:
        return self.stack_height

    def get_can_stack(self) -> bool:
        return self.can_stack

    def get_can_sit(self) -> bool:
        return self.can_sit

    def get_is_walkable(self) -> bool:
        return self.is_walkable

    def get_sprite_id(self) -> int:
        return self.sprite_id

    def get_allow_recycle(self) -> bool:
        return self.allow_recycle

    def get_allow_trade(self) -> bool:
        return self.allow_trade

    def get_allow_marketplace_sell(self) -> bool:
        return self.allow_marketplace_sell

    def get_allow_gift(self) -> bool:
        return self.allow_gift

    def get_allow_inventory_stack(self) -> bool:
        return self.allow_inventory_stack

    def get_interaction_type(self) -> str:
        return self.interaction_type

    def get_interaction_modes_count(self) -> int:
        return self.interaction_modes_count

    def get_vending_ids(self) -> int:
        return self.vending_ids

    def get_is_arrow(self) -> bool:
        return self.is_arrow

    def get_height_adjustable(self) -> bool:
        return self.height_adjustable

    def get_effect_m(self) -> int:
        return self.effect_m

    def get_effect_f(self) -> int:
        return self.effect_f
