'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    zeros = list(filter(lambda ii: ii == 0, arr))
    no_zeros = list(filter(lambda ii: ii != 0, arr)) + zeros
    return no_zeros


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
