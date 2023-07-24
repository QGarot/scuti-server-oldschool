def encode_int32(i: int, num_bytes: int) -> bytes:
    """
    :param i:
    :param num_bytes:
    :return:
    """
    bz_res = bytearray(num_bytes)
    for j in range(num_bytes):
        k = (num_bytes - j - 1) * 6
        bz_res[j] = 64 + (i >> k & 63)
    return bytes(bz_res)


def decode_int32(bz_data) -> int:
    """
    :param bz_data:
    :return:
    """
    i = 0
    j = 0
    for k in range(len(bz_data) - 1, -1, -1):
        x = int(bz_data[k] - 64)
        if j > 0:
            x *= int(64 ** j)
        i += x
        j += 1
    return i
