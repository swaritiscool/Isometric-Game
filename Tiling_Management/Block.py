class Block():
    def __init__(self, name, i, j, z, grid_x, grid_y, mov_weight, breakable):
        self.name = name
        self.i = i
        self.j = j
        self.z = z
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.mov_weight = mov_weight
        self.breakable = breakable
