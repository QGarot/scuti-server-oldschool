from communication.incoming.message_event import MessageEvent
from communication.outgoing.users.scr_send_user_info_message_composer import ScrSendUserInfoMessageComposer
from game.catalog.catalog_manager import CatalogManager
from game.users.user import User
from game.users.user_manager import UserManager
from network.messages.client_message import ClientMessage
import time
from utils.date import days_to_hours, hours_to_minutes, minutes_to_seconds


class PurchaseFromCatalogEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage) -> None:
        page_id = request.pop_wired_int32()
        catalog_item_id = request.pop_wired_uint()
        extra_data = request.pop_fixed_string()

        # TODO: create a purchase handler
        catalog_item = CatalogManager.get_instance().get_catalog_item_by_id(catalog_item_id)
        if catalog_item is not None:
            if catalog_item.get_name() == "HABBO_CLUB_BASIC_1_MONTH":
                t = time.time()
                one_month_in_seconds = minutes_to_seconds(hours_to_minutes(days_to_hours(31)))
                current_sub_expire = user.get_subscription().get_expiration()

                user.get_subscription().set_subscription_type("hc")
                if current_sub_expire - t > 0:
                    user.get_subscription().set_expiration(current_sub_expire + one_month_in_seconds)
                else:
                    user.get_subscription().set_expiration(int(time.time()) + one_month_in_seconds)

                UserManager.get_instance().get_dao().save_subscription(user)
                user.send(ScrSendUserInfoMessageComposer(user.get_subscription()))
        else:
            print("No catalog item found with that id (" + str(catalog_item_id) + ").")
