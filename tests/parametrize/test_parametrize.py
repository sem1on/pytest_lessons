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
    """
    Позитивная проверка деления двух чисел
    """
    assert first_value / second_value == result


@pytest.mark.parametrize("first_value, second_value, error", [
    (10, 0, ZeroDivisionError),
    (21, '3', TypeError)
])
def test_calculate_error(first_value, second_value, error):
    """
    Проверка возникновения ошибки при невалидных данных или делении на 0
    """
    with pytest.raises(error):
        first_value / second_value