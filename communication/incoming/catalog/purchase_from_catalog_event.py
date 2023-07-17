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
            if catalog_item.get_name() in ["HABBO_CLUB_BASIC_1_MONTH", "HABBO_CLUB_BASIC_3_MONTH", "HABBO_CLUB_VIP_1_MONTH", "HABBO_CLUB_VIP_3_MONTHS"]:
                PurchaseFromCatalogEvent.handle_subscription(user, catalog_item.get_name())
        else:
            print("No catalog item found with that id (" + str(catalog_item_id) + ").")

    @staticmethod
    def handle_subscription(user: User, subscription_name: str):
        # Cannot buy subscription if the user is already member of a club
        if user.get_subscription().is_valid():
            user.send_alert("You are already a " + user.get_subscription().get_subscription_type() + " member! "
                            "Please renew your subscription once it expires.")
        else:
            # Get sub. type & period
            sub_type = subscription_name.split("_")[2]
            period = int(subscription_name.split("_")[3])

            if sub_type == "BASIC":
                user.get_subscription().set_subscription_type("hc")
            elif sub_type == "VIP":
                user.get_subscription().set_subscription_type("vip")
            else:
                user.get_subscription().set_subscription_type("hc")
            user.get_subscription().set_expiration(int(time.time()) + minutes_to_seconds(hours_to_minutes(days_to_hours(period * 31))))

            UserManager.get_instance().get_dao().save_subscription(user)
            user.send(ScrSendUserInfoMessageComposer(user.get_subscription()))
            user.send_alert("You just join a club!")
