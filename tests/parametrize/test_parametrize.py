import pytest


@pytest.mark.skip #Пропуск теста
def test_another():
    assert 1 == 1


@pytest.mark.parametrize("first_value, second_value, result", [
     (10, 5, 2),
     (-10, -2, 5),
     (-22, 11, -2)
])
def test_calculation(first_value, second_value, result):
     assert first_value / second_value == result


@pytest.mark.parametrize("first_value, second_value, error", [
    (10, 0, ZeroDivisionError),
    (21, '3', TypeError)
])
def test_calculate_error(first_value, second_value, error):
    with pytest.raises(error):
        first_value / second_value