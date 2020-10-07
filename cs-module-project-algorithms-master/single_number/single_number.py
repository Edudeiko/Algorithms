'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    list_arr = []
    for ii in arr:
        if ii in list_arr:
            list_arr.remove(ii)
        else:
            list_arr.append(ii)
    return list_arr.pop()

'''
Another solution
'''
# 2 * sum(set(arr)) - sum(arr)

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
