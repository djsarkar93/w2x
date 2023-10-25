"""
Selection Sort
########################################################################################################################
LEFT to RIGHT sorting
########################################################################################################################
Unstable Sort
    [5,3,5,7,8,2]
        iter-1: [2,3,5,7,8,5]
        iter-2: [2,3,5,7,8,5]
        iter-3: [2,3,5,7,8,5]
        iter-4: [2,3,5,5,8,7]
        iter-5: [2,3,5,5,7,8]
########################################################################################################################
Usecase:
    Educational Purposes
    Space Constraints
    Limited Swap Operations
########################################################################################################################
Space Complexity: O( 1 )
########################################################################################################################
Time Complexity:
    Best:       O( n^2 )
    Average:    O( n^2 )
    Worst:      O( n^2 )
"""
import os


def selection_sort(arr):
    n = len(arr)
    
    for i in range(0, n-1):                             # 1st to 2nd last
        tmp_idx = i

        for j in range(i+1, n):                         # i+1 to last
            if arr[j] < arr[tmp_idx]:                   # ASC - < | DESC - >
                tmp_idx = j
        
        arr[i], arr[tmp_idx] = arr[tmp_idx], arr[i]


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')

    arr = [5,3,5,7,8,2]
    print(f'Original = {arr}')

    selection_sort(arr)
    print(f'Ascending = {arr}')
