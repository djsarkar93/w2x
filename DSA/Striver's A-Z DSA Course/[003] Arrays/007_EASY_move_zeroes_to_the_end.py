"""
Moves zeroes to the end
########################################################################################################################
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note: that you must do this in-place without making a copy of the array.
########################################################################################################################
Example 1:
    Input:  nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]

Example 2:
    Input:  nums = [0]
    Output: [0]
"""
import os


########################################################################################################################
# Brute Force Solution
# Approach: 
#   [1] Loop over arr             --> copy non-zero elements to TMP
#   [2] Loop over TMP             --> arr[i] = tmp_arr[i]
#   [3] Loop from len(TMP) to n-1 --> arr[i] = 0
# Time Complexity:  O( 2n )
# Space Complexity: O( n )
########################################################################################################################
def remove_zeroes_BF(arr):
    n = len(arr)

    tmp_arr = []
    for i in range(0, n):
        if arr[i] != 0:
           tmp_arr.append(arr[i])

    for i in range(len(tmp_arr)):
        arr[i] = tmp_arr[i]
    
    for i in range(len(tmp_arr), n):
        arr[i] = 0


########################################################################################################################
# Optimal Solution
# Approach: 
#   [1] Loop over arr        --> When first 0 is found, j = i & break. Else, return
#   [2] Loop from j+1 to n-1 --> If arr[i] is non-zero, SWAP(arr[j], arr[i]) & j++. Else, do nothing
# Time Complexity:  O( n )
# Space Complexity: O( 1 )
########################################################################################################################
def remove_zeroes_OPT(arr):
    n = len(arr)

    j = -1
    for i in range(0, n):
        if arr[i] == 0:
            j = i
            break
    else:
        return 
    
    for i in range(j+1, n):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')

    arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
    print(f'Original = {arr}')

    remove_zeroes_BF(arr)
    print(f'Brute Force = {arr}')

    arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
    remove_zeroes_OPT(arr)
    print(f'Optimal = {arr}')
