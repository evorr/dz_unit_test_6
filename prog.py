class Compare:
    def __init__(self, lst1, lst2):
        self.lst1 = lst1
        self.lst2 = lst2

    def get_average(self, lst: list[int]):
        for item in lst:
            if not isinstance(item, int):
                raise ValueError(f' {item} not int')
        if len(lst):
            return sum(lst) / len(lst)
        return 0.0

    def compare_lists(self) -> str:
        average_list1 = self.get_average(self.lst1)
        average_list2 = self.get_average(self.lst2)
        if average_list1 > average_list2:
            return 'Первый список имеет большее среднее значение'
        elif average_list1 < average_list2:
            return 'Второй список имеет большее среднее значение'
        else:
            return 'Средние значения равны'