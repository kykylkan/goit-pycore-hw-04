import pathlib
from salary import total_salary

# set path to the file here in showers
SALARY_FILE = pathlib.Path("data.txt")

CURRENT_DIR = pathlib.Path(__file__).parent


def main():
    # fix file path if it is necessary
    file_path = (
        SALARY_FILE if pathlib.Path.is_file(SALARY_FILE) else CURRENT_DIR / SALARY_FILE
    )

    total, average = total_salary(file_path)

    print(f"Total salary: {total}\nAverage salary: {average}")


if __name__ == "__main__":
    main()
