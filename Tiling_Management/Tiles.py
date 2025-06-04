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
