class Tiles():
    def __init__(self, *args):
        self.blocks = []
        for block in args:
            self.blocks.append(block)

    def add(self, *args):
        for block in args:
            self.blocks.append(block)

    def get(self):
        return self.blocks

    def get_dict(self):
        tile_map = {}
        for block in self.blocks:
            key = (block.i, block.j, block.z)
            tile_map[key] = {
                "name": block.name,
                "mov_weight": block.mov_weight,
                "breakable": block.breakable
            }
        return tile_map
