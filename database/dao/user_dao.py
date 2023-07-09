from database.database import Database
from game.users.user import User
from game.users.user_details import UserDetails


class UserDao:
    def __init__(self, db: Database):
        self.db = db

    def login_sso(self, user: User, sso: str) -> bool:
        """
        Check sso login and fill user details
        :param user:
        :param sso:
        :return: True if user is connecting with correct ticket, False if not.
        """
        success = False
        req = self.db.get("SELECT id,"
                          "username,"
                          "mail,"
                          "look,"
                          "motto,"
                          "gender,"
                          "auth_ticket,"
                          "rank,"
                          "credits,"
                          "pixels,"
                          "shells"
                          " FROM users WHERE auth_ticket = '" + sso + "'")
        if len(req) == 1:
            user_info = req[0]
            user.set_details(UserDetails(user_info[0], user_info[1], user_info[2], user_info[3], user_info[4],
                                         user_info[5], user_info[6], user_info[7], user_info[8], user_info[9],
                                         user_info[10]))
            success = True

        return success

    def fill_subscription(self, user: User) -> None:
        user_id = user.get_details().get_id()
        req = self.db.get("SELECT subscription, end FROM users_subscriptions WHERE user_id = " + str(user_id))
        if len(req) == 1:
            user_subscription = req[0]
            user_subscription_type = user_subscription[0]
            user_subscription_end = user_subscription[1]

            user.get_subscription().set_subscription_type(user_subscription_type)
            user.get_subscription().set_expiration(user_subscription_end)
        else:
            print("No subscription found with that user id!")

    def save_details(self, user: User) -> None:
        self.db.update(table_name="users",
                       attributes={
                           "username": user.get_details().get_username(),
                           "rank": user.get_details().get_rank(),
                           "credits": user.get_details().get_credits(),
                           "pixels": user.get_details().get_pixels(),
                           "shells": user.get_details().get_shells(),
                           "look": user.get_details().get_figure(),
                           "motto": user.get_details().get_motto()
                       },
                       sql_condition="id = " + str(user.get_details().get_id()))

    def save_subscription(self, user: User) -> None:
        self.db.update(table_name="users_subscriptions",
                       attributes={
                           "subscription": user.get_subscription().get_subscription_type(),
                           "end": user.get_subscription().get_expiration()
                       },
                       sql_condition="user_id = " + str(user.get_details().get_id()))
