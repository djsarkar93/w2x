########################################################################################################################
# Merge Sort 
# ----------------------------------------------------------------------------------------------------------------------
# Stable
# ----------------------------------------------------------------------------------------------------------------------
# Time  Complexity: Worst Case - O(nlogn)    | Avg Case - O(nlogn)    | Best Case - O(nlogn)
# Space Complexity: Worst Case - O(n + logn) | Avg Case - O(n + logn) | Best Case - O(n + logn) [O(logn) - auxiliary stack space]
########################################################################################################################


def merge(arr, start, mid, end):
    merged_list = []
    lidx = start
    ridx = mid + 1
    
    while lidx <= mid and ridx <= end:
        if arr[lidx] <= arr[ridx]:
            merged_list.append( arr[lidx] )
            lidx += 1 
        else:
            merged_list.append( arr[ridx] )
            ridx += 1
    
    while lidx <= mid:
        merged_list.append( arr[lidx] )
        lidx += 1
    
    while ridx <= end:
        merged_list.append( arr[ridx] )
        ridx += 1
    
    for i in range(start, end+1):
        arr[i] = merged_list[i - start]


def merge_sort(arr, start, end):
    if start >= end:
        return
    
    mid = start + (end - start)//2
    
    merge_sort(arr, start, mid)
    merge_sort(arr, mid+1, end)
    
    merge(arr, start, mid, end)


arr = [5,3,5,8,7,2]
print(f'arr = {arr}')

merge_sort(arr, 0, len(arr)-1)
print(f'arr = {arr}')
