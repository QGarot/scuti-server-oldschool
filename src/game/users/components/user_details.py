class UserDetails:
    def __init__(self):
        # Basic info definition
        self.id = None
        self.username = None
        self.email = None
        self.figure = None
        self.motto = None
        self.sex = None
        self.sso_ticket = None
        self.machine_id = None
        self.rank = None

        # Currencies
        self.credits = None
        self.pixels = None
        self.shells = None

        # Respect points
        self.respect = None
        self.daily_respect_points = None

    def fill(self, id: int, username: str, email: str, figure: str, motto: str, sex: str, sso_ticket: str,
                 rank: int, credits: int, pixels: int, shells: int):
        # Basic info definition
        self.id = id
        self.username = username
        self.email = email
        self.figure = figure
        self.motto = motto
        self.sex = sex
        self.sso_ticket = sso_ticket
        self.machine_id = None
        self.rank = rank

        # Currencies
        self.credits = credits
        self.pixels = pixels
        self.shells = shells

        # Respect points
        self.respect = 0
        self.daily_respect_points = 3

    # Getters
    def get_id(self) -> int:
        """
        :return: user id
        """
        return self.id

    def get_username(self) -> str:
        """
        :return: user name
        """
        return self.username

    def get_figure(self) -> str:
        """
        :return: user look
        """
        return self.figure

    def get_motto(self) -> str:
        """
        :return: user description/motto
        """
        return self.motto

    def get_sex(self) -> str:
        """
        :return: user gender
        """
        return self.sex

    def get_sso_ticket(self) -> str:
        """
        :return: user login sso ticket
        """
        return self.sso_ticket

    def get_rank(self) -> int:
        """
        :return: user rank id
        """
        return self.rank

    def get_credits(self) -> int:
        """
        :return: credits amount
        """
        return self.credits

    def get_pixels(self) -> int:
        """
        :return: pixels amount
        """
        return self.pixels

    def get_shells(self) -> int:
        """
        :return: shells amount
        """
        return self.shells

    def get_respect(self) -> int:
        """
        :return: respect
        """
        return self.respect

    def get_daily_respect_points(self) -> int:
        """
        :return: daily respect points
        """
        return self.daily_respect_points

    # Setters
    def set_username(self, name: str) -> None:
        """
        Set a new username
        :param name:
        :return:
        """
        self.username = name

    def set_email(self, email: str) -> None:
        """
        Set a new email adress
        :param email:
        :return:
        """
        self.email = email

    def set_figure(self, figure: str) -> None:
        """
        Set a new look
        :param figure:
        :return:
        """
        self.figure = figure

    def set_motto(self, motto: str) -> None:
        """
        Set a new profile description
        :param motto:
        :return:
        """
        self.motto = motto

    def set_rank(self, rank: int) -> None:
        """
        Set a new rank
        :param rank:
        :return:
        """
        self.rank = rank

    def add_credits(self, amount: int) -> None:
        """
        Add credits
        :param amount: could be positive or negative
        :return:
        """
        self.credits = self.credits + amount

    def add_pixels(self, amount: int) -> None:
        """
        Add pixels
        :param amount: could be positive or negative
        :return:
        """
        self.pixels = self.pixels + amount

    def add_shells(self, amount: int) -> None:
        """
        Add shells
        :param amount: could be positive or negative
        :return:
        """
        self.shells = self.shells + amount

    # Other
