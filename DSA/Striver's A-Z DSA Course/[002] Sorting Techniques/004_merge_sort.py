"""
Merge Sort
########################################################################################################################
A Divide & Conquer algorithm
########################################################################################################################
Stable Sort
########################################################################################################################
Usecase:
    No Space Constraints
    Large Data Sets - Efficient for sorting large-scale data due to its O(n log n) time complexity
    External Sorting - Ideal when dataset exceed memory capacity, using sequential external storage operations.
    Linked List - Effective for sorting linked lists by reordering links, minimizing data handling overhead.
########################################################################################################################
Space Complexity: O( n )
########################################################################################################################
Time Complexity:
    Best:       O( n log n )
    Average:    O( n log n )
    Worst:      O( n log n )
"""
import os


def merge(arr, start, mid, end):
    merged_list = []                            # Temporary array
    lidx = start                                # Starting index of left half
    ridx = mid+1                                # Starting index of right half

    while lidx <= mid and ridx <= end:          # Storing elements in the temporary array in a sorted manner
        if arr[ lidx ] <= arr[ ridx ]:
            merged_list.append(arr[lidx])
            lidx += 1
        else:
            merged_list.append(arr[ridx])
            ridx += 1
    
    while lidx <= mid:                          # If elements are still left on the left half
        merged_list.append(arr[lidx])
        lidx += 1
    
    while ridx <= end:                          # If elements are still left on the right half
        merged_list.append(arr[ridx])
        ridx += 1
    
    for i in range(start, end+1):               # Transfering all elements from temporary to arr
        arr[i] = merged_list[i - start]


def mergesort(arr, start, end):
    if start >= end:                            # Further divide not possible
        return
    
    mid = start + (end - start)//2              # same - (start + end)//2

    mergesort(arr, start, mid)                  # Divide left half
    mergesort(arr, mid+1, end)                  # Divide right half

    merge(arr, start, mid, end)                 # Conquer left & right halves


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')

    arr = [5,3,5,8,7,2]
    print(f'Original = {arr}')

    mergesort(arr, 0, len(arr)-1)
    print(f'Ascending = {arr}')
