def selection_sort(arr):
    # loop through n-1 elements
    for ii in range(0, len(arr) - 1):
        cur_index = ii
        smallest_index = cur_index
        # (hint, can do in 3 loc)
        for i in range(ii + 1, len(arr)):
            if arr[i] < arr[smallest_index]:
                smallest_index = i
        
        (arr[ii], arr[smallest_index]) = (arr[smallest_index], arr[ii]) # swap (a,b) = (b,a)

    return arr

# other solution
# def selection_sort_2(arr, size)
#     for step in range(size):
#         min_idx = step
        
#     for index in range(step + 1, size):
        
#         if arr[index] < arr[min_idx]:
#             min_idx = index
            
#     (arr[step], arr[min_idx]) = (arr[min_idx], arr[step])

# data = [-2, 4, 0, 45, 11, -9]
# size = len(data)
# selection_sort_2(data, size)
# print('Sorted Array:', data)

'''
other solutions can be found here
https://github.com/Edudeiko/Algorithms/blob/master/cs-module-project-iterative-sorting-master/src/notebook/sorting_search.ipynb
'''

def bubble_sort(arr):
    
    for index in range(len(arr)):
        for index_unsorted in range(0, len(arr) - index -1):
            
            # To sort in descending order, change > to < in this line.
            if arr[index_unsorted] > arr[index_unsorted + 1]:
                
                # swap if greater is at the rear position
                (arr[index_unsorted], arr[index_unsorted + 1]) = (arr[index_unsorted + 1], arr[index_unsorted])

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    
    maximum=0
    for index in range(len(arr)):
        if arr[index] < 0:
            return f'Error, negative numbers not allowed in Count Sort'
        if arr[index] > maximum:
            maximum = arr[index]

        
    # Count the number of times each value appears.
    # counts[0] stores the number of 0's in the input, etc
    counts = [0] * (maximum + 1)
    
    # Run through the input list
    for index in arr:
        counts[index] += 1
    
    # Overwrite counts to hold the next index an item with
    num_items_before = 0
    for sorted_item in range(maximum + 1):
        for _ in range(counts[sorted_item]):
            arr[num_items_before] = sorted_item
            
            # Make sure the next index with the same value goes after the one just placed
            num_items_before += 1

    return arr


def counting_sort_2(arr, maximum=None):
    # $%$Start
    if len(arr) == 0:
        return arr
    if maximum is None:
        maximum = max(arr)
    # count the number of each element in original arr
    buckets = [0] * (maximum+1)
    for value in arr:
        if value < 0:
            return "Error, negative numbers not allowed in Count Sort"
        else:
            buckets[value] += 1
    # reinsert values into original array using counts
    j = 0
    for i in range(0, len(buckets)):
        while buckets[i] > 0:
            arr[j] = i
            j += 1
            buckets[i] -= 1
    # $%$End
    return arr
