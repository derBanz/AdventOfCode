# Part 1
print("------- Part 1 -------")

data = []
with open('data.txt') as file:
    for line in file:
        data.append(line.strip())


class Grid:

    grid = list()
    width = 0
    height = 0

    def __init__(self, width, height):
        grid = list()
        for h in range(height):
            grid.append([])
            for w in range(width):
                grid[-1].append(".")
        self.grid = grid
        self.width = width
        self.height = height


    def __repr__(self):
        t = [' '.join([cell for cell in row]) for row in self.grid]
        return ('\n'.join(t))


    def execute(self, command):
        for command in command:
            self.command(command)

    
    def command(self, command):
        command = command.split(" ")
        if command[0] == "rect":
            dimensions = command[1].split("x")
            self.rect(int(dimensions[0]), int(dimensions[1]))
        elif command[0] == "rotate":
            key = command[1]
            position = int(command[2][2:])
            amount = int(command[-1])
            self.rotate(key, position, amount)


    def rect(self, width, height):
        for r, row in enumerate(self.grid):
            if r < height:
                for c, cell in enumerate(row):
                    if c < width:
                        self.grid[r][c] = "#"


    def rotate(self, key, position, amount):
        if key == "column":
            self.rotatecolumn(position, amount)
        elif key == "row":
            self.rotaterow(position, amount)


    def rotatecolumn(self, position, amount):
        values = list()
        for i in range(len(self.grid)):
            values.append(self.grid[i][position])
        for i in range(len(self.grid)):
            self.grid[i][position] = values[i - amount]


    def rotaterow(self, position, amount):
        values = list()
        for i in range(len(self.grid[position])):
            values.append(self.grid[position][i])
        for i in range(len(self.grid[position])):
            self.grid[position][i] = values[i - amount]


    def countpixels(self):
        counter = 0
        for row in self.grid:
            for cell in row:
                counter += cell == "#"
        return counter



grid = Grid(50, 6)
grid.execute(data)
pixels = grid.countpixels()

print(f"After the intermediate voltage checks, {pixels} pixels are lit.")
print(grid)