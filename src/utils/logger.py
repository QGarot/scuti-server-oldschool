def info(msg: str):
    print("[Info] " + msg)


def error(msg: str):
    print("[Error] " + msg)


def log_packet(header: int, packet_detail: str):
    print("[Packet "+str(header)+"] " + packet_detail)

