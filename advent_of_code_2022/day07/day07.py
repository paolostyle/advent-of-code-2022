import re

from anytree import NodeMixin  # type: ignore

FILE_REGEX = re.compile(r"(\d+) ([A-z\.]+)")


class File(NodeMixin):
    def __init__(self, name, size, parent=None):
        self.name = name
        self.parent = parent
        self.size = size


class Directory(NodeMixin):
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent

    @property
    def size(self):
        return sum([child.size for child in self.children])

    def get_directories(self):
        return [node for node in self.descendants if isinstance(node, Directory)]


def create_file_tree(input: str) -> Directory:
    root = Directory("/", parent=None)
    cwd = root

    for line in input.splitlines()[1:]:
        if line.startswith("$ cd "):
            directory = line.split("$ cd ")[1]
            if directory == "..":
                cwd = cwd.parent
            else:
                cwd = Directory(directory, parent=cwd)
        elif file := FILE_REGEX.search(line):
            size, name = file.groups()
            File(name=name, size=int(size), parent=cwd)

    return root


def part_1(input: str) -> int:
    root = create_file_tree(input)

    return sum([dir.size for dir in root.get_directories() if dir.size <= 100000])


def part_2(input: str) -> int:
    DISK_SPACE = 70000000
    REQUIRED_FREE_SPACE = 30000000

    root = create_file_tree(input)

    current_free_space = DISK_SPACE - root.size
    missing_free_space = REQUIRED_FREE_SPACE - current_free_space

    dirs = root.get_directories()
    return min([dir.size for dir in dirs if dir.size >= missing_free_space])
