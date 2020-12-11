"""
Тестирование задач на циклы

Ускорение с Numba
Python (+numba) быстрее Си — серьёзно?! Часть 1. Теория
https://habr.com/ru/post/484136/
Python (+numba) быстрее Си — серьёзно?! Часть 2. Практика
https://habr.com/ru/post/484142/

Numba: A High Performance Python Compiler
https://numba.pydata.org/
Однострочная многократная оптимизация кода на Python с использованием Numba
https://vc.ru/dev/134449-odnostrochnaya-mnogokratnaya-optimizaciya-koda-na-python-s-ispolzovaniem-numba
"""
import numpy as np
from math import pow
import datetime
import numba

@numba.jit(nopython=True)
def eq_a3_b3_c3_d3_v1(n:int) -> int:
    i: int =0; a:int; b:int; c:int; d:int;
    for a in range(n+1):
        a3 = pow(a, 3);
        for b in range(n+1):
            b3 = pow(b, 3);
            a3b3 = a3+b3
            for c in range(n+1):
                c3 = pow(c, 3);
                for d in range(n+1):
                    if a3b3 == c3+pow(d,3):
                        i+=1
                        # print ('%5d  %5d  %5d  %5d  %5d' % (i, a, b, c, d))
    return i

@numba.jit(nopython=True)
def eq_a3_b3_c3_d3_v2(n:int) -> int:
    i: int =0; a:int; b:int; c:int; d:int;
    for a in range(n+1):
        for b in range(n+1):
            for c in range(n+1):
                for d in range(n+1):
                    if ((a==c) and (b==d)) or ((a==d) and (b==c)):
                        i+=1
                        #print ('%5d  %5d  %5d  %5d  %5d' % (i, a, b, c, d))
    return i


def eq_a3_b3_c3_d3():
    """
    найти все положительные целочисленные решения уравнения a^3 + b^3 = c^3 + d^3,
    где a, b, c, d - целые числа между 1 to 1000
    """
    n=100
    #-------- Первый вариант
    starttme = datetime.datetime.now()
    ii = eq_a3_b3_c3_d3_v1(n)
    print('Время выполнения = ', datetime.datetime.now()-starttme)
    print('Число значений= ', ii) # 20661

    # s = # множество для хранения ответов"
    # i : int; j : int
    # dat = np.zero([n,n], dtype=int)
    # словарь множество для хранения ответов"

    # -------- Сокращенный вариант
    starttme = datetime.datetime.now()
    ii = eq_a3_b3_c3_d3_v2(n)
    print('Время выполнения = ', datetime.datetime.now()-starttme)
    print('Число значений= ', ii) # 20301

    #-------- Второй вариант
    # Не понял, посмотреть
    # снова https://fooobar.com/questions/2338979/how-to-find-all-positive-integer-solutions-to-an-cubic-equation
    # starttme = datetime.datetime.now()
    # for a in range(n+1):
    #     a3 = pow(a, 3);
    #     for b in range(n+1):
    #         b3 = pow(b, 3);
    #         a3b3 = a3+b3
    #         for c in range(n+1):
    #             c3 = pow(c, 3);
    #             for d in range(n+1):
    #                 if a3b3 == c3+pow(d,3):
    #                     i+=1
    #                     # print ('%5d  %5d  %5d  %5d  %5d' % (i, a, b, c, d))
    # print('Время выполнения = ', datetime.datetime.now()-starttme)
    # print('Число значений= ',i) # 20661
