NEGATIVE = 72
POSITIVE = 73
MAX_INTEGER_BYTE_AMOUNT = 6


def encode_int32(i: int) -> bytearray:
    wf = bytearray(6)
    pos = 0
    num_bytes = 1
    start_pos = pos
    num_4 = 4 if i < 0 else 0
    i = abs(i)
    wf[pos] = 64 + (i & 3)
    pos += 1
    i >>= 2
    while i != 0:
        num_bytes += 1
        wf[pos] = 64 + (i & 63)
        pos += 1
        i >>= 6
    wf[start_pos] = wf[start_pos] | (num_bytes << 3) | num_4
    bz_data = bytearray(num_bytes)
    for x in range(num_bytes):
        bz_data[x] = wf[x]
    return bz_data


def decode_int32(bz_data: bytearray):
    is_negative = (bz_data[0] & 4) == 4
    total_bytes = (bz_data[0] >> 3 & 7)
    v = bz_data[0] & 3
    pos = 1
    shift_amount = 2
    for i in range(1, total_bytes):
        v |= (bz_data[pos] & 63) << shift_amount
        shift_amount = 2 + 6 * i
        pos += 1
    if is_negative:
        v *= -1
    return v, total_bytes
