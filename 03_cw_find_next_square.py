"""
Fundamentals
Task 32 from codewars.com

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter.
Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.

Завершите метод findNextSquare,
который находит следующий целочисленный полный квадрат после переданного в качестве параметра.
Напомним, что полный квадрат - это целое число n такое, что sqrt (n) также является целым числом.
Если параметр сам по себе не является точным квадратом, следует вернуть -1.
Вы можете предположить, что параметр неотрицательный.
"""
import math

def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    dat:float
    if sq>0:
        dat=math.sqrt(sq)
        (fr_, int_) = math.modf(dat)
        print('dat = ', dat)
        print('math.modf = ', fr_, int_)
        if ( abs(fr_)<1e-38 ):
            res = int(int_)+1;
            print(res)
            return res*res
        else:
            return -1
    else:
        return -1


print('find_next_square = ', find_next_square(101))