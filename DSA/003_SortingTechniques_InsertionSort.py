########################################################################################################################
# Insertion Sort 
# ----------------------------------------------------------------------------------------------------------------------
# Stable
# ----------------------------------------------------------------------------------------------------------------------
# Time  Complexity: Worst Case - O(n)     |   Avg Case - O(n^2)   |   Best Case - O(n^2)
# Space Complexity: Worst Case - O(1)     |   Avg Case - O(1)     |   Best Case - O(1)
########################################################################################################################


def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1, n):
        bkp = arr[i]
        
        j = i-1
        while j >= 0 and arr[j] > bkp:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = bkp


def insertion_sort_recursive(arr, end):
    if end <= 0:
        return
    
    insertion_sort_recursive(arr, end-1)
    
    bkp = arr[end]
    j = end-1
    while j >= 0 and arr[j] > bkp:
        arr[j+1] = arr[j]
        j -= 1 
    
    arr[j+1] = bkp


arr = [5,4,10,1,6,2]
print(f'arr = {arr}')

insertion_sort(arr)
print(f'arr = {arr}')
