from is_leap_year import leap_year_check

def test_is_leap_year_happy():
    assert leap_year_check(2020) == True
    assert leap_year_check(2000) == True
    assert leap_year_check(2024) == True

def test_is_leap_year_unhappy():
    assert leap_year_check(2018) == False
    assert leap_year_check(2022) == False
    assert leap_year_check(2025) == False