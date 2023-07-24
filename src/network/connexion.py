from asyncore import dispatcher_with_send
from src.utils.base_64_encoding import decode_int32
from src.network.messages.client_message import ClientMessage
from src.communication.message_handler import handle
from src.game.users.user_manager import UserManager


class Connection(dispatcher_with_send):

    def new_session(self):
        UserManager.get_instance().new_session(self)

    def handle_read(self) -> None:
        data = self.recv(1024)
        if data.startswith(b"<policy-file-request/>"):
            policy = '<?xml version="1.0"?>' \
                     '<cross-domain-policy>' \
                     '<allow-access-from domain="*" to-ports="*" />' \
                     '</cross-domain-policy>' + chr(0)
            self.socket.sendall(policy.encode())
            print("Policy encode")
        try:
            user = UserManager.get_instance().get_user_by_socket(self)
            if data[0] == 64:
                pos = 0
                msg_id = None
                content = None
                while pos < len(data):
                    msg_length = decode_int32([data[pos], data[pos + 1], data[pos + 2]])
                    pos = pos + 3
                    msg_id = decode_int32([data[pos], data[pos + 1]])
                    pos = pos + 2

                    content = bytearray(msg_length - 2)
                    for i in range(len(content)):
                        content[i] = data[pos]
                        pos += 1

                client_message = ClientMessage(msg_id, content)
                handle(user, client_message.header, client_message)
            else:
                UserManager.get_instance().disconnect(user)
        except:
            pass
