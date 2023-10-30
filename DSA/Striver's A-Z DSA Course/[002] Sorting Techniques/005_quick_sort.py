"""
Quick Sort
########################################################################################################################
A Divide & Conquer algorithm
########################################################################################################################
Unstable Sort
########################################################################################################################
Space Complexity:
    Best:       O( 1 ) + O( log n )     [Where, O(log n) is the auxiliary stack space]
    Average:    O( 1 ) + O( log n )     [Where, O(log n) is the auxiliary stack space]
    Worst:      O( 1 ) + O( n )         [Where, O(n)     is the auxiliary stack space]
########################################################################################################################
Time Complexity:
    Best:       O( n log n )
    Average:    O( n log n )
    Worst:      O( n^2 )
"""
import os


def partition(arr, start, end):
    pivot = arr[end]                                # Choosing the last element as pivot
    i = start - 1

    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[end] = arr[end], arr[i + 1]     # Place the pivot correctly
    return i + 1


def quick_sort(arr, start, end):
    if start >= end:                                # Further divide not possible
        return
    
    pivot_idx = partition(arr, start, end)          # Partition the array

    quick_sort(arr, start, pivot_idx - 1)           # Before pivot
    quick_sort(arr, pivot_idx + 1, end)             # After pivot


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')

    arr = [5,3,5,8,7,2]
    print(f'Original = {arr}')

    quick_sort(arr, 0, len(arr)-1)
    print(f'Ascending = {arr}')
