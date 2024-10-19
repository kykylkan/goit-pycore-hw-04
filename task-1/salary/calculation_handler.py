from .data_loading import load_data, prepare_data


# avg salary amount
def calc_avg_salary(salaries: list[int]) -> int:
    return round(sum(salaries) / len(salaries))


# total salary amount
def calc_total_salary(salaries: list[int]) -> int:
    return sum(salaries)


# get total salary as a tuple
def total_salary(file_path: str) -> tuple[int]:
    file_data = load_data(file_path)
    employees = prepare_data(file_data)
    salaries = []

    for person in employees:
        try:
            amount = int(person.split(",").pop())
            salaries.append(amount)
        except Exception:
            # if we ahve any error with data, we will skip the person.
            # p.s. we can set default 0 for a sallary but I think in this case it is not good
            pass

    result = (
        (calc_total_salary(salaries), calc_avg_salary(salaries))
        if len(salaries)
        else (0, 0)
    )

    return result
