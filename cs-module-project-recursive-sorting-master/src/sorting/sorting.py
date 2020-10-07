def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    
    l = 0
    r = 0
    
    for i in range(0, elements):
        if l == len(arrA):
            merged_arr[i] = arrB[r]
            r += 1
            
        elif r == len(arrB):
            merged_arr[i] = arrA[l]
            l += 1
            
        elif arrA[l] < arrB[r]:
            merged_arr[i] = arrA[l]
            l += 1
            
        elif arrA[l] > arrB[r]:
            merged_arr[i] = arrB[r]
            r += 1

    return merged_arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        arrA = arr[:mid]
        arrB = arr[mid:]
        arrA = merge_sort(arrA)
        arrB = merge_sort(arrB)
        return merge(arrA, arrB)
    return arr

def merge_sort_2(arr):
    if len(arr) > 1:
        
        # mid is the point where the array is divided into two subarrays
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        # Sort the two halves
        merge_sort_2(left)
        merge_sort_2(right)
        
        i = j = k = 0
        
        # Until we reach either end of either Left or Right, pick larger among
        # elements Left and Right and place them in the correct position
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
                
        # When we run out of elements in either Left or Right,
        # pick up the remaining elements
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    new = mid + 1
    
    # if merge is already sorted
    if arr[mid] <= arr[new]:
        return
    
    #two pointers to maintain start of both arrays to merge
    while start <= mid and new <= end:
        
        # if element 1 is in right place
        if arr[start] <= arr[new]:
            start += 1
        else:
            value = arr[new]
            index = new
            
            # shift all the elements between element 2, right by 1
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1
                
            arr[start] = value
            
            # Update all the pointers
            start += 1
            mid += 1
            new +=1

def merge_sort_in_place(arr, l, r):
    # cache = {} ?
    if (r - l) > 1:

        mid = 1 + (r - l) // 2
        # sort first and second halfs
        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid, r)
        
        merge_in_place(arr, l, mid, r)


def printList(array):
    for ii in range(len(array)):
        print(array[ii], end=', ')

arrA = [0, 22, 55, 99]
arrB = [-2, 33, 44, 77]

_merge_ = merge(arrA, arrB)

array = [5, 3, 1, 0, 7, 4, 10, -3]
array_2 = [55, 33, 11, 0, 77, 44, 88, -33]

sorted_1 = merge_sort(array)
sorted_2 = merge_sort_2(array_2)
print('\n')
printList(_merge_)
print('\n')
printList(sorted_1)
print('\n')
printList(sorted_2)


recursive - sorting.py:
def merge_in_place_solution(arr, start, mid, end):
    # $%$Start
    # based on C solution at: https://www.geeksforgeeks.org/in-place-merge-sort/
    start2 = mid + 1
    # If the direct merge is already sorted
    if arr[mid] <= arr[start2]:
        return
    # Two pointers to maintain start
    # of both arrays to merge
    while start <= mid and start2 <= end:
        # If element 1 is in right place
        if arr[start] <= arr[start2]:
            start += 1
        else:
            value = arr[start2]
            index = start2
            # Shift all the elements between element 1
            # element 2, right by 1.
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1
            arr[start] = value
            # Update all the pointers
            start += 1
            mid += 1
            start2 += 1
    # $%$End
def merge_sort_in_place(arr, l, r):
    # $%$Start
    if l < r:
        # Same as (l + r) // 2, but avoids overflow
        # for large l and r
        m = l + (r - l) // 2
        # Sort first and second halves
        merge_sort_in_place_solution(arr, l, m)
        merge_sort_in_place_solution(arr, m + 1, r)
        merge_in_place(arr, l, m, r)
    # $%$End
