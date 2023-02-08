import utils.WireEncoding
import utils.Base64Encoding


class ServerMessage:
    def __init__(self, message_id=None):
        self.body = []
        self.message_id = message_id

    def append_boolean(self, boolean):
        if boolean:
            self.body.append(0x49)
        else:
            self.body.append(0x48)

    def append_byte(self, b):
        self.body.append(b)

    def append_bytes(self, data):
        if data and len(data) > 0:
            self.body.extend(data)

    def append_int32(self, i):
        self.append_bytes(utils.WireEncoding.encode_int32(i))

    def append_raw_int32(self, i):
        self.append_string(str(i), encoding='ASCII')

    def append_raw_uint(self, i):
        self.append_raw_int32(int(i))

    def append_string(self, s, encoding='UTF-8'):
        if s and len(s) > 0:
            self.append_bytes(s.encode(encoding))

    def append_string_with_break(self, s, break_char=2):
        self.append_string(s)
        self.append_byte(break_char)

    def append_uint(self, i):
        self.append_int32(int(i))

    def clear(self):
        self.body = []

    def get_bytes(self):
        buffer = [0] * (self.length() + 3)
        buffer2 = utils.Base64Encoding.encode_int32(self.message_id, 2)
        buffer[0] = buffer2[0]
        buffer[1] = buffer2[1]
        for i in range(self.length()):
            buffer[i + 2] = self.body[i]
        buffer[-1] = 1
        return buffer

    def to_body_string(self):
        return ''.join(map(chr, self.body))

    def __str__(self):
        return f'{self.header()}{self.to_body_string()}'

    def length(self):
        return len(self.body)

    def header(self):
        return ''