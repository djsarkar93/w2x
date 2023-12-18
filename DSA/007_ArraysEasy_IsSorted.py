########################################################################################################################
# Is (Array) Sorted
########################################################################################################################


########################################################################################################################
# Optimal Solution
# ----------------------------------------------------------------------------------------------------------------------
# Time  Complexity: O(n)
# Space Complexity: O(1)
########################################################################################################################


def is_sorted(arr):
    n = len(arr)
    
    for i in range(1, n):
        if arr[i-1] > arr[i]:
            return False
    
    return True


arr = [1, 2, 3, 4, 5]
result = is_sorted(arr)
print(f'arr = {arr} | is sorted?: {result}')

arr = [1, 2, 3, 5, 4]
result = is_sorted(arr)
print(f'arr = {arr} | is sorted?: {result}')
