from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    jobs = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    for job in jobs:
        assert job.keys() == {'title', 'salary', 'type'}
        assert job.keys() is not {'titulo', 'salario', 'tipo'}
