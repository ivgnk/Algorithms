"""
Тестирование работы с numpy + random
"""
import numpy as np
import random
import numba
import datetime

def numpy_test1():
    """
    Запишем в массив числа и строки
    """
    d = np.array((10,20,'test'))
    print(d[0])
    print(d[1])
    print(d[2])
    c = set((3, 4, 2 ,0 ,1))
    print(c)


def test_numpy_test(f) -> None:
    starttme = datetime.datetime.now()
    f()
    print('Время выполнения = ', datetime.datetime.now()-starttme)



# @numba.njit
def numpy_test2():
    """
    Операции с массивами
    Optimize your code using profilers
    https://www.jetbrains.com/help/pycharm/profiler.html
    """
    # random.random.seed()
    n:int = 100000
    c = np.zeros(n)
    d = np.zeros(n)
    for i in range(n):
        c[i] = random.random()
        d[i] = random.random()
    e = c+d
    e1:float = e.sum()
    c1:float = c.sum()
    d1:float = d.sum()
    ff:float = c1 + d1
    print('e1 = ',e1,'ff = ', ff)
