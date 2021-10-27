"""
Your task is to make a function that can take any non-negative integer as an argument
and return it with its digits in descending order.
Essentially, rearrange the digits to create the highest possible number.

Ваша задача - создать функцию, которая может принимать любое неотрицательное целое число в качестве аргумента
и возвращать его с цифрами в порядке убывания.
По сути, переставьте цифры, чтобы получить максимально возможное число.

Examples:
Input: 42145 Output: 54421
Input: 145263 Output: 654321
Input: 123456789 Output: 987654321
"""
# Сортировка списка
# https://pythonim.ru/list/metod-sort-python)
def descending_order(num):
    s = str(num)
    n = len(s)
    llist = []
    for i in range(n):
        # print(s[i])
        llist.append(s[i])
    llist.sort(reverse=True)
    # print(llist)
    s2="".join(llist)
    # print(s2)
    int_ = int(s2)
    # print(type(int_))
    return int_

print(descending_order(42145))