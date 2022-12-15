from string import ascii_lowercase

VALUES = {
    "S": 1,
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
        start = cls.start[0]
        end = cls.end[0]
        path.append(end)
        cls.sort_sources(start)
        end.get_shortest_path(path, start)
        return start.shortest_path


    @classmethod
    def sort_sources(cls, goal):
        for node in cls.nodes.values():
            node.sources.sort(key=lambda s: abs(goal.x - s.x) + abs(goal.y - s.y))


    @classmethod
    def find_ideal_location(cls):
        potential = list()
        current = 0
        end = cls.end[0]
        for node in cls.nodes.values():
            if VALUES[node.value] == 1:
                potential.append(node)
        for location in potential:
            if location.shortest_path == 0:
                path = []
                cls.sort_sources(location)
                end.get_shortest_path(path, location)
            if current == 0 or current > location.shortest_path:
                current = location.shortest_path
        return current



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


    def get_shortest_path(self, path, goal):
        if self == goal:
            return
        for source in self.sources:
            if source.value != "E" and (source.shortest_path == 0 or source.shortest_path > self.shortest_path + 1):
                source.shortest_path = self.shortest_path + 1
                path.append(source)
                source.get_shortest_path(path, goal)
        path.pop()