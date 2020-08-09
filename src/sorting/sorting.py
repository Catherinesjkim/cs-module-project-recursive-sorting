# TO-DO: complete the helper function below to merge 2 sorted arrays

# constructs randomized array of length 'size', each element is randomly selected from the range 0 up to 'max'
def create_array(size=8, max=50):
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
"""Consider an array with 8 elements, when you split the problem, it becomes 2 arrays of 4 elements, then split it again and it becomes 4 arrays of 2 elements. When it finally becomes 8 arrays of 1 element, that's when you join it together but you work your way up combining the 8 arrays of 1 element to 4 arrays of 2 elements, and so forth"""

# iterative 
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements # [0,0,0,0,0,0,0,0]
    # result = []
    arrA_pointer = arrB_pointer = 0  # initialize both array indexes into zero
    # we use the array lengths often, so it's handy to make variables
    arrA_length, arrB_length = len(arrA), len(arrB)

    for _ in range(elements):
        if arrA_pointer < arrA_length and arrB_pointer < arrB_length:
            # we check which value from the start of each array is smaller
            # if the item at the beginning of the left array is smaller,
            if arrA[arrA_pointer] <= arrB[arrB_pointer]:
                # add it to the sorted array/result
                #result.append(arrA[arrA_pointer])
                merged_arr[arrA_pointer + arrB_pointer] = arrA[arrA_pointer]
                # increment left pointer plus equals one
                arrA_pointer += 1

            # else if the above is not the case, then there's one another conclusion.
            else:  # if the item at the beginning of the right list is smaller,
                # add it to the sorted array/result
                # result.append(arrB[arrB_pointer])
                merged_arr[arrA_pointer + arrB_pointer] = arrB[arrB_pointer]
                # increment the right pointer
                arrB_pointer += 1

        # If the above is not the case, and the for loop does not trigger, we know that there is an element either on the left or right array.
        # If we've reached the end of the left array, add the elements from the right array
        elif arrA_pointer == arrA_length:
            # result.append(arrB[arrB_pointer])
            merged_arr[arrA_pointer + arrB_pointer] = arrB[arrB_pointer] # right array
            arrB_pointer += 1

        # If we've reached the end of the right array, add the elements from the left array
        elif arrB_pointer == arrB_length:
            # result.append(arrA[arrA_pointer])
            merged_arr[arrA_pointer + arrB_pointer] = arrA[arrA_pointer] # left array
            arrA_pointer += 1

    # return result
    return merged_arr

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

