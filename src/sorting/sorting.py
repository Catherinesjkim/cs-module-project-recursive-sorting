# TO-DO: complete the helper function below to merge 2 sorted arrays

# constructs randomized array of length 'size', each element is randomly selected from the range 0 up to 'max'
def create_array(size=10, max=50):
    from random import randint
    return [randint(0, max) for _ in range(size)]

# print(create_array())

# Since we "divide" and then "conquer", we can think about the total runtime of merge sort as O(Log(N)) * O(N) or 
# O(N * Log(N))

# The divide and conquer algo splits an array in half, and keeps splitting the list by 2 until it only has singular elements
# Adjacent elements become sorted pairs, then sorted pairs are merged and sorted with other pairs as well
# this process continues until we get a sorted list with all the elements of the unsorted input list

# recursively split the array in half until we have arrays with size one
# we then merge each half that was split, sorting them in the process
# arrA: left array
# arrB: right array
# recombination/dividing step: O Log(N) step
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements 
    result = []  # sorted array - final output array
    arrA_idx, arrB_idx = 0, 0 # initialize both array indeces into zero because the smalles ends of both arrays will be at the beginning since they are both in sorted order
    # we continue iterating until we've used up all the elements in one of the input arrays
    while arrA_idx < len(arrA) and arrB_idx < len(arrB): # base case
            # on each iteration, we compare the elements seen at the top of the array &
            if arrA[arrA_idx] < arrB[arrB_idx]:
                # append whichever is smaller onto a merged array/result
                result.append(arrA[arrA_idx])
                # increment the index for the array we pulled from to prevent writing the same element onto the merged array again
                arrA_idx += 1
            else: # if the item at the beginning of the right list is smaller,
                # add it to the sorted array/result
                result.append(arrB[arrB_idx])
                # increment the index for the array we pulled from to prevent writing the same element onto the merged array again
                arrB_idx += 1
    # at the end of the while loop, we extend the merged array with wichever of the two input arrays wasn't completely used up inside the while loop. 
    # i.e. if after the while loop, if a index variable is equal to the input arrA, we already know that we pushed all of the elements into the result array. If this is the case, then it must be true that there's at least one element in arrB. So, we push at least one element to the end of the result array. 
    if arrA_idx == len(arrA): result.extend(arrB[arrB_idx:])
    else:                     result.extend(arrA[arrA_idx:])
    
    # at the end of the function return the newly merged result array/
    return result 

# test case
# a=[1,3, 5]
# b=[2,4,6]
# print(merge(a, b))

# TO-DO: implement the Merge Sort function below recursively
# divide and conquer algo == recursion
# base case is when you have an array with only 1 element
# to move towards the base case, you must repeatedly divide the original collection in half until we reach the base case
# arrays with a single element is the base case because they are already sorted
# then "merge" these sorted pieces back together
# merging step: O(N) step
def merge_sort(arr):
    # if the length of the array is a single element, return it
    # because an array of zero or one element is already sorted, by definition
    if len(arr) <= 1: return arr
    # split the list in half and call merge sort recursively on each half
    
    # use floor division to get the midpoint, indices must be integers
    midpoint = int(len(arr) // 2)
    
    # sort and merge each half
    # recursive calls 
    arrA = merge_sort(arr[:midpoint]) # left half will be up to the midpoint
    arrB = merge_sort(arr[midpoint:]) # right half will be from midpoint to the end
    
    # merge the sorted arrays (left & right) into a new one
    return merge(arrA, arrB)
    

# verify it works
a = create_array()
print(a)

s=merge_sort(a)
print(s)



# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

