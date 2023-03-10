from database.database import Database
from game.users.user import User


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
        req = self.db.get("SELECT id, username, mail, look, motto, gender, auth_ticket, rank, credits FROM users WHERE auth_ticket = '" + sso + "'")
        if len(req) == 1:
            user_info = req[0]
            user.get_details().fill(user_info[0],
                                    user_info[1],
                                    user_info[2],
                                    user_info[3],
                                    user_info[4],
                                    user_info[5],
                                    user_info[6],
                                    user_info[7],
                                    user_info[8])
            success = True

        return success


