import os
from datetime import datetime
from second_task import logger_2

# 3 Применить написанный логгер к приложению из любого предыдущего д/з.

# ДЗ по итераторам (п.1)

class FlatIterator:
    def __init__(self, list_of_lists):
        self.flat_list = []
        self.flatten(list_of_lists)

    def flatten(self, lst):
        for item in lst:
            if type(item) == list:
                self.flatten(item)
            else:
                self.flat_list.append(item)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.flat_list):
            item = self.flat_list[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration


def test_3():
    @logger_2('log_iter.log')
    def list_of_lists(lol):
        return FlatIterator(lol).flat_list

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    flat_list = list_of_lists(list_of_lists_1)


if __name__ == '__main__':
    test_3()
