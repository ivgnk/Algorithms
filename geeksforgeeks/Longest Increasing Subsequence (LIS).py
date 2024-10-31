"""
https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/

Given an array arr[] of size N, the task is to find the length
of the Longest Increasing Subsequence (LIS) i.e.,
the longest possible subsequence in which the elements
of the subsequence are sorted in increasing order.

Examples:

Input: arr[] = {3, 10, 2, 1, 20}
Output: 3
Explanation: The longest increasing subsequence is 3, 10, 20

Input: arr[] = {30, 20, 10}
Output:1
Explanation: The longest increasing subsequences are {30}, {20} and (10)


Input: arr[] = {2, 2, 2}
Output: 1
Explanation:  We consider only strictly increasing.


Input: arr[] = {10, 20, 35, 80}
Output: 4
Explanation: The whole array is sorted

Using Recursion – Exponential Time and Linear Space
Using Memoization – O(n^2) Time and O(n) Space
Using Bottom Up Tabulation – O(n^2) Time and O(n) Space
Using Binary Search – O(n Log n) Time and O(n) Space
Related Articles :

also algo
https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
https://en.wikipedia.org/wiki/Longest_increasing_subsequence
"""

from icecream import ic
# Longest Increasing Subsequence Size
def LIS_Bottom_Up_Tabulation(arr):
    n = len(arr)
    # Declare the list (array) for LIS and
    # initialize LIS values for all indexes
    lis = [1] * n

    # Compute optimized LIS values in bottom
    # -up manner
    for i in range(1, n):
        for prev in range(0, i):
            if arr[i] > arr[prev]:
                lis[i] = max(lis[i], lis[prev] + 1)

    # Return the maximum of all LIS values
    return max(lis)

# Longest Decreasing Subsequence Size
def LDS_Bottom_Up_Tabulation(arr):
    n = len(arr)
    lds = [1] * n

    for i in range(1, n):
        for prev in range(0, i):
            if arr[i] < arr[prev]:
                lds[i] = max(lds[i], lds[prev] + 1)
    # Return the maximum of all LIS values
    return max(lds)


if __name__ == '__main__':
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    ic(arr)
    ic(LIS_Bottom_Up_Tabulation(arr))
    ic(arr)
    arr = [10, 20, 30, 40, 50, 60, 70, 80]
    ic(LIS_Bottom_Up_Tabulation(arr))
    arr = [10, 20, 30, 40, 50, 60, 70, 80]
    ic(arr)
    ic(LDS_Bottom_Up_Tabulation(arr))
    arr = list(reversed(arr))
    ic(arr)
    ic(LDS_Bottom_Up_Tabulation(arr))
    ic(arr)
    ic(LIS_Bottom_Up_Tabulation(arr))
