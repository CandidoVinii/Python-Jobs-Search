from typing import Union, List, Dict
from .jobs import read


def get_max_salary(path: str) -> int:
    dataFromCsv = read(path)
    max_salary = []
    for data in dataFromCsv:
        if data["max_salary"] != "" and data["max_salary"].isdigit():
            max_salary.append(int(data["max_salary"]))
    return max(max_salary)


def get_min_salary(path: str) -> int:
    dataFromCsv = read(path)
    min_salary = []
    for data in dataFromCsv:
        if data["min_salary"] != "" and data["min_salary"].isdigit():
            min_salary.append(int(data["min_salary"]))
    return min(min_salary)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if (
        "max_salary" not in job
        or "min_salary" not in job
        or not str(job["max_salary"]).isdigit()
        or not str(job["min_salary"]).isdigit()
    ):
        raise ValueError
    elif int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError
    elif not str(salary).isnumeric() and type(salary) != int:
        raise ValueError
    elif int(salary) >= int(job["min_salary"]) and int(salary) <= int(
            job["max_salary"]
    ):
        return True
    else:
        return False


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    list_jobs_found = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                list_jobs_found.append(job)
        except ValueError:
            print("Invalid data, try again later...")
    return list_jobs_found
