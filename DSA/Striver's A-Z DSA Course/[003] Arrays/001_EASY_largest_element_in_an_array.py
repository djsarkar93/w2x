"""
Find the largest / smallest element in an array
"""
import os


########################################################################################################################
# Brute Force Solution
# Approach: 
#   [1] Sort using merge sort or quick sort
#   [2] Get last element
# Time Complexity:
#   [a] Merge Sort - B/A/W: O(n log n)
#   [b] Quick Sort - B/A  : O(n log n)      W: O( n^2 )
# Space Complexity:
#   [a] Merge Sort - O(n) [ignoring the stack space]
#   [b] Quick Sort - O(1) [ignoring the stack space]
########################################################################################################################
def quick_sort(arr, start, end):
    def partition(arr, start, end):
        pivot = arr[end]
        i = start - 1
        for j in range(start, end):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[end] = arr[end], arr[i+1]
        return i+1
    
    if start >= end:
        return
    pivot_idx = partition(arr, start, end)
    quick_sort(arr, start, pivot_idx - 1)
    quick_sort(arr, pivot_idx + 1, end)


def merge_sort(arr, start, end):
    def merge(arr, start, mid, end):
        merged_list = []
        lidx = start
        ridx = mid+1
        while lidx<=mid and ridx<=end:
            if arr[lidx] <= arr[ridx]:
                merged_list.append(arr[lidx])
                lidx += 1
            else:
                merged_list.append(arr[ridx])
                ridx += 1
        while lidx<=mid:
            merged_list.append(arr[lidx])
            lidx += 1
        while ridx<=end:
            merged_list.append(arr[ridx])
            ridx += 1
        for i in range(start, end+1):
            arr[i] = merged_list[i-start]
    
    if start >= end:
        return
    mid = start + (end-start)//2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid+1, end)
    merge(arr, start, mid, end)


def get_largest_element_BF(arr):
    #quick_sort(arr, start=0, end=len(arr)-1)
    merge_sort(arr, start=0, end=len(arr)-1)
    return arr[-1]


########################################################################################################################
# Better Solution
########################################################################################################################
# Does not exist.


########################################################################################################################
# Optimal Solution
# Approach: 
#   [1] Linear search
# Time Complexity:  O( n )
# Space Complexity: O( 1 )
########################################################################################################################
def get_largest_element_OPT(arr):
    n = len(arr)
    largest = arr[0]

    for i in range(1, n):
        largest = max(largest, arr[i])                  # Smallest - min() / Largest - max()
    
    return largest


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')

    arr = [5,3,5,8,7,2]
    print(f'Original = {arr}')

    n = get_largest_element_BF(arr)
    print(f'Largest Element (Brute Force) = {n}')

    print(f'Largest Element (Better) = N/A')

    arr = [5,3,5,8,7,2]
    n = get_largest_element_OPT(arr)
    print(f'Largest Element (Optimal) = {n}')
