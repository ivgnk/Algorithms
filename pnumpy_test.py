"""
Тестирование работы с numpy
"""
import numpy as np

def numpy_test1():
    d = np.array((10,20,'test'))
    print(d[0])
    print(d[1])
    print(d[2])
    c = set((3, 4, 2 ,0 ,1))
    print(c)