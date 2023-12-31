########################################################################################################################
# Selection Sort 
# ----------------------------------------------------------------------------------------------------------------------
# Unstable
# ----------------------------------------------------------------------------------------------------------------------
# Time  Complexity: Worst Case - O(n^2)   |   Avg Case - O(n^2)   |   Best Case - O(n^2)
# Space Complexity: Worst Case - O(1)     |   Avg Case - O(1)     |   Best Case - O(1)
########################################################################################################################


def selection_sort(arr):
    n = len(arr)
    
    for i in range(0, n-1):
        tmp = i
        
        for j in range(i+1, n):
            if arr[j] < arr[tmp]:
                tmp = j
        
        arr[i], arr[tmp] = arr[tmp], arr[i]


arr = [5,3,5,7,8,2]
print(f'arr = {arr}')

selection_sort(arr)
print(f'arr = {arr}')
