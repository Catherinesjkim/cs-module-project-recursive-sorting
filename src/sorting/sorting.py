# TO-DO: complete the helper function below to merge 2 sorted arrays
# Since we "divide" and then "conquer", we can think about the total runtime of merge sort as O(Log(N)) * O(N) or 
# O(N * Log(N))

# The divide and conquer algo splits an array in half, and keeps splitting the list by 2 until it only has singular elements
# Adjacent elements become sorted pairs, then sorted pairs are merged and sorted with other pairs as well
# this process continues until we get a sorted list with all the elements of the unsorted input list

# recursively split the array in half until we have arrays with size one
# we then merge each half that was split, sorting them in the process
# arrA: left array
# arrB: right array
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    
    result = [] # result/sorted array
    arrA_pointer = arrB_pointer = 0 # initialize both array indexes into zero
    
    # we use the array lengths often, so it's handy to make variables
    arrA_length, arrB_length = len(arrA), len(arrB)
    
    for _ in range(elements):
        if arrA_pointer < arrA_length and arrB_pointer < arrB_length:
            # we check which value from the start of each array is smaller
            # if the item at the beginning of the left array is smaller, 
            if arrA[arrA_pointer] <= arrB[arrB_pointer]:
                # add it to the sorted array/result
                result.append(arrA[arrA_pointer])
                # increment left pointer plus equals one
                arrA_pointer += 1
                
            # else if the above is not the case, then there's one another conclusion. 
            else: # if the item at the beginning of the right list is smaller,
                # add it to the sorted array/result
                result.append(arrB[arrB_pointer])
                # increment the right pointer
                arrB_pointer += 1
        
        # If the above is not the case, and the for loop does not trigger, we know that there is an element either on the left or right array.
        # If we've reached the end of the left array, add the elements from the right array
        elif arrA_pointer == arrA_length:
            result.append(arrB[arrB_pointer])
            arrB_pointer += 1
            
        # If we've reached the end of the right array, add the elements from the left array
        elif arrB_pointer == arrB_length:
            result.append(arrA[arrA_pointer])
            arrA_pointer += 1

    return result

# TO-DO: implement the Merge Sort function below recursively
# divide and conquer algo == recursion
# base case is when you have an array with only 1 element
# to move towards the base case, you must repeatedly divide the original collection in half until we reach the base case
# arrays with a single element is the base case because they are already sorted
# then "merge" these sorted pieces back together
def merge_sort(arr):
    # if the length of the array is a single element, return it
    if len(arr) <= 1:
        return arr
    
    # use floor division to get midpoint, indices must be integers
    midpoint = int(len(arr) // 2)
    
    # sort and merge each half
    # recursive calls 
    arrA = merge_sort(arr[:midpoint]) # left half will be up to the midpoint
    arrB = merge_sort(arr[midpoint:]) # right half will be from midpoint to the end
    
    # merge the sorted arrays (left & right) into a new one
    return merge(arrA, arrB)
    
# verify it works
random_array_of_nums = [120, 45, 68, 250, 176]
print(random_array_of_nums)

random_array_of_nums = merge_sort(random_array_of_nums)
print(random_array_of_nums)


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

