class CatalogPage:
    def __init__(self, id: int, parent_id: int, caption: str, visible: bool, enabled: bool, min_rank: int, club_only: bool, icon_color: int, icon_img: int, layout: str,
                 layout_headline: str, layout_teaser: str, layout_special: str, text1: str, text2: str, text_details: str, text_teaser: str, text_link_desc: str,
                 text_link_page: str):
        self.id = id
        self.parent_id = parent_id
        self.caption = caption
        self.visible = visible
        self.enabled = enabled
        self.min_rank = min_rank
        self.club_only = club_only
        self.icon_color = icon_color
        self.icon_image = icon_img
        self.layout = layout
        self.layout_headline = layout_headline
        self.layout_teaser = layout_teaser
        self.layout_special = layout_special
        self.text1 = text1
        self.text2 = text2
        self.text_details = text_details
        self.text_teaser = text_teaser
        self.text_link_desc = text_link_desc
        self.text_link_page = text_link_page

    def get_id(self) -> int:
        return self.id

    def get_parent_id(self) -> int:
        return self.parent_id

    def get_caption(self) -> str:
        return self.caption

    def is_visible(self) -> bool:
        return self.visible

    def is_enabled(self) -> bool:
        return self.enabled

    def get_min_rank(self) -> int:
        return self.min_rank

    def is_club_only(self) -> bool:
        return self.club_only

    def get_icon_color(self) -> int:
        return self.icon_color

    def get_icon_image(self) -> int:
        return self.icon_image

    def get_layout(self) -> str:
        return self.layout

    def get_layout_headline(self) -> str:
        return self.layout_headline

    def get_layout_teaser(self) -> str:
        return self.layout_teaser

    def get_layout_special(self) -> str:
        return self.layout_special

    def get_text1(self) -> str:
        return self.text1

    def get_text2(self) -> str:
        return self.text2

    def get_text_details(self) -> str:
        return self.text_details

    def get_text_teaser(self) -> str:
        return self.text_teaser

    def get_text_link_desc(self) -> str:
        return self.text_link_desc

    def get_text_link_page(self) -> str:
        return self.text_link_page
