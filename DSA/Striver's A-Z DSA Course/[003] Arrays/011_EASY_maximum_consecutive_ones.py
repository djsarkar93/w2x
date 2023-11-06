"""
Count Maximum Consecutive One’s in the array
########################################################################################################################
Given a binary array nums, return the maximum number of consecutive 1's in the array.
########################################################################################################################
Example 1:
    Input:          nums = [1,1,0,1,1,1]
    Output:         3
    Explanation:    The first two digits or the last three digits are consecutive 1s. 
                    The maximum number of consecutive 1s is 3.

Example 2:
    Input:          nums = [1,0,1,1,0,1]
    Output:         2
"""
import os


def find_max_consecutive_ones(arr):
    n = len(arr)
    maxi = 0
    count = 0
    for i in range(n):
        if arr[i] == 1:
            count += 1
        else:
            count = 0
        maxi = max(maxi, count)
    return maxi


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')

    arr = [1, 1, 0, 1, 1, 1, 0, 1, 1]
    print(f'Original: {arr}')

    print(f'The maximum consecutive 1\'s are: {find_max_consecutive_ones(arr)}')
