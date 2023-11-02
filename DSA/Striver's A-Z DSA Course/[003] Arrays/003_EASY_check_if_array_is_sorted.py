"""
Check if array is sorted
"""
import os


########################################################################################################################
# Optimal Solution
# Approach: 
#   [1] Linear search if not (arr[i] <= arr[i+1])
# Time Complexity:  O( n )
# Space Complexity: O( 1 )
########################################################################################################################
def is_sorted(arr):
    n = len(arr)

    for i in range(0, n-1):
        if not (arr[i] <= arr[i+1]):
            return False
    
    return True


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')

    arr = [5,3,5,8,7,2,8,1]
    print(f'Array = {arr}')
    print(f'Is sorted? {is_sorted(arr)}')

    arr = [1,2,2,3,4,4,5]
    print(f'Array = {arr}')
    print(f'Is sorted? {is_sorted(arr)}')
