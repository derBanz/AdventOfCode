import os

# Part 1
print("------- Part 1 -------")


data = list()
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'data.txt')) as file:
    for line in file:
        data.append(line.strip())

class Tree:
    def __init__(self):
        self.root = Folder("/")
        self.folders = [self.root]
        self.currfolder = None

    def get_folders(self):
        value = ""
        for folder in folders:
            value += folder

    def build(self, data):
        for i, line in enumerate(data):
            if line[0] == "$":
                line = line.split(" ")
                if line[1] == "cd":
                    if line[2] == "..":
                        self.currfolder.get_filesize()
                        self.change_current_folder(self.currfolder.parent)
                    else:
                        self.change_current_folder(line[2], parent=self.currfolder)
            elif line[0:3] == "dir":
                folder = Folder(line[4:], self.currfolder)
                self.folders.append(folder)
                self.currfolder.add_file(folder)
            elif line[0] != "$":
                line = line.split(" ")
                value = int(line[0])
                newfile = File(line[1], value)
                try:
                    self.currfolder.add_file(newfile)
                except:
                    print(i)
        while self.currfolder:
            self.currfolder.get_filesize()
            self.change_current_folder(self.currfolder.parent)

    def change_current_folder(self, name, parent=None):
        folder = name
        if type(name) != Folder:
            folder = next(
                (folder for folder in self.folders if folder.name == name and folder.parent == parent),
                None
            )
        self.currfolder = folder


    def get_foldersize(self, lower, upper):
        size = 0
        for folder in self.folders:
            if folder.size in range(lower, upper):
                size += folder.size
        return size

    def delete_smallest_directory(self, required):
        totalspace = 70000000
        tobedeleted = required - (totalspace - self.root.size)
        delete = min([folder for folder in self.folders if folder.size >= tobedeleted ], key=lambda x: x.size)
        return delete


class Folder:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.files = []
        self.size = 0

    def __repr__(self):
        return self.name + "( " + str(self.size) + " )"

    def add_file(self, newfile):
        self.files.append(newfile)

    def get_filesize(self):
        self.size = 0
        for newfile in self.files:
            self.size += newfile.size

    
class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return self.name + "( " + str(self.size) + " )"


tree = Tree()
tree.build(data)

print(f"The sum of sizes is {tree.get_foldersize(lower=0, upper=100000)} for directory smaller than 100000.")

# Part 2
print("------- Part 2 -------")

print(f"The directory we choose to delete is {tree.delete_smallest_directory(30000000)}.")
