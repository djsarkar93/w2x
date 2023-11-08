"""
Longest subarray with sum K
########################################################################################################################
Given an array and a sum k, we need to print the length of the longest subarray that sums to k.
Note:
    The array has only positive numbers
########################################################################################################################
Example 1:
    Input:          array = {2,3,5}, k = 5
    Result:         2
    Explanation:    The longest subarray with sum 5 is {2, 3}. And its length is 2.

Example 2:
    Input Format:   array = {2,3,5,1,9}, k = 10
    Result:         3
    Explanation:    The longest subarray with sum 10 is {2, 3, 5}. And its length is 3.
"""
import os
from re import L


########################################################################################################################
# Brute Force Solution
# Approach:
#   [1] Compute the sum of all contigous subarrays.
#   [2] If sum = k, maxLen = max(maxLen, len(subarrays))
# Time Complexity:  O( n^2 )
# Space Complexity: O( 1 )
########################################################################################################################
def get_longest_subarray_BF(arr, k):
    n = len(arr)

    max_len = 0
    for i in range(0, n):
        running_sum = 0

        for j in range(i, n):
            running_sum += arr[j]

            if running_sum == k:
                curr_len = j - i + 1
                max_len = max(max_len, curr_len)
    
    return max_len


########################################################################################################################
# Better Solution
# Approach:
#   [1] Loop i from 0 to n
#   [2] compute running sum upto i
#   [3] If running_sum == k, update max_len. Else, do nothing.
#   [4] If (running_sum - k) in running sum hash_map, update max_len. Else, do nothing.
#   [4] If current running_sum not in running sum hash_map, add. Else, do nothing.
# Time Complexity:  O( n )
# Space Complexity: O( n )
########################################################################################################################
def get_longest_subarray_BTR(arr, k):
    n = len(arr)
    max_len = 0
    running_sum = 0
    pre_sum_map = {}
    for i in range(0, n):
        running_sum += arr[i]

        if running_sum == k:
            curr_len = i+1
            max_len = max(max_len, curr_len)
        
        rem = running_sum - k

        if rem in pre_sum_map:                  
            curr_len = i - pre_sum_map[rem]
            max_len = max(max_len, curr_len)
            
        if running_sum not in pre_sum_map:
            pre_sum_map[running_sum] = i
    
    return max_len


########################################################################################################################
# Optimal Solution
# Note: Only if array element are >= 0
# Approach:
#   [1] 2 pointer and greedy approach
# Time Complexity:  O( 2n )
# Space Complexity: O( 1 )
########################################################################################################################
def get_longest_subarray_OPT(arr, k):
    n = len(arr)
    max_len = 0
    subarr_sum = 0
    left = right = 0
    while right < n:
        subarr_sum += arr[right]

        while subarr_sum > k and left <= right:
            subarr_sum -= arr[left]
            left += 1
        
        if subarr_sum == k:
            cur_len = right - left + 1
            max_len = max(max_len, cur_len)
        
        right += 1
    return max_len


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')

    arr = [1,2,3,1,1,1,1,3,3]
    k = 3
    print(f'Array: {arr}, k: {k}')

    rslt = get_longest_subarray_BF(arr, k)
    print(f'Brute Force: {rslt}')

    rslt = get_longest_subarray_BTR(arr, k)
    print(f'Better: {rslt}')

    rslt = get_longest_subarray_OPT(arr, k)
    print(f'Optimal: {rslt}')
