"""
Fundamentals
Given an array of integers, find the one that appears an odd number of times.
There will always be only one integer that appears an odd number of times.

Дан массив целых чисел, найдите то число, которое встречается нечетное количество раз.
(В массиве целых неотрицательных) всегда будет только одно целое число, которое встречается нечетное количество раз.
Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
"""

def find_it(seq):
    n = len(seq)
    mmax = max(seq)
    n2 = mmax + 1
    llist=[0]*n2
    # определяем число вхождений каждого числа в последовательность
    for i in range(n):
        for j in range(n2):
            if seq[i] == j:
               llist[j] = llist[j]+1
    # выделяем число, которое встречается нечетное число раз
    # http://python-teach.ru/python-dlya-nachinayushhih/opredelenie-chetnosti-chisla-v-python/
    for j in range(n2):
        if (llist[j] %2 ) != 0:
            res = j
    return res

seq = [7]
seq = [0]
seq = [1,1,2]
seq = [0,1,0,1,0]
seq = [1,2,2,3,3,3,4,3,3,3,2,2,1]
print(find_it(seq))