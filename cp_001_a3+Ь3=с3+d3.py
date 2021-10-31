"""
2020_Карьера программиста_Макдауэлл.pdf, стр. 64-65
вывести все положительные целочисnенные решения уравнения а 3 + Ь3 = с3 + d3, где а,
Ь, с и d - целые числа в диапазоне от 1 до 1000.
"""
import time
import copy
# определение времени https://pythononline.ru/question/kak-uznat-vremya-vypolneniya-programmy-na-python

# первый вариант, самый простой
def proc1():
    n = 80
    n1 = n + 1
    num = 0
    t0 = time.time()
    for a in range(1,n1,1):
        for b in range(1,n1,1):
            for c in range(1, n1, 1):
                for d in range(1, n1, 1):
                    if a**3 + b**3 == c**3 + d**3:
                        print(a, b, c, d)
                        num = num + 1
    t1 = time.time()
    print('Время работы proc1 = ', t1-t0,'  вариантов =  ', num)
    # proc1 (80) =  Время работы proc1 =  27.35299015045166   вариантов =   12968 из 40 960 000

def proc2():
    n = 80
    n1 = n + 1
    num = 0
    t0 = time.time()
    for a in range(1,n1,1):
        a3 = a**3
        for b in range(1,n1,1):
            b3 = b**3
            a3b3 = a3 + b3
            for c in range(1, n1, 1):
                c3 = c**3
                for d in range(1, n1, 1):
                    if a3b3 == c3 + d**3:
                        print(a, b, c, d)
                        num = num + 1
    t1 = time.time()
    print('Время работы proc2 = ', t1-t0,'  вариантов =  ', num)
    # proc2 (80) =  7.810699462890625   вариантов =   12968 из 40 960 000

def proc3():
    n = 80
    n1 = n + 1
    num = 0
    t0 = time.time()
    dlist = [None]
    for d in range(1, n1, 1):
        dlist.append(d**3)
    print(dlist)

    for a in range(1,n1,1):
        a3 = a**3
        for b in range(1,n1,1):
            b3 = b**3
            a3b3 = a3 + b3
            for c in range(1, n1, 1):
                c3 = c**3
                a3b3c3 = a3b3-c3
                for d in range(1, n1, 1):
                    if a3b3c3  ==  dlist[d]:
                        print(a, b, c, d)
                        num = num + 1
                        break
    t1 = time.time()
    print('Время работы proc3 = ', t1-t0,'  вариантов =  ', num)
    # proc3 (80) =   6.977806329727173   вариантов =   12968 из 40 960 000
    # proc3 (80) =   6.617917060852051   вариантов =   12968 из 40 960 000 - без печать результата
    # proc3 (80) =   1.4058294296264648  вариантов =   12968 из 40 960 000 - с заранее заготовленным dlist

def proc4():
    n = 80
    n1 = n + 1
    num = 0
    t0 = time.time()
    dlist = [None]
    for d in range(1, n1, 1):
        dlist.append(d**3)
    print(dlist)
    alist = copy.deepcopy(dlist)
    blist = copy.deepcopy(dlist)
    clist = copy.deepcopy(dlist)

    # A = [[0] * n1 for i in range(n1)]
    # for a in range(1,n1,1):
    #     for b in range(1,n1,1):
    #         A[a][b] = alist[a] + blist[b]

    for a in range(1,n1,1):
        for b in range(1,n1,1):
            a3b3 = alist[a] + blist[b]
            for c in range(1, n1, 1):
                a3b3c3 = a3b3 - clist[c] # A[a][b]-clist[c]
                for d in range(1, n1, 1):
                    if a3b3c3  ==  dlist[d]:
                        print(a, b, c, d)
                        num = num + 1
                        break
    t1 = time.time()
    print('Время работы proc4 = ', t1-t0,'  вариантов =  ', num)
    # proc3 (80) =   1.2964744567871094   вариантов =   12968 из 40 960 000 - без печать результата

proc4()