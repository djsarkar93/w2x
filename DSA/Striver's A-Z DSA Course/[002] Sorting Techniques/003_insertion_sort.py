"""
Insertion Sort
########################################################################################################################
Stable Sort
    [5,|3,5,7,8,2]
    [3,|5,5,7,8,2]

    [3,5,|5,7,8,2]

    [3,5,5,|7,8,2]

    [3,5,5,7,|8,2]

    [3,5,5,7,8,|2]
    [3,5,5,7,8,|8]
    [3,5,5,7,7,|8]
    [3,5,5,5,7,|8]
    [3,5,5,5,7,|8]
    [3,3,5,5,7,|8]
    [2,3,5,5,7,|8]
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


def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        tmp = arr[i]
        
        j = i-1
        while j >= 0 and arr[j] > tmp:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = tmp


def recursive_insertion_sort(arr, end):
    if end <= 0:
        return
    
    recursive_insertion_sort(arr, end-1)

    tmp = arr[end]
    j = end - 1
    while j >= 0 and arr[j] > tmp:
        arr[j+1] = arr[j]
        j -= 1
    
    arr[j+1] = tmp



if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')

    arr = [5,4,10,1,6,2]
    print(f'Original = {arr}')

    insertion_sort(arr)
    print(f'Ascending = {arr}')

    arr = [5,4,10,1,6,2]
    print(f'Original = {arr}')

    recursive_insertion_sort(arr, end=len(arr)-1)
    print(f'Ascending = {arr}')
