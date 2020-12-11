"""
Тестирование вывода данных
"""
import sys

def create_empty_data_structures() -> None:
    """
    Создаение пустых стркутур данных
    """
    a = []
    b = ()
    c = dict()
    d = {}
    print(a,b,c,d)
    print(type(a), type(b), type(c), type(d))

def get_data_from_cmdln()-> None:
    """
    Взять данные из командной строки
    """
    i:int
    arr = sys.argv[:]
    print('\nПервый вывод')
    for a in arr:
        print(a)

    print('\nВторой вывод')
    for i in range(len(arr)):
        print(i,arr[i])
