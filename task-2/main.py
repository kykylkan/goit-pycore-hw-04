import pathlib
from cats import get_cats_info

# set path to the file here in showers
SALARY_FILE = pathlib.Path("./data.txt")

CURRENT_DIR = pathlib.Path(__file__).parent


def main():
    # fix file path if it is necessary
    file_path = (
        SALARY_FILE if pathlib.Path.is_file(SALARY_FILE) else CURRENT_DIR / SALARY_FILE
    )

    cats = get_cats_info(file_path)
    print(cats)

if __name__ == "__main__":
    main()
