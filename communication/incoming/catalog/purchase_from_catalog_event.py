from communication.incoming.message_event import MessageEvent
from communication.outgoing.users.scr_send_user_info_message_composer import ScrSendUserInfoMessageComposer
from game.catalog.catalog_manager import CatalogManager
from game.users.user import User
from game.users.user_manager import UserManager
from network.messages.client_message import ClientMessage
import time


class PurchaseFromCatalogEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage) -> None:
        page_id = request.pop_wired_int32()
        item_id = request.pop_wired_uint()
        extra_data = request.pop_fixed_string()

        SUBSCRIPTION_CLUB_ITEM_ID = 4533
        if item_id == SUBSCRIPTION_CLUB_ITEM_ID:
            t = time.time()
            current_sub_expire = user.get_subscription().get_expiration()

            user.get_subscription().set_subscription_type("hc")
            if current_sub_expire - t > 0:
                user.get_subscription().set_expiration(current_sub_expire + 31 * 24 * 60 * 60)
            else:
                user.get_subscription().set_expiration(int(time.time()) + 31 * 24 * 60 * 60)

            UserManager.get_instance().get_dao().save_subscription(user)
            user.send(ScrSendUserInfoMessageComposer(user.get_subscription()))
