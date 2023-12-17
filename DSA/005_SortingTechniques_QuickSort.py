########################################################################################################################
# Quick Sort 
# ----------------------------------------------------------------------------------------------------------------------
# Unstable
# ----------------------------------------------------------------------------------------------------------------------
# Time  Complexity: Worst Case - O(n^2)      | Avg Case - O(nlogn)       | Best Case - O(nlogn)
# Space Complexity: Worst Case - O(1) + O(n) | Avg Case - O(1) + O(logn) | Best Case - O(1) + O(logn) [O(n) / O(logn) - auxiliary stack space]
########################################################################################################################


def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1 
    
    for j in range(start, end):
        if arr[j] < pivot:
            i += 1 
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[end] = arr[end], arr[i+1]
    return i+1


def quick_sort(arr, start, end):
    if start >= end:
        return
    
    pivot_index = partition(arr, start, end)
    
    quick_sort(arr, start, pivot_index-1)
    quick_sort(arr, pivot_index+1, end)


arr = [5,3,5,8,7,2]
print(f'arr = {arr}')

quick_sort(arr, 0, len(arr)-1)
print(f'arr = {arr}')
