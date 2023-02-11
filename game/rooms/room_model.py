def generate_array(x: int, y: int) -> list:
    res = []
    for i in range(y):
        res.append([])
        for _ in range(x):
            res[i].append(0)

    return res


OPEN = 1
BLOCKED = 0


class RoomModel:
    def __init__(self, name: str, door_x: int, door_y: int, door_z: int, door_rotation: int, height_map: str):
        self.name = name
        self.door_x = door_x
        self.door_y = door_y
        self.door_z = door_z
        self.door_rotation = door_rotation
        self.height_map = height_map

        self.map_size_x = None
        self.map_size_y = None

        self.square_state = None
        self.square_floor_height = None

        self.generate()

    def generate(self):
        self.height_map = self.height_map.lower()
        tmp_height_map = self.height_map.split(chr(13))
        self.map_size_x = len(tmp_height_map[0])
        self.map_size_y = len(tmp_height_map)

        self.square_state = generate_array(self.map_size_x, self.map_size_y)
        self.square_floor_height = generate_array(self.map_size_x, self.map_size_y)

        for y in range(self.map_size_y):
            if y > 0:
                tmp_height_map[y] = tmp_height_map[y][1:]

            for x in range(self.map_size_x):
                square = tmp_height_map[y][x].strip().lower()
                if square == "x":
                    self.square_state[y][x] = BLOCKED
                else:
                    self.square_state[y][x] = OPEN
                    self.square_floor_height[y][x] = float(square)

        self.square_floor_height[self.door_y][self.door_x] = self.door_z

    def string_builder(self) -> str:
        res = ""
        arr = self.height_map.split("\r\n")
        for i in range(len(arr)):
            text = arr[i]
            if text != "":
                res = res + text
                res = res + "\r\n"
        return res

    def floor_height_map(self, packet):
        arr = self.height_map.split(chr(13))
        for i in range(self.map_size_y):
            if i > 0:
                arr[i] = arr[i][1:]
            for j in range(self.map_size_x):
                text = arr[i][j].strip().lower()
                if self.door_x == j and self.door_y == i:
                    text = str(int(self.door_z))
                packet.append_string(text)
            packet.append_string(chr(13))


hp = "xxxxxxxxxxxx\r\nxxxx00000000\r\nxxxx00000000\r\nxxxx00000000\r\nxxxx00000000\r\nxxxx00000000\r\nxxxx00000000\r\nxxxx00000000\r\nxxxx00000000\r\nxxxx00000000\r\nxxxx00000000\r\nxxxx00000000\r\nxxxx00000000\r\nxxxx00000000\r\nxxxxxxxxxxxx\r\nxxxxxxxxxxxx"
model = RoomModel("model_a", 3, 5, 0, 2, hp)



