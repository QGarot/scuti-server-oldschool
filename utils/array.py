class Matrix:
    def __init__(self, length_x: int, length_y: int, default=None):
        self.length_x = length_x
        self.length_y = length_y
        self.default_value = default

        self.matrix = []
        self.generate()

    def generate(self) -> None:
        for y in range(self.length_y):
            self.matrix.append([])
            for x in range(self.length_x):
                self.matrix[y].append(self.default_value)

    def print(self) -> None:
        for y in range(self.length_y):
            print(self.matrix[y])
        print("")

    def get(self, x, y) -> list:
        return self.matrix[y][x]

    def set(self, x, y, val) -> None:
        self.matrix[y][x] = val
