"""
Linear Search
"""
import os


########################################################################################################################
# Optimal Solution
# Approach: 
#   [1] Loop over arr        --> True if arr[i] == n else False
# Time Complexity:  O( n )
# Space Complexity: O( 1 )
########################################################################################################################
def linear_search_OPT(arr, k):
    n = len(arr)

    for i in range(0, n):
        if arr[i] == k:
            return True
    
    return False


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')

    arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
    print(f'Original = {arr}')

    print(f'is 4 present? {linear_search_OPT(arr, 4)}')
    print(f'is 7 present? {linear_search_OPT(arr, 7)}')
