"""
https://www.codewars.com/kata/551f23362ff852e2ab000037/train/python
 /3/
  \7\ 4
 2 \4\ 6
8 5 \9\ 3
Let's say that the 'slide down' is the maximum sum of consecutive numbers from the top to the bottom of the pyramid.
As you can see, the longest 'slide down' is 3   7   4   9 = 23  Your task is to write a function

Допустим, «скольжение вниз» - это максимальная сумма последовательных чисел сверху вниз пирамиды.
Как видите, самый длинный слайд вниз - 3 7 4 9 = 23. Ваша задача написать функцию
"""
def longest_slide_down(pyramid):
    curri = 0 # номер строки
    currN = 0 # номер элемента в строке
    sum = pyramid[curri][currN]
    print()
    llen = len(pyramid)
    while curri < llen-1:
        curri = curri + 1
        currN1 = currN+1
        if currN1 < llen-1:
            if pyramid[curri][currN] > pyramid[curri][currN1]:
                sum = sum + pyramid[curri][currN]
            else:
                sum = sum + pyramid[curri][currN1]
                currN = currN1
        else:
            sum = sum + pyramid[curri][currN]
        print(curri,sum)
    return sum

dat2 = [
            [75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20,  4, 82, 47, 65],
            [19,  1, 23, 75,  3, 34],
            [88,  2, 77, 73,  7, 63, 67],
            [99, 65,  4, 28,  6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
            ] # 1074
dat = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]  # 23

print(longest_slide_down (dat2))