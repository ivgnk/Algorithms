"""
Fundamentals
Given an array of integers, find the one that appears an odd number of times.
There will always be only one integer that appears an odd number of times.

Дан массив целых чисел, найдите то число, которое встречается нечетное количество раз.
(В массиве целых) всегда будет только одно целое число, которое встречается нечетное количество раз.
Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
"""

numbers = [1, 2, 2, 3, 3, 4, 5]
numbers = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
numbers = [7]
numbers = [0]
numbers = [1,1,2]
numbers = [0,1,0,1,0]
numbers = [1,2,2,3,3,3,4,3,3,3,2,2,1]
numbers = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
numbers = [1,1,2,-2,5,2,4,4,-1,-2,5]


# получить уникальные элементы списка python
# https://pythonru.com/primery/kak-poluchit-unikalnye-jelementy-spiska-python
def get_unique_numbers(numbers):
    list_of_unique_numbers = []
    unique_numbers = set(numbers)
    for number in unique_numbers:
        list_of_unique_numbers.append(number)
    return list_of_unique_numbers

def find_it(seq):
    llist2 = get_unique_numbers(seq)  # получить уникальные элементы списка python
    n = len(llist2)
    llist3 = [0]*n # создать список - счетчик числа элементов, начльные нули
    for lel in seq:
        for i in range(n):
            if lel == llist2[i]:
                llist3[i] = llist3[i] + 1
    # выделяем число, которое встречается нечетное число раз
    # http://python-teach.ru/python-dlya-nachinayushhih/opredelenie-chetnosti-chisla-v-python/
    for i in range(n):
        if (llist3[i] %2 ) != 0:
            res = llist2[i]
    return res

print(get_unique_numbers(numbers))
print(find_it(numbers))

