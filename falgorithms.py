def reverse_dat(a,b):
    """
    Входные данные: массив numpy
    Выходные данные: обращенный массив numpy
    """

    # a=10; b=20
    # print(a,b)
    # (b, a) = (a, b)
    # print(a,b)

    #  c = b;  b1 = a;   a1 = c
    [b, a] = [a, b]
    return a, b

