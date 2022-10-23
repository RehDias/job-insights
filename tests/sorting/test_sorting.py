import pytest
from src.sorting import sort_by

result_min = [
  {'title': 'Web developer', 'min_salary': '0', 'max_salary': '0'},
  {'title': 'Back end developer', 'min_salary': '0', 'max_salary': '3000'},
  {'title': 'Front end developer', 'min_salary': '1000', 'max_salary': '0'},
  {'title': 'Full stack end developer', 'min_salary': '4000',
      'max_salary': '8000'},
  ]
result_max = [
  {'title': 'Full stack end developer', 'min_salary': '4000',
      'max_salary': '8000'},
  {'title': 'Back end developer', 'min_salary': '0', 'max_salary': '3000'},
  {'title': 'Web developer', 'min_salary': '0', 'max_salary': '0'},
  {'title': 'Front end developer', 'min_salary': '1000', 'max_salary': '0'},
  ]
jobs = [
  {'title': 'Web developer', 'min_salary': '0', 'max_salary': '0'},
  {'title': 'Front end developer', 'min_salary': '1000', 'max_salary': '0'},
  {'title': 'Back end developer', 'min_salary': '0', 'max_salary': '3000'},
  {'title': 'Full stack end developer', 'min_salary': '4000',
      'max_salary': '8000'},
]


def test_sort_by_criteria():
    sort_by(jobs, 'min_salary')
    assert jobs == result_min
    sort_by(jobs, 'max_salary')
    assert jobs == result_max
    with pytest.raises(
      ValueError, match='invalid sorting criteria: wrong_criteria'
      ):
        sort_by(jobs, 'wrong_criteria')
