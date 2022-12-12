from string import ascii_lowercase

VALUES = {
    "S": 0,
    "E": 27
}
for i, char in enumerate(ascii_lowercase, 1):
    VALUES[char] = i

class Node:
    
    nodes = dict()
    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        self.value = char
        self.shortest_path = 0
        self.nodes[f"({self.x}, {self.y})"] = self
        self.targets = []

    def __repr__(self):
        return f"{self.value} ({self.x}, {self.y})"

    @classmethod
    def find_shortest_path(cls):
        start = None
        for k, node in cls.nodes.items():
            if k.startswith("S"):
                start = node
                break
        start.get_shortest_path()
        return start.shortest_path


    def find_targets(self):
        north = self.nodes.get(f"({self.x}, {self.y - 1})")
        south = self.nodes.get(f"({self.x}, {self.y + 1})")
        east = self.nodes.get(f"({self.x + 1}, {self.y})")
        west = self.nodes.get(f"({self.x - 1}, {self.y})")
        if north != None and VALUES[north.value] <= VALUES[self.value] + 1:
            self.targets.append(north)
        if south != None and VALUES[south.value] <= VALUES[self.value] + 1:
            self.targets.append(south)
        if east != None and VALUES[east.value] <= VALUES[self.value] + 1:
            self.targets.append(east)
        if west != None and VALUES[west.value] <= VALUES[self.value] + 1:
            self.targets.append(west)

    def get_shortest_path(self):
        path = []
        for target in self.targets:
            if target.shortest_path == 0 and target.value != "E":
                target.get_shortest_path()
            path.append(target.shortest_path + 1)
        self.shortest_path = min(path)