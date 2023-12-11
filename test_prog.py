import pytest
from prog import Compare


@pytest.fixture
def list1():
    return [1, 2, 3, 4, 5]


@pytest.fixture
def list2():
    return [2, 3, 4, 5, 6]


# Проверка инициализации списка 1
def test_init_lst_1():
    assert Compare([1, 2, 3], [5, 6, 7]).lst1 == [1, 2, 3], 'fail'


# Проверка инициализации списка 2
def test_init_lst_2():
    assert Compare([1, 2, 3], [5, 6, 7]).lst2 == [5, 6, 8], 'fail'


# Проверяем выпадение ошибки, если в спике есть не int
def test_not_int():
    with pytest.raises(ValueError):
        assert Compare([2, 3, 4, 5, 6], [2, 3, 4, 5, 'g']).get_average([2, 3, 4, 5, 'g'])


# Проверяем возврат нулего значения, если передан пустой список
def test_empty_list():
    assert Compare([], []).get_average([]) == 0.0, 'test failed'


# Проверяем правильность вычисления среднего арифметического
def test_get_averages(list1, list2):
    assert Compare(list1, list2).get_average(list1) == 3, 'fail'


# Проверяем когда среднее значение первого списка больше второго
def test_first_average_more(list1, list2):
    assert Compare(list2, list1).compare_lists() == 'Первый список имеет большее среднее значение', 'fail'


# Проверяем когда среднее значение второго списка больше первого
def test_second_average_more(list1, list2):
    assert Compare(list1, list2).compare_lists() == 'Второй список имеет большее среднее значение', 'fail'


# Проверяем когда средние значения списков равны
def test_equal_averages(list1):
    assert Compare(list1, list1).compare_lists() == 'Средние значения равны', 'fail'
