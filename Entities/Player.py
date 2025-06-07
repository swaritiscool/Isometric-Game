class Player():
    def __init__(self, i, j, z, money, health, destination):
        self.i = i
        self.j = j
        self.z = z
        self.money = money
        self.health = health
        self.destination = destination
        self.mov_opt = []

    def update_movement_options(self, tile_map):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # down, right, up, left
        self.mov_opt = []

        for di, dj in directions:
            if self.i < 0:
                self.i = 0
            if self.j < 0:
                self.j = 0
            ni, nj = self.i + di, self.j + dj
            key = (ni, nj, self.z)
            if key in tile_map:
                block_data = tile_map[key]
                block_data["mov_weight"] = 1
                if block_data["mov_weight"] >= 0:
                    self.mov_opt.append((ni, nj, self.z))

    def move(self, tile_map):
        current = (self.i, self.j, self.z)

        if current == self.destination:
            return

        self.update_movement_options(tile_map)

        dest_i, dest_j, dest_z = self.destination
        best_next = None
        min_dist = float('inf')

        for option in self.mov_opt:
            oi, oj, oz = option
            dist = abs(dest_i - oi) + abs(dest_j - oj)  # Manhattan distance
            if dist < min_dist:
                min_dist = dist
                best_next = (oi, oj, oz)

        if best_next:
            self.i, self.j, x = best_next
            print(f"Moved to {best_next}")
