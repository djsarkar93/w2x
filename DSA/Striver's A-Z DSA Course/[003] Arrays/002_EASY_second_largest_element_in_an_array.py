"""
Find the second largest and smallest element in an array
"""
import os


########################################################################################################################
# Brute Force Solution
# Approach: 
#   [1] Sort array
#   [2] If no duplicates, return 2nd_largest = arr[n-2] | 2nd_smallest = arr[1] 
#   [3] If duplicates,
#       let,            largest = arr[n-1]          |                   smallest = arr[0]
#       for largest,    Loop i from n-2 to 0        |   for largest,    Loop i from 1 to n-1
#                           if arr[i] < L: return   |                       if arr[i] > S: return
# Time Complexity:  O( n log n ) + O(n)
# Space Complexity: O(1) or O(n) + O(1)
########################################################################################################################
def get_2nd_largest_element_BF(arr):
    arr.sort()
    n = len(arr)
    largest = arr[n-1]
    for i in range(n-2, -1, -1):
        if arr[i] < largest:
            return arr[i]
    return None


def get_2nd_smallest_element_BF(arr):
    arr.sort()
    n = len(arr)
    smallest = arr[0]
    for i in range(1, n):
        if arr[i] > smallest:
            return arr[i]
    return None


########################################################################################################################
# Better Solution
# Approach: 
#   [1] Let, largest = -INF         |   samllest = INF
#   [2] Loop i from 0 to n-1: Find largest / samllest
#   [3] Let, 2nd_largest = -INF     |   2nd_samllest = INF
#       Loop i from 0 to n-1: 
#           If not largest/samllest: 
#               Find 2nd_largest / 2nd_samllest
# Time Complexity:  O( 2n )
# Space Complexity: O( 1 )
########################################################################################################################
def get_2nd_largest_element_BST(arr):
    n = len(arr)
    if n <= 1:                          # Edge case: Array has 0 or 1 element
        return None
    largest = float('-inf')
    for i in range(n):
        largest = max(largest, arr[i])
    second_largest = float('-inf')
    for i in range(n):
        if arr[i] != largest:
            second_largest = max(second_largest, arr[i])
    return None if second_largest == float('-inf') else second_largest


def get_2nd_smallest_element_BST(arr):
    n = len(arr)
    if n <= 1:                          # Edge case: Array has 0 or 1 element
        return None
    smallest = float('inf')
    for i in range(n):
        smallest = min(smallest, arr[i])
    second_smallest = float('inf')
    for i in range(n):
        if arr[i] != smallest:
            second_smallest = min(second_smallest, arr[i])
    return None if second_smallest == float('inf') else second_smallest


########################################################################################################################
# Optimal Solution
# Approach: 
#   [1] Let, largest = arr[0] 2nd_largest = -INF    |   samllest = arr[0] 2nd_smallest = INF
#   [2] Loop i from 1 to n-1
#   [3] if arr[i] > largest:                                2nd_largest = largest & largest = arr[i]
#     elif arr[i] < largest and arr[i] > 2nd_smallest:      2nd_largest = arr[i]
#
#       if arr[i] < samllest:                                2nd_smallest = samllest & samllest = arr[i]
#     elif arr[i] > samllest and arr[i] < 2nd_smallest:      2nd_smallest = arr[i]
# Time Complexity:  O( n )
# Space Complexity: O( 1 )
########################################################################################################################
def get_2nd_largest_element_OPT(arr):
    n = len(arr)
    largest = arr[0]
    second_largest = float('-inf')
    for i in range(1, n):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] < largest and arr[i] > second_largest:
            second_largest = arr[i]
    return None if second_largest == float('-inf') else second_largest


def get_2nd_smallest_element_OPT(arr):
    n = len(arr)
    smallest = arr[0]
    second_smallest = float('inf')
    for i in range(1, n):
        if arr[i] < smallest:
            second_smallest = smallest
            smallest = arr[i]
        elif arr[i] > smallest and arr[i] < second_smallest:
            second_smallest = arr[i]
    return None if second_smallest == float('inf') else second_smallest


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')

    arr = [5,3,5,8,7,2,8,1]
    print(f'Original = {arr}')

    print(f'2nd Largest (Brute Force) = {get_2nd_largest_element_BF(arr)}')
    print(f'2nd Smallest (Brute Force) = {get_2nd_smallest_element_BF(arr)}')

    print(f'2nd Largest (Better) = {get_2nd_largest_element_BST(arr)}')
    print(f'2nd Smallest (Better) = {get_2nd_smallest_element_BST(arr)}')

    print(f'2nd Largest (Optimal) = {get_2nd_largest_element_OPT(arr)}')
    print(f'2nd Smallest (Optimal) = {get_2nd_smallest_element_OPT(arr)}')

