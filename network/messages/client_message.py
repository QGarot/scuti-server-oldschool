from utils.Base64Encoding import decode_int32
import utils.WireEncoding


class ClientMessage:
    def __init__(self, header, body=None):
        if body is None:
            body = bytearray(0)
        self.header = header
        self.body = body
        self.pointer = 0

        self.remaining_length = len(self.body) - self.pointer

    def advance_pointer(self, i):
        self.pointer += i

    def get_body(self):
        return self.body.decode("utf-8")

    def plain_read_bytes(self, bytes):
        if bytes > self.remaining_length:
            bytes = self.remaining_length

        buffer = bytearray(bytes)
        index = 0
        for i in range(self.pointer, self.pointer + bytes):
            buffer[index] = self.body[i]
            index += 1
        return buffer

    def pop_base_64_boolean(self):
        b = self.remaining_length > 0 and self.body[self.pointer] == 0x41
        self.pointer = self.pointer + 1
        return b

    def pop_fixed_int_32(self):
        return int(self.pop_fixed_string("ascii"))

    def pop_fixed_string(self, encoding="utf-8"):
        return self.read_fixed_value().decode(encoding).replace(chr(1), " ")

    def pop_fixed_uint_32(self):
        return self.pop_fixed_int_32()

    def pop_int32(self):
        return int.from_bytes(self.read_bytes(2), "big")

    def pop__uint32(self):
        return self.pop_int32()

    def pop_wired_boolean(self):
        b = self.remaining_length > 0 and self.body[self.pointer] == 0x49
        self.pointer = self.pointer + 1
        return b

    def pop_wired_int32(self):
        if self.remaining_length < 1:
            return 0

        bzData = self.plain_read_bytes(6)
        num2 = utils.WireEncoding.decode_int32(bzData)
        self.pointer = self.pointer + 6
        return num2

    def pop_wired_uint(self):
        return self.pop_wired_int32()

    def read_bytes(self, Bytes):
        if Bytes > self.remaining_length:
            Bytes = self.remaining_length
        buffer = bytearray(Bytes)
        for i in range(Bytes):
            buffer[i] = self.body[self.pointer]
            self.pointer += 1
        return buffer

    def read_fixed_value(self):
        bytes = decode_int32(self.read_bytes(2))
        return self.read_bytes(bytes)

    def reset_pointer(self):
        self.pointer = 0

    def __str__(self):
        return self.header + self.body.decode("utf-8")
