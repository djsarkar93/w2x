"""
Left / Right rotate array by D place
"""
import os


########################################################################################################################
# Brute Force Solution
# Approach: 
#   [1] TMP = arr[0:d)          |   arr[(n-d):n)
#   [2] Loop i from d to (n-1)  |   from (n-d-1) to 0
#   [3]     Move current element +d places left / right
#   [4] Copy TMP to array
# Time Complexity:  O( n+d )
# Space Complexity: O( d )
########################################################################################################################
def rotate_left_BF(arr, d):
    n = len(arr)
    d = d % n

    tmp = []
    for i in range(0, d):           # O(d)
        tmp.append(arr[i])

    for i in range(d, n):           # O(n-d)
        arr[i-d] = arr[i]
    
    i = i-d+1
    for j in range(0, len(tmp)):    # O(d)
        arr[i] = tmp[j]
        i += 1
    

def rotate_right_BF(arr, d):
    n = len(arr)
    d = d % n

    tmp = []
    for i in range(n-d, n):         # O(d)
        tmp.append(arr[i])
    
    for i in range(n-d-1, -1, -1):  # O(n-d)
        arr[i+d] = arr[i]
    
    for i in range(len(tmp)):       # O(d)
        arr[i] = tmp[i]


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


def rotate_left_OPT(arr, d):
    n = len(arr)
    d = d % n
    reverse(arr, start = 0, end = d-1)
    reverse(arr, start = d, end = n-1)
    reverse(arr, start = 0, end = n-1)


def rotate_right_OPT(arr, d):
    n = len(arr)
    d = d % n
    reverse(arr, start = 0, end = n-1-d)
    reverse(arr, start = n-d, end = n-1)
    reverse(arr, start = 0, end = n-1)


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')

    arr = [1,2,3,4,5]
    print(f'Original = {arr}')

    rotate_left_BF(arr, d = 23)
    print(f'Left Rotated = {arr}')

    arr = [1,2,3,4,5]
    rotate_right_BF(arr, d = 23)
    print(f'Right Rotated = {arr}')

    arr = [1,2,3,4,5]
    print(f'Original = {arr}')

    rotate_left_OPT(arr, d = 23)
    print(f'Left Rotated = {arr}')

    arr = [1,2,3,4,5]
    rotate_right_OPT(arr, d = 23)
    print(f'Right Rotated = {arr}')
