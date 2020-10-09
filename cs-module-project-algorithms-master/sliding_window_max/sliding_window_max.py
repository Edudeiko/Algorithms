'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
import time
from collections import deque


start = time.process_time()

'''
O(1) for deque -> append
O(n) for deque -> pop
'''
def sliding_window_max(nums, k):
    
    dq = deque()
    
    window_max = []
    
    for ii in range(len(nums)):
        while dq and nums[ii] >= nums[dq[-1]]:
            dq.pop()
            
        dq.append(ii)
        
        if ii >= k and dq and dq[0] <= ii - k:
            dq.popleft()
            
        if ii >= k -1:
            window_max.append(nums[dq[0]])

    return window_max


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
    elapsed = (time.process_time() - start)
    print(f'time to run: {elapsed}')


'''
O(n log n)
'''
# def sliding_window_max(nums, k):
    
#     window_max = []  # create an empty list to store numbers
    
#     start = 0  # start with 0
    
#     end = k # end with k
    
#     for _ in range( 0, len(nums) + 1 - k ):
#         # loop from 0 to sliding window
#         temp = nums[start:end]  # store temp result
#         window_max.append(max(temp))  # append the result
#         start += 1  # adjust start and end
#         end += 1

#     return window_max


# if __name__ == '__main__':
#     # Use the main function here to test out your implementation 
#     arr = [1, 3, -1, -3, 5, 3, 6, 7]
#     k = 3

#     print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
#     elapsed = (time.process_time() - start)
#     print(f'time to run: {elapsed}')