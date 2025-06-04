class Player():
    def __init__(self, i, j, z, money, health, destination):
        self.i = i
        self.j = j
        self.z = z
        self.money = money
        self.health = health
        self.destination = destination
        """
            Let's keep destination = (i, j, z)

            Each block has some weight, so using this weight attribute, we can control.
            if out character should go on the block next to it or not.
            
            Total 4 blocks around the Player at once...

            Based on vertical stuff. If there is something above, you can't see what's below.
        """

    def move(self, destination: tuple):
        """
            Add code to move the player... will be given the destination
        """
        pass
