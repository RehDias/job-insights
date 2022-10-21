from src.counter import count_ocurrences


def test_counter():
    count_developer = count_ocurrences('tests/mocks/jobs.csv', 'Developer')
    count_full_time = count_ocurrences('tests/mocks/jobs.csv', 'full Time')
    assert count_developer == 3
    assert count_full_time == 2
