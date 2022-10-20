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
        with open('src/jobs.csv', encoding='utf-8') as file:
            jobs = csv.DictReader(file, delimiter=',', quotechar='"')
    except FileNotFoundError:
        print('Arquivo não encontrado!')
    return [jobs]
