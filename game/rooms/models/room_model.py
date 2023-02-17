
# Utils
def generate_array(x: int, y: int) -> list:
    """
    Generate a matrix filled with 0
    :param x: rows
    :param y: lines
    :return:
    """
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

        self.tile_states = None
        self.tile_heights = None

        self.parse()

    def parse(self) -> None:
        """
        Parse height map, generate tiles state and tiles heights
        :return:
        """
        lines = self.height_map.split("\r\n")
        self.map_size_y = len(lines)
        self.map_size_x = len(lines[0])
        self.tile_states = generate_array(self.map_size_x, self.map_size_y)
        self.tile_heights = generate_array(self.map_size_x, self.map_size_y)

        temporary_height_map = ""
        for y in range(self.map_size_y):
            line = lines[y]
            for x in range(self.map_size_x):
                tile = line[x]

                if tile.isdigit():
                    tile = int(tile)
                    self.tile_states[y][x] = OPEN
                    self.tile_heights[y][x] = tile
                else:
                    self.tile_states[y][x] = BLOCKED
                    self.tile_heights[y][x] = 0

                if x == self.door_x and y == self.door_y:
                    self.tile_states[y][x] = OPEN
                    self.tile_heights[y][x] = self.door_z

                temporary_height_map += str(tile)

            temporary_height_map += chr(13)

        self.height_map = temporary_height_map


hp_a = "xxxxxxxxxxxx\r\nxxxx00000000\r\nxxxx00000000\r\nxxxx00000000\r\nxxxx00000000\r\nxxxx00000000\r\nxxxx00000000\r\nxxxx00000000\r\nxxxx00000000\r\nxxxx00000000\r\nxxxx00000000\r\nxxxx00000000\r\nxxxx00000000\r\nxxxx00000000\r\nxxxxxxxxxxxx\r\nxxxxxxxxxxxx"
model_a = RoomModel("model_a", 3, 5, 0, 2, hp_a)

hp_b = "xxxxxxxxxxxxxxxxxxx\r\nxxxxxxx222222222222\r\nxxxxxxx222222222222\r\nxxxxxxx222222222222\r\nxxxxxxx222222222222\r\nxxxxxxx222222222222\r\nxxxxxxx222222222222\r\nxxxxxxx22222222xxxx\r\nxxxxxxx11111111xxxx\r\nx222221111111111111\r\nx222221111111111111\r\nx222221111111111111\r\nx222221111111111111\r\nx222221111111111111\r\nx222221111111111111\r\nx222221111111111111\r\nx222221111111111111\r\nx2222xx11111111xxxx\r\nx2222xx00000000xxxx\r\nx2222xx000000000000\r\nx2222xx000000000000\r\nx2222xx000000000000\r\nx2222xx000000000000\r\n22222xx000000000000\r\nx2222xx000000000000\r\nxxxxxxxxxxxxxxxxxxx"
model_b = RoomModel("model_p", 0, 23, 2, 2, hp_b)
