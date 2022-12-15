from string import ascii_lowercase

VALUES = {
    "S": 1,
    "E": 26
}
for i, char in enumerate(ascii_lowercase, 1):
    VALUES[char] = i

class Node:
    end = []
    nodes = dict()
    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        self.value = char
        if char == "E":
            self.end.append(self)
        self.shortest_path = 0
        self.nodes[f"({self.x}, {self.y})"] = self
        self.sources = []
        self.visited = False

    def __repr__(self):
        return f"{self.value} ({self.x}, {self.y})"

    @classmethod
    def find_shortest_path(cls, goalvalue):
        cls.reset()
        end = cls.end[0]
        current = [end]
        end.visited = True
        newcurrent = list()
        while True:
            for node in current:
                node.find_sources()
                for source in node.sources:
                    if not source.visited:
                        source.visited = True
                        source.shortest_path = node.shortest_path + 1
                        if source.value == goalvalue:
                            return source.shortest_path
                        newcurrent.append(source)
            current = newcurrent
            newcurrent = list()


    @classmethod
    def reset(cls):
        for node in cls.nodes.values():
            node.visited = 0
            node.shortest_path = 0


    def find_sources(self):
        north = self.nodes.get(f"({self.x}, {self.y - 1})")
        south = self.nodes.get(f"({self.x}, {self.y + 1})")
        east = self.nodes.get(f"({self.x + 1}, {self.y})")
        west = self.nodes.get(f"({self.x - 1}, {self.y})")
        if north != None and VALUES[north.value] + 1 >= VALUES[self.value]:
            self.sources.append(north)
        if south != None and VALUES[south.value] + 1 >= VALUES[self.value]:
            self.sources.append(south)
        if east != None and VALUES[east.value] + 1 >= VALUES[self.value]:
            self.sources.append(east)
        if west != None and VALUES[west.value] + 1 >= VALUES[self.value]:
            self.sources.append(west)