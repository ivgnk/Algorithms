"""
Write a function called sumIntervals/sum_intervals() that accepts an array of intervals, and returns the sum of all the interval lengths.
Overlapping intervals should only be counted once.
апишите функцию с именем sumIntervals, которая принимает массив интервалов и возвращает сумму всех длин интервалов.
Перекрывающиеся интервалы следует считать только один раз.

Intervals are represented by a pair of integers in the form of an array.
The first value of the interval will always be less than the second value.
Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.

Overlapping Intervals
List containing overlapping intervals:

[  [1,4],   [7, 10],   [3, 5]  ]
The sum of the lengths of these intervals is 7.
Since [1, 4] and [3, 5] overlap, we can treat the interval as [1, 5], which has a length of 4.

Examples:
sumIntervals( [   [1,2],   [6, 10],   [11, 15] ] ); // => 9
sumIntervals( [   [1,4],   [7, 10],   [3, 5] ] ); // => 7
sumIntervals( [[1,5], [10, 20], [1, 6], [16, 19], [5, 11]] ); // => 19
"""
import numpy as np

def sum_of_intervals(intervals):
    llen = len(intervals)
    # for i in range(llen):   print(intervals[i][0],'  ',intervals[i][1])
    print(llen)
    nnn = np.empty(shape=3, dtype=object)
    np_arr = np.array(intervals)
    for i in range(llen):
        n1 = np.arange(start=intervals[i][0], stop = intervals[i][1]+1, step = 1, dtype=int)
        nnn[i] = n1
    # # for int_ in intervals:
    # #    r1 = np.array(int_)
    print(np_arr)
    print(nnn)
    # return llen

intervals =  [ [1,2], [6, 10], [11, 15] ]
print(sum_of_intervals(intervals))
