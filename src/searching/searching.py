# TO-DO: Implement a recursive implementation of binary search
# Track the search space by using two index - start and end
# Initially, the whole array is our search space
# at each step, we find the mid value in the search space and compare it with target value
# Find out if a key target exists in the sorted list 
def binary_search(arr, start, end, target):  
    # start = 0
    # end = n-1
    # Base condition (search space is exhausted)
    if start > end:
        return -1
        
    # we find the mid space in the search space and compares it with key value
    mid = (start + end) // 2
    
    # overflow can happen. Use below 
    # mid = left + (right - left) / 2
        
    # Compare target with the middle element - if element is present at the middle itself
    # Base condition (key value is found)
    if target == arr[mid]:
        # If target matches with the middle element, return the mid index
        return mid
    
    # if target value is smaller than the middle element in the array,
    elif target < arr[mid]:
        # discard all elements in the right search space including the mid element i.e. arr[mid...high]
        return binary_search(arr, start, mid - 1, target)
        # now our new hgh would be mid - 1
        
    else:
        # otherwise, discard all elements in the left search space including the mid element i.e. arr[low...mid]
        return binary_search(arr, mid + 1, end, target)
        # now our new low would be mid + 1
# Repeat the process until target is found or the search space is exhausted
         
# Test
if __name__ == '__main__':
    
    arr = [2, 5, 6, 8, 9, 10]
    key = 11

    (start, end) = (0, len(arr) - 1)
    # Function call
    index = binary_search(arr, start, end, key)

    if index != -1:
        print("Element is present at index ", index)
    else:
        print("Element is not present in the array")        




# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

