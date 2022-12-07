from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf-8") as f:
        fileDataReader = csv.DictReader(f, delimiter=",", quotechar='"')
        return list(fileDataReader)


def get_unique_job_types(path: str) -> List[str]:
    dataFromCsv = read(path)
    set_job_type = set()
    for data in dataFromCsv:
        set_job_type.add(data["job_type"])
    orderList = list(set_job_type)
    return orderList


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
