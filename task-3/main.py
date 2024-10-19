import sys
from tree import render_tree

def main():
    _, dir_path = sys.argv

    # render the tree of directory
    render_tree(dir_path)


if __name__ == "__main__":
    main()
