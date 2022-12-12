from string import ascii_lowercase

VALUES = {
    "S": 0,
    "E": 27
}
for i, char in enumerate(ascii_lowercase, 1):
    VALUES[char] = i

class Node:
    end = []
    start = []
    nodes = dict()
    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        self.value = char
        if char == "E":
            self.end.append(self)
        elif char == "S":
            self.start.append(self)
        self.shortest_path = 0
        self.nodes[f"({self.x}, {self.y})"] = self
        self.sources = []

    def __repr__(self):
        return f"{self.value} ({self.x}, {self.y})"

    @classmethod
    def find_shortest_path(cls):
        path = []
        path.append(cls.end[0])
        cls.end[0].get_shortest_path(path)
        return cls.start[0].shortest_path


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
        self.sources.sort(key=lambda x: abs(self.start[0].x - x.x) + abs(self.start[0].y - x.y))


    def get_shortest_path(self, path):
        if self.value == "S":
            return
        for source in self.sources:
            if source.value != "E" and (source.shortest_path == 0 or source.shortest_path > self.shortest_path + 1):
                source.shortest_path = self.shortest_path + 1
                path.append(source)
                source.get_shortest_path(path)
        path.pop()