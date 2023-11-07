"""
Find missing number in an array
########################################################################################################################
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
########################################################################################################################
Example 1:
    Input:          nums = [3,0,1]
    Output:         2
    Explanation:    n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
                    2 is the missing number in the range since it does not appear in nums.

Example 2:
    Input:          nums = [0,1]
    Output:         2
    Explanation:    n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 
                    2 is the missing number in the range since it does not appear in nums.

Example 3:
    Input:          nums = [9,6,4,2,3,5,7,0,1]
    Output:         8
    Explanation:    n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 
                    8 is the missing number in the range since it does not appear in nums.
"""
import os


########################################################################################################################
# Brute Force Solution
# Approach: 
#   [1] Loop i from 0 to n+1
#   [2] Linear search for all i in arr
#   [3] Return i when not found
# Time Complexity:  O( n^2 )
# Space Complexity: O( 1 )
########################################################################################################################
def linear_search(arr, k):
    for i, num in enumerate(arr):
        if num == k:
            return True
    return False


def missing_number_BF(arr):
    n = len(arr)
    for i in range(0, n+1):
        if not linear_search(arr, i):
            return i


########################################################################################################################
# Better Solution
# Approach: 
#   [1] Initialize FREQ = [0] * (n+1)
#   [2] Store the frequency of each number
#   [3] Return index of num whoes frequency is 0
# Time Complexity:  O( 2n )
# Space Complexity: O( n )
########################################################################################################################
def missing_number_BTR(arr):
    n = len(arr)
    freq = [0] * (n+1)
    for i in range(n):
        freq[ arr[i] ] += 1
    for i in range(n+1):
        if freq[i] == 0:
            return i


########################################################################################################################
# Optimal Solution 1
# Approach: 
#   [1] SUM(0 to n) - SUM(arr)
# Time Complexity:  O( n )
# Space Complexity: O( 1 )
########################################################################################################################
def missing_number_OPT1(arr):
    n = len(arr)
    sum_n = (n*(n+1))//2
    sum_arr = 0
    for i in range(n):
        sum_arr += arr[i]
    return sum_n - sum_arr


########################################################################################################################
# Optimal Solution 2
# Approach: 
#   [1] Two important properties of XOR
#       a ^ a = 0
#       0 ^ a = a
#   [2] xor1 = XOR all the numbers in the given array
#   [3] xor2 = XOR all the numbers between 1 to N
#   [4] xor1 ^ xor2
# Time Complexity:  O( n )
# Space Complexity: O( 1 )
########################################################################################################################
def missing_number_OPT2(arr):
    n = len(arr)
    xor1 = xor2 = 0
    for i in range(0, n):
        xor1 ^= arr[i]
        xor2 ^= i
    xor2 ^= n
    return xor1 ^ xor2


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')

    arr1 = [0,1]
    arr2 = [3,0,1]
    arr3 = [9,6,4,2,3,5,7,0,1]
    print(f'\t\t{arr1}\t|\t{arr2}\t|\t{arr3}')

    print(f'Brute Force:\t{missing_number_BF(arr1)}\t|\t{missing_number_BF(arr2)}\t\t|\t{missing_number_BF(arr3)}')
    print(f'Better:\t\t{missing_number_BTR(arr1)}\t|\t{missing_number_BTR(arr2)}\t\t|\t{missing_number_BTR(arr3)}')
    print(f'Optimal 1:\t{missing_number_OPT1(arr1)}\t|\t{missing_number_OPT1(arr2)}\t\t|\t{missing_number_OPT1(arr3)}')
    print(f'Optimal 2:\t{missing_number_OPT2(arr1)}\t|\t{missing_number_OPT2(arr2)}\t\t|\t{missing_number_OPT2(arr3)}')
