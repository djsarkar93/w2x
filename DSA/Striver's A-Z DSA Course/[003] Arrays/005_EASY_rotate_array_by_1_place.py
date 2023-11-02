"""
Left / Right Rotate array by 1 place
"""
import os


########################################################################################################################
# Optimal Solution
# Approach: 
#   [1] Copy left / right most element to TMP
#   [2] Loop from 1 to (n-1)    |   from (n-2) to 0
#   [3]     Move current element left / right
#   [4] Copy TMP to last / first position
# Time Complexity:  O( n )
# Space Complexity: O( 1 )
########################################################################################################################
def left_rotate(arr):
    n = len(arr)
    tmp = arr[0]
    for i in range(1, n):
        arr[i-1] = arr[i]
    arr[i] = tmp


def right_rotate(arr):
    n = len(arr)
    tmp = arr[n-1]
    for i in range(n-2, -1, -1):
        arr[i+1] = arr[i]
    arr[i] = tmp


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')

    arr = [1,2,3,4,5]
    print(f'Original = {arr}')

    left_rotate(arr)
    print(f'Left Rotated = {arr}')

    arr = [1,2,3,4,5]
    right_rotate(arr)
    print(f'Right Rotated = {arr}')
