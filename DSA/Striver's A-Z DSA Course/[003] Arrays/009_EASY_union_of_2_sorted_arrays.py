"""
Union of Two Sorted Arrays
"""
import os


########################################################################################################################
# Brute Force Solution
# Approach: 
#   [1] Add array 1 & 2 to a set.
#   [2] Return the set as a list.
# Time Complexity:  O( m + n )
# Space Complexity: O( m + n )
########################################################################################################################
def find_union_BF(arr1, arr2):
    result = set()
    result.update(arr1)
    result.update(arr2)
    return list(result)


########################################################################################################################
# Optimal Solution
# Approach: 
#   [1] Use the merge algorithm
# Time Complexity:  O( m + n )
# Space Complexity: O( 1 )
########################################################################################################################
def find_union_OPT(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    i = j = 0
    result = []

    while i < m and j < n:
        if arr1[i] < arr2[j]:
            if len(result) == 0 or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
        else:
            if len(result) == 0 or result[-1] != arr2[j]:
                result.append(arr2[j])
            j += 1
    
    while i < m:
        if result[-1] != arr1[i]:
            result.append(arr1[i])
        i += 1
    
    while j < n:
        if result[-1] != arr2[j]:
            result.append(arr2[j])
        j += 1
    
    return result


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')

    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr2 = [2, 3, 4, 4, 5, 11, 12]
    print(f'Array 1 = {arr1}')
    print(f'Array 2 = {arr2}')

    result = find_union_BF(arr1, arr2)
    print(f'Union of arr1 and arr2 is (Brute Force): {result}')

    result = find_union_OPT(arr1, arr2)
    print(f'Union of arr1 and arr2 is (Optimal): {result}')
