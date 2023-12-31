########################################################################################################################
# Bubble Sort 
# ----------------------------------------------------------------------------------------------------------------------
# Stable
# ----------------------------------------------------------------------------------------------------------------------
# Time  Complexity: Worst Case - O(n)     |   Avg Case - O(n^2)   |   Best Case - O(n^2)
# Space Complexity: Worst Case - O(1)     |   Avg Case - O(1)     |   Best Case - O(1)
########################################################################################################################


def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n-1, -1, -1):
        did_swap = False
        
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                did_swap = True
        
        if not did_swap:
            break


def bubble_sort_recursive(arr, end):
    if end <= 0:
        return
    
    did_swap = False
    
    for j in range(0, end):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            did_swap = True
    
    if not did_swap:
        return
    
    bubble_sort_recursive(arr, end-1)


arr = [5,3,5,7,8,2]
print(f'arr = {arr}')

bubble_sort(arr)
print(f'arr = {arr}')
