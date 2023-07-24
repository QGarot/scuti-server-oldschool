import time
from src.utils.date import seconds_to_days


class ClubSubscription:
    def __init__(self):
        self.subscription_type = ""  # "vip" or "hc"
        self.expiration = 0

    def get_subscription_type(self) -> str:
        return self.subscription_type

    def is_valid(self) -> bool:
        return self.expiration > int(time.time()) \
            and (self.get_subscription_type() == "vip" or self.get_subscription_type() == "hc")

    def delete(self) -> None:
        self.expiration = 0
        self.subscription_type = ""

    def get_days_left(self) -> int:
        if self.is_valid():
            return seconds_to_days(self.expiration - int(time.time()))
        else:
            return 0

    def set_subscription_type(self, sub_type: str) -> None:
        self.subscription_type = sub_type

    def set_expiration(self, end: int) -> None:
        self.expiration = end

    def get_expiration(self) -> int:
        return self.expiration
