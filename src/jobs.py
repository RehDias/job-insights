import csv
from functools import lru_cache


@lru_cache
def read(path: str):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """

    try:
        with open(path, mode='r', encoding='utf-8') as file:
            jobs_reader = csv.DictReader(file, delimiter=',', quotechar='"')
            jobs = [row for row in jobs_reader]

    except FileNotFoundError:
        print('Arquivo não encontrado!')
    return jobs
