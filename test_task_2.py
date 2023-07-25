from task_2 import get_most_populars
import pytest

def test_get_most_populars():
    result = get_most_populars()
    expected = 'Александр: 10 раз(а), Евгений: 5 раз(а), Максим: 4 раз(а)'
    assert result == expected