nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator:
    def __init__(self, in_list):
        self.stop_iter = False
        self.in_list = in_list
        self.ind_i = 0
        self.ind_j = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stop_iter:
            while self.ind_i < len(self.in_list):
                if self.ind_j < len(self.in_list[self.ind_i]):
                    el = self.in_list[self.ind_i][self.ind_j]
                    self.ind_j += 1
                    return el

                self.ind_i += 1
                self.ind_j = 0
            self.stop_iter = True
        raise StopIteration


print('Задание 1\n')

for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)

print('\nЗадание 2\n')

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]


def flat_generator(some_list):
    for s_list in some_list:
        for el in s_list:
            yield el


for item in flat_generator(nested_list):
    print(item)
