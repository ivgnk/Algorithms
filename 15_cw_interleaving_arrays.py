"""
Create a function, that accepts an arbitrary number of arrays and
returns a single array generated by alternately appending elements from the passed in arguments.
If one of them is shorter than the others, the result should be padded with empty elements.

Создайте функцию, которая принимает произвольное количество массивов и
возвращает единственный массив, сгенерированный путем поочередного добавления элементов из переданных аргументов.
Если один из них короче других, результат должен быть дополнен пустыми элементами.

Examples:
interleave([1, 2, 3], ["c", "d", "e"]) == [1, "c", 2, "d", 3, "e"]
interleave([1, 2, 3], [4, 5]) == [1, 4, 2, 5, 3, None]
interleave([1, 2, 3], [4, 5, 6], [7, 8, 9]) == [1, 4, 7, 2, 5, 8, 3, 6, 9]
interleave([]) == []
"""

def interleave(*args):
    # Находим длины списков и максимальную их длину, создаем новый список
    n = len(args)
    maxnlen = -1
    nlen = []
    for llist in args:
        currlen = len(llist)
        nlen.append(currlen)
        maxnlen = max(maxnlen, currlen)
    reslist =[None]*(maxnlen*n)
    # print(maxnlen*n)
    # print(nlen)

    # заполняем новый список
    for n2, l_arg in enumerate(args):
        currii = n2
        for i in range(maxnlen):
            print(currii)
            if i < nlen[n2]:
                reslist[currii] = l_arg[i]
            else:
                reslist[currii] = None
            currii = currii + n
    return reslist

# print(interleave([1, 2, 3], [4, 5, 6], [7, 8, 9]))
# print(interleave([1, 2, 3], [4, 5, 6, 7], [7, 8, 9, 10, 11]))
print(interleave([1, 2, 3], ["c", "d", "e"]))
print(interleave([1, 2, 3], [4, 5]))
print(interleave([]))
