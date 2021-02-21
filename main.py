class Cube:
    """Class to store the Rubik's cube in a list and its methods to perform operations, initializes itself to a solved
    Rubik's cube.


    """

    def __init__(self, n: int):
        self.n = n
        self.cube = [[[] for x in range(n)] for x in range(6)]

        for x in range(6):
            for y in range(n):
                self.cube[x][y] = [x for i in range(n)]

    def __str__(self):
        """Method to print out folded out Rubik's cube"""
        string = ""
        for x in range(self.n):
            string += self.n * " " + ''.join(str(x) for x in self.cube[0][x]) + self.n * " " + "\n"

        for x in range(self.n):
            string += ''.join(str(x) for x in self.cube[1][x]) + ''.join(str(x) for x in self.cube[2][x]) + ''.join(str(x) for x in self.cube[3][x]) + "\n"

        for x in range(self.n * 2):
            string += self.n * " " + ''.join(str(x) for x in self.cube[4 + x // self.n][x % self.n]) + self.n * " " + "\n"

        return string

    def flipCenter(self, orientation: int, flips: int):

        pass

    def flipEdge(self, orientation: int, flips: int):

        pass


c = Cube(5)
print(c)
