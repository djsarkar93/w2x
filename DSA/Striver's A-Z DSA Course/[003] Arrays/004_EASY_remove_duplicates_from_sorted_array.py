"""
Remove duplicates from sorted array
########################################################################################################################
Two pointer approach
########################################################################################################################
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
- Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
  The remaining elements of nums are not important as well as the size of nums.
- Return k.
########################################################################################################################
Example 1:
    Input:          nums = [1,1,2]
    Output:         2, nums = [1,2,_]
    Explanation:    Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
                    It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
    Input:          nums = [0,0,1,1,1,2,2,3,3,4]
    Output:         5, nums = [0,1,2,3,4,_,_,_,_,_]
    Explanation:    Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
                    It does not matter what you leave beyond the returned k (hence they are underscores).
"""
import os


########################################################################################################################
# Optimal Solution
# Approach: 
#   [1] Two pointer approach
# Time Complexity:  O( n )
# Space Complexity: O( 1 )
########################################################################################################################
def removeDuplicates(arr):
    n = len(arr)

    i = 0
    for j in range(1, n):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    
    return i + 1


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')

    arr = [0,0,1,1,1,2,2,3,3,4]
    print(f'Array = {arr}')

    k = removeDuplicates(arr)
    print(f'k = {k}')
    print(f'arr = {arr[:k] + ["_"]*(len(arr)-k)}')
