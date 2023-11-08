"""
Longest subarray with sum K
########################################################################################################################
Given an array and a sum k, we need to print the length of the longest subarray that sums to k.
Note:
    The array has both positive & negative numbers
########################################################################################################################
Example 1:
    Input:          array = {2,3,5}, k = 5
    Result:         2
    Explanation:    The longest subarray with sum 5 is {2, 3}. And its length is 2.

Example 2:
    Input Format:   array = {-1, 1, 1}, k = 1
    Result:         3
    Explanation:    The longest subarray with sum 1 is {-1, 1, 1}. And its length is 3.
"""
import os


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
                cur_len = j-i+1
                max_len = max(max_len, cur_len)
    return max_len


########################################################################################################################
# Better Solution
########################################################################################################################
# Does not exist.


########################################################################################################################
# Optimal Solution
# Approach:
#   [1] Loop i from 0 to n
#   [2] compute running sum upto i
#   [3] If running_sum == k, update max_len. Else, do nothing.
#   [4] If (running_sum - k) in running sum hash_map, update max_len. Else, do nothing.
#   [4] If current running_sum not in running sum hash_map, add. Else, do nothing.
# Time Complexity:  O( n )
# Space Complexity: O( n )
########################################################################################################################
def get_longest_subarray_OPT(arr, k):
    n = len(arr)
    max_len = 0
    running_sum = 0
    pre_sum_map = {}
    for i in range(0, n):
        running_sum += arr[i]

        if running_sum == k:
            cur_len = i+1
            max_len = max(max_len, cur_len)
        
        rem = running_sum - k

        if rem in pre_sum_map:
            cur_len = i - pre_sum_map[rem]
            max_len = max(max_len, cur_len)
        
        if running_sum not in pre_sum_map:
            pre_sum_map[running_sum] = i
    return max_len


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')

    arr = [1,2,3,1,1,1,1,3,-3]
    k = 3
    print(f'Array: {arr}, k: {k}')

    rslt = get_longest_subarray_BF(arr, k)
    print(f'Brute Force: {rslt}')

    rslt = get_longest_subarray_OPT(arr, k)
    print(f'Optimal: {rslt}')
