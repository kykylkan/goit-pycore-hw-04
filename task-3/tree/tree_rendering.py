import pathlib
from colorama import Fore

CURRENT_DIR = pathlib.Path(__file__).parent

# fill empty space with some symbol by depth level
TREE_SPACER = "-"

# >= 1 - print with max depth; 0 - print current dir name; -1 - all levels;
TREE_MAX_LEVEL_DEPTH = -1


# print file or dir name with a spacer
def print_item_info(path: pathlib.Path, level: int = 0):
    # get a color based on path type
    color = Fore.BLUE if path.is_dir() else Fore.YELLOW

    # generate spacer based on level
    lines = [TREE_SPACER for x in range(level)]

    # it was tryig...bad it does'nt work correctly
    # msg = color + f"{path.name:{TREE_SPACER}>{level}}" + Fore.RESET

    msg = color + "".join(lines) + path.name + Fore.RESET
    print(msg)


def get_files_list(dir: pathlib.Path, level: int = 1) -> None:

    # check depth level condition
    if TREE_MAX_LEVEL_DEPTH == 0 or (
        TREE_MAX_LEVEL_DEPTH > -1 and level > TREE_MAX_LEVEL_DEPTH
    ):
        return

    # recursive iteraction
    for path in dir.iterdir():
        print_item_info(path, level)

        if path.is_dir():
            res = get_files_list(path, level + 1)


def render_tree(dir_path: str, spacer: str = "-", max_level: int = -1) -> None:
    dir = pathlib.Path(dir_path)

    if not dir.is_dir():
        print("It is not a dir!")
        return

    global TREE_SPACER, TREE_MAX_LEVEL_DEPTH

    TREE_SPACER = spacer

    try:
        # set correct level even with wrong value
        TREE_MAX_LEVEL_DEPTH = int(max_level)
        TREE_MAX_LEVEL_DEPTH = -1 if TREE_MAX_LEVEL_DEPTH < -1 else TREE_MAX_LEVEL_DEPTH
    except:
        print("Level is wrong! Will be used default -1 for max depth")

    # print current dir name
    print_item_info(dir)

    # render the tree
    get_files_list(dir)
