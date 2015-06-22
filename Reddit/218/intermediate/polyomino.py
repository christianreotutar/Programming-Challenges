class Polyomino:

    def __init__(self, nodes):
        self.nodes = nodes

    def __str__(self):
        string = "["
        for i in range(len(self.nodes)):
            string += str(self.nodes[i]) + ", "
        string = string[:-2]
        string += "]"
        return string
