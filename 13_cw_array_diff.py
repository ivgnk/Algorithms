"""
Fundamentals
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
It should remove all values from list a, which are present in list b keeping their order.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]

Ваша цель - реализовать функцию различия, которая вычитает один список из другого и возвращает результат.
Он должен удалить все значения из списка a, которые присутствуют в списке b, сохраняя их порядок.
"""

def array_diff(a, b):
    # Вырожденные случаи
    llenс = len(a)
    c = [True]*llenс
    if (a == []) or (b==[]):
        return a
    else: # основной случай
        la = len(a);  lb = len(b)
        # n = 0 # число различных значений
        for i in range(la):
            for j in range(lb):
                bb = (a[i] == b[j])
                if bb:
                    c[i] = False
                    continue
        for i in range(la-1,-1,-1):
            if not c[i]:
                del a[i]
    return a

# print(array_diff([1, 2], [1]), [2])
print(array_diff([1, 2, 2, 2, 3], [2]), [2])