"""
Single among pairs
########################################################################################################################
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
########################################################################################################################
Example 1:
    Input:  nums = [2,2,1]
    Output: 1

Example 2:
    Input:  nums = [4,1,2,1,2]
    Output: 4

Example 3:
    Input:  nums = [1]
    Output: 1
"""
import os


########################################################################################################################
# Brute Force Solution
# Approach:
#   [1] For each element in the arr, Loop over the array and count its frequency
#   [2] If frequency == 1, return 
# Time Complexity:  O( n^2 )
# Space Complexity: O( 1 )
########################################################################################################################
def get_single_number_BF(arr):
    n = len(arr)
    for i in range(n):
        num = arr[i]
        count = 0
        for j in range(n):
            if arr[j] == num:
                count += 1
        if count == 1:
            return arr[i]
    return None


########################################################################################################################
# Better Solution 1
# Approach:
#   [1] Track the frequency of each element in a list
#   [2] Return element where frequency is 1
#   [3] The list approach doesn't work if list has '-'ev numbers --> use hash map
# Time Complexity:  O( 2n+k )
# Space Complexity: O( k+1 )
########################################################################################################################
def get_single_number_BTR1(arr):
    n = len(arr)

    maxi = float('-inf')
    for i in range(n):                  # O(n)
        maxi = max(maxi, arr[i])
    
    freq_list = [0] * (maxi+1)
    for i in range(n):                  # O(n)
        freq_list[ arr[i] ] += 1
    
    for i in range(maxi+1):             # O(k)
        if freq_list[i] == 1:
            return i
    
    return None


########################################################################################################################
# Better Solution 2
# Approach:
#   [1] Track the frequency of each element in a hashmap
#   [2] Iterate over the hashmap, Return key where value is 1
# Time Complexity:  O( 3/2n+1 )
# Space Complexity: O( n/2+1 )
########################################################################################################################
def get_single_number_BTR2(arr):
    n = len(arr)
    
    freq_map = {}
    for i in range(0, n):                                   # O(n)
        freq_map[ arr[i] ] = freq_map.get(arr[i], 0) + 1
    
    for k, v in freq_map.items():                           # O(n/2+1)
        if v == 1:
            return k
    
    return None


########################################################################################################################
# Optimal Solution
# Approach:
#   [1] XOR the elements of the array
# Time Complexity:  O( n )
# Space Complexity: O( 1 )
########################################################################################################################
def get_single_number_OPT(arr):
    n = len(arr)
    xor = 0
    for i in range(0, n):
        xor ^= arr[i]
    return xor


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')

    arr1 = [9]
    arr2 = [2,2,1]
    arr3 = [4,1,2,1,2]
    print(f'\t\t{arr1}\t|\t{arr2}\t|\t{arr3}')

    print(f'Brute Force:\t{get_single_number_BF(arr1)}\t|\t{get_single_number_BF(arr2)}\t\t|\t{get_single_number_BF(arr3)}')
    print(f'Better 1:\t{get_single_number_BTR1(arr1)}\t|\t{get_single_number_BTR1(arr2)}\t\t|\t{get_single_number_BTR1(arr3)}')
    print(f'Better 2:\t{get_single_number_BTR2(arr1)}\t|\t{get_single_number_BTR2(arr2)}\t\t|\t{get_single_number_BTR2(arr3)}')
    print(f'Optimal:\t{get_single_number_OPT(arr1)}\t|\t{get_single_number_OPT(arr2)}\t\t|\t{get_single_number_OPT(arr3)}')
