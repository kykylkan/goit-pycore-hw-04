# load file data
def load_data(file_name: str) -> list[str]:
    file_data = []

    try:
        with open(file_name, "r") as file:
            file_data = file.readlines()
    except FileNotFoundError:
        print("File not found.")
    except Exception:
        print("Uknown error.")

    return file_data


# get none empty records
def prepare_data(lines: list[str]) -> list[str]:
    return [line.strip() for line in lines if line.strip()]
