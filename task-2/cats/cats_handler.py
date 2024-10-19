from .data_loading import load_data, prepare_data


def get_cats_info(file_path: str) -> list[dict]:
    file_data = load_data(file_path)
    employees = prepare_data(file_data)
    cats = []
    # keys = ["id", "name", "age"]

    for person in employees:
        try:
            id, name, age = person.split(",")
            cat = {
                'id': id.strip(),
                'name': name.strip(),
                'age': int(age.strip() or 0)
            }

            # can be like that, but it is more complex for reading
            # cat = dict(zip(keys, [id.strip(), name.strip(), int(age.strip())]))

            cats.append(cat)
        except Exception as e:
            print(e)

    return cats
