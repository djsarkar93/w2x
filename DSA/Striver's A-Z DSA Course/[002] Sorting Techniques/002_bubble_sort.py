"""
Bubble Sort
########################################################################################################################
RIGHT to LEFT sorting
########################################################################################################################
Stable Sort
    [(5,3),5,7,8,2]
    [3,(5,5),7,8,2]
    [3,5,(5,7),8,2]
    [3,5,5,(7,8),2]
    [3,5,5,7,(8,2)]
    [3,5,5,7,2,8]

    [(3,5),5,7,2,8]
    [3,(5,5),7,2,8]
    [3,5,(5,7),2,8]
    [3,5,5,(7,2),8]
    [3,5,5,2,7,8]

    [(3,5),5,2,7,8]
    [3,(5,5),2,7,8]
    [3,5,(5,2),7,8]
    [3,5,2,5,7,8]

    [(3,5),2,5,7,8]
    [3,(5,2),5,7,8]
    [3,2,5,5,7,8]

    [(3,2),5,5,7,8]
    [2,3,5,5,7,8]
########################################################################################################################
Usecase:
    Educational Purposes
    Space Constraints
########################################################################################################################
Space Complexity: O( 1 )
########################################################################################################################
Time Complexity:
    Best:       O( n )
    Average:    O( n^2 )
    Worst:      O( n^2 )
"""
import os


def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1, -1, -1):                        # last to 1st
        did_swap = False

        for j in range(0, i):                           # 1st to i-1 (2nd last)
            if arr[j] > arr[j+1]:                       # ASC - > | DESC - <
                arr[j], arr[j+1] = arr[j+1], arr[j]
                did_swap = True
        
        if not did_swap:
            break


def recursive_bubble_sort(arr, end):
    if end <= 0:                                          # When empty or only 1 element, do nothing
        return
    
    for j in range(0, end):                               # 1st to 2nd last
        if arr[j] > arr[j+1]:                             # ASC - > | DESC - <
            arr[j], arr[j+1] = arr[j+1], arr[j]
    
    recursive_bubble_sort(arr, end-1)                     # last to 1st


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')

    arr = [5,3,5,7,8,2]
    print(f'Original = {arr}')

    bubble_sort(arr)
    print(f'Ascending = {arr}')

    arr = [5,3,5,7,8,2]
    print(f'Original = {arr}')

    recursive_bubble_sort(arr, end = len(arr)-1)
    print(f'Ascending = {arr}')
