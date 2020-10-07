'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Less than two ints, no product
    if len(arr) < 2:
        print(f'Need at least two ints to proceed')
        
    sum_of_all_ints_EXCEPT_index = [None] * len(arr)
    
    sum_now = 1
    
    # For each int, find sum of all int BEFORE it, then store total for each time
    for ii in range(len(arr)):
        sum_of_all_ints_EXCEPT_index[ii] = sum_now
        sum_now *= arr[ii]
    
    # Now find sum of integers AFTER int and store it
    sum_now = 1
    
    for ii in range(len(arr) -1, -1, -1):
        sum_of_all_ints_EXCEPT_index[ii] *= sum_now
        sum_now *= arr[ii]
        
    return sum_of_all_ints_EXCEPT_index


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
