"""
Fundamentals
Task 01 from codewars.com

Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
For example:
summation(2) -> 3
1 + 2
summation(8) -> 36
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
"""

def summation(num):
    sum = 0
    for i in range(1,num+1):
        sum = sum+i
    return sum

print(summation(3))