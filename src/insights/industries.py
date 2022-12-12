from typing import List, Dict
from .jobs import read


def get_unique_industries(path: str) -> List[str]:
    dataFromCsv = read(path)
    set_job_type = set()
    for data in dataFromCsv:
        if data["industry"] != "":
            set_job_type.add(data["industry"])
    orderList = list(set_job_type)
    return orderList


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    industry_types = [job for job in jobs if job["industry"] == industry]
    return industry_types
