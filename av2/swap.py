def swap(lista):
    return [(item2, item1) for item1, item2 in lista]


if __name__ == '__main__':
    print(swap([('a', 1), ('b', 2), ('c', 3)]))
