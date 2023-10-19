import pytest

from gradescsv import newGrades, mixGrades


# @pytest.fixture
# def get_grades():
#     g = newGrades
#     return g

@pytest.mark.parametrize('input_data', newGrades)
def test_grades(input_data):
    assert input_data['avg'] >= mixGrades[input_data['Grade']]

