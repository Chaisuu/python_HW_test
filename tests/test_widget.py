import pytest

from src.widget import get_date




@pytest.mark.parametrize("data, expected", [
    ("2018-07-11T02:26:18.671407", "11.07.2018"),
    ("2018-10-14T08:21:33.419441", "14.10.2018"),
    ("2018-09-12T21:27:25.241689", "12.09.2018"),
    ("2018-06-30T02:08:58.425572", "30.06.2018"),
    ("2019-07-03T18:35:29.5123", "03.07.2019")
])
def test_get_date(data, expected):
    assert get_date(data) == expected
