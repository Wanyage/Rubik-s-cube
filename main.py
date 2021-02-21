class Cube:
    """"Class to store the Rubik's cube in a list and its methods to perform operations, initializes itself to a solved
    Rubik's cube.


    """

    def __init__(self, n: int):
        self.cube = [[[] for x in range(n)] for x in range(6)]

        for x in range(6):
            for y in range(n):
                self.cube[x][y] = [x for i in range(0, n)]

    def centerFlip(self, n: int, orientation: int, direction: int):
        pass

    def edgeFlip(self, n: int, orientation: int, direction: int):
        pass

c = Cube(3)
