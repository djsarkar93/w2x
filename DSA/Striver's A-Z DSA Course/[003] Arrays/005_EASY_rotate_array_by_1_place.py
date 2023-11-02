"""
Left / Right Rotate array by 1 place
"""
import os


########################################################################################################################
# Brute Force Solution
# Approach: 
#   [1] Copy left / right most element to TMP
#   [2] Loop from 1 to (n-1)    |   from (n-2) to 0
#   [3]     Move current element left / right
#   [4] Copy TMP to last / first position
# Time Complexity:  O( n )
# Space Complexity: O( 1 )
########################################################################################################################
def rotate_left_BF(arr):
    n = len(arr)
    tmp = arr[0]
    for i in range(1, n):
        arr[i-1] = arr[i]
    arr[i] = tmp


def rotate_right_BF(arr):
    n = len(arr)
    tmp = arr[n-1]
    for i in range(n-2, -1, -1):
        arr[i+1] = arr[i]
    arr[i] = tmp


########################################################################################################################
# Optimal Solution
# Approach: 
#   [1] Let, rotate d=1 elements
#   [2] Reverse index 0 to d-1  |   index 0 to (n-1)-d
#   [3] Reverse index d to n-1  |   index n-d to n-1
#   [4] Reverse index 0 to n-1
# Time Complexity:  O( n )
# Space Complexity: O( 1 )
########################################################################################################################
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def rotate_left_OPT(arr, d=1):
    n = len(arr)
    reverse(arr, start = 0, end = d-1)
    reverse(arr, start = d, end = n-1)
    reverse(arr, start = 0, end = n-1)


def rotate_right_OPT(arr, d=1):
    n = len(arr)
    reverse(arr, start = 0, end = n-1-d)
    reverse(arr, start = n-d, end = n-1)
    reverse(arr, start = 0, end = n-1)


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')

    arr = [1,2,3,4,5]
    print(f'Original = {arr}')
    
    rotate_left_BF(arr)
    print(f'Left Rotated = {arr}')
    
    arr = [1,2,3,4,5]
    rotate_right_BF(arr)
    print(f'Right Rotated = {arr}')


    arr = [1,2,3,4,5]
    print(f'Original = {arr}')

    rotate_left_OPT(arr)
    print(f'Left Rotated = {arr}')

    arr = [1,2,3,4,5]
    rotate_right_OPT(arr)
    print(f'Right Rotated = {arr}')
