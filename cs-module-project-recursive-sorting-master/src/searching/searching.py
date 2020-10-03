# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if start > end:
        return False
    else:
        mid = (start + end) / 2
        if x == arr[mid]:
            return mid
        else:
            if target < arr[mid]:  # target is on the right side
                return binary_search(arr, target, mid + 1, end)
            else:
                return binary_search(arr, target, start, mid - 1)

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
