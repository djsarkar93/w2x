########################################################################################################################
# Second Largest Element Of An Array
########################################################################################################################


########################################################################################################################
# Brute Force Solution
# ----------------------------------------------------------------------------------------------------------------------
# Time  Complexity: O(nlogn)     + O(n)
# Space Complexity: O(1) or O(n) + O(1)
########################################################################################################################


def find_second_largest_BF(arr):
    arr.sort()
    largest = arr[-1]               # smallest = arr[0]
    
    n = len(arr)
    for i in range(n-2, -1, -1):    # Loop 1 to n-1
        if arr[i] < largest:        # if arr[i] > smallest, return
            return arr[i]
    
    return None


########################################################################################################################
# Better Solution
# ----------------------------------------------------------------------------------------------------------------------
# Time  Complexity: O(2n)
# Space Complexity: O(1)
########################################################################################################################


def find_second_largest_BTR(arr):
    n = len(arr)
    
    largest = float('-inf')                 # smallest = float('inf')
    for i in range(0, n):
        largest = max(arr[i], largest)      # smallest = min(arr[i], smallest)
    
    second_largest = float('-inf')          # 2nd_smallest = float('inf')
    for i in range(0, n):
        if arr[i] != largest:               # For all (arr[i] != 2nd_smallest), find 2nd_smallest
            second_largest = max(arr[i], second_largest)
    
    return second_largest


########################################################################################################################
# Optimal Solution
# ----------------------------------------------------------------------------------------------------------------------
# Time  Complexity: O(n)
# Space Complexity: O(1)
########################################################################################################################


def find_second_largest_OPT(arr):
    n = len(arr)
    
    second_largest = float('-inf')                          # 2nd_smallest = float('inf')
    largest = arr[0]
    for i in range(0, n):
        if arr[i] > largest:                                # If arr[i] < smallest, then 2nd_smallest, smallest = smallest, arr[i]
            second_largest = largest
            largest = arr[i]
        elif arr[i] < largest and arr[i] > second_largest:  # If (arr[i] > smallest) & (arr[i] < 2nd_smallest), then 2nd_smallest = arr[i]
            second_largest = arr[i]
    
    return second_largest


arr = [5,3,5,8,7,2,8,1]
print(f'arr = {arr}')

print(f'2nd Largest (Brute Force) = {find_second_largest_BF(arr)}')
print(f'2nd Largest (Better) = {find_second_largest_BTR(arr)}')
print(f'2nd Largest (Optimal) = {find_second_largest_OPT(arr)}')
